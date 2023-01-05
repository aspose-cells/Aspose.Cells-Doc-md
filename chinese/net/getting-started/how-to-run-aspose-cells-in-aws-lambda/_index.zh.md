---
title: 如何在 AWS Lambda 中运行 Aspose.Cells
type: docs
description: 使用 Docker 将 Aspose.Cells 功能集成到您的应用程序中，无论您的开发堆栈中采用何种技术。了解如何在 Docker 容器中使用 Aspose .Cells
weight: 141
url: /zh/net/how-to-run-aspose-cells-in-aws-lambda/
---
## 准备 AWS 环境

1. 注册一个 AWS 账户：
[注册AWS账户](https://aws.amazon.com/)
1. 登录您的 AWS 账户，在您的账户下添加一个 IAM 用户。可以参考AWS官方文档：
[添加 IAM 用户](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. 添加权限“AmazonS3FullAccess”，请使用相同的方法，添加EC2和Elastic Beanstalk，每个都有完全访问权限。
1. 在最后一步，确保您获得了 IAM 用户名、密钥、密钥 ID 和“credentials.csv”文件，您需要妥善保存它们。
现在确保您的 IAM 用户具有 S3、EC2、Elastic Beanstalk 的完全访问权限。看：
   
**![AWS 访问](AwsAccess.png)**

## 安装适用于 Visual Studio 的 AWS 工具包

1. 安装 Visual Studio 2019 或以上版本。
1. 下载并安装 AWS Toolkit for Visual Studio：
[AWS 工具包](https://aws.amazon.com/visualstudio/)

## 创建一个在 AWS Lambda 中运行的项目

1. 在Visual Studio中创建一个ASP.NET Core Web Application，编写测试代码，从nuget获取Aspose.Cells。

1. 确保测试项目在您的本地机器上运行良好，然后将其部署到 AWS Elastic Beanstalk：
右键单击项目名称，选择“发布到 AWS Elastic Beanstalk”。 （此选项仅在您安装 AWS Toolkit for Visual Studio 后存在）。
1. 您需要使用您的 AWS 账户和 IAM 用户添加一个新用户，您可以导入在上一步中获得的“credentials.csv”文件。
1. 发布成功，你会得到一个链接地址：`http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
等待10分钟链接生效，即可访问！
