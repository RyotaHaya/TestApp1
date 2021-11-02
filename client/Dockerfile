FROM node:lts-alpine
RUN mkdir /app
WORKDIR /app

#環境構築に必要なライブラリが記載されたファイルを指定
COPY ./client/package.json ./
COPY ./client/yarn.lock ./

#ライブラリのインストール
RUN yarn install

RUN yarn run build

# 本番環境時に動作させたいコマンドを指定
CMD ["yarn", "run", "start"]