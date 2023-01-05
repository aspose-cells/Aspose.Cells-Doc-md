---
title: استرداد بيانات اتصال SQL
type: docs
weight: 10
url: /ar/net/retrieving-sql-connection-data/
---
{{% alert color="primary" %}}

 يمكن أن يساعدك Aspose.Cells في استرداد بيانات اتصال SQL. يتضمن ذلك أي وكافة البيانات المطلوبة لإجراء اتصال بخادم SQL ، على سبيل المثال ،**URL الخادم**, **اسم االمستخدم**, **اسم الطاولة**, **استعلام SQL كامل**, **نوع الاستعلام**, **موقع الجدول** ، و**اسم النطاق المسمى** المرتبطة بها.

{{% /alert %}}

في Microsoft Excel ، اتصل بقاعدة بيانات عن طريق:

1.  النقر فوق ملف**بيانات** القائمة والاختيار**من مصادر أخرى** تليها**من SQL Server**.
1.  ثم حدد**بيانات** تليها**روابط**.
1. استخدم معالج الاتصالات للاتصال بقاعدة البيانات وإنشاء استعلام قاعدة بيانات.

يوفر Aspose.Cells الخاصية Workbook.DataConnections لاسترجاع الوصلات الخارجية. تقوم بإرجاع مجموعة من كائنات ExternalConnection في المصنف.

إذا كان كائن ExternalConnection يحتوي على بيانات اتصال SQL ، فيمكن أن يكون نوع لصق لكائن DBConnection ويمكن استخدام خصائصه لاسترداد أمر قاعدة البيانات ونوع الأمر ووصف الاتصال ومعلومات الاتصال وبيانات الاعتماد وما إلى ذلك.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}
