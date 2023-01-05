---
title: كيفية تشغيل Aspose.Cells في AWS Lambda
type: docs
description: ادمج وظيفة Aspose.Cells في تطبيقك باستخدام Docker بغض النظر عن التكنولوجيا الموجودة في حزمة التطوير الخاصة بك. تعرف على كيفية استخدام Aspose .Cells في حاوية Docker
weight: 141
url: /ar/net/how-to-run-aspose-cells-in-aws-lambda/
---
## جهز بيئة AWS

1.  تسجيل حساب AWS:
[سجّل حساب AWS](https://aws.amazon.com/)
1. قم بتسجيل الدخول إلى حساب AWS الخاص بك ، وأضف مستخدم IAM ضمن حسابك. يمكنك الرجوع إلى مستند AWS الرسمي:
[إضافة مستخدم IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. إضافة إذن "AmazonS3FullAccess" ، يرجى استخدام نفس الطريقة ، إضافة EC2 و Elastic Beanstalk ، وصول كامل لكل منهما.
1. في الخطوة الأخيرة ، تأكد من حصولك على اسم مستخدم IAM ، والمفتاح ، ومعرف المفتاح ، وملف "credentials.csv" ، فأنت بحاجة إلى حفظها جيدًا.
 تأكد الآن من أن مستخدم IAM الخاص بك لديه S3 ، EC2 ، Elastic Beanstalk ، وصول كامل. نرى:
   
**! [AWS Access] (AwsAccess.png)**

## قم بتثبيت مجموعة أدوات AWS لبرنامج Visual Studio

1. قم بتثبيت Visual Studio 2019 أو إصدار أعلى.
1.  قم بتنزيل وتثبيت مجموعة أدوات AWS لبرنامج Visual Studio:
[مجموعة أدوات AWS](https://aws.amazon.com/visualstudio/)

## أنشئ مشروعًا يعمل في AWS Lambda

1. قم بإنشاء ASP.NET Core Web Application في Visual Studio ، واكتب رمز الاختبار ، واحصل على Aspose.Cells من nuget.

1. تأكد من أن مشروع الاختبار يعمل جيدًا على جهازك المحلي ، ثم انشره في AWS Elastic Beanstalk:
انقر بزر الماوس الأيمن على اسم المشروع واختر "النشر على AWS Elastic Beanstalk". (لن يوجد هذا الخيار إلا بعد تثبيت مجموعة أدوات AWS لبرنامج Visual Studio).
1.  ستحتاج إلى إضافة مستخدم جديد بحساب AWS الخاص بك ومستخدم IAM ، ويمكنك استيراد ملف "credentials.csv" الذي تحصل عليه في الخطوة السابقة.
1. انشر النجاح ، سوف تحصل على عنوان ارتباط مثل: `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/`
 انتظر لمدة 10 دقائق حتى يتم تفعيل الرابط ، ثم يمكنك زيارته!
