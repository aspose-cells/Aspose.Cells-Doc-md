---
title: تحميل الدفتر بحجم ورقة الطابعة المحدد
type: docs
weight: 430
url: /ar/python-net/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

يمكنك تحديد حجم ورق الطابعة الخاص بك أثناء تحميل دفتر العمل الخاص بك باستخدام الطريقة [**LoadOptions.set_paper_size()**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/set_paper_size). يُرجى ملاحظة أنه إذا قمت بإنشاء ملف جديد في MS Excel، ستجد أن حجم الورق هو نفس إعداد طابعة الافتراضي في جهازك.

{{% /alert %}}

يوضح الكود النموذجي التالي استخدام الطريقة [**LoadOptions.set_paper_size()**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/set_paper_size). يقوم أولاً بإنشاء دفتر عمل، ثم يحفظه في تدفق الذاكرة في تنسيق XLSX. ثم يقوم بتحميله بحجم ورق A5 ويحفظه في تنسيق PDF. ثم يقوم بتحميله مرة أخرى بحجم ورق A3 ويحفظه مرة أخرى في تنسيق PDF. إذا فتحت ملفات PDF الناتجة وفحصت أحجامها، سترى أنها مختلفة. إحداها A5 والأخرى A3. يُرجى تحميل [ملف PDF الناتج A5](5115234.pdf) و [ملف PDF الناتج A3](5115233.pdf) الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-LoadWorkbookWithPrinterSize-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
