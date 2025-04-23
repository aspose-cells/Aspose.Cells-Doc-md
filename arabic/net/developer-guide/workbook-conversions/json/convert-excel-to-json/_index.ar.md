---
title: تحويل إكسل إلى JSON
type: docs
weight: 300
url: /ar/net/convert-excel-to-json/
description: تعلم كيفية تحويل ملف إكسل إلى JSON باستخدام Aspose.Cells.
keywords: تصدير الدفتر إلى JSON بدون Office 2013، Office 2016، Office 2019 و Office 365
---

{{% alert color="primary" %}}

تدعم Aspose.Cells تحويل دفتر العمل إلى ملف Json (كائن التبادل بيانات الجافا) .

{{% /alert %}}

## **تحويل دفتر العمل Excel إلى JSON**

لا داعي للتساؤل حول كيفية تحويل دفتر الأوامر إكسل إلى JSON، لأن مكتبة Apose.Cells for .NET لديها أفضل قرار. يقدم واجهة برمجة التطبيقات Aspose.Cells الدعم لتحويل جداول البيانات إلى تنسيق JSON. لتصدير دفتر الأوامر إلى JSON، قم بتمرير [**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) كالمعلمة الثانية للطريقة [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). يمكنك أيضًا استخدام فئة [**JsonSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/JsonSaveoptions) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى JSON.

المثال التالي يوضح تصدير دفتر العمل من Excel إلى Json. يرجى الاطلاع على الكود لتحويل [الملف المصدر](sample.xlsx) إلى ملف Json الذي تم إنشاؤه بواسطة الكود للإحالة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New.cs" >}}

المثال التالي الذي يستخدم فئة JsonSaveOptions لتحديد إعدادات إضافية يوضح تصدير دفتر العمل من Excel إلى JSON. يرجى الاطلاع على الكود لتحويل [الملف المصدر](sample.xlsx) إلى ملف Json الذي تم إنشاؤه بواسطة الكود للإحالة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New2.cs" >}}

{{< app/cells/assistant language="csharp" >}}
