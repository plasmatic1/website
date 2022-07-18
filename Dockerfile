FROM ruby:2.6.5

WORKDIR /usr/src/app
COPY . .

RUN gem install bundler -v 2.2.21
RUN bundle install

CMD ["jekyll", "serve", "--host", "0.0.0.0", "--port", "8000"]