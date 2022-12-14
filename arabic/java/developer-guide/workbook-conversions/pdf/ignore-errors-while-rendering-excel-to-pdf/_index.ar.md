---
title: تجاهل الأخطاء أثناء تحويل Excel إلى PDF
type: docs
weight: 70
url: /ar/java/ignore-errors-while-rendering-excel-to-pdf/
---
## **سيناريوهات الاستخدام الممكنة**

في بعض الأحيان ، عندما تقوم بتحويل ملف Excel إلى PDF ، تحدث أخطاء أو استثناءات وتنتهي عملية التحويل. يمكنك تجاهل كل هذه الأخطاء أثناء عملية التحويل باستخدام ملف[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)منشأه. بهذه الطريقة ، ستكتمل عملية التحويل بسلاسة دون إلقاء أي خطأ أو استثناء ولكن قد يحدث فقدان للبيانات. لذلك ، يرجى استخدام هذه الخاصية فقط إذا لم يكن فقدان البيانات أمرًا بالغ الأهمية بالنسبة لك.

## **تجاهل الأخطاء أثناء تحويل Excel إلى PDF**

الكود التالي يقوم بتحميل ملف[نموذج لملف Excel](55541813.xlsx)لكن ملف Excel النموذجي خاطئ ويحدث خطأ أثناء ملف[التحويل إلى PDF](55541814.pdf)في 17.11 ولكن بما أننا نستخدم[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)الملكية ، فإنه لا يلقي خطأ. ومع ذلك ، يتم فقد شكل دائري يشبه السهم الأحمر كما هو موضح في لقطة الشاشة هذه.

![ما يجب القيام به: image_بديل_نص](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
