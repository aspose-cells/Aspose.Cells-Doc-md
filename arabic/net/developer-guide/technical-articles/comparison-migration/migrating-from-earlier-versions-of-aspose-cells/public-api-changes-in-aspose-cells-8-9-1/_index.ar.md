---
title: تغييرات واجهة برمجة التطبيقات العمومية في Aspose.Cells 8.9.1
type: docs
weight: 310
url: /ar/net/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي طرأت على واجهة برمجة التطبيقات في Aspose.Cells من الإصدار 8.9.0 إلى 8.9.1 والتي قد تكون مثيرة لاهتمام مطوري الوحدات/التطبيقات. إنه يشتمل ليس فقط على الطرق العامة الجديدة والمحدثة، والفئات المضافة والمحذوفة الخ، ولكن أيضاً وصف لأي تغييرات في السلوك وراء الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **مصادر الخطوط القابلة للتكوين**
أصبحت Aspose.Cells for .NET تعرض عددًا من الصفوف لتوفير الدعم لمصادر الخطوط القابلة للتكوين لعرض الجداول الخاصة. وفيما يلي قائمة الصفوف التي تمت إضافتها مع Aspose.Cells for .NET 8.9.1.

1. تحديد تهيئات الخطوط الفئة تحدد إعدادات الخطوط.
1. فئة FontSourceBase هي فئة قاعدية مجردة للفئات التي تسمح للمستخدم بتحديد مصادر الخطوط المختلفة.
1. تمثل فئة FileFontSource ملف الخط TrueType الفردي المخزن في نظام ملفات النظام.
1. تمثل فئة FolderFontSource المجلد الذي يحتوي على ملفات خط TrueType.
1. تمثل فئة MemoryFontSource ملف الخط TrueType الفردي المخزن في الذاكرة.
1. تحدد تعداد عناصر نوع مصدر الخط من خلال تعداد FontSourceType.

بفضل التغييرات المذكورة أعلاه، يسمح Aspose.Cells for .NET بتحديد الخطوط كالتفاصيل أدناه.

1. ضبط مجلد خط مخصص واحد أثناء استخدام طريقة FontConfigs.SetFontFolder.
1. ضبط عدة مجلدات خط مخصصة أثناء استخدام طريقة FontConfigs.SetFontFolders.
1. ضبط مصادر الخط من مجلد خط مخصص، ملف خط واحد أو بيانات خط من مجموعة بايت أثناء استخدام طريقة FontConfigs.SetFontSources.

فيما يلي سيناريو استخدام بسيط للطرق المذكورة أعلاه.

**C#**

