---
title: تحميل الدفتر بحجم ورقة الطابعة المحدد
type: docs
weight: 430
url: /ar/go-cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

يمكنك تحديد حجم ورقة الطابعة المفضل لديك أثناء تحميل دفتر العمل باستخدام طريقة [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/). يرجى ملاحظة، إذا قمت بإنشاء ملف جديد في MS Excel، ستجد أن حجم الورقة هو نفسه إعدادات الطابعة الافتراضية في جهازك.

{{% /alert %}}

يوضح الكود النموذجي التالي استخدام طريقة [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/). ينشئ أولاً دفتر عمل ثم يحفظه في تدفق الذاكرة بصيغة XLSX. ثم يحمله بحجم ورق A5 ويحفظه بصيغة PDF. ثم يعيده تحميله بحجم ورق A3 ويحفظه مرة أخرى بصيغة PDF. إذا فتحت ملفات PDF الناتجة وتحققت من حجم الورق فيها، سترى أنها مختلفة. واحدة A5 والأخرى A3. يرجى تحميل ملف [PDF الناتج A5](PrinterSize-a5_out.pdf) و[PDF الناتج A3](PrinterSize-a3_out.pdf) الذي أنشأه الكود للمرجع.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookWithPrinterSize.go" >}}
