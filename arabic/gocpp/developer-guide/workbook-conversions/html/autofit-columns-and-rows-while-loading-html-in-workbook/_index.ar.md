---
title: تلقائي ضبط الأعمدة والصفوف عند تحميل HTML في Workbook باستخدام Golang عبر C++
linktitle: تناسب تلقائي للأعمدة والصفوف أثناء تحميل HTML في مصنف
type: docs
weight: 120
url: /ar/go-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: تعلم كيفية التوفيق التلقائي للأعمدة والصفوف أثناء تحميل HTML في دفتر العمل باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تلائم الأعمدة والصفوف أثناء تحميل ملف HTML داخل كائن المفكرة. يرجى ضبط الخاصية [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) إلى **true** لهذا الغرض.

## **تلائم الأعمدة والصفوف تلقائيًا أثناء تحميل HTML في دفتر العمل**

الكود النموذجي التالي يقوم أولاً بتحميل HTML النموذجي في Workbook بدون أي خيارات تحميل وحفظه في تنسيق XLSX. ثم يقوم مرة أخرى بتحميل HTML النموذجي في Workbook ولكن هذه المرة، يقوم بتحميل الـ HTML بعد ضبط الخاصية [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) على **true** وحفظه في تنسيق XLSX. يرجى تنزيل كل من ملفات الإكسيل الناتجة، أي [ملف الإكسيل الناتج بدون تناسب الأعمدة والصفوف](outputWithout_AutoFitColsAndRows.xlsx) و [ملف الإكسيل الناتج مع تناسب الأعمدة والصفوف](outputWith_AutoFitColsAndRows.xlsx). اللقطة الشاشية التالية توضح تأثير الخاصية [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) على كل من ملفات الإكسيل الناتجة.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutofitColumnsAndRowsWhileLoadingHtmlInWorkbook.go" >}}
