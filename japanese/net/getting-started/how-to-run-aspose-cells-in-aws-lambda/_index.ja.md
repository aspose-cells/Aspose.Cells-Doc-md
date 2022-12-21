---
title: AWS Lambda で Aspose.Cells を実行する方法
type: docs
description: 開発スタックに含まれるテクノロジーに関係なく、Docker を使用して Aspose.Cells の機能をアプリケーションに統合します。 Docker コンテナで Aspose .Cells を使用する方法を学ぶ
weight: 141
url: /ja/net/how-to-run-aspose-cells-in-aws-lambda/
---
## AWS 環境を準備する

1. AWS アカウントを登録します。
[AWS アカウントを登録する](https://aws.amazon.com/)
1. AWS アカウントにログインし、アカウントに IAM ユーザーを追加します。 AWS の公式ドキュメントを参照できます。
[IAM ユーザーを追加](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. パーミッション「AmazonS3FullAccess」を追加し、同様にEC2とElastic Beanstalkを追加し、それぞれにフルアクセスを付与します。
1. 最後のステップで、IAM ユーザー名、キー、キー ID、および「credentials.csv」ファイルを取得したことを確認します。これらを適切に保存する必要があります。
ここで、IAM ユーザーに S3、EC2、Elastic Beanstalk、フル アクセスがあることを確認します。見る：
   
**![AWS アクセス](AwsAccess.png)**

## AWS Toolkit for Visual Studio をインストールする

1. Visual Studio 2019 以降のバージョンをインストールします。
1.  AWS Toolkit for Visual Studio をダウンロードしてインストールします。
[AWS ツールキット](https://aws.amazon.com/visualstudio/)

## AWS Lambda で実行するプロジェクトを作成する

1. Visual Studio で ASP.NET コア Web アプリケーションを作成し、テスト コードを記述し、nuget から Aspose.Cells を取得します。

1. テスト プロジェクトがローカル マシンで正常に実行されることを確認してから、AWS Elastic Beanstalk にデプロイします。
プロジェクト名を右クリックし、[AWS Elastic Beanstalk に公開] を選択します。 (このオプションは、AWS Toolkit for Visual Studio をインストールした後にのみ存在します)。
1.  AWS アカウントと IAM ユーザーを使用して新しいユーザーを追加する必要があります。前の手順で取得した「credentials.csv」ファイルをインポートできます。
1. 公開に成功すると、次のようなリンク アドレスが表示されます: `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
リンクが有効になるまで 10 分待ってから、アクセスしてください。
