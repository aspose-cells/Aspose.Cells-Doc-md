---
title: إنشاء مخطط عن طريق معالجة العلامات الذكية
type: docs
weight: 180
url: /ar/java/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}} 

توفر واجهات برمجة التطبيقات Aspose.Cells فئة WorkbookDesigner للعمل مع العلامات الذكية حيث يتم وضع التنسيق والصيغ في جداول بيانات المصمم ثم معالجتها مقابل مصدر (مصادر) البيانات المحددة لملء البيانات وفقًا للعلامات الذكية. من الممكن أيضًا إنشاء مخططات Excel من خلال معالجة العلامات الذكية ، والتي ستتطلب الخطوات التالية.

- إنشاء جدول بيانات المصمم
- معالجة جدول بيانات المصمم مقابل مصدر البيانات المحدد
- إنشاء مخطط على أساس البيانات المأهولة

{{% /alert %}} 
## **إنشاء جدول بيانات مصمم**
جدول بيانات المصمم هو ملف Excel بسيط تم إنشاؤه باستخدام تطبيق Excel Microsoft أو Aspose.Cells APIs التي تحتوي على التنسيق المرئي والصيغ والعلامات الذكية ، حيث يتم ملء المحتويات في وقت التشغيل.

{{% alert color="primary" %}} 

 تتوفر معلومات مفصلة عن العلامات الذكية[هنا](/cells/ar/java/smart-markers/).

{{% /alert %}} 

من أجل البساطة ، سنقوم بإنشاء جدول بيانات المصمم باستخدام Aspose.Cells for Java API ، ثم نقوم بمعالجته لاحقًا على مصدر بيانات تم إنشاؤه ديناميكيًا لأغراض العرض التوضيحي.

**Java**

{{< highlight "csharp" >}}

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

إذا قمت بحفظ جدول البيانات الناتج في هذه المرحلة ، فستظهر البيانات الموجودة في ورقة العمل على النحو التالي.

![ما يجب القيام به: image_بديل_نص](generate-chart-by-processing-smart-markers_1.png)
## **معالجة جدول بيانات المصمم**
 من أجل معالجة جدول بيانات المصمم ، يجب أن يكون لدينا مصدر بيانات يتوافق مع العلامات الذكية المستخدمة في جدول بيانات المصمم. على سبيل المثال ، قمنا بإنشاء إدخال Smart Marker كـ**& = $ رؤوس (أفقيًا)**، التي تمثل المتغير حسب الاسم رؤوس بينما المفتاح**(عرضي)** يقترح أنه يجب ملء البيانات أفقيًا.

لتوضيح حالة الاستخدام هذه ، سننشئ مصدر البيانات من البداية ونعالجها مقابل جدول بيانات المصمم الذي تم إنشاؤه في الخطوة السابقة. ومع ذلك ، في سيناريو الوقت الفعلي ، قد تكون البيانات متاحة بالفعل لمزيد من المعالجة حتى تتمكن من تخطي إنشاء مصدر البيانات إذا كانت البيانات متاحة بالفعل.

**Java**

{{< highlight "csharp" >}}

 //Create string arrays which will serve as data sources to the smart markers

String[]headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[]year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[]year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[]year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[]year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

معالجة العلامات الذكية بسيطة للغاية على النحو التالي.

**Java**

{{< highlight "csharp" >}}

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

إذا قمت بحفظ جدول البيانات في هذه المرحلة ، فستظهر البيانات على النحو التالي.

![ما يجب القيام به: image_بديل_نص](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

يستخدم مقتطف التعليمات البرمجية أعلاه المثيل الحالي لفئة المصنف الذي تم إنشاؤه في الخطوة الأولى. إذا كان لديك بالفعل ملف جدول بيانات المصمم على القرص أو الذاكرة ، فيمكنك إنشاء مثيل لفئة المصنف عن طريق تحميل جدول بيانات المصمم الحالي.

{{% /alert %}} 
## **إنشاء الرسم البياني**
بمجرد وضع البيانات في مكانها الصحيح ، كل ما يتعين علينا القيام به هو إنشاء مخطط بناءً على مصدر البيانات. من أجل الحفاظ على المثال بسيطًا ، سنستخدم طريقة Chart.setChartDataRange حتى لا نضطر إلى تكوين المخطط بشكل أكبر.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





يبدو الرسم البياني النهائي على النحو التالي.

![ما يجب القيام به: image_بديل_نص](generate-chart-by-processing-smart-markers_3.png)
