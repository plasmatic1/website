FROM ruby:3.2.3

WORKDIR /usr/src/app
COPY . .

# Run reload_data.py
RUN apt update
RUN apt install python3-pip -y
RUN pip3 install -r requirements.txt
RUN python3 reload_data.py

# Install deps for website
RUN gem install bundler
RUN bundle install

CMD ["jekyll", "serve", "--host", "0.0.0.0", "--port", "8000"]
