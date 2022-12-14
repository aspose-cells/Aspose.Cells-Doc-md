---
title: API عام تغييرات في Aspose.Cells 16.10.0
type: docs
weight: 340
url: /ar/net/public-api-changes-in-aspose-cells-16-10-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 9.0.0 إلى 16.10.0 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **دعم تأثيرات الانعكاس**
كشف Aspose.Cells 16.10.0 عن فئة ReflectionEffect إلى جانب خاصية Shape.Reflection من أجل التحكم في تأثيرات الانعكاس لعنصر الشكل. فئة ReflectionEffect لها الخصائص التالية.

- ReflectionEffect.Blur: الحصول على / تعيين نصف قطر التمويه بوحدة النقاط.
- ReflectionEffect.Direction: الحصول على / تحديد اتجاه منحدر تدرج ألفا بالنسبة إلى الشكل نفسه.
- ReflectionEffect.Distance: الحصول على / تحديد مسافة الانعكاس في وحدة من النقاط.
- ReflectionEffect.FadeDirection: يحصل / يحدد الاتجاه لتعويض الانعكاس.
- ReflectionEffect.RotWithShape: يحصل / يحدد إذا كان الانعكاس يجب أن يدور مع الشكل.
- ReflectionEffect.Size: الحصول على / تعيين موضع النهاية (على طول منحدر تدرج ألفا) لقيمة ألفا النهائية بوحدة النسبة المئوية.
- ReflectionEffect.Transparency: الحصول على / تعيين درجة شفافية الانعكاس الأولي كقيمة من 0.0 (معتم) إلى 1.0 (واضح).
- ReflectionEffect.Type: الحصول على / تعيين تأثير الانعكاس المحدد مسبقًا.

