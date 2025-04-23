---
title: تغييرات واجهة برمجة التطبيقات العمومية في Aspose.Cells 8.9.1
type: docs
weight: 320
url: /ar/java/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي طرأت على واجهة برمجة التطبيقات في Aspose.Cells من الإصدار 8.9.0 إلى 8.9.1 والتي قد تكون مثيرة لاهتمام مطوري الوحدات/التطبيقات. إنه يشتمل ليس فقط على الطرق العامة الجديدة والمحدثة، والفئات المضافة والمحذوفة الخ، ولكن أيضاً وصف لأي تغييرات في السلوك وراء الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **مصادر الخطوط القابلة للتكوين**
Aspose.Cells for Java قد عرضت عددًا من الفئات لتزويد الدعم لمصادر الخطوط القابلة للتكوين لتقديم جداول البيانات. إليك قائمة الفئات التي تمت إضافتها مع Aspose.Cells for Java 8.9.1.

1. تحديد تهيئات الخطوط الفئة تحدد إعدادات الخطوط.
1. فئة FontSourceBase هي فئة قاعدية مجردة للفئات التي تسمح للمستخدم بتحديد مصادر الخطوط المختلفة.
1. تمثل فئة FileFontSource ملف الخط TrueType الفردي المخزن في نظام ملفات النظام.
1. تمثل فئة FolderFontSource المجلد الذي يحتوي على ملفات خط TrueType.
1. تمثل فئة MemoryFontSource ملف الخط TrueType الفردي المخزن في الذاكرة.
1. تحدد تعداد عناصر نوع مصدر الخط من خلال تعداد FontSourceType.

مع التغييرات المذكورة أعلاه في المكان، يسمح الرقم Aspose.Cells for Java بتحديد الخطوط كما يلي.

1. تعيين مجلد خط مخصص واحد أثناء استخدام طريقة FontConfigs.setFontFolder.
1. تعيين مجلدات خط مخصصة متعددة أثناء استخدام طريقة FontConfigs.setFontFolders.
1. تعيين مصادر الخط من مجلد خط مخصص، ملف خط فردي أو بيانات خط من مصفوفة بايت أثناء استخدام طريقة FontConfigs.setFontSources.

فيما يلي سيناريو استخدام بسيط للطرق المذكورة أعلاه.

**Java**

