---
title: إسترداد بيانات اتصال SQL
type: docs
weight: 10
url: /ar/python-net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

يمكن لـ Aspose.Cells لـ Python via .NET مساعدتك في استرجاع بيانات اتصال SQL. يشمل ذلك أي وجميع البيانات المطلوبة لإجراء اتصال بخادم SQL، على سبيل المثال، **عنوان URL للخادم**، **اسم المستخدم**، **اسم الجدول**، **استعلام SQL كامل**، **نوع الاستعلام**، **موقع الجدول**، و **اسم النطاق المسمى** المرتبط به.

{{% /alert %}}

في برنامج Microsoft Excel، الاتصال بقاعدة بيانات عن طريق:

1. النقر على القائمة **البيانات** واختيار **من مصادر أخرى** تلاها **من خادم SQL**.
1. ثم اختيار **البيانات** تلاها **اتصالات**.
1. استخدام معالج الاتصالات للاتصال بقاعدة البيانات وإنشاء استعلام قاعدة البيانات.

يوفر Aspose.Cells لـ Python via .NET خاصية Workbook.DataConnections لاسترجاع الاتصالات الخارجية. تعيد مجموعة من كائنات ExternalConnection في كتاب العمل.

إذا احتوى كائن ExternalConnection على بيانات اتصال SQL، يمكن تحويل نوعه إلى كائن DBConnection ويمكن استخدام خصائصه لاسترداد أمر قاعدة بيانات، نوع الأمر، وصف الاتصال، معلومات الاتصال، بيانات الاعتماد، وما إلى ذلك.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-RetrievingSQLConnectionData-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
