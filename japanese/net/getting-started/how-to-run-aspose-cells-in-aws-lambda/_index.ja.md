---
title: AWS LambdaでAspose.Cellsを実行する方法
type: docs
description: 開発スタックに関係なくDockerコンテナ内でAspose.Cells機能を使用する方法を学び、アプリケーションにAspose.Cells機能を統合します。"
weight: 141
url: /ja/net/how-to-run-aspose-cells-in-aws-lambda/
---

## AWS環境の準備

1. AWSアカウントを登録します: 
[AWSアカウントを登録](https://aws.amazon.com/)
1. AWSアカウントにログインし、アカウントにIAMユーザーを追加します。AWS公式ドキュメントを参照してください:
[IAMユーザーを追加](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. "AmazonS3FullAccess"権限を追加します。同様に、EC2およびElastic Beanstalkに対してそれぞれの完全アクセス権も追加します。
1. 最後の手順で、IAMユーザー名、キー、キーID、および"credentials.csv"ファイルを確実に取得し、これらを適切に保存してください。
   今、IAMユーザーがS3、EC2、Elastic Beanstalkに対して完全なアクセス権を持っていることを確認してください。参照:

**![AWSアクセス](AwsAccess.png)**

## Visual Studio用AWS Toolkitのインストール

1. Visual Studio 2019またはそれ以降のバージョンをインストールします。
1. AWS Toolkit for Visual Studioをダウンロードしてインストールします: 
[AWS Toolkit](https://aws.amazon.com/visualstudio/)

## AWS Lambdaで実行するプロジェクトの作成

1. Visual StudioでASP.NET Core Web Applicationを作成し、テストコードを記述し、NuGetからAspose.Cellsを取得します。

1. テストプロジェクトがローカルマシンで正常に実行されることを確認し、それをAWS Elastic Beanstalkにデプロイします:
   プロジェクト名を右クリックし、「AWS Elastic Beanstalkに発行」を選択します。（このオプションは、AWS Toolkit for Visual Studioをインストールした後にのみ存在します）。 
1. AWSアカウントとIAMユーザーを使用して新しいユーザーを追加する必要があります。前の手順で取得した"credentials.csv"ファイルをインポートすることができます。 
1. 公開に成功すると、`http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`のようなリンクアドレスが取得できます。
   リンクが有効になるのを待ってから、10分後にアクセスすることができます。
