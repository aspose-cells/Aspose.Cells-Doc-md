---
title: تحويل إكسل إلى JSON
type: docs
weight: 300
url: /ar/python-java/convert-excel-to-json/
description: تعلم كيفية تحويل ملف إكسل إلى JSON باستخدام Aspose.Cells for Python via Java.
keywords: تصدير الدفتر إلى JSON بدون Office 2013، Office 2016، Office 2019 و Office 365
---

{{% alert color="primary" %}}

تدعم واجهة برمجة التطبيقات Aspose.Cells for Python via Java تحويل ورقة عمل إلى ملف Json (JavaScript Object Notation).

{{% /alert %}}

## **تحويل دفتر العمل Excel إلى JSON**

لا داعي للتساؤل حول كيفية تحويل دفتر العمل في Excel إلى JSON، لأن مكتبة Aspose.Cells for Python via Java لديها أفضل قرار. توفر واجهة برمجة التطبيقات (API) لـ Aspose.Cells for Python via Java دعمًا لتحويل الجداول إلى تنسيق JSON. لتصدير دفتر العمل إلى JSON، قم بتمرير الـ [**SaveFormat.JSON**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat) كمعلمة ثانوية لطريقة [**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\)). يمكنك أيضاً استخدام الـ [**JsonSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/JsonSaveOptions) لتحديد الإعدادات الإضافية لتصدير صفحة العمل إلى JSON.

المثال التالي يوضح تصدير ورقة العمل إكسل إلى Json. يرجى الرجوع إلى الكود لتحويل [الملف المصدر](sample.xlsx) إلى ملف Json الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON.py" >}}

المثال التالي الذي يستخدم فئة JsonSaveOptions لتحديد إعدادات إضافية يوضح تصدير دفتر العمل من Excel إلى JSON. يرجى الاطلاع على الكود لتحويل [الملف المصدر](sample.xlsx) إلى ملف Json الذي تم إنشاؤه بواسطة الكود للإحالة.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON2.py" >}}
