---
title: إنشاء رسم بياني عن طريق معالجة العلامات الذكية
type: docs
weight: 180
url: /ar/java/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}} 

توفر واجهات برمجة التطبيقات Aspose.Cells فئة WorkbookDesigner للعمل مع العلامات الذكية حيث يتم وضع التنسيق والصيغ في جداول العمل المصممة ثم يتم معالجتها ضد مصادر البيانات المحددة لملء البيانات وفقًا للعلامات الذكية. كما أنه من الممكن أيضًا إنشاء رسوم بيانية في Excel عن طريق معالجة العلامات الذكية، وهذا سيتطلب الخطوات التالية.

- إنشاء جدول بيانات المصمم
- معالجة جدول بيانات المصمم ضد مصادر البيانات المحددة
- إنشاء رسم بياني بناءً على البيانات المحددة

{{% /alert %}} 
## **إنشاء جدول بيانات المصمم**
جدول بيانات المصمم هو ملف Excel بسيط يتم إنشاؤه باستخدام تطبيق Microsoft Excel أو واجهات برمجة التطبيقات Aspose.Cells الذي يحتوي على التنسيق البصري والصيغ والعلامات الذكية، حيث يتم ملؤها في وقت التشغيل.

{{% alert color="primary" %}} 

المعلومات المفصلة حول العلامات الذكية متوفرة [هنا](/cells/ar/java/smart-markers/).

{{% /alert %}} 

من أجل البساطة، سنقوم بإنشاء ورقة الجدول المصممة باستخدام واجهة برمجة التطبيقات Aspose.Cells for Java، ومن ثم معالجتها ضد مصدر بيانات تم إنشاؤه ديناميكيًا لأغراض العرض.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access the first (default) Worksheet from the collection

Worksheet dataSheet = book.getWorksheets().get(0);

//Name the first Worksheet for referencing

dataSheet.setName("ChartData");

//Access the CellsCollection of ChartData Worksheet

Cells cells = dataSheet.getCells();

//Place the markers in the Worksheet according to desired layout

cells.get("A1").putValue("&=$Headers(horizontal)");

cells.get("A2").putValue("&=$Year2000(horizontal)");

cells.get("A3").putValue("&=$Year2005(horizontal)");

cells.get("A4").putValue("&=$Year2010(horizontal)");

cells.get("A5").putValue("&=$Year2015(horizontal)");

{{< /highlight >}}

إذا قمت بحفظ ورقة الجدول الناتجة في هذه المرحلة، سيبدو البيانات في الورقة كما يلي.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_1.png)
## **معالجة ورقة الجدول المصممة**
من أجل معالجة ورقة الجدول المصممة، يجب أن يكون لدينا مصدر بيانات يتوافق مع العلامات الذكية المستخدمة في ورقة الجدول المصممة. على سبيل المثال، لقد أنشأنا إدخالًا لعلامة ذكية باسم **&=$Headers(horizontal)**، الذي يمثل المتغير حسب الاسم Headers في حين أن المفتاح **(horizontal)** يشير إلى أن البيانات يجب أن تملأ أفقيًا.

من أجل استعراض هذه الحالة الاستخدام، سنقوم بإنشاء مصدر البيانات من البداية ومعالجته ضد ورقة الجدول المصممة التي تم إنشاؤها في الخطوة السابقة. ومع ذلك، في حالة الوقت الحقيقي، قد تكون البيانات متاحة بالفعل لمزيد من المعالجة، لذا يمكنك تخطي إنشاء مصدر البيانات إذا كانت البيانات متاحة بالفعل.

**Java**

{{< highlight csharp >}}

 //Create string arrays which will serve as data sources to the smart markers

String[] headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[] year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[] year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[] year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[] year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

إن معالجة العلامات الذكية بسيطة تماما كما يلي.

**Java**

{{< highlight csharp >}}

 //Create an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner();

//Set the Workbook property for the instance of WorkbookDesigner

designer.setWorkbook(book);

//Set data sources for smart markers

designer.setDataSource("Headers", headers);

designer.setDataSource("Year2000", year2000);

designer.setDataSource("Year2005", year2005);

designer.setDataSource("Year2010", year2010);

designer.setDataSource("Year2015", year2015);

//Process the designer spreadsheet against the provided data sources

designer.process();

{{< /highlight >}}

إذا قمت بحفظ ورقة البيانات في هذه المرحلة، ستبدو البيانات كما يلي.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

يرجى ملاحظة أن كود المثال السابق يستخدم نسخة الكائن الموجودة مسبقًا من فئة Workbook التي تم إنشاؤها في الخطوة الأولى. إذا كان لديك بالفعل ملف ورقة الجدول المصممة على القرص أو الذاكرة، يمكنك إنشاء نسخة من فئة Workbook عن طريق تحميل ورقة الجدول المصممة الموجودة.

{{% /alert %}} 
## **إنشاء الرسم البياني**
بمجرد وجود البيانات، كل ما علينا فعله هو إنشاء رسم بياني يستند إلى مصدر البيانات. من أجل الحفاظ على السبيل المثالي، سنستخدم طريقة Chart.setChartDataRange بحيث لا يلزمنا تكوين الرسم البياني بشكل أكبر.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





يبدو الرسم البياني النهائي كما يلي.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_3.png)
