---
title: تجاهل الأخطاء أثناء تحويل Excel إلى PDF
type: docs
weight: 80
url: /ar/net/ignore-errors-while-rendering-excel-to-pdf/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان عند تحويل ملف Excel إلى PDF، قد تحدث أخطاء أو استثناءات ويتوقف عملية التحويل. يمكنك تجاهل كل هذه الأخطاء أثناء عملية التحويل باستخدام [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror) الخاصية. بهذه الطريقة، ستكتمل عملية التحويل بسلاسة دون رمي أي خطأ أو استثناء ولكن قد يحدث فقدان للبيانات. لذا، يرجى استخدام هذه الخاصية فقط إذا كان فقدان البيانات غير مهم بالنسبة لك.

## **تجاهل الأخطاء أثناء تحويل Excel إلى PDF**

يقوم الكود التالي بتحميل [ملف Excel عينة](55541778.xlsx) ولكن ملف Excel العينة به أخطاء ويقوم برمي خطأ أثناء [التحويل إلى PDF](55541779.pdf) في 17.11 ولكن نظرًا لاستخدامنا [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror) الخاصية، فإنه لا يرمي خطأ. ومع ذلك، يتم فقدان إحدى *أشكال السهم الأحمر المستدير* كما هو موضح في هذا لقط.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
