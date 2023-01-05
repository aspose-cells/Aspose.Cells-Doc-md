---
title: استرجاع تفاصيل مصادر البيانات الخارجية
type: docs
weight: 10
url: /ar/java/retrieving-external-data-sources-details/
---
{{% alert color="primary" %}} 

في بعض الأحيان ، قد ترغب في استرداد معلومات حول مصادر البيانات الخارجية. على سبيل المثال ، قد ترغب في رؤية بيانات اتصال SQL. يمكن أن تتضمن هذه المعلومات أي أنواع من البيانات المطلوبة للاتصال بخادم SQL ، على سبيل المثال عنوان URL للخادم واسم المستخدم واسم الجدول الأساسي واستعلام SQL ونوع الاستعلام وموقع الجدول وما إلى ذلك.

يوفر Aspose.Cells بعض الاستدعاءات المفيدة لاسترداد مثل هذه التفاصيل من قواعد بيانات الشركة المرتبطة بملفات Excel النموذجية.

{{% /alert %}} 
## **استرجاع تفاصيل مصادر البيانات الخارجية**
يوضح المثال التالي كيفية الحصول على اتصال قاعدة البيانات والتفاصيل الأخرى. يستخدم المثال ملف Excel بسيطًا يحتوي على ارتباطات بمصدر بيانات خارجي (SQL Server).

عند تشغيل الكود ، تتم طباعة تفاصيل الاتصال على وحدة التحكم.

**معلومات اتصال SQL** 

![ما يجب القيام به: image_بديل_نص](retrieving-external-data-sources-details_1.png)







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrievingExternalDataSourcesDetails-RetrievingExternalDataSourcesDetails.java" >}}






