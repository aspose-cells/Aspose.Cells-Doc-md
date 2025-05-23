---
title: إسترداد بيانات اتصال SQL
type: docs
weight: 10
url: /ar/net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

يمكن لـ Aspose.Cells مساعدتك في استرداد بيانات اتصال SQL. يشمل ذلك أي وكل البيانات المطلوبة للاتصال بخادم SQL، على سبيل المثال، **رابط الخادم**, **اسم المستخدم**, **اسم الجدول**, **استعلام SQL كامل**, **نوع الاستعلام**, **موقع الجدول**, و**اسم النطاق المسمى** المرتبط به.

{{% /alert %}}

في برنامج Microsoft Excel، الاتصال بقاعدة بيانات عن طريق:

1. النقر على القائمة **البيانات** واختيار **من مصادر أخرى** تلاها **من خادم SQL**.
1. ثم اختيار **البيانات** تلاها **اتصالات**.
1. استخدام معالج الاتصالات للاتصال بقاعدة البيانات وإنشاء استعلام قاعدة البيانات.

توفر Aspose.Cells خاصية Workbook.DataConnections لاسترداد الاتصالات الخارجية. يُعيد مجموعة من الكائنات ExternalConnection في الدفتر.

إذا احتوى كائن ExternalConnection على بيانات اتصال SQL، يمكن تحويل نوعه إلى كائن DBConnection ويمكن استخدام خصائصه لاسترداد أمر قاعدة بيانات، نوع الأمر، وصف الاتصال، معلومات الاتصال، بيانات الاعتماد، وما إلى ذلك.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
