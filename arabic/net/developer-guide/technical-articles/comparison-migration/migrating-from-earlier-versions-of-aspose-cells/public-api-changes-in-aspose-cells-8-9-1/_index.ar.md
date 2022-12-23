---
title: عام API التغييرات في Aspose.Cells 8.9.1
type: docs
weight: 310
url: /ar/net/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.9.0 إلى 8.9.1 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **مصادر الخطوط القابلة للتكوين**
قام Aspose.Cells for .NET بعرض عدد من الفئات لتوفير الدعم لمصادر أطقم الطباعة القابلة للتكوين لتقديم جداول البيانات. فيما يلي قائمة بالفئات التي تمت إضافتها بالرقم Aspose.Cells for .NET 8.9.1.

1. تحدد فئة FontConfigs إعدادات الخط.
1. فئة FontSourceBase هي فئة أساسية مجردة للفئات التي تسمح للمستخدم بتحديد مصادر الخطوط المختلفة.
1. تمثل فئة FileFontSource ملف خط TrueType الفردي المخزن في نظام الملفات.
1. تمثل فئة FolderFontSource المجلد الذي يحتوي على ملفات خطوط TrueType.
1. تمثل فئة MemoryFontSource ملف خط تروتايب الفردي المخزن في الذاكرة.
1. يحدد تعداد FontSourceType نوع مصدر الخط.

مع التغييرات المذكورة أعلاه في المكان ، فإن Aspose.Cells for .NET يسمح بتعيين الخطوط كما هو مفصل أدناه.

1. قم بتعيين مجلد خط مخصص واحد أثناء استخدام طريقة FontConfigs.SetFontFolder.
1. قم بتعيين مجلد خط مخصص متعدد أثناء استخدام طريقة FontConfigs.SetFontFolders.
1. قم بتعيين مصادر الخطوط من مجلد خط مخصص أو ملف خط مفرد أو بيانات خط من مصفوفة بايت أثناء استخدام طريقة FontConfigs.SetFontSources.

فيما يلي سيناريو الاستخدام البسيط للطرق المذكورة أعلاه.

**C#**

