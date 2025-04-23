---
title: تحويل إكسل إلى JSON
type: docs
weight: 20
url: /ar/java/convert-excel-to-json/
description: تعلم كيفية تحويل ملف Excel إلى JSON باستخدام Aspose.Cells for Java API.
keywords: Java تصدير الورقة العمل إلى json، تحويل Excel إلى JSON باستخدام Java، حفظ Excel إلى JSON في Java، تحويل الورقة العمل إلى JSON باستخدام Java، حفظ الورقة العمل إلى JSON في Java، تصدير Excel إلى JSON via Java.
---

{{% alert color="primary" %}}

تدعم Aspose.Cells تحويل دفتر العمل إلى ملف Json (كائن التبادل بيانات الجافا) .

{{% /alert %}}

## **كيفية تحويل دفتر العمل في Excel إلى JSON**

لا حاجة للتساؤل عن كيفية تحويل مصنف Excel إلى JSON، لأن مكتبة Aspose.Cells للغة Java تتخذ أفضل قرار. توفر واجهة برمجة التطبيقات Aspose.Cells للغة Java دعمًا لتحويل جداول البيانات إلى تنسيق JSON. لتصدير مصنف العمل إلى JSON، قم بتمرير [**SaveFormat.JSON**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) كثاني معلمة لطريقة [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.lang.String-int-). يمكنك أيضًا استخدام الطبقة [**JsonSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonSaveOptions) لتحديد الإعدادات الإضافية لتصدير ورقة العمل إلى JSON.

المثال التالي يوضح تصدير ورقة العمل إكسل إلى Json. يرجى الرجوع إلى الكود لتحويل [الملف المصدر](sample.xlsx) إلى ملف Json الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON.java" >}}

المثال التالي الذي يستخدم فئة JsonSaveOptions لتحديد إعدادات إضافية يوضح تصدير دفتر العمل من Excel إلى JSON. يرجى الاطلاع على الكود لتحويل [الملف المصدر](sample.xlsx) إلى ملف Json الذي تم إنشاؤه بواسطة الكود للإحالة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON2.java" >}}
{{< app/cells/assistant language="java" >}}
