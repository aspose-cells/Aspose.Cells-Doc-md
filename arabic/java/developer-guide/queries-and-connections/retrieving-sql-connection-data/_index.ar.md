---
title: استرداد بيانات اتصال SQL
type: docs
weight: 20
url: /ar/java/retrieving-sql-connection-data/
---
{{% alert color="primary" %}} 

 يمكن أن يساعدك Aspose.Cells في استرداد بيانات اتصال SQL. يتضمن ذلك أي وجميع البيانات المطلوبة لإجراء اتصال بخادم SQL ، على سبيل المثال ،**URL الخادم**, **اسم االمستخدم**, **اسم الطاولة**, **استعلام SQL كامل**, **نوع الاستعلام**, **موقع الجدول** ، و**اسم النطاق المسمى** المرتبطة بها.

{{% /alert %}} 

في Microsoft Excel ، اتصل بقاعدة بيانات عن طريق:

1.  النقر فوق ملف**بيانات** القائمة والاختيار**من مصادر أخرى** تليها**من SQL Server**.
1.  ثم حدد**بيانات** تليها**روابط**.
1. استخدم معالج الاتصالات للاتصال بقاعدة البيانات وإنشاء استعلام قاعدة بيانات.

**إظهار خيار اتصال SQL في Microsoft Excel** 

![ما يجب القيام به: image_بديل_نص](retrieving-sql-connection-data_1.png)

يوفر Aspose.Cells طريقة Workbook.getDataConnections () لاسترجاع الوصلات الخارجية. تقوم بإرجاع مجموعة من كائنات ExternalConnection في المصنف.

إذا كان كائن ExternalConnection يحتوي على بيانات اتصال SQL ، فيمكن أن يكون نوع لصق في كائن DBConnection خصائصه المستخدمة لاسترداد أمر قاعدة البيانات ، ونوع الأمر ، ووصف الاتصال ، ومعلومات الاتصال ، وبيانات الاعتماد ، وما إلى ذلك.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}






