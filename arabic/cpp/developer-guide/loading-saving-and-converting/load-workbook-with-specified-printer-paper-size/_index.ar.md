---
title: تحميل الدفتر بحجم ورقة الطابعة المحدد
type: docs
weight: 430
url: /ar/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

يمكنك تحديد حجم ورق الطابعة الخاص بك أثناء تحميل دفتر العمل الخاص بك باستخدام الطريقة [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). يُرجى ملاحظة أنه إذا قمت بإنشاء ملف جديد في MS Excel، ستجد أن حجم الورق هو نفس إعداد طابعة الافتراضي في جهازك.

{{% /alert %}}

يوضح رمز المثال التالي استخدام طريقة [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). ينشئ في البداية دفتر عمل، ثم يحفظه في تدفق الذاكرة بتنسيق XLSX. ثم يتم تحميله بحجم ورقة A5 وحفظه بصيغة PDF. ثم يتم تحميله مرة أخرى بحجم ورقة A3 وحفظه مرة أخرى كملف PDF. إذا فتحت ملفات PDF الناتجة وتحقق من حجم الورق، ستجد أنها مختلفة. واحدة بحجم A5 والأخرى بحجم A3. يرجى تحميل [ملف PDF الناتج من A5](PrinterSize-a5_out.pdf) و[ملف PDF الناتج من A3](PrinterSize-a3_out.pdf) الناتج عن الكود كمراجع.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
