---
title: API عام تغييرات في Aspose.Cells 16.10.0
type: docs
weight: 350
url: /ar/java/public-api-changes-in-aspose-cells-16-10-0/
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

 تحقق من المقال المفصل على[العمل مع تأثيرات الانعكاس](/cells/ar/java/working-with-the-reflection-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of ReflectionEffect from the Shape object

ReflectionEffect reflection = shape.getReflection();

//Set its Blur, Size, Transparency and Distance properties

reflection.setBlur(30);

reflection.setSize(90);

reflection.setTransparency(0.5);

reflection.setDistance(80);

//Save the result in XLSX format

book.save("output.xlsx");

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

 تحقق من المقال المفصل على[العمل مع تأثيرات الظل](/cells/ar/java/working-with-the-shadow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of ShadowEffect from the Shape object

ShadowEffect shadow = shape.getShadowEffect();

//Set its Angle, Blur, Size, Transparency and Distance properties

shadow.setAngle(150);

shadow.setBlur(30);

shadow.setSize(90);

shadow.setTransparency(0.5);

shadow.setDistance(80);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **دعم تأثيرات الوهج**
كشف Aspose.Cells 16.10.0 خاصية Shape.Glow جنبًا إلى جنب مع فئة GlowEffect التي تسمح معًا بضبط تأثير التوهج لكائن الشكل. تحدد فئة GlowEffect تأثير التوهج ، حيث تتم إضافة مخطط تمويه اللون خارج حواف الكائن باستخدام الخصائص التالية.

- GlowEffect.Size: الحصول على / تعيين نصف قطر التوهج بوحدة النقاط.
- GlowEffect.Transparency: الحصول على / تعيين درجة شفافية تأثير التوهج التي تتراوح من 0.0 (معتم) إلى 1.0 (واضح).

فيما يلي سيناريو الاستخدام البسيط لخاصية Shape.Glow.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[العمل مع تأثير الوهج](/cells/ar/java/working-with-the-glow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of GlowEffect from the Shape object

GlowEffect glow = shape.getGlow();

//Set its Size & Transparency properties

glow.setSize(90);

glow.setTransparency(0.5);

//Save the result in XLSX format

book.save("output.xlsx");

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

 تحقق من المقال المفصل على[العمل مع تنسيق ثلاثي الأبعاد](/cells/ar/java/working-with-the-threedformat-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of ThreeDFormat from the Shape object

ThreeDFormat threeD = shape.getThreeDFormat();

//Set its ContourWidth & ExtrusionHeight properties

threeD.setContourWidth(15);

threeD.setExtrusionHeight(30);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **دعم أنماط WordArt في نص الشكل**
كشف Aspose.Cells 16.10.0 عن طرق FontSettingCollection.SetWordArtStyle & FontSetting.SetWordArtStyle لتعيين نمط WordArt المضبوط مسبقًا على نص عنصر الشكل.

فيما يلي سيناريو الاستخدام البسيط للطرق المذكورة أعلاه.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[العمل مع أنماط WordArt](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Create a TextBox with some text

int index = sheet.getTextBoxes().add(0, 0, 100, 700);

TextBox textBox = (TextBox)sheet.getShapes().get(index);

textBox.setText("Aspose File Format APIs");

textBox.getFont().setSize(44);

//Set preset WordArt style to the text of the shape

FontSetting fntSetting = (FontSetting)textBox.getCharacters().get(0);

fntSetting.setWordArtStyle(PresetWordArtStyle.WORD_ART_STYLE_15);

{{< /highlight >}}
### **دعم أنماط WordArt المضمنة**
كشف Aspose.Cells 16.10.0 عن طريقة ShapeCollection.AddWordArt جنبًا إلى جنب مع تعداد PresetWordArtStyle من أجل توفير الدعم لإضافة كائنات WordArt سابقة الإعداد منذ Excel 2007.

فيما يلي سيناريو استخدام بسيط لطريقة ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[أضف WordArt بأنماط مضمنة](/cells/ar/java/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access ShapeCollection of first worksheet

ShapeCollection shapes = sheet.getShapes();

//Add WordArt with built-in styles

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_1, "Aspose File Format APIs", 00, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **تمت إضافة طريقة XmlMapCollection.Add**
كشف Aspose.Cells عن طريقة XmlMapCollection.Add التي تسمح بإضافة خريطة Xml إلى جدول بيانات. فيما يلي سيناريو استخدام بسيط لطريقة XmlMapCollection.Add.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[أضف خريطة XML إلى جدول البيانات](/cells/ar/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **تمت إضافة Cells.LinkToXmlMap**
كشف Aspose.Cells الآن الأسلوب Cells.LinkToXmlMap لربط الخلايا بعناصر مخطط XML. فيما يلي سيناريو الاستخدام البسيط لطريقة Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[ارتباط Cells بعناصر خريطة XML](/cells/ar/java/link-cells-to-xml-map-elements/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook("sample.xlsx");

//Access the XML Map from the spreadsheet

XmlMap map = book.getWorksheets().getXmlMaps().get(0);

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Map FIELD1 and FIELD2 to cell A1 and B2

sheet.getCells().linkToXmlMap(map.getName(), 0, 0, "/root/row/FIELD1");

sheet.getCells().linkToXmlMap(map.getName(), 1, 1, "/root/row/FIELD2");

//Map FIELD4 and FIELD5 to cell C3 and D4

sheet.getCells().linkToXmlMap(map.getName(), 2, 2, "/root/row/FIELD4");

sheet.getCells().linkToXmlMap(map.getName(), 3, 3, "/root/row/FIELD5");

//Map FIELD7 and FIELD8 to cell E5 and F6

sheet.getCells().linkToXmlMap(map.getName(), 4, 4, "/root/row/FIELD7");

sheet.getCells().linkToXmlMap(map.getName(), 5, 5, "/root/row/FIELD8");

{{< /highlight >}}
### **تمت إضافة خاصية ListColumn.Formula**
كشف Aspose.Cells 16.10.0 الخاصية ListColumn.Formula من أجل نشر المعادلة تلقائيًا إلى الصفوف المدرجة حديثًا.

فيما يلي سيناريو استخدام بسيط لخاصية ListColumn.Formula.

{{% alert color="primary" %}} 

 تحقق من المقال المفصل على[نشر الصيغة تلقائيًا في كائن القائمة](/cells/ar/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Add column headings in cell A1 and B1

sheet.getCells().get(0, 0).putValue("Column A");

sheet.getCells().get(0, 1).putValue("Column B");

//Add list object, set its name and style

ListObject listObject = sheet.getListObjects().get(sheet.getListObjects().add(0, 0, 1, sheet.getCells().getMaxColumn(), true));

listObject.setTableStyleType(TableStyleType.TABLE_STYLE_MEDIUM_14);

listObject.setDisplayName("Table");

//Set the formula of second column so that it could automatically propagate to new rows while entering data

listObject.getListColumns().get(1).setFormula("=[Column A]+ 1");

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
