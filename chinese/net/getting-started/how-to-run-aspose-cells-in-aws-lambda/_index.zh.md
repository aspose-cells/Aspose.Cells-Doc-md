---
title: 在AWS Lambda中运行Aspose.Cells的方法
type: docs
description: "将Aspose.Cells的功能集成到您的应用程序中，无论开发堆栈中使用的是什么技术，都可以使用Docker。了解如何在Docker容器中使用Aspose .Cells。"
weight: 141
url: /zh/net/how-to-run-aspose-cells-in-aws-lambda/
---

## 准备AWS环境

1. 注册AWS账号: 
[注册AWS账号](https://aws.amazon.com/)
1. 登录您的AWS账号，在您的账户下添加IAM用户。您可以参考AWS官方文档:
[添加IAM用户](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. 添加权限“AmazonS3FullAccess”，请使用相同方式，添加EC2和弹性Beanstalk，每个都有完全访问权限。
1. 在最后一步，确保您获得IAM用户名、密钥、密钥ID和“credentials.csv”文件，需要妥善保存它们。
   现在确保您的IAM用户具有S3、EC2、弹性Beanstalk的完全访问权限。见:

**![AWS访问](AwsAccess.png)**

## 在 Visual Studio 中安装 AWS Toolkit

1. 安装 Visual Studio 2019 或更高版本。
1. 下载并安装 AWS Toolkit for Visual Studio: 
[AWS Toolkit](https://aws.amazon.com/visualstudio/)

## 创建在 AWS Lambda 中运行的项目

1. 在 Visual Studio 中创建一个 ASP.NET Core Web 应用程序，编写测试代码，从 nuget 中获取 Aspose.Cells。

1. 确保测试项目在本地机器上可以正常运行，然后将其部署到 AWS 弹性 Beanstalk:
   右键单击项目名称，选择“发布到 AWS 弹性 Beanstalk”。(此选项仅在安装 AWS Toolkit for Visual Studio 后才会存在)。 
1. 您需要使用您的AWS账户和IAM用户添加新用户，您可以导入在先前步骤中获得的“credentials.csv”文件。 
1. 发布成功，您将获得一个类似的链接地址:`http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`。
   等待10分钟使链接生效，然后您就可以访问它了!
{{< app/cells/assistant language="csharp" >}}
