---
title: تجاهل الأخطاء أثناء تصيير Excel إلى PDF باستخدام Golang عبر C++
linktitle: تجاهل الأخطاء أثناء تحويل Excel إلى PDF
type: docs
weight: 80
url: /ar/go-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: تعلم كيفية تجاهل الأخطاء أثناء تحويل Excel إلى PDF باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا عندما تقوم بتحويل ملف Excel الخاص بك إلى PDF، تحدث أخطاء أو استثناءات وتنتهي عملية التحويل. يمكنك تجاهل كل هذه الأخطاء أثناء عملية التحويل باستخدام الخاصية [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/). بهذه الطريقة، ستكتمل عملية التحويل بسلاسة دون إظهار أي خطأ أو استثناء، ولكن قد يحدث فقدان للبيانات. لذلك، يرجى استخدام هذه الخاصية فقط إذا لم يكن فقدان البيانات أمراً حرجًا بالنسبة لك.

## **تجاهل الأخطاء أثناء تحويل Excel إلى PDF**

الكود أدناه يقوم بتحميل [ملف Excel النموذجي](55541778.xlsx) لكن الملف يحتوى على أخطاء ويرمي خطأ خلال [التحويل إلى PDF](55541779.pdf) في 17.11، ولكن بما أننا نستخدم الخاصية [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/)، فذلك لا يسبب خطأ. ومع ذلك، فإن شكل سهم أحمر منحني واحد كما هو موضح في لقطة الشاشة يفقد.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IgnoreErrorsWhileRenderingExcelToPdf.go" >}}
