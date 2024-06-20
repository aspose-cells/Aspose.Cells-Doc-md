---
title: تناسب تلقائي للأعمدة والصفوف أثناء تحميل HTML في مصنف
type: docs
weight: 120
url: /ar/python-net/autofit-columns-and-rows-while-loading-html-in-workbook/
description: يشير هذا الموضوع إلى كيفية تكييف الأعمدة والصفوف أثناء تحميل ملف HTML في دفتر العمل باستخدام Aspose.Cells للبيثون via NET.
keywords: تكييف الأعمدة والصفوف أثناء تحميل ملف HTML في دفتر العمل، تكييف الأعمدة والصفوف لتحميل ملف HTML.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تلائم الأعمدة والصفوف أثناء تحميل ملف HTML داخل كائن المفكرة. يرجى ضبط الخاصية [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) إلى **true** لهذا الغرض.

## **تلائم الأعمدة والصفوف تلقائيًا أثناء تحميل HTML في دفتر العمل**

الكود النموذجي التالي يقوم أولاً بتحميل HTML النموذجي في Workbook بدون أي خيارات تحميل وحفظه في تنسيق XLSX. ثم يقوم مرة أخرى بتحميل HTML النموذجي في Workbook ولكن هذه المرة، يقوم بتحميل الـ HTML بعد ضبط الخاصية [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) على **true** وحفظه في تنسيق XLSX. يرجى تنزيل كل من ملفات الإكسيل الناتجة، أي [ملف الإكسيل الناتج بدون تناسب الأعمدة والصفوف](outputWithout_AutoFitColsAndRows.xlsx) و [ملف الإكسيل الناتج مع تناسب الأعمدة والصفوف](outputWith_AutoFitColsAndRows.xlsx). اللقطة الشاشية التالية توضح تأثير الخاصية [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) على كل من ملفات الإكسيل الناتجة.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.py" >}}

