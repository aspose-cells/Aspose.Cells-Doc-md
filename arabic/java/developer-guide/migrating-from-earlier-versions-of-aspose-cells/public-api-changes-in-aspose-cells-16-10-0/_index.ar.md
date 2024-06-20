---
title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.Cells 16.10.0
type: docs
weight: 350
url: /ar/java/public-api-changes-in-aspose-cells-16-10-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 9.0.0 إلى 16.10.0 التي قد تكون مثيرة للاهتمام لمطوري الوحدة / التطبيق. يتضمن ليس فقط الأساليب العامة الجديدة والمحدثة والفئات المضافة والمحذوفة وما إلى ذلك ، ولكن أيضًا وصفًا لأي تغييرات في السلوك وراء الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **دعم لتأثيرات الانعكاس**
قدمت Aspose.Cells 16.10.0 فئة ReflectionEffect بالإضافة إلى خاصية Shape.Reflection للتحكم في تأثيرات الانعكاس لكائن Shape. تحتوي فئة ReflectionEffect على الخصائص التالية.

- ReflectionEffect.Blur: يحصل/يضع قيمة نصف قطر الطمس بوحدة النقاط.
- ReflectionEffect.Direction: يحصل/يعين اتجاه التدرج ألفا بالنسبة إلى الشكل نفسه.
- ReflectionEffect.Distance: يحصل/يعين مسافة الانعكاس بوحدة النقاط.
- ReflectionEffect.FadeDirection: يحصل/يعين الاتجاه لتحويل الانعكاس.
- ReflectionEffect.RotWithShape: يحصل/يعين ما إذا كان الانعكاس يجب أن يدور مع الشكل.
- ReflectionEffect.Size: يحصل/يعين الموضع النهائي (على طول التدرج ألفا) لقيمة نهاية ألفا بوحدة النسبة المئوية.
- ReflectionEffect.Transparency: يحصل/يعين درجة شفافية الانعكاس البدءية كقيمة من 0.0 (غير شفاف) إلى 1.0 (واضحة).
- ReflectionEffect.Type: يحصل/يعين تأثير الانعكاس المحدد مسبقًا.

ها هو سيناريو استخدام بسيط لخاصية Shape.Reflection.

{{% alert color="primary" %}} 

