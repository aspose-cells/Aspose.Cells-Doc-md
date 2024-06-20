---
title: تجاهل الأخطاء أثناء تحويل Excel إلى PDF
type: docs
weight: 80
url: /ar/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: تعلم كيفية تجاهل الأخطاء أثناء عرض ملف إكسل إلى PDF باستخدام Aspose.Cells لبيثون via .NET API.
keywords: تجاهل الأخطاء أثناء عرض ملف Excel إلى PDF باستخدام Python, تجاهل الأخطاء أثناء حفظ Excel إلى PDF باستخدام Python, تجاهل الأخطاء أثناء تحويل Excel إلى PDF باستخدام Python, تجاهل الأخطاء لملف PDF في Python
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان عند تحويل ملف Excel إلى PDF، قد تحدث أخطاء أو استثناءات ويتوقف عملية التحويل. يمكنك تجاهل كل هذه الأخطاء أثناء عملية التحويل باستخدام [**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/) الخاصية. بهذه الطريقة، ستكتمل عملية التحويل بسلاسة دون رمي أي خطأ أو استثناء ولكن قد يحدث فقدان للبيانات. لذا، يرجى استخدام هذه الخاصية فقط إذا كان فقدان البيانات غير مهم بالنسبة لك.

## **تجاهل الأخطاء أثناء تحويل Excel إلى PDF**

يقوم الكود التالي بتحميل [ملف Excel عينة](55541778.xlsx) ولكن ملف Excel العينة به أخطاء ويقوم برمي خطأ أثناء [التحويل إلى PDF](55541779.pdf) في 17.11 ولكن نظرًا لاستخدامنا [**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/) الخاصية، فإنه لا يرمي خطأ. ومع ذلك، يتم فقدان إحدى *أشكال السهم الأحمر المستدير* كما هو موضح في هذا لقط.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
