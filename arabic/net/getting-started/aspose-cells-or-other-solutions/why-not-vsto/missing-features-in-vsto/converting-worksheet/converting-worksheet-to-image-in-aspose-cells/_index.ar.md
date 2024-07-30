---
title: تحويل ورقة عمل إلى صورة في Aspose.Cells
type: docs
weight: 20
url: /ar/net/converting-worksheet-to-image-in-aspose-cells/
---

هذا المستند مصمم لتوفير فهم مفصل للمطورين حول كيفية تحويل ورقة عمل إلى ملف صورة وورقة عمل مع عدة صفحات إلى ملف صورة لكل صفحة.
في بعض الأحيان، قد تحتاج إلى تقديم الأوراق العمل كصور، على سبيل المثال لاستخدامها في التطبيقات أو صفحات الويب. قد تحتاج إلى إدراج الصور في مستند Word، ملف PDF، عرض تقديمي بوربوينت أو استخدامها في سيناريو آخر. ببساطة، ترغب في عرض الورقة العمل كصورة. تدعم Aspose.Cells تحويل الأوراق العمل في ملفات Microsoft Excel إلى صور. أيضًا، تدعم Aspose.Cells تحويل دفتر العمل إلى ملفات صور متعددة، ملف واحد لكل صفحة.

قد تستخدم أتمتة Office لتحقيق هذا، ولكن أتمتة Office لها عيوبها الخاصة. هناك عدة أسباب وقضايا معقدة، على سبيل المثال الأمان والاستقرار والتوسعة / السرعة والسعر والميزات. بإختصار، هناك العديد من الأسباب، ولكن السبب الرئيسي هو أن شركة Microsoft نفسها توصي بشدة ضد أتمتة Office.

يوضح هذا المقال كيفية إنشاء تطبيق وحدة تحكم في Visual Studio.Net، وتحويل ورقة عمل إلى صورة، وورقة عمل إلى صورة واحدة لكل ورقة عمل ببضعة وأبسط أسطر من الكود باستخدام واجهة برمجة التطبيقات Aspose.Cells. يجب عليك استيراد فئة Aspose.Cells.Rendering إلى برنامجك/مشروعك. لديها عدة فئات قيمة، على سبيل المثال، SheetRender، ImageOrPrintOptions، WorkbookRender الخ. فئة Aspose.Cells.Rendering.SheetRender تمثل ورقة عمل لعرض الصور لورقة العمل، لديها أسلوب **ToImage** يمكن تحويل ورقة عمل مباشرة إلى ملف صورة(صور) محددة بخصائص أو خياراتك المطلوبة. يمكنها إرجاع كائن **System.Drawing.Bitmap** ويمكنك حفظ ملف صورة على القرص/التيار. هناك العديد من تنسيقات الصور المدعومة، على سبيل المثال .bmp، .png، .gif، .jpg، .jpeg، .tiff، .emf الخ.

{{< highlight csharp >}}

//Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image type

imgOptions.ImageType = ImageType.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **تحميل رمز عينة**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
