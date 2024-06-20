---
title: السيطرة على تحميل الموارد الخارجية في سجل Excel لتحويلها إلى ملف PDF
type: docs
weight: 40
url: /ar/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **سيناريوهات الاستخدام المحتملة**

قد يحتوي ملف Excel الخاص بك على موارد خارجية مثل الصور المرتبطة أو الكائنات. عند تحويل ملف Excel الخاص بك إلى PDF، يسترد Aspose.Cells هذه الموارد الخارجية ويقوم بتحويلها إلى PDF. ولكن في بعض الأحيان، قد لا ترغب في تحميل هذه الموارد الخارجية وأكثر من ذلك، قد ترغب في التلاعب بها. يمكنك القيام بذلك باستخدام [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) الذي ينفذ واجهة [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider).

## **التحكم في تحميل الموارد الخارجية في دفتر العمل في MS Excel أثناء تحويله إلى PDF**

توضح الشفرة النموذجية التالية كيفية استخدام [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) للتحكم في تحميل الموارد الخارجية والتلاعب بها. يرجى التحقق من [ملف Excel النموذجي](50528322.xlsx) المستخدم داخل الشفرة و [ملف PDF الناتج](50528325.pdf) الذي تم إنشاؤه بواسطة الشفرة. يوضح ال [اللقطة الشاشة](50528326.png) كيف تم استبدال [الصورة الخارجية القديمة](50528324.png) في ملف Excel النموذجي بـ [صورة جديدة](50528323.png) في ملف PDF الناتج.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}
