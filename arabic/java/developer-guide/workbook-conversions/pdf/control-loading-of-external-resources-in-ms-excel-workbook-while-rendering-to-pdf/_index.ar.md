---
title: السيطرة على تحميل الموارد الخارجية في سجل Excel لتحويلها إلى ملف PDF
type: docs
weight: 40
url: /ar/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **سيناريوهات الاستخدام المحتملة**

قد يحتوي ملف Excel الخاص بك على موارد خارجية مثل الصور أو الأشياء المرتبطة. عند تحويل ملف Excel الخاص بك إلى PDF، يقوم Aspose.Cells بإسترداد هذه الموارد الخارجية وتقديمها إلى PDF. ولكن في بعض الأحيان، قد لا ترغب في تحميل هذه الموارد الخارجية وبالمزيد من ذلك، قد ترغب في معالجتها. يمكنك القيام بذلك باستخدام [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) الذي ينفذ واجهة [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider).

## **التحكم في تحميل الموارد الخارجية في دفتر العمل في MS Excel أثناء تحويله إلى PDF**

يشرح الرمز البرمجي عينة التالي كيفية الاستفادة من [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) للتحكم في تحميل الموارد الخارجية ومعالجتها. يرجى التحقق من [ملف الإكسل العيني](50528353.xlsx) المستخدم داخل الرمز البرمجي وال [PDF الناتج](50528354.pdf) الذي تم إنشاؤه بواسطة الرمز. [لقطة الشاشة](50528357.png) تظهر كيف تم استبدال [الصورة الخارجية القديمة](50528356.png) في ملف الإكسل العيني ب [صورة جديدة](50528355.png) في PDF الناتج.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
{{< app/cells/assistant language="java" >}}
