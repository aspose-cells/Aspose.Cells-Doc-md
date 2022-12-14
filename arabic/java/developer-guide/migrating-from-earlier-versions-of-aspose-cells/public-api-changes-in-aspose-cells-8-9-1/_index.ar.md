---
title: عام API التغييرات في Aspose.Cells 8.9.1
type: docs
weight: 320
url: /ar/java/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.9.0 إلى 8.9.1 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **مصادر الخطوط القابلة للتكوين**
قام Aspose.Cells for Java بعرض عدد من الفئات لتوفير الدعم لمصادر أطقم الطباعة القابلة للتكوين لتقديم جداول البيانات. فيما يلي قائمة بالفئات التي تمت إضافتها بالرقم Aspose.Cells for Java 8.9.1.

1. تحدد فئة FontConfigs إعدادات الخط.
1. فئة FontSourceBase هي فئة أساسية مجردة للفئات التي تسمح للمستخدم بتحديد مصادر الخطوط المختلفة.
1. تمثل فئة FileFontSource ملف خط TrueType الفردي المخزن في نظام الملفات.
1. تمثل فئة FolderFontSource المجلد الذي يحتوي على ملفات خطوط TrueType.
1. تمثل فئة MemoryFontSource ملف خط تروتايب الفردي المخزن في الذاكرة.
1. يحدد تعداد FontSourceType نوع مصدر الخط.

مع التغييرات المذكورة أعلاه في المكان ، فإن Aspose.Cells for Java يسمح بتعيين الخطوط كما هو مفصل أدناه.

1. قم بتعيين مجلد خط مخصص واحد أثناء استخدام طريقة FontConfigs.setFontFolder.
1. قم بتعيين مجلد خط مخصص متعدد أثناء استخدام طريقة FontConfigs.setFontFolders.
1. قم بتعيين مصادر الخطوط من مجلد خط مخصص أو ملف خط مفرد أو بيانات خط من مصفوفة بايت أثناء استخدام طريقة FontConfigs.setFontSources.

فيما يلي سيناريو الاستخدام البسيط للطرق المذكورة أعلاه.

**Java**

