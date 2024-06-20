---
title: إظهار علامة الفتح في الخلايا
type: docs
weight: 70
url: /ar/net/show-leading-apostrophe-in-cells/
---

في Microsoft Excel، تكون علامة الفتح الأولى في قيمة الخلية مخفية. توفر Aspose.Cells ميزة عرض علامة الفتح افتراضيًا. لهذا الغرض، يوفر الواجهة البرمجية الخاصية [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle). تشير هذه الخاصية ما إذا كان تعيين الخاصية [QuotePrefix](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) عند إدخال قيمة السلسلة التي تبدأ بعلامة اقتباس واحدة إلى الخلية. تعيين الخاصية [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) إلى **false** سيعرض علامة الفتح الأولى في ملف الإكسل الناتج.

الصورة الملتقطة التالية تُظهر ملف إكسل الناتج مع علامة الفتح المرئية.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

الكود المقتطف التالي يظهر هذا عن طريق إضافة البيانات بواسطة العلامات الذكية في ملف إكسل المصدر. يتم إرفاق ملفات إكسل المصدر والإخراج للرجوع إليها.

[ملف المصدر](98107425.xlsx)

[ملف الإخراج](98107426.xlsx)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

يتم تقديم تنفيذ فئة *DataObject* تحت:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