تحقق من المقال المفصل عن [العمل مع تأثيرات الانعكاس](/cells/ar/java/working-with-the-reflection-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
قد أظهرت Aspose.Cells 16.10.0 خاصية Shape.ShadowEffect إلى جانب صنف ShadowEffect الذي يتيح بالكامل تعيين تأثير الظل على كائن Shape. يحتوي صنف ShadowEffect على الخصائص التالية.

- ShadowEffect.Angle: يحصل/يعين زاوية الإضاءة التي تتراوح بين 0 إلى 359.9 درجة.
- ShadowEffect.Blur: يحصل/يعين ضبابية الظل التي تتراوح بين 0 إلى 100 نقطة.
- ShadowEffect.Color: يحصل/يعين لون الظل.
- ShadowEffect.Distance: يحصل/يعين المسافة الظل التي تتراوح بين 0 إلى 200 نقطة.
- ShadowEffect.PresetType: يحصل/يعين نوع الظل المحدد مسبقًا للظل.
- ShadowEffect.Size: يحصل/يعين حجم الظل الذي يتراوح بين 0 إلى 2.0.سيكون لا معنى له في حالة الظل الداخلي.
- ShadowEffect.Transparency: يحصل/يعين درجة شفافية الظل التي تتراوح من 0.0 (غير شفاف) إلى 1.0 (واضحة).

ها هو سيناريو استخدام بسيط للخاصية المذكورة أعلاه.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [العمل مع تأثيرات الظل](/cells/ar/java/working-with-the-shadow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **الدعم لتأثيرات التوهج**
أعرضت Aspose.Cells 16.10.0 خاصية Shape.Glow بالإضافة إلى فئة GlowEffect التي تُسمح معًا بتعيين تأثير التوهج لكائن الشكل. تحدد فئة GlowEffect تأثير توهج، حيث يتم إضافة إطار مضبب للون خارج حواف الكائن باستخدام الخصائص التالية.

- GlowEffect.Size: يحصل/يقوم بتعيين نصف قطر التوهج بوحدة النقاط.
- GlowEffect.Transparency: يحصل/يقوم بتعيين درجة شفافية تأثير التوهج تتراوح بين 0.0 (غير شفاف) و 1.0 (واضح).

إليك سيناريو استخدام بسيط لخاصية Shape.Glow.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [العمل مع تأثيرات التوهج](/cells/ar/java/working-with-the-glow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **الدعم لتنسيق ثلاثي الأبعاد**
أعرضت Aspose.Cells 16.10.0 خاصية Shape.ThreeDFormat بالإضافة إلى فئة ThreeDFormat التي يمكن استخدامها معًا للتحكم في تنسيق الأبعاد ثلاثية الشكل. تُمثل فئة ThreeDFormat تنسيق الأبعاد الثلاثية للشكل وتحتوي على الخصائص التالية.

- ThreeDFormat.BottomBevelHeight: يحصل/يقوم بتعيين ارتفاع الحافة السفلية أو مدى تطبيقها على الشكل، بوحدة النقاط.
- ThreeDFormat.BottomBevelType: يحصل/يقوم بتعيين نوع الحافة السفلية أو مدى تطبيقها على الشكل، بوحدة النقاط.
- ThreeDFormat.BottomBevelWidth: يحصل/يقوم بتعيين عرض الحافة السفلية أو مدى تطبيقها على الشكل، بوحدة النقاط.
- ThreeDFormat.ContourColor: يحصل/يقوم بتعيين لون التحديد على الشكل.
- ThreeDFormat.ContourWidth: يحصل/يقوم بتعيين عرض التحديد على الشكل، بوحدة النقاط.
- ThreeDFormat.ExtrusionColor: يحصل على لون الإرتفاع على الشكل.
- ThreeDFormat.ExtrusionHeight: يحصل/يقوم بتعيين ارتفاع الإرتفاع المطبق على الشكل، بوحدة النقاط.
- ThreeDFormat.LightAngle: يحصل/يقوم بتعيين زاوية أضواء الإرتفاع.
- ThreeDFormat.Lighting: يحصل/يقوم بتعيين نوع الجو الخفيف.
- ThreeDFormat.LightingDirection: يحصل/ يحدد الاتجاه الذي يتوجه منه معدات الإضاءة بالنسبة للمشهد.
- ThreeDFormat.Material: يمثل المواد المُعينة التي تجمع مع خصائص الإضاءة لإعطاء المظهر والشعور النهائي للشكل.
- ThreeDFormat.Perspective: يحصل/ يحدد الزاوية التي يمكن من خلالها رؤية كائن ThreeDFormat.
- ThreeDFormat.PresetCameraType: يحصل/ يحدد كاميرا الاستخراج المُعينة.
- ThreeDFormat.RotationX: يحصل/ يحدد دوران الشكل المنتفخ حول محور الإكس بوحدة من الدرجات.
- ThreeDFormat.RotationY: يحصل/ يحدد دوران الشكل المنتفخ حول محور الواي بوحدة من الدرجات.
- ThreeDFormat.RotationZ: يحصل/ يحدد دوران الشكل المنتفخ حول محور الزد بوحدة من الدرجات.
- ThreeDFormat.TopBevelHeight: يحصل/ يحدد ارتفاع الحافة العلوية أو مدى تطبيقها في الشكل بوحدة من النقاط.
- ThreeDFormat.TopBevelType: يحصل/ يحدد نوع الحافة العلوية أو مدى تطبيقها في الشكل بوحدة من النقاط.
- ThreeDFormat.TopBevelWidth: يحصل/ يحدد عرض الحافة العلوية أو مدى تطبيقها في الشكل بوحدة من النقاط.
- ThreeDFormat.Z: يُعرِّف المسافة من الأرض للشكل ثلاثي الأبعاد.

فيما يلي سيناريو الاستخدام البسيط لخاصية Shape.ThreeDFormat.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [العمل مع تنسيقات ثلاثية الأبعاد](/cells/ar/java/working-with-the-threedformat-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **دعم لأنماط WordArt في نص الشكل**
كشفت Aspose.Cells 16.10.0 عن أساليب FontSettingCollection.SetWordArtStyle & FontSetting.SetWordArtStyle لضبط أسلوب WordArt المُعين مسبقًا لنص الشكل.

فيما يلي سيناريو استخدام بسيط للطرق المذكورة أعلاه.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول ال[عمل مع أساليب WordArt](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
### **دعم لأساليب WordArt المضمنة**
أتاح Aspose.Cells 16.10.0 طريقة إضافة الكلمات الفنية (WordArt) مع قائمة تمهيدية لأسلوب WordArtPreserenumeration بهدف دعم إضافة كائنات WordArt التي تم تحديدها مسبقًا منذ إصدار Excel 2007.

إليك سيناريو استخدام بسيط لطريقة إضافة الكلمات الفنية (WordArt) في مجموعة الأشكال.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [إضافة الكلمات الفنية (WordArt) بأنماط مدمجة](/cells/ar/java/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
أتاح Aspose.Cells طريقة XmlMapCollection.Add التي تسمح بإضافة خريطة XML إلى جدول بيانات. إليك سيناريو استخدام بسيط لطريقة XmlMapCollection.Add.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [إضافة خريطة XML إلى جدول بيانات](/cells/ar/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **تمت إضافة طريقة Cells.LinkToXmlMap**
أتاح Aspose.Cells الآن طريقة Cells.LinkToXmlMap بهدف ربط الخلايا بعناصر خريطة XML. إليك سيناريو استخدام بسيط لطريقة Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [ربط الخلايا بعناصر خريطة XML](/cells/ar/java/link-cells-to-xml-map-elements/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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
أتاح Aspose.Cells 16.10.0 خاصية ListColumn.Formula بهدف نقل الصيغة تلقائيًا إلى الصفوف المدخلة حديثًا.

إليك سيناريو استخدام بسيط لخاصية ListColumn.Formula.

{{% alert color="primary" %}} 

تحقق من المقال المفصل حول [نقل الصيغة تلقائيًا في كائن القائمة](/cells/ar/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

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

listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