{{< highlight "csharp" >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[]{ fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[]bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

 تقبل كلتا الطريقتين FontConfigs.setFontFolder & FontConfigs.setFontFolders معلمة ثانية من النوع المنطقي. تمرير صحيح كمعامل ثان سيوجه Aspose.Cells APIs للبحث في المجلدات الفرعية عن ملفات الخطوط.

{{% /alert %}} 

Aspose.Cells for Java يسمح أيضًا بتوصيف استبدال الخط. هذه الآلية مفيدة عندما لا يكون الخط المطلوب متاحًا على الجهاز حيث يجب إجراء التحويل. يمكن للمستخدمين توفير قائمة بأسماء الخطوط كبديل للخط المطلوب في الأصل. من أجل تحقيق ذلك ، كشفت واجهات برمجة التطبيقات Aspose.Cells طريقة FontConfigs.setFontSubstitutes التي تقبل معلمتين. المعلمة الأولى هي من نوع السلسلة ، والتي يجب أن تكون اسم الخط الذي يجب استبداله. المعلمة الثانية هي مصفوفة من نوع السلسلة. يمكن للمستخدمين توفير قائمة بأسماء الخطوط كبديل لاسم الخط الأصلي (المحدد في المعلمة الأولى).

فيما يلي سيناريو استخدام بسيط لطريقة FontConfigs.SetFontSubstitutes.

**Java**

{{< highlight "csharp" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

يوفر Aspose.Cells for Java أيضًا وسائل لجمع المعلومات حول المصادر والبدائل التي تم تعيينها.

1. تقوم طريقة FontConfigs.getFontSources بإرجاع مصفوفة من النوع FontSourceBase تحتوي على قائمة بمصادر الخطوط المحددة. في حالة عدم تعيين أي مصادر ، ستُرجع طريقة FontConfigs.getFontSources مصفوفة فارغة.
1. يقبل أسلوب FontConfigs.getFontSubstitutes معلمة من نوع سلسلة تسمح بتحديد اسم الخط الذي تم تعيين بديل له. في حالة عدم تعيين أي استبدال لاسم الخط المحدد ، فإن طريقة FontConfigs.getFontSubstitutes ستعيد فارغة.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول FontConfigs ، يرجى مراجعة المقال على[تكوين الخطوط لتقديم جداول البيانات](/cells/ar/java/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **تمت إضافة واجهة IFilePathProvider وخاصية HtmlSaveOptions.FilePathProvider**
Aspose.Cells for Java 8.9.1 يسمح بالحصول على / تعيين IFilePathProvider لتصدير أوراق العمل إلى ملفات HTML منفصلة. تُعد واجهات برمجة التطبيقات الجديدة هذه مفيدة في السيناريوهات حيث تشير الارتباطات التشعبية في ورقة عمل واحدة إلى موقع في ورقة عمل أخرى ، حيث تكون متطلبات التطبيق هي تقديم كل ورقة عمل إلى ملف HTML منفصل. يسمح تنفيذ IFilePathProvider بالحفاظ على الارتباطات التشعبية المذكورة أعلاه سليمة بغض النظر عن حقيقة أنها تشير إلى موقع في ملف HTML ناتج منفصل.

فيما يلي سيناريو الاستخدام البسيط لخاصية HtmlSaveOptions.FilePathProvider.

**Java**

{{< highlight "csharp" >}}

 // تحميل جدول بيانات في مثيل مصنف

كتاب المصنف = مصنف جديد (dir + "sample.xlsx") ؛

// احفظ كل ورقة عمل لفصل ملف HTML

 لـ (int i = 0 ؛ i< book.getWorksheets().getCount(); i++)

{

	book.getWorksheets().setActiveSheetIndex(i);

	//Create an instance of HtmlSaveOptions & set FilePathProvider property

	HtmlSaveOptions options = new HtmlSaveOptions();

	options.setExportActiveWorksheetOnly(true);

	options.setFilePathProvider(new IFilePathProvider() 

	{ 

		public String getFullName(String sheetName)

		{

		    if ("Sheet2".equals(sheetName))

		    {

		        return "sheet1.html";

		    }

		    else if ("Sheet3".equals(sheetName))

		    {

		        return "sheet2.html";

		    }



		    return "";

		}

	});



	 //Write HTML file to disc

	 book.save(dir + "sheet"+ i +".html", options);

}

{{< /highlight >}}

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذا التحسين ، يرجى مراجعة المقالة الموجودة على[تنفيذ واجهة IFilePathProvider](/cells/ar/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **تمت إضافة خاصية CopyOptions.ReferToDestinationSheet & Overload لـ Cells.copyRows Method**
كشف Aspose.Cells for Java API الخاصية CopyOptions من النوع المنطقي .ReferToDestinationSheet جنبًا إلى جنب مع التحميل الزائد للطريقة Cells.copyRows لتسهيل عملية نسخ الصفوف عندما تحتوي الصفوف المراد نسخها أيضًا على مخطط ومصدر بياناته. يمكن للمطورين الاستفادة من واجهات برمجة التطبيقات الجديدة هذه لتوجيه مصدر بيانات المخطط إلى أوراق العمل المصدر أو الوجهة.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet containing the chart & its data source

Worksheet source = book.getWorksheets().get(0);

//Add a new worksheet to the collection

Worksheet destination = book.getWorksheets().get(book.getWorksheets().add());

//Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.setReferToDestinationSheet(true);

//Copy the rows

destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة على[التحكم في مصدر بيانات المخطط أثناء نسخ الصفوف](/cells/ar/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **تمت إضافة CalculationOptions.Recursive Property**
كشف Aspose.Cells for Java 8.9.1 خيارات حساب النوع المنطقي. يؤدي تعيين CalculationOptions.Recursive property إلى true وتمرير الكائن إلى Workbook.calculateFormula طريقة توجيه Aspose.Cells APIs لحساب الخلايا التابعة بشكل متكرر عند حساب الخلايا التي تعتمد على الخلايا الأخرى.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة على[تحسين وقت الحساب](/cells/ar/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **خاصية CellsHelper.FontDir التي عفا عليها الزمن**
يُنصح باستخدام طريقة FontConfigs.setFontFolder (String، boolean) مع المجلد العودي إلى false بدلاً من ذلك.
### **خاصية CellsHelper.FontDirs التي عفا عليها الزمن**
استخدم طريقة FontConfigs.setFontFolders (String []، boolean) مع المجلد العودي إلى false بدلاً من ذلك.
### **خاصية CellsHelper.FontFiles التي عفا عليها الزمن**
استخدم طريقة FontConfigs.setFontSources (FontSourceBase []) بدلاً من ذلك.
