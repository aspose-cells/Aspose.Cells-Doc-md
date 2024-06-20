---
title: التغييرات في واجهة برمجة التطبيقات العامة في Aspose.Cells 8.9.0
type: docs
weight: 300
url: /ar/net/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات العامة في Aspose.Cells من الإصدار 8.8.3 إلى 8.9.0 التي قد تكون مثيرة لاهتمام مطوري الوحدات/التطبيقات. يتضمن الوثيقة ليس فقط الطرق العامة الجديدة والمحدثة والفئات المُضافة والمُزالة إلخ، بل وصفًا لأي تغييرات في السلوك وراء الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تمت إضافة خاصية HtmlSaveOptions.DefaultFontName**
بواسطة الاصدار Aspose.Cells for .NET 8.9.0 تم عرض خاصية DefaultFontName لفئة HtmlSaveOptions التي تسمح بتحديد اسم الخط الافتراضي أثناء تقديم جداول البيانات إلى تنسيق HTML. سيتم استخدام الخط الافتراضي فقط عندما لا يكون موجوداً خط النمط. قيمة الخاصية HtmlSaveOptions.DefaultFontName بالمعنى الافتراضي هي null وهذا يعني أن API Aspose.Cells for .NET ستستخدم الخط الجامعي الذي يحمل نفس العائلة مع الخط الأصلي.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال حول [تعيين الخط الافتراضي لتقديم جداول البيانات إلى شكل HTML](/cells/ar/net/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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
يسمح الإصدار Aspose.Cells for .NET 8.9.0 بتعيين اسم الخط الافتراضي لفئة ImageOrPrintOptions من خلال عرض خاصية DefaultFont. يمكن استخدام الخاصية عندما لا يتم تحديد الأحرف اليونيكود في جدول البيانات بالخط الصحيح بناءً على ذلك قد تظهر هذه الأحرف على شكل مربعات في الصور الناتجة.

{{% alert color="primary" %}} 

قم بتعيين خاصية DefaultFont إلى MingLiu أو MS Gothic لعرض الأحرف اليونيكود. إذا لم يتم تعيين الخاصية المذكورة، فسوف يستخدم Aspose.Cells الخط الأساسي للنظام لعرض الأحرف اليونيكود.

{{% /alert %}} {{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال حول [تعيين الخط الافتراضي لتقديم جداول البيانات إلى تنسيق الصور](/cells/ar/net/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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


### **تمت إضافة خاصية IsExcel2003Compatible لـ PivotTable.**
قامت Aspose.Cells for .NET بتعريض خاصية IsExcel2003Compatible من نوع Boolean لفئة PivotTable التي تسمح بتحديد ما إذا كانت جدول البيانات متوافقًا مع Excel 2003 لأغراض التحديث. القيمة الافتراضية لخاصية IsExcel2003Compatible هي true، مما يعني أنه يجب أن يكون السلسلة أقل من أو تساوي 255 حرفًا. إذا كانت السلسلة أكبر من 255 حرفًا، سيتم قصها. إذا كانت القيمة false، فلن يتم فرض القيد المذكور سابقًا.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال حول [Compatibility for Excel 2003 for Refreshing Pivot Tables](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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
لـ Aspose.Cells.GridWeb for .NET 8.9.0 تمت تعريض الطريقة {GetVersion} الخاصة بالمصنع والتي تعيد الإصدار الخاص بمكون GridWeb.
