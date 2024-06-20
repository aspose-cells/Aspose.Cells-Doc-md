---
title: تجاهل الأخطاء أثناء تحويل Excel إلى PDF
type: docs
weight: 70
url: /ar/java/ignore-errors-while-rendering-excel-to-pdf/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، عند تحويل ملف Excel إلى PDF، تحدث أخطاء أو استثناءات ويتوقف عملية التحويل. يمكنك تجاهل كل هذه الأخطاء أثناء عملية التحويل باستخدام الخاصية [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError) . وبهذه الطريقة، ستكتمل عملية التحويل بسلاسة دون أن تقذف أي خطأ أو استثناء ولكن قد يحدث فقدان للبيانات. لذا يرجى استخدام هذه الخاصية فقط إذا كان فقدان البيانات غير حرج بالنسبة لك.

## **تجاهل الأخطاء أثناء تحويل Excel إلى PDF**

يلتقط الكود التالي [ملف Excel عينة](55541813.xlsx) ولكن ملف Excel العينة به خطأ يُقذف خلال [التحويل إلى PDF](55541814.pdf) في 17.11 ولكن نظرًا لاستخدامنا للخاصية [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError) ، لا يتم رمي خطأ. ومع ذلك، يتم فقدان شكل أحمر مستدير يشبه السهم كما هو موضح في لقطة الشاشة هذه.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
