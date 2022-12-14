---
title: احتواء تلقائي للأعمدة والصفوف أثناء تحميل HTML في المصنف
type: docs
weight: 120
url: /ar/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---
## **سيناريوهات الاستخدام الممكنة**

يمكنك احتواء الأعمدة والصفوف تلقائيًا أثناء تحميل ملف HTML داخل كائن المصنف. يرجى ضبط**[HtmlLoadOptions.AutoFitColsAndRows] (https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** الملكية ل**حقيقي**لهذا الغرض.

## **احتواء تلقائي للأعمدة والصفوف أثناء تحميل HTML في المصنف**

 يقوم نموذج التعليمات البرمجية التالي أولاً بتحميل نموذج HTML في المصنف دون أي خيارات تحميل وحفظه بتنسيق XLSX. ثم يقوم مرة أخرى بتحميل نموذج HTML في المصنف ولكن هذه المرة ، يقوم بتحميل HTML بعد تعيين ملف**[HtmlLoadOptions.AutoFitColsAndRows] (https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** الملكية ل**حقيقي**ويحفظه بتنسيق XLSX. يرجى تنزيل كل من ملفات إكسل الناتجة مثل[إخراج ملف Excel بدون AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) و[إخراج ملف Excel مع AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx) . تُظهر لقطة الشاشة التالية تأثير**[HtmlLoadOptions.AutoFitColsAndRows] (https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)**الخاصية على كلا ملفات إكسل الإخراج.

![ما يجب القيام به: image_بديل_نص](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