{{< highlight csharp >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[] { fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[] bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

يقبل كلتا الطرقتين FontConfigs.setFontFolder و FontConfigs.setFontFolders المعامل الثاني من نوع مضاد. تمرير القيمة true كمعامل ثانوي سيوجه API Aspose.Cells إلى البحث في المجلدات الفرعية عن ملفات الخطوط. 

{{% /alert %}} 

Aspose.Cells for Java ايضا يسمح بتكوين بديل الخط. هذا الآلية مفيدة عندما الخط المطلوب غير متاح على الجهاز الذي يجب فيه اجراء التحويل. يمكن للمستخدمين تقديم قائمة من أسماء الخطوط كبديل للخط المطلوب في الأصل. من اجل تحقيق ذلك, API Aspose.Cells جعلت المعرضات لطريقة FontConfigs.setFontSubstitutes التي تقبل 2 معلمة. المعلمة الأولى من نوع سلسلة, يجب ان يكون الاسم الخط الذي يجب استبداله. المعلمة الثانية من نوع سلسلة. المستخدمين يمكنهم تقديم قائمة من أسماء الخطوط كبديل لاسم الخط الأصلي (المحدد في المعلمة الأولى).

فيما يلي سيناريو استخدام بسيط لطريقة FontConfigs.SetFontSubstitutes.

**Java**

{{< highlight csharp >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

ايضا قدم Aspose.Cells for Java وسائل لجمع المعلومات حول ما إذا كانت المصادر والاستبدالات قد تم تعيينها.

1. طريقة FontConfigs.getFontSources تقوم بإرجاع مصفوفة من نوع FontSourceBase تحتوي على قائمة المصادر الخط المحددة. في حالة عدم تحديد المصادر، ستقوم طريقة FontConfigs.getFontSources بإرجاع مصفوفة فارغة.
1. تقبل طريقة FontConfigs.getFontSubstitutes معلمة من نوع سلسلة تتيح تحديد اسم الخط الذي تم تحديد استبداله. في حالة عدم تحديد استبدال لاسم الخط المحدد، ستقوم طريقة FontConfigs.getFontSubstitutes بإرجاع قيمة فارغة.

{{% alert color="primary" %}} 

للمزيد من التفاصيل حول FontConfigs، يرجى مراجعة المقالة على [تكوين الخطوط لرسم الجداول الجديدة](/cells/ar/java/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **تمت إضافة واجهة IFilePathProvider وخاصية HtmlSaveOptions.FilePathProvider**
Aspose.Cells for Java 8.9.1 يسمح بالحصول على / تعيين IFilePathProvider لتصدير الأوراق العمل إلى ملفات HTML منفصلة. هذه الواجهات الجديدة مفيدة في السيناريوهات حيث تشير الروابط الفائقة في ورقة العمل إلى موقع في ورقة عمل أخرى، حيث تتطلب التطبيق رسم كل ورقة عمل لملف HTML منفصل. تنفيذ IFilePathProvider يسمح بالاحتفاظ بالروابط الفائقة المذكورة سابقًا بغض النظر عما إذا كانت تشير إلى موقع في ملف HTML منفصل.

فيما يلي سيناريو الاستخدام البسيط لخاصية HtmlSaveOptions.FilePathProvider.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save each Worksheet to separate  HTML file

for (int i = 0; i < book.getWorksheets().getCount(); i++)

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

لمزيد من التفاصيل حول هذا التحسين، يرجى مراجعة المقالة حول [تنفيذ واجهة IFilePathProvider](/cells/ar/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **تمت إضافة خاصية CopyOptions.ReferToDestinationSheet والتحميل الزائد لأسلوب Cells.copyRows.**
Aspose.Cells for Java API قد عرضت خاصية نوع Boolean CopyOptions.ReferToDestinationSheet جنبًا إلى جنب مع التحميل الزائد لأسلوب Cells.copyRows لتيسير عملية نسخ الصفوف عندما تحتوي الصفوف المراد نسخها أيضًا على رسم بياني ومصدر بياناته. يمكن للمطورين استخدام هذه الواجهات الجديدة لتوجيه مصدر بيانات الرسم البياني إلى أوراق العمل المصدر أو الوجهة.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

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

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقالة حول [التحكم في مصدر البيانات للرسم البياني أثناء نسخ الصفوف](/cells/ar/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **تمت إضافة خاصية CalculationOptions.Recursive.**
Aspose.Cells for Java 8.9.1 قد عرضت خاصية Boolean CalculationOptions.Recursive. ضبط خاصية CalculationOptions.Recursive على true وتمرير الكائن إلى أسلوب Workbook.calculateFormula يوجه واجهات Aspose.Cells لحساب الخلايا التي تعتمد تلقائيًا على حساب الخلايا الأخرى.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقالة حول [تحسين وقت الحساب](/cells/ar/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **واجهات برمجة التطبيق القديمة**
### **خاصية CellsHelper.FontDir المهجورة**
يُنصح باستخدام أسلوب FontConfigs.setFontFolder(String, boolean) مع تكرار المجلد إلى false بدلاً من ذلك.
### **خاصية CellsHelper.FontDirs المهجورة**
استخدم أسلوب FontConfigs.setFontFolders(String[], boolean) مع تكرار المجلد إلى false بدلاً من ذلك.
### **الواجهات المهجورة خاصية CellsHelper.FontFiles**
استخدم طريقة FontConfigs.setFontSources(FontSourceBase[]) بدلاً من ذلك.
{{< app/cells/assistant language="java" >}}