فيما يلي سيناريو الاستخدام البسيط لخاصية Shape.Reflection.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[العمل مع تأثيرات الانعكاس](/cells/ar/net/working-with-the-reflection-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of ReflectionEffect from the Shape object

var reflection = shape.Reflection;

// Set its Blur, Size, Transparency and Distance properties

reflection.Blur = 30;

reflection.Size = 90;

reflection.Transparency = 0.5;

reflection.Distance = 80;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **دعم تأثيرات الظل**
كشف Aspose.Cells 16.10.0 عن خاصية Shape.ShadowEffect جنبًا إلى جنب مع فئة ShadowEffect والتي تتيح معًا ضبط تأثير الظل على كائن الشكل. فئة ShadowEffect لها الخصائص التالية.

- ShadowEffect.Angle: الحصول على / ضبط زاوية الإضاءة التي تتراوح من 0 إلى 359.9 درجة.
- ShadowEffect.Blur: الحصول على وتمويه الظل الذي يتراوح من 0 إلى 100 نقطة.
- ShadowEffect.Color: الحصول على / تعيين لون الظل.
- ShadowEffect.Distance: الحصول على / تحديد مسافة الظل التي تتراوح من 0 إلى 200 نقطة.
- ShadowEffect.PresetType: الحصول على / تعيين نوع الظل المحدد مسبقًا للظل.
- ShadowEffect.Size: الحصول على / تعيين حجم الظل الذي يتراوح من 0 إلى 2.0. سيكون بلا معنى في حالة الظل الداخلي.
- ShadowEffect.Transparency: الحصول على / تعيين درجة شفافية الظل التي تتراوح من 0.0 (معتم) إلى 1.0 (واضح).

فيما يلي سيناريو استخدام بسيط للممتلكات المذكورة أعلاه.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[العمل مع تأثيرات الظل](/cells/ar/net/working-with-the-shadow-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of ShadowEffect from the Shape object

var shadow = shape.ShadowEffect;

// Set its Angle, Blur, Size, Transparency and Distance properties

shadow.Angle = 150;

shadow.Blur = 30;

shadow.Size = 90;

shadow.Transparency = 0.5;

shadow.Distance = 80;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **دعم تأثيرات الوهج**
كشف Aspose.Cells 16.10.0 خاصية Shape.Glow جنبًا إلى جنب مع فئة GlowEffect التي تسمح معًا بضبط تأثير التوهج لكائن الشكل. تحدد فئة GlowEffect تأثير التوهج ، حيث تتم إضافة مخطط تمويه اللون خارج حواف الكائن باستخدام الخصائص التالية.

- GlowEffect.Size: الحصول على / تعيين نصف قطر التوهج بوحدة النقاط.
- GlowEffect.Transparency: الحصول على / تعيين درجة شفافية تأثير التوهج التي تتراوح من 0.0 (معتم) إلى 1.0 (واضح).

فيما يلي سيناريو الاستخدام البسيط لخاصية Shape.Glow.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[العمل مع تأثير الوهج](/cells/ar/net/working-with-the-glow-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of GlowEffect from the Shape object

var glow = shape.Glow;

// Set its Size & Transparency properties

glow.Size = 90;

glow.Transparency = 0.5;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **دعم تنسيق ثلاثي الأبعاد**
كشف Aspose.Cells 16.10.0 عن خاصية Shape.ThreeDFormat جنبًا إلى جنب مع فئة ThreeDFormat والتي يمكن استخدامها معًا للتحكم في التنسيق ثلاثي الأبعاد لكائن الشكل. تمثل فئة ThreeDFormat التنسيق ثلاثي الأبعاد للشكل ولها الخصائص التالية.

- ThreeDFormat.BottomBevelHeight: الحصول على / تعيين ارتفاع الشطبة السفلية أو المسافة التي يتم تطبيقها في الشكل ، في وحدة النقاط.
- ThreeDFormat.BottomBevelType: الحصول على / تعيين نوع الشطبة السفلية أو إلى أي مدى يتم تطبيقه في الشكل ، في وحدة النقاط.
- ThreeDFormat.BottomBevelWidth: الحصول على / تعيين عرض مجسم مشطوف الحواف السفلي أو إلى أي مدى يتم تطبيقه في الشكل ، في وحدة النقاط.
- ThreeDFormat.ContourColor: الحصول على / تعيين لون محيط الشكل.
- ThreeDFormat.ContourWidth: الحصول على / تعيين عرض المحيط على الشكل ، في وحدة النقاط.
- ThreeDFormat.ExtrusionColor: الحصول على لون البثق على الشكل.
- ThreeDFormat.ExtrusionHeight: الحصول على / تعيين ارتفاع البثق للشكل ، في وحدة النقاط.
- ThreeDFormat.LightAngle: الحصول على / ضبط زاوية مصابيح البثق.
- ThreeDFormat.Lighting: يحصل / يحدد نوع جهاز الإضاءة.
- ThreeDFormat.LightingDirection: الحصول على / تحديد الاتجاه الذي يتم منه توجيه منصة الإضاءة بالنسبة إلى المشهد.
- ThreeDFormat.Material: يمثل المادة المحددة مسبقًا التي يتم دمجها مع خصائص الإضاءة لإعطاء الشكل والمظهر النهائيين للشكل.
- ThreeDFormat.Perspective: الحصول على / تعيين الزاوية التي يمكن من خلالها عرض كائن ThreeDFormat.
- ThreeDFormat.PresetCameraType: الحصول على / تعيين كاميرا البثق المعدة مسبقًا.
- ThreeDFormat.RotationX: الحصول على / تعيين دوران الشكل المبثوق حول المحور السيني بوحدة الدرجات.
- ThreeDFormat.RotationY: الحصول على / تعيين دوران الشكل المبثوق حول المحور Y بوحدة الدرجات.
- ThreeDFormat.RotationZ: الحصول على / تعيين دوران الشكل المبثوق حول المحور Z في وحدة الدرجات.
- ThreeDFormat.TopBevelHeight: الحصول على / تعيين ارتفاع الشطبة العلوية أو المسافة التي يتم تطبيقها في الشكل ، في وحدة النقاط.
- ThreeDFormat.TopBevelType: الحصول على / تعيين نوع مجسم مشطوف الحواف العلوي أو إلى أي مدى يتم تطبيقه في الشكل ، في وحدة النقاط.
- ThreeDFormat.TopBevelWidth: الحصول على / تعيين عرض مجسم مشطوف الحواف العلوي أو إلى أي مدى يتم تطبيقه في الشكل ، في وحدة النقاط.
- ThreeDFormat.Z: يحدد المسافة من الأرض للشكل ثلاثي الأبعاد.

فيما يلي سيناريو الاستخدام البسيط لخاصية Shape.ThreeDFormat.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[العمل مع تنسيق ثلاثي الأبعاد](/cells/ar/net/working-with-the-threedformat-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of ThreeDFormat from the Shape object

var threeD = shape.ThreeDFormat;

// Set its ContourWidth & ExtrusionHeight properties

threeD.ContourWidth = 15;

threeD.ExtrusionHeight = 30;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **دعم أنماط WordArt في نص الشكل**
كشف Aspose.Cells 16.10.0 عن طرق FontSettingCollection.SetWordArtStyle & FontSetting.SetWordArtStyle لتعيين نمط WordArt المضبوط مسبقًا على نص عنصر الشكل.

فيما يلي سيناريو الاستخدام البسيط للطرق المذكورة أعلاه.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[العمل مع أنماط WordArt](/cells/ar/net/set-preset-wordart-style-to-the-text-of-the-shape/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create workbook object

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Create a TextBox with some text

var textBox = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 700);

textBox.Text = "Aspose File Format APIs";

textBox.Font.Size = 44;

// Set preset WordArt style to the text of the shape

FontSetting fntSetting = textBox.GetCharacters()[0]as FontSetting;

fntSetting.SetWordArtStyle(PresetWordArtStyle.WordArtStyle3);

{{< /highlight >}}


### **دعم أنماط WordArt المضمنة**
كشف Aspose.Cells 16.10.0 عن طريقة ShapeCollection.AddWordArt جنبًا إلى جنب مع تعداد PresetWordArtStyle من أجل توفير الدعم لإضافة كائنات WordArt سابقة الإعداد منذ Excel 2007.

فيما يلي سيناريو استخدام بسيط لطريقة ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[أضف WordArt بأنماط مضمنة](/cells/ar/net/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access ShapeCollection of first worksheet

var shapes = sheet.Shapes;

// Add WordArt with built-in styles

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle1, "Aspose File Format APIs", 00, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **تمت إضافة طريقة XmlMapCollection.Add**
كشف Aspose.Cells عن طريقة XmlMapCollection.Add التي تسمح بإضافة خريطة Xml إلى جدول بيانات. فيما يلي سيناريو استخدام بسيط لطريقة XmlMapCollection.Add.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[أضف خريطة XML إلى جدول البيانات](/cells/ar/net/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Add xml map from the sample.xml to the workbook

book.Worksheets.XmlMaps.Add("sample.xml");

{{< /highlight >}}


### **تمت إضافة Cells.LinkToXmlMap**
كشف Aspose.Cells الآن الأسلوب Cells.LinkToXmlMap لربط الخلايا بعناصر مخطط XML.

فيما يلي سيناريو الاستخدام البسيط لطريقة Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[ارتباط Cells بعناصر خريطة XML](/cells/ar/net/link-cells-to-xml-map-elements/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook("sample.xlsx");

// Access the XML Map from the spreadsheet

var map = book.Worksheets.XmlMaps[0];

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Map FIELD1 and FIELD2 to cell A1 and B2

sheet.Cells.LinkToXmlMap(map.Name, 0, 0, "/root/row/FIELD1");

sheet.Cells.LinkToXmlMap(map.Name, 1, 1, "/root/row/FIELD2");

// Map FIELD4 and FIELD5 to cell C3 and D4

sheet.Cells.LinkToXmlMap(map.Name, 2, 2, "/root/row/FIELD4");

sheet.Cells.LinkToXmlMap(map.Name, 3, 3, "/root/row/FIELD5");

// Map FIELD7 and FIELD8 to cell E5 and F6

sheet.Cells.LinkToXmlMap(map.Name, 4, 4, "/root/row/FIELD7");

sheet.Cells.LinkToXmlMap(map.Name, 5, 5, "/root/row/FIELD8");

{{< /highlight >}}


### **تمت إضافة خاصية ListColumn.Formula**
كشف Aspose.Cells 16.10.0 الخاصية ListColumn.Formula من أجل نشر المعادلة تلقائيًا إلى الصفوف المدرجة حديثًا.

فيما يلي سيناريو استخدام بسيط لخاصية ListColumn.Formula.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[نشر الصيغة تلقائيًا في كائن القائمة](/cells/ar/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Add column headings in cell A1 and B1

sheet.Cells[0, 0].PutValue("Column A");

sheet.Cells[0, 1].PutValue("Column B");

// Add list object, set its name and style

var listObject = sheet.ListObjects[sheet.ListObjects.Add(0, 0, 1, sheet.Cells.MaxColumn, true)];

listObject.TableStyleType = TableStyleType.TableStyleMedium2;

listObject.DisplayName = "Table";

// Set the formula of second column so that it could automatically propagate to new rows while entering data

listObject.ListColumns[1].Formula = "=[Column A]+ 1";

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **دعم لحساب الوظائف المخصصة مع GridWeb**
كشف Aspose.Cells.GridWeb 16.10.0 خاصية GridWeb.CustomCalculationEngine جنبًا إلى جنب مع فئة GridAbstractCalculationEngine التي تسمح جميعها بتعريف وحساب الوظائف المخصصة من داخل مكون GridWeb.

فيما يلي سيناريو الاستخدام البسيط لواجهات برمجة التطبيقات المذكورة أعلاه.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[حساب الوظائف المخصصة مع GridWeb](/cells/ar/net/calculate-custom-functions-in-gridweb/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 private class GridWebCustomCalculationEngine : GridAbstractCalculationEngine

{

    public override void Calculate(GridCalculationData data)

    {

        //  Calculate MYTESTFUNC() with your own logic.

        //For example, you can multiply MYTESTFUNC() parameter with 2 so

        // MYTESTFUNC(3.0) will return 6

        // MYTESTFUNC(4.0) will return 8

        // MYTESTFUNC(5.0) will return 10

        if ("MYTESTFUNC".Equals(data.FunctionName.ToUpper()))

        {

            data.CalculatedValue = (decimal)(2.0 * (double)data.GetParamValue(0));

        }

    }

}


if (Page.IsPostBack == false && GridWeb1.IsPostBack == false)

{

    // Assign your own custom calculation engine to GridWeb

    GridWeb1.CustomCalculationEngine = new GridWebCustomCalculationEngine();

    // Access the active worksheet and add your custom function in cell B3

    GridWorksheet sheet = GridWeb1.ActiveSheet;

    GridCell cell = sheet.Cells["B3"];

    cell.Formula = "=MYTESTFUNC(9.0)";

    // Calculate the GridWeb formula

    GridWeb1.CalculateFormula();

}

{{< /highlight >}}
