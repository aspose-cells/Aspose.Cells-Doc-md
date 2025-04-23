---
title: تناسب تلقائي للأعمدة والصفوف أثناء تحميل HTML في مصنف
type: docs
weight: 70
url: /ar/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تلائم تلقائيًا الأعمدة والصفوف أثناء تحميل ملف HTML داخل كائن [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). يرجى ضبط الخاصية [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) إلى **true** لهذا الغرض.

## **تلائم الأعمدة والصفوف تلقائيًا أثناء تحميل HTML في دفتر العمل**

يحمل الكود العيني أدناه الصورة العينية الأولية العينية في المفكرة دون أي خيارات تحميل ويحفظها بتنسيق XLSX. ثم يحمل الصورة العينية العينية مرة أخرى في المفكرة ولكن هذه المرة، يحمل الصورة العينية الأولية بعد ضبط الخاصية [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) إلى **true** ويحفظها بتنسيق XLSX. يرجى تنزيل كلا ملفات إكسيل الناتجة، أي [ملف إكسيل الناتج بدون تلائم تلقائي للأعمدة والصفوف](outputWithout_AutoFitColsAndRows.xlsx) و [ملف إكسيل الناتج مع تلائم تلقائي للأعمدة والصفوف](outputWith_AutoFitColsAndRows.xlsx). توضح اللقطة الشاشية التالية تأثير الخاصية [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) على كلا ملفات إكسيل الناتج.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
{{< app/cells/assistant language="java" >}}
