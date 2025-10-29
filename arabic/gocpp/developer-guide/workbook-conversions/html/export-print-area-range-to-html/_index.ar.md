---
title: تصدير نطاق منطقة الطباعة إلى HTML باستخدام جولانغ عبر C++
linktitle: تصدير نطاق منطقة الطباعة إلى HTML
type: docs
weight: 60
url: /ar/go-cpp/export-print-area-range-to/
description: تعلم كيفية تصدير نطاق منطقة الطباعة إلى HTML باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

هذه حالة شائعة حيث نحتاج إلى تصدير فقط منطقة الطباعة، أي نطاق معين من الخلايا، بدلاً من الورقة بأكملها إلى HTML. تتوفر هذه الميزة حاليًا لتصنيع PDF، ومع ذلك، يمكنك الآن تنفيذ هذه المهمة لـ HTML أيضًا. أولاً، ضع منطقة الطباعة في كائن إعداد الصفحة لورقة العمل. لاحقًا، استخدم علم [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportprintareaonly/) لتصدير النطاق المحدد فقط.

## **الكود المثالي**

يحمِّل رمز النموذج التالي مصنف عمل ثم يصدر منطقة الطباعة إلى HTML. يمكن تنزيل ملف الاختبار لهذه الميزة من الرابط التالي:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportPrintAreaRangeToHtml.go" >}}
