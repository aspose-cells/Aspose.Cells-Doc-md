---
title: إسترداد بيانات اتصال SQL
type: docs
weight: 20
url: /ar/java/retrieving-sql-connection-data/
---

{{% alert color="primary" %}} 

يمكن لـ Aspose.Cells مساعدتك في استرجاع بيانات اتصال SQL. يشمل ذلك أي بيانات مطلوبة للاتصال بخادم SQL، على سبيل المثال، **عنوان URL الخادم**، **اسم المستخدم**، **اسم الجدول**، **استعلام SQL كامل**، **نوع الاستعلام**، **موقع الجدول**، و**اسم التدرج المسمى** المرتبط به.

{{% /alert %}} 

في برنامج Microsoft Excel، الاتصال بقاعدة بيانات عن طريق:

1. النقر على القائمة **البيانات** واختيار **من مصادر أخرى** تلاها **من خادم SQL**.
1. ثم اختيار **البيانات** تلاها **اتصالات**.
1. استخدام معالج الاتصالات للاتصال بقاعدة البيانات وإنشاء استعلام قاعدة البيانات.

**عرض الخيارات الخاصة بالاتصال بقاعدة بيانات SQL في Microsoft Excel** 

![todo:image_alt_text](retrieving-sql-connection-data_1.png)

توفر Aspose.Cells طريقة Workbook.getDataConnections() لاسترجاع الاتصالات الخارجية. تُرجع مجموعة من كائنات ExternalConnection في الدفتر.

إذا كان كائن ExternalConnection يحتوي على بيانات اتصال SQL، فيمكن تحويله إلى كائن DBConnection واستخدام خصائصه لاسترجاع أمر قاعدة البيانات، نوع الأمر، وصف الاتصال، معلومات الاتصال، بيانات الاعتماد، وما إلى ذلك.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}






{{< app/cells/assistant language="java" >}}