{{< highlight "csharp" >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[]{ fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

تقبل كلتا الطريقتين FontConfigs.SetFontFolder & FontConfigs.SetFontFolders معلمة ثانية من النوع المنطقي. تمرير صحيح كمعامل ثان سيوجه Aspose.Cells APIs للبحث في المجلدات الفرعية عن ملفات الخطوط.

{{% /alert %}} 

Aspose.Cells for .NET يسمح أيضًا بتوصيف استبدال الخط. هذه الآلية مفيدة عندما لا يكون الخط المطلوب متاحًا على الجهاز حيث يجب إجراء التحويل. يمكن للمستخدمين توفير قائمة بأسماء الخطوط كبديل للخط المطلوب في الأصل. من أجل تحقيق ذلك ، كشفت واجهات برمجة التطبيقات Aspose.Cells طريقة FontConfigs.SetFontSubstitutes التي تقبل معلمتين. المعلمة الأولى هي من نوع السلسلة ، والتي يجب أن تكون اسم الخط الذي يجب استبداله. المعلمة الثانية هي مصفوفة من نوع السلسلة. يمكن للمستخدمين توفير قائمة بأسماء الخطوط كبديل لاسم الخط الأصلي (المحدد في المعلمة الأولى).

فيما يلي سيناريو استخدام بسيط لطريقة FontConfigs.SetFontSubstitutes.

**C#**

{{< highlight "csharp" >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}



يوفر Aspose.Cells for .NET أيضًا وسائل لجمع المعلومات حول المصادر والبدائل التي تم تعيينها.

1. تقوم طريقة FontConfigs.GetFontSources بإرجاع مصفوفة من النوع FontSourceBase تحتوي على قائمة بمصادر الخطوط المحددة. في حالة عدم تعيين أي مصادر ، سيعيد التابع FontConfigs.GetFontSources مصفوفة فارغة.
1. يقبل أسلوب FontConfigs.GetFontSubstitutes معلمة من نوع سلسلة تسمح بتحديد اسم الخط الذي تم تعيين بديل له. في حالة عدم تعيين أي استبدال لاسم الخط المحدد ، فإن طريقة FontConfigs.GetFontSubstitutes ستعيد فارغة.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول FontConfigs ، يرجى مراجعة المقال على[تكوين الخطوط لتقديم جداول البيانات](/cells/ar/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **تمت إضافة واجهة IFilePathProvider وخاصية HtmlSaveOptions.FilePathProvider**
Aspose.Cells for .NET 8.9.1 يسمح بالحصول على / تعيين IFilePathProvider لتصدير أوراق العمل لفصل ملفات HTML. تعد واجهات برمجة التطبيقات الجديدة هذه مفيدة في السيناريوهات حيث تشير الارتباطات التشعبية الموجودة في ورقة عمل واحدة إلى موقع في ورقة عمل أخرى ، حيث تكون متطلبات التطبيق هي عرض كل ورقة عمل لفصل ملف HTML. يسمح تنفيذ IFilePathProvider بالحفاظ على الارتباطات التشعبية المذكورة أعلاه سليمة بغض النظر عن حقيقة أنها تشير إلى موقع في ملف ناتج منفصل HTML.

فيما يلي سيناريو الاستخدام البسيط لخاصية HtmlSaveOptions.FilePathProvider.

**C#**

{{< highlight "csharp" >}}

 // تحميل جدول بيانات في مثيل مصنف

var book = مصنف جديد (dir + "sample.xlsx") ؛

// احفظ كل ورقة عمل لفصل ملف HTML

 لـ (int i = 0 ؛ i< book.Worksheets.Count; i++)

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



فيما يلي كيفية تنفيذ واجهة IFilePathProvider.

**C#**

{{< highlight "csharp" >}}

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

 لمزيد من التفاصيل حول هذا التحسين ، يرجى مراجعة المقالة الموجودة على[تنفيذ واجهة IFilePathProvider](/cells/ar/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **تمت إضافة خاصية CopyOptions.ReferToDestinationSheet & Overload لـ Cells.CopyRows Method**
كشف Aspose.Cells for .NET API الخاصية CopyOptions من النوع المنطقي .ReferToDestinationSheet جنبًا إلى جنب مع التحميل الزائد للطريقة Cells.CopyRows لتسهيل عملية نسخ الصفوف عندما تحتوي الصفوف المراد نسخها أيضًا على مخطط ومصدر بياناته. يمكن للمطورين الاستفادة من واجهات برمجة التطبيقات الجديدة هذه لتوجيه مصدر بيانات المخطط إلى أوراق العمل المصدر أو الوجهة.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

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

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة على[التحكم في مصدر بيانات المخطط أثناء نسخ الصفوف](/cells/ar/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **تمت إضافة CalculationOptions.Recursive Property**
كشف Aspose.Cells for .NET 8.9.1 خيارات حساب النوع المنطقي. إعداد CalculationOptions.Recursive property إلى true وتمرير الكائن إلى Workbook.CalculateFormula يوجه Aspose.Cells APIs لحساب الخلايا التابعة بشكل متكرر عند حساب الخلايا التي تعتمد على الخلايا الأخرى.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة على[تحسين وقت الحساب](/cells/ar/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **خاصية CellsHelper.FontDir التي عفا عليها الزمن**
يُنصح باستخدام طريقة FontConfigs.SetFontFolder (سلسلة ، منطقية) مع المجلد العودي إلى false بدلاً من ذلك.
### **خاصية CellsHelper.FontDirs التي عفا عليها الزمن**
استخدم أسلوب FontConfigs.SetFontFolders (سلسلة [] ، منطقي) مع مجلد متكرر إلى خطأ بدلاً من ذلك.
### **خاصية CellsHelper.FontFiles التي عفا عليها الزمن**
استخدم طريقة FontConfigs.SetFontSources (FontSourceBase []) بدلاً من ذلك.
