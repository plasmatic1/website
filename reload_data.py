import json
import requests
import ratelimit
import calendar
from datetime import date

UPD_DMOJ = True
UPD_CF = True

DMOJ_HANDLES = ['Plasmatic']
DMOJ_CONTEST_COUNT = 5
CF_HANDLES = ['Plasmatic', 'thinking_space', 'wasureta', 'kenos']
CF_CONTEST_COUNTS = [3, 1, 1, 1]

accounts = []
dmoj_contests = []
cf_contests = []


@ratelimit.sleep_and_retry
@ratelimit.limits(calls=60, period=60)
def fetch_dmoj(url):
    return requests.get(url).json()['data']['object']


def num_suffix(num):
    num %= 10
    if num == 1: return 'st'
    elif num == 2: return 'nd'
    elif num == 3: return 'rd'
    return 'th'


# DMOJ
if UPD_DMOJ:
    print('== Fetching DMOJ user data ==')
    contests_to_check = []
    for handle in DMOJ_HANDLES:
        print(f'Fetching handle {handle}')
        data = fetch_dmoj(f'https://dmoj.ca/api/v2/user/{handle}')
        accounts.append({
            'display': f'DMOJ: {handle}',
            'url': f'https://dmoj.ca/user/{handle}',
            'rating': data['rating'],
            'max_rating': max(map(lambda c: int(c['rating']) if c['rating'] else 0, data['contests']))
        })

        # Gets CONTEST_COUNT contests sorted by highest rating
        contests_to_check.extend(map(lambda c: (c['key'], handle), filter(lambda c: c['rating'], data['contests'])))

    for contest_key, handle in contests_to_check:
        print(f'Fetching contest {contest_key} under handle {handle}')
        data = fetch_dmoj(f'https://dmoj.ca/api/v2/contest/{contest_key}')

        tot_participants = 0
        rank = -1
        for user in data['rankings']:
            tot_participants += not user['is_disqualified']
            if user['user'] == handle and rank == -1:
                rank = tot_participants

        dmoj_contests.append({
            'name': data['name'],
            'key': contest_key,
            'handle': handle,
            'rank': rank,
            'tot_participants': tot_participants,
            'percentile': rank / (tot_participants + 1)
        })

    print(f'Taking top {DMOJ_CONTEST_COUNT} participations')
    dmoj_contests = sorted(dmoj_contests, key=lambda c: c['percentile'])[:DMOJ_CONTEST_COUNT]


# Codeforces
if UPD_CF:
    print('== Fetching CF User Data ==')
    contests_to_check = []
    for handle, contest_count, data in zip(CF_HANDLES, CF_CONTEST_COUNTS, requests.get(f'https://codeforces.com/api/user.info?handles={";".join(CF_HANDLES)}').json()['result']):
        print(f'Fetching handle {handle}')
        accounts.append({
            'display': f'Codeforces: {handle}',
            'url': f'https://codeforces.com/profile/{handle}',
            'rating': data['rating'],
            'max_rating': data['maxRating']
        })

        contests_to_check.extend(sorted(
            map(lambda c: (handle, c['contestName'], c['contestId'], c['rank'], c['oldRating'] + 4 * (c['newRating'] - c['oldRating']) if c['oldRating'] else -1),
                requests.get(f'https://codeforces.com/api/user.rating?handle={handle}').json()['result']),
            key=lambda c: c[-1], reverse=True)[:contest_count])

    for handle, name, id, rank, _ in contests_to_check:
        cf_contests.append({
            'name': f'{name}',
            'key': id,
            'handle': handle,
            'rank': rank,
            'tot_participants': -1
        })

# Write
with open('_data/auto_accounts.json', 'w') as f:
    json.dump(accounts, f)
if UPD_DMOJ:
    with open('_data/dmoj_contests.json', 'w') as f:
        json.dump(dmoj_contests, f)
if UPD_CF:
    with open('_data/cf_contests.json', 'w') as f:
        json.dump(cf_contests, f)
with open('_data/fetch_time.json', 'w') as f:
    today = date.today()
    json.dump({'time_display': f'{calendar.month_name[today.month]} {today.day}{num_suffix(today.day)}, {today.year}'}, f)
