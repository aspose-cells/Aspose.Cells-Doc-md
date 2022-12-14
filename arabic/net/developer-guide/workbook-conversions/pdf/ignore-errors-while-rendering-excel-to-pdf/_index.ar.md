---
title: تجاهل الأخطاء أثناء تحويل Excel إلى PDF
type: docs
weight: 80
url: /ar/net/ignore-errors-while-rendering-excel-to-pdf/
---
## **سيناريوهات الاستخدام الممكنة**

 في بعض الأحيان ، عندما تقوم بتحويل ملف Excel إلى PDF ، تحدث أخطاء أو استثناءات وتنتهي عملية التحويل. يمكنك تجاهل كل هذه الأخطاء أثناء عملية التحويل باستخدام ملف[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)منشأه. بهذه الطريقة ، ستكتمل عملية التحويل بسلاسة دون إلقاء أي خطأ أو استثناء ولكن قد يحدث فقدان للبيانات. لذلك ، يرجى استخدام هذه الخاصية فقط إذا لم يكن فقدان البيانات أمرًا بالغ الأهمية بالنسبة لك.

## **تجاهل الأخطاء أثناء تحويل Excel إلى PDF**

 الكود التالي يقوم بتحميل ملف[نموذج لملف Excel](55541778.xlsx) لكن نموذج ملف Excel خاطئ ويحدث خطأ أثناء[التحويل إلى PDF](55541779.pdf) في 17.11 ولكن بما أننا نستخدم[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)الملكية ، فإنه لا يلقي خطأ. ومع ذلك ، واحد*مستدير السهم الأحمر مثل الشكل*كما هو موضح في لقطة الشاشة هذه.

![ما يجب القيام به: image_بديل_نص](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
