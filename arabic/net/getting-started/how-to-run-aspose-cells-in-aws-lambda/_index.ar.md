---
title: كيفية تشغيل Aspose.Cells في AWS Lambda
type: docs
description: "دمج وظائف Aspose.Cells في تطبيقك باستخدام Docker بغض النظر عن التكنولوجيا المستخدمة في مكدس التطوير الخاص بك. تعرف على كيفية استخدام Aspose. Cells في حاوية Docker."
weight: 141
url: /ar/net/how-to-run-aspose-cells-in-aws-lambda/
---

## إعداد بيئة AWS

1. سجّل في حساب AWS: 
[سجل حساب AWS](https://aws.amazon.com/)
1. قم بتسجيل الدخول إلى حسابك في AWS، وأضف مستخدم IAM تحت حسابك. يمكنك الرجوع إلى الوثيقة الرسمية لـ AWS:
[أضف مستخدم IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. إضافة إذن "AmazonS3FullAccess"، يرجى استخدام نفس الطريقة، إضافة إذن EC2 وElastic Beanstalk، والوصول الكامل لكل منهما.
1. في الخطوة الأخيرة، تأكد من الحصول على اسم مستخدم IAM ومفتاح وهوية المفتاح، وملف “credentials.csv”، يجب عليك حفظها بشكل جيد.
   تأكد الآن من أن مستخدم IAM الخاص بك لديه وصول كامل إلى S3 وEC2 وElastic Beanstalk. انظر:

**![الوصول إلى AWS](AwsAccess.png)**

## قم بتثبيت AWS Toolkit for Visual Studio

1. قم بتثبيت برنامج Visual Studio 2019 أو أحدث.
1. قم بتنزيل وتثبيت AWS Toolkit for Visual Studio: 
[AWS Toolkit](https://aws.amazon.com/visualstudio/)

## أنشئ مشروع يعمل في AWS Lambda

1. قم بإنشاء تطبيق ويب ASP.NET Core في Visual Studio, قم بكتابة رمز اختباري، واحصل على Aspose.Cells من نوجيت.

1. تأكد من أن مشروع الاختبار يعمل بشكل جيد على جهازك المحلي، ثم قم بنشره إلى AWS Elastic Beanstalk:
   انقر بزر الماوس الأيمن على اسم المشروع، اختر "النشر إلى AWS Elastic Beanstalk". (سيظهر هذا الخيار فقط بعد تثبيت AWS Toolkit for Visual Studio). 
1. ستحتاج إلى إضافة مستخدم جديد باستخدام حساب AWS الخاص بك ومستخدم IAM، يمكنك استيراد ملف "credentials.csv" الذي حصلت عليه في الخطوة السابقة. 
1. نجاح النشر، ستحصل على رابط عنوان مثل: `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
   انتظر 10 دقائق حتى يتم التأثير على الرابط، ثم يمكنك زيارته!
{{< app/cells/assistant language="csharp" >}}
