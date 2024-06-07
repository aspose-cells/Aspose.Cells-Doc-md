---
title: 如何在AWS Lambda中运行Aspose.Cells
type: docs
description: "将Aspose.Cells功能集成到您的应用程序中，无论开发堆栈中使用的技术是什么，都可以使用Docker。了解如何在Docker容器中使用Aspose .Cells。"
weight: 141
url: /zh/net/how-to-run-aspose-cells-in-aws-lambda/
---

## 准备AWS环境

1. 注册AWS账号: 
[注册AWS账号](https://aws.amazon.com/)
1. 登录您的AWS账号，在您的账户下添加IAM用户。您可以参考AWS官方文档:
[添加IAM用户](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. 添加权限“AmazonS3FullAccess”，请使用相同方式，为EC2和Elastic Beanstalk各添加完全访问权限。
1. 在最后一步，确保您获得IAM用户名、密钥、密钥ID和“credentials.csv”文件，您需要保存它们。
   现在确保您的IAM用户具有S3、EC2、Elastic Beanstalk的完全访问权限。请参阅:

**![AWS访问](AwsAccess.png)**

## 为Visual Studio安装AWS Toolkit

1. 安装2019年或更高版本的Visual Studio。
1. 下载并安装AWS Toolkit for Visual Studio: 
[AWS Toolkit](https://aws.amazon.com/visualstudio/)

## 在AWS Lambda中创建一个项目

1. 在Visual Studio中创建一个ASP.NET Core Web应用程序，在nuget中获取Aspose.Cells，编写测试代码。

1. 确保测试项目在本地机器上正常运行，然后将其部署到AWS Elastic Beanstalk中:
   右键单击项目名称，选择"发布到AWS Elastic Beanstalk"（此选项仅在安装了Visual Studio的AWS工具包后才存在）。 
1. 您需要使用您的AWS帐户和IAM用户添加一个新用户，可以导入您在上一步骤中获取的"credentials.csv"文件。 
1. 发布成功后，您将获得一个类似`http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`的链接地址。
   等待10分钟使链接生效，然后您就可以访问它了！
