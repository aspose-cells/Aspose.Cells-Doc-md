---
title: تناسب تلقائي للأعمدة والصفوف أثناء تحميل HTML في مصنف
type: docs
weight: 120
url: /ar/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تلائم الأعمدة والصفوف أثناء تحميل ملف HTML داخل كائن المفكرة. يرجى ضبط الخاصية [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) إلى **true** لهذا الغرض.

## **تلائم الأعمدة والصفوف تلقائيًا أثناء تحميل HTML في دفتر العمل**

الكود النموذجي التالي يقوم أولاً بتحميل HTML النموذجي في Workbook بدون أي خيارات تحميل وحفظه في تنسيق XLSX. ثم يقوم مرة أخرى بتحميل HTML النموذجي في Workbook ولكن هذه المرة، يقوم بتحميل الـ HTML بعد ضبط الخاصية [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) على **true** وحفظه في تنسيق XLSX. يرجى تنزيل كل من ملفات الإكسيل الناتجة، أي [ملف الإكسيل الناتج بدون تناسب الأعمدة والصفوف](outputWithout_AutoFitColsAndRows.xlsx) و [ملف الإكسيل الناتج مع تناسب الأعمدة والصفوف](outputWith_AutoFitColsAndRows.xlsx). اللقطة الشاشية التالية توضح تأثير الخاصية [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) على كل من ملفات الإكسيل الناتجة.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
