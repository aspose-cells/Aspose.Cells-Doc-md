---
title: تحويل إكسل إلى HTML مع تلميح باستخدام C++
linktitle: تحويل Excel إلى HTML مع تلميح سريع
type: docs
weight: 200
url: /ar/go-cpp/convert-excel-to-html-with-tooltip/
description: تحويل إكسل إلى HTML أثناء إضافة تلميحات باستخدام Aspose.Cells باستخدام C++.
---

## **تحويل Excel إلى HTML مع تلميحة**

 قد توجد حالات يتم فيها قطع النص في HTML الناتج وترغب في عرض النص الكامل كتلميح عند التمرير فوقه. تدعم Aspose.Cells ذلك عن طريق توفير خاصية [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/). تعيين الخاصية [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/) إلى **true** سيضيف النص الكامل كتلميح في HTML الناتج.

تُظهر الصورة التالية التلميح السريع في ملف HTML المولد.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

الرمز التالي يحمل ملف Excel [المصدر](98107416.xlsx) ويولد ملف HTML [الناتج](98107417.zip) مع أداة التلميح.

الكود المثالي

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToHtmlWithTooltip.go" >}}
