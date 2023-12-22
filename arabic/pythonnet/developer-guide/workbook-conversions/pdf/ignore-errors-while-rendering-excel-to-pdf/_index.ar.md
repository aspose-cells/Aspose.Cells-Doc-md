---
title: تجاهل الأخطاء أثناء تقديم Excel إلى PDF
type: docs
weight: 80
url: /ar/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: تعرف على كيفية تجاهل الأخطاء أثناء عرض Excel على PDF مع Aspose.Cells for Python via .NET API.
keywords: Python Ignore Errors while Rendering Excel to PDF, Ignore Errors while saving Excel to PDF using Python, Python Ignore Errors while converting Excel to PDF, Ignore Errors for Excel to PDF in python
---
##  **سيناريوهات الاستخدام المحتملة**

 في بعض الأحيان، عند تحويل ملف Excel الخاص بك إلى PDF، تحدث أخطاء أو استثناءات وتنتهي عملية التحويل. يمكنك تجاهل كافة هذه الأخطاء أثناء عملية التحويل باستخدام[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)ملكية. بهذه الطريقة ستكتمل عملية التحويل بسلاسة دون حدوث أي خطأ أو استثناء ولكن قد يحدث فقدان للبيانات. لذلك، يرجى استخدام هذه الخاصية فقط إذا لم يكن فقدان البيانات أمرًا بالغ الأهمية بالنسبة لك.

##  **تجاهل الأخطاء أثناء تقديم Excel إلى PDF**

 الكود التالي يقوم بتحميل[عينة من ملف إكسل](55541778.xlsx) لكن نموذج ملف Excel خاطئ ويؤدي إلى حدوث خطأ أثناء[التحويل إلى PDF](55541779.pdf) في 17.11 ولكن بما أننا نستخدم[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)الملكية، فإنه لا يلقي خطأ. ومع ذلك، واحد*سهم أحمر مدور مثل الشكل*كما هو موضح في هذه الصورة المفقودة.

![ما يجب القيام به:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

##  **عينة من الرموز**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
