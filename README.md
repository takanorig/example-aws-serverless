# AWS Serverless Example

AWS Serverless Example

## 開発環境

### 事前準備

#### 必要モジュールの確認
- npm >= 6.14.8
    - `$ npm --version`
- python >= 3.8.0
    - `$ python --version`
- aws cli >= 2.0.0
    - `$ aws --version`


#### AWSプロファイルの作成

AWSのプロファイルを作成する。すでに作成されている場合は不要。

```
$ aws configure --profile {your-proflie}
AWS Access Key ID [None]: {your-access-key}
AWS Secret Access Key [None]: {your-secret-access-key}
Default region name [None]: us-west-2
Default output format [None]: json
```


### Python

ここでは、Pyenv および Poetry を利用する。

- Pyenv(pyenv-win) Install
    - https://pyenv-win.github.io/pyenv-win/#installation
- Poetry Install
    - https://python-poetry.org/docs/#introduction

Pyenvを利用して、Python3.8.0をインストールする。

```
$ cd example-aws-serverless
$ pyenv install 3.8.0
$ pyenv local 3.8.0
$ pyenv rehash
```

インストールが完了したら、以下のようにしてバージョンを確認する。

```
$ python --version
Python 3.8.0

$ poetry --version
Poetry version 1.0.10
```

Poetryの設定として、プロジェクト内に `.venv` ディレクトリが作成されるようにする。

```
$ poetry config virtualenvs.in-project true
```

Python仮想環境にて、Poeryを利用して関連モジュールをインストールする。

```
$ cd example-aws-serverless
$ poetry install
```

上記を行うと、example-aws-serverless 配下に `.venv` というPython仮想環境が作成される。
このPython仮想環境を利用して作業をする場合は、以下のようにして仮想環境をアクティブ化する。

```
$ . ./.venv/bin/activate

(.venv) $ python --version
Python 3.8.0
```

### Serverless Framework

Serverless Framework をインストールする。
既にインストールされている場合は、最新版にアップデートする。

```
$ npm install -g serverless
```
```
$ npm update -g serverless
```

関連モジュールをインストールする。

```
$ cd example-aws-serverless
$ npm install
```

## Deploy

依存モジュールが更新されている場合は、以下の手順で requirements.txt を更新する。
- Windowsなどの場合は、改行コードをLFにすること。そうでないとデプロイ時に失敗する。

```
$ cd example-aws-serverless
$ poetry export -f requirements.txt > requirements.txt
$ move ./requirements.txt ./src/
```

予め、共通的なリソースをデプロイする。
- 更新がない限りは、一度デプロイされていれば良い。

```
cd ./src/resources
$ sls deploy --stage {stage} --region {region} --profile {your-profile} --config serverless-lamdalayers.yml
$ sls deploy --stage {stage} --region {region} --profile {your-profile} --config serverless-cognito.yml
```

その上で、各サービスごとに Severless Famework を利用してデプロイを行う。

```
$ cd ./src/{service}
$ sls deploy --profile {your-profile}
```