{{< highlight csharp >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[] { fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

كل من طرق FontConfigs.SetFontFolder وFontConfigs.SetFontFolders تقبل نوع باراميتر ثاني من نوع Boolean. تمرير true كباراميتر ثاني سيوجه واجهات برمجة التطبيقات لـ Aspose.Cells للبحث في المجلدات الفرعية عن ملفات الخطوط.

{{% /alert %}} 

 كما يسمح Aspose.Cells for .NET أيضا بتكوين استبدال الخطوط. هذا الآلية مفيدة عندما لا يتوفر الخط المطلوب على الجهاز الذي سيتم فيه التحويل. يمكن للمستخدمين تقديم قائمة باسماء الخطوط بديلاً عن الخط المطلوب أصلا. ولتحقيق ذلك، قد قدمت واجهات برمجة التطبيقات لـ Aspose.Cells الطريقة FontConfigs.SetFontSubstitutes التي تقبل 2 معامل. الباراميتر الأول من نوع string، والذي يجب أن يكون اسم الخط الذي يجب استبداله. الباراميتر الثاني هو مصفوفة من نوع string. يمكن للمستخدمين تقديم قائمة باسماء الخطوط كاستبدال لاسم الخط الأصلي (المحدد في الباراميتر الأول).

فيما يلي سيناريو استخدام بسيط لطريقة FontConfigs.SetFontSubstitutes.

**C#**

{{< highlight csharp >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[] { "Times New Roman", "Calibri" });

{{< /highlight >}}



  توفر Aspose.Cells for .NET وسائل أيضاً لجمع المعلومات حول الخطوط والاستبدالات التي تم تعيينها.

1. تقوم طريقة FontConfigs.GetFontSources بإرجاع مصفوفة من نوع FontSourceBase التي تحتوي على قائمة مصادر الخطوط المحددة. في حالة عدم تعيين مصادر، ستقوم طريقة FontConfigs.GetFontSources بإرجاع مصفوفة فارغة.
1. تقبل طريقة FontConfigs.GetFontSubstitutes معاملا من نوع string الذي يسمح بتحديد اسم الخط الذي تم تعيين استبدال له. في حالة عدم تعيين استبدال لاسم الخط المحدد، ستقوم طريقة FontConfigs.GetFontSubstitutes بإرجاع قيمة null.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول FontConfigs، يرجى مراجعة المقالة حول [تكوين الخطوط لتقديم جداول بيانات الجداول](/cells/ar/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **تمت إضافة واجهة IFilePathProvider وخاصية HtmlSaveOptions.FilePathProvider**
 يسمح Aspose.Cells for .NET 8.9.1 بالحصول/التعيين لـIFilePathProvider لتصدير أوراق عمل إلى ملفات HTML منفصلة. هذه واجهات برمجة التطبيقات الجديدة مفيدة في السيناريوهات حيث تشير الروابط الهيبرنق في صفحة عمل واحدة إلى موقع في صفحة عمل أخرى، حيث متطلبات التطبيق هي تقديم كل ورقة عمل إلى ملف HTML منفصل. تنفيذ IFilePathProvider يسمح بالاحتفاظ بالروابط الهيبرنق المذكورة سابقاً بغض النظر عن حقيقة أنها تشير إلى موقع في ملف HTML ناتج منفصل.

فيما يلي سيناريو الاستخدام البسيط لخاصية HtmlSaveOptions.FilePathProvider.

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save each Worksheet to separate HTML file

for (int i = 0; i < book.Worksheets.Count; i++)

{

    book.Worksheets.ActiveSheetIndex = i;

    // Create an instance of HtmlSaveOptions & set FilePathProvider property

    var options = new HtmlSaveOptions

    {

        ExportActiveWorksheetOnly = true,

        FilePathProvider = new FilePathProvider()

    };

    // Write HTML file to disc

    book.Save(dir + string.Format(@"sheet{0}.html", i), options);

}

{{< /highlight >}}



إليك كيفية تنفيذ واجهة IFilePathProvider.

**C#**

{{< highlight csharp >}}

 public class FilePathProvider : IFilePathProvider

{

    public FilePathProvider()

    {

    }

    /// <summary>

    /// Gets the full path of the file by Worksheet name when exporting Worksheet to html separately.

    /// So the references among the Worksheets can be exported correctly.

    /// </summary>

    /// <param name="sheetName">Worksheet name</param>

    /// <returns>the full path of the file</returns>

    public string GetFullName(string sheetName)

    {

        if ("Sheet2".Equals(sheetName))

        {

            return "sheet1.html";

        }

        else if ("Sheet3".Equals(sheetName))

        {

            return "sheet2.html";

        }

        return "";

    }

}

{{< /highlight >}}

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذا التحسين، يرجى مراجعة المقالة حول [تنفيذ واجهة IFilePathProvider](/cells/ar/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **تمت إضافة خاصية CopyOptions.ReferToDestinationSheet Property وOverload for Cells.CopyRows Method**
 Aspose.Cells for .NET API قد قامت بتعريض خاصية نوع Boolean CopyOptions.ReferToDestinationSheet بالإضافة إلى إعادة تحميل Cells.CopyRows method من أجل تسهيل عملية نسخ الصفوف عندما تحتوي الصفوف المراد نسخها أيضاً على مخطط ومصدر بياناته. يمكن للمطورين الاستفادة من هذه واجهات برمجة التطبيقات الجديدة لتوجيه مصدر البيانات لمخطط إلى ورقة البيانات الأصلية أو الناتجة.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet containing the chart & its data source

var source = book.Worksheets[0];

// Add a new worksheet to the collection

var destination = book.Worksheets[book.Worksheets.Add()];

// Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.ReferToDestinationSheet = true;

// Copy the rows

destination.Cells.CopyRows(source.Cells, 0, 0, source.Cells.MaxDisplayRange.RowCount, options);

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقالة حول [السيطرة على مصدر البيانات لمخطط أثناء نسخ الصفوف](/cells/ar/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **تمت إضافة خاصية CalculationOptions.Recursive.**
Aspose.Cells for .NET 8.9.1 قد قامت بتعريض خاصية نوع Boolean CalculationOptions.Recursive. ضبط خاصية CalculationOptions.Recursive إلى true وتمرير الكائن إلى طريقة Workbook.CalculateFormula يوجه واجهات برمجة التطبيقات لـ Aspose.Cells لحساب الخلايا التابعة بشكل متكرر عند حساب الخلايا التي تعتمد على خلايا أخرى.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقالة حول [تحسين وقت الحساب](/cells/ar/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **واجهات برمجة التطبيق القديمة**
### **خاصية CellsHelper.FontDir المهجورة**
يُنصح باستخدام الطريقة FontConfigs.SetFontFolder(string, bool) مع تكرار المجلد غير صحيح بدلاً من ذلك.
### **خاصية CellsHelper.FontDirs المهجورة**
استخدام الطريقة FontConfigs.SetFontFolders(string[], bool) مع تكرار المجلد غير صحيح بدلاً من ذلك.
### **الواجهات المهجورة خاصية CellsHelper.FontFiles**
استخدام الطريقة FontConfigs.SetFontSources(FontSourceBase[]) بدلاً من ذلك.
