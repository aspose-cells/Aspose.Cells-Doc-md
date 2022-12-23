---
title: التحكم في تحميل الموارد الخارجية في مصنف MS Excel أثناء التقديم إلى PDF
type: docs
weight: 40
url: /ar/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **سيناريوهات الاستخدام الممكنة**

قد يحتوي ملف Excel الخاص بك على موارد خارجية مثل الصور أو الكائنات المرتبطة. عند تحويل ملف Excel إلى PDF ، يقوم Aspose.Cells باسترداد هذه الموارد الخارجية وتقديمها إلى PDF. لكن في بعض الأحيان ، لا تريد تحميل هذه الموارد الخارجية وأكثر من ذلك ، فأنت تريد التلاعب بها. يمكنك القيام بذلك باستخدام[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)الذي ينفذ[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)واجهه المستخدم.

## **التحكم في تحميل الموارد الخارجية في مصنف MS Excel أثناء التقديم إلى PDF**

 يشرح نموذج التعليمات البرمجية التالي كيفية الاستفادة من[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) للتحكم في تحميل الموارد الخارجية والتلاعب بها. رجاء تاكد من[نموذج لملف Excel](50528322.xlsx) المستخدمة داخل الكود و[الإخراج PDF](50528325.pdf) التي تم إنشاؤها بواسطة الكود. ال[لقطة شاشة](50528326.png) يوضح كيف[الصورة الخارجية القديمة](50528324.png) في نموذج ملف Excel تم استبداله بامتداد[صورة جديدة](50528323.png) في الإخراج PDF.

![ما يجب القيام به: image_بديل_نص](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}
