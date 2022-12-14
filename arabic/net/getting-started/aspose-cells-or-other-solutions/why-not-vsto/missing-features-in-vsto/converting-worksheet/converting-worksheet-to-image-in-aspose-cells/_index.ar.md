---
title: تحويل ورقة العمل إلى صورة في Aspose.Cells
type: docs
weight: 20
url: /ar/net/converting-worksheet-to-image-in-aspose-cells/
---
تم تصميم هذا المستند لتزويد المطورين بفهم تفصيلي حول كيفية تحويل ورقة العمل إلى ملف صورة وورقة عمل بها صفحات متعددة إلى ملف صورة لكل صفحة.
 في بعض الأحيان ، قد تحتاج إلى تقديم أوراق العمل كصور ، على سبيل المثال لاستخدامها في التطبيقات أو صفحات الويب. قد تحتاج إلى إدراج الصور في مستند Word ، ملف**بي دي إف** ملف ، وهو عرض تقديمي PowerPoint أو استخدامها في بعض السيناريوهات الأخرى. ببساطة ، تريد تقديم ورقة العمل كصورة. يدعم Aspose.Cells تحويل أوراق العمل في Microsoft ملفات Excel إلى صور. ايضا،**Aspose.Cells** يدعم تحويل مصنف إلى ملفات صور متعددة ، واحد لكل صفحة.

يمكنك استخدام Office Automation لتحقيق ذلك ، ولكن أتمتة Office لها عيوبها الخاصة. هناك عدة أسباب ومشكلات متضمنة: على سبيل المثال الأمان والاستقرار وقابلية التوسع / السرعة والسعر والميزات. باختصار ، هناك العديد من الأسباب ، ولكن السبب الرئيسي هو أن Microsoft أنفسهم يوصون بشدة بعدم أتمتة Office.

توضح هذه المقالة كيفية إنشاء تطبيق وحدة التحكم في Visual Studio.Net ، وتحويل ورقة العمل إلى صورة ، وورقة العمل إلى صورة واحدة لكل ورقة عمل مع بضعة أسطر من التعليمات البرمجية باستخدام Aspose.Cells API ، تحتاج إلى استيراد Aspose.Cells.Rendering إلى برنامجك / مشروعك. يحتوي على العديد من الفئات القيمة ، على سبيل المثال SheetRender و ImageOrPrintOptions و WorkbookRender وما إلى ذلك.**ToImage** الطريقة التي يمكنها تحويل ورقة عمل مباشرة إلى ملف (ملفات) صورة محددة بالسمات أو الخيارات التي تريدها. يمكن أن يعود**System.Drawing.Bitmap** كائن ويمكنك حفظ ملف صورة على القرص / دفق. هناك العديد من تنسيقات الصور المدعومة ، مثل .bmp ، .png ، .gif ، .jpg ، .jpeg ، .tiff ، .emf ، إلخ.

{{< highlight "csharp" >}}

 //Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image format

imgOptions.ImageFormat = System.Drawing.Imaging.ImageFormat.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
