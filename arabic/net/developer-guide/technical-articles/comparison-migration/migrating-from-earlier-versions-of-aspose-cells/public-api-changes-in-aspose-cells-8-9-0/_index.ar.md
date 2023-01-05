---
title: API العام التغييرات في Aspose.Cells 8.9.0
type: docs
weight: 300
url: /ar/net/public-api-changes-in-aspose-cells-8-9-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.8.3 إلى 8.9.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمت إضافة خاصية HtmlSaveOptions.DefaultFontName**
كشف Aspose.Cells for .NET 8.9.0 الخاصية DefaultFontName لفئة HtmlSaveOptions التي تسمح بتحديد اسم الخط الافتراضي أثناء تحويل جداول البيانات إلى تنسيق HTML. سيتم استخدام الخط الافتراضي فقط في حالة عدم وجود خط النمط. القيمة الافتراضية لخاصية HtmlSaveOptions.DefaultFontName خالية مما يعني أن Aspose.Cells for .NET API سيستخدم الخط العام الذي له نفس العائلة مع الخط الأصلي.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة على[تحديد الخط الافتراضي لتحويل جداول البيانات إلى نسق HTML](/cells/ar/net/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **تمت إضافة خاصية ImageOrPrintOptions.DefaultFont**
Aspose.Cells for .NET 8.9.0 يسمح بتعيين اسم طاقم الطباعة الافتراضي لفئة ImageOrPrintOptions عن طريق كشف خاصية الخط الافتراضي. يمكن استخدام الخاصية المذكورة عندما لا يتم تعيين أحرف Unicode في جدول البيانات بالخط الصحيح في نمط الخلية ، وبالتالي قد تظهر هذه الأحرف ككتل في الصور الناتجة.

{{% alert color="primary" %}} 

قم بتعيين خاصية الخط الافتراضي إلى MingLiu أو MS Gothic لإظهار أحرف Unicode. إذا لم يتم تعيين الخاصية المذكورة ، فسيستخدم Aspose.Cells الخط الافتراضي للنظام لإظهار أحرف Unicode.

{{% /alert %}} {{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة على[تعيين الخط الافتراضي لعرض جداول البيانات في تنسيقات الصورة](/cells/ar/net/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of ImageOrPrintOptions

var options = new ImageOrPrintOptions();

// Set default font name for image rendering

options.DefaultFont = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet to be rendered

var sheet = book.Worksheets[0];

// Create an instance of SheetRender

var render = new SheetRender(sheet, options);

// Save spreadsheet to image

render.ToImage(0, dir + "output.png");

{{< /highlight >}}


### **تمت إضافة خاصية PivotTable.IsExcel2003 المتوافقة**
كشف Aspose.Cells for .NET API نوع Boolean الخاصية IsExcel2003Comp Compatible لفئة PivotTable التي تسمح بتحديد ما إذا كان PivotTable متوافقًا مع Excel 2003 لأغراض التحديث. القيمة الافتراضية للخاصية المتوافقة IsExcel2003 هي true ، وهذا يعني أن السلسلة يجب أن تكون أقل من أو تساوي 255 حرفًا. إذا كانت السلسلة أكبر من 255 حرفًا ، فسيتم قطعها. إذا كانت خاطئة ، فلن يتم فرض القيد المذكور أعلاه.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة على[التوافق مع Excel 2003 لتحديث الجداول المحورية](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the desired Pivot Table from the spreadsheet

var pivot = book.Worksheets[0].PivotTables[0];

// Set Excel 2003 compatibility to false

pivot.IsExcel2003Compatible = false;

// Refresh & recalculate Pivot Table

pivot.RefreshData();

pivot.CalculateData();

{{< /highlight >}}


### **تمت إضافة طريقة GridWeb.GetVersion**
كشف Aspose.Cells.GridWeb for .NET 8.9.0 طريقة المصنع {GetVersion}} التي تُرجع نسخة الإصدار لمكون GridWeb.
