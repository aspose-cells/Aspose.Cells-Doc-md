---
title: Как запустить Aspose.Cells в AWS Lambda
type: docs
description: "Интегрируйте функциональность Aspose.Cells в свое приложение, используя Docker, независимо от используемых технологий в вашем стеке разработки. Узнайте, как использовать Aspose.Cells в контейнере Docker."
weight: 141
url: /ru/net/how-to-run-aspose-cells-in-aws-lambda/
---

## Подготовка среды AWS

1. Зарегистрируйте учетную запись AWS: 
[Зарегистрировать учетную запись AWS](https://aws.amazon.com/)
1. Войдите в свою учетную запись AWS, добавьте IAM-пользователя в вашей учетной записи. Вы можете обратиться к официальному документу AWS:
[Добавить IAM-пользователя](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. Добавьте разрешение “AmazonS3FullAccess”, пожалуйста, используйте тот же способ, добавьте полный доступ к EC2 и Elastic Beanstalk для каждого из них.
1. На последнем шаге убедитесь, что у вас есть имя IAM-пользователя, ключ, идентификатор ключа и файл “credentials.csv”, вам нужно хорошо их сохранить.
   Теперь убедитесь, что ваш IAM-пользователь имеет доступ к S3, EC2, Elastic Beanstalk. см.:

**![Доступ AWS](AwsAccess.png)**

## Установка AWS Toolkit для Visual Studio

1. Установите Visual Studio 2019 или более позднюю версию.
1. Скачайте и установите AWS Toolkit для Visual Studio: 
[AWS Toolkit](https://aws.amazon.com/visualstudio/)

## Создание проекта, запускаемого в AWS Lambda

1. Создайте в Visual Studio веб-приложение ASP.NET Core, напишите тестовый код, получите Aspose.Cells из NuGet.

1. Убедитесь, что тестовый проект работает нормально на вашем локальном компьютере, затем разверните его в AWS Elastic Beanstalk:
   Щелкните правой кнопкой мыши по названию проекта, выберите "Опубликовать в AWS Elastic Beanstalk". (Эта опция появится только после установки AWS Toolkit для Visual Studio). 
1. Вам нужно будет добавить нового пользователя с вашей учетной записью AWS и IAM пользователя, вы можете импортировать файл "credentials.csv", который вы получили на предыдущем шаге. 
1. Успешная публикация, вы получите ссылку типа: `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
   Подождите 10 минут, чтобы ссылка начала действовать, затем вы сможете посетить ее!
{{< app/cells/assistant language="csharp" >}}
