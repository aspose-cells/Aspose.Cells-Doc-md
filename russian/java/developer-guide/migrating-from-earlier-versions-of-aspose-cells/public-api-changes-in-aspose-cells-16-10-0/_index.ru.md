---
title: Общедоступный API Изменения в Aspose.Cells 16.10.0
type: docs
weight: 350
url: /ru/java/public-api-changes-in-aspose-cells-16-10-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 9.0.0 до 16.10.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка эффектов отражения**
Aspose.Cells 16.10.0 предоставляет класс ReflectionEffect вместе со свойством Shape.Reflection для управления эффектами отражения объекта Shape. Класс ReflectionEffect имеет следующие свойства.

- ReflectionEffect.Blur: получает/задает радиус размытия в точках.
- ReflectionEffect.Direction: получает/задает направление градиента альфа-канала относительно самой фигуры.
- ReflectionEffect.Distance: получает/устанавливает расстояние отражения в единицах точек.
- ReflectionEffect.FadeDirection: получает/задает направление смещения отражения.
- ReflectionEffect.RotWithShape: получает/устанавливает, должно ли отражение вращаться вместе с фигурой.
- ReflectionEffect.Size: получает/задает конечную позицию (вдоль шкалы альфа-градиента) конечного альфа-значения в процентах.
- ReflectionEffect.Transparency: получает/задает степень начальной прозрачности отражения в виде значения от 0,0 (непрозрачный) до 1,0 (прозрачный).
- ReflectionEffect.Type: получает/устанавливает предустановленный эффект отражения.

Вот простой сценарий использования свойства Shape.Reflection.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Работа с эффектами отражения](/cells/ru/java/working-with-the-reflection-effect-of-shape-or-chart/)

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
### **Поддержка теневых эффектов**
Aspose.Cells 16.10.0 предоставляет свойство Shape.ShadowEffect вместе с классом ShadowEffect, которые все вместе позволяют установить эффект тени для объекта Shape. Класс ShadowEffect имеет следующие свойства.

- ShadowEffect.Angle: получает/устанавливает угол освещения в диапазоне от 0 до 359,9 градусов.
- ShadowEffect.Blur: получает и задает размытие тени в диапазоне от 0 до 100 баллов.
- ShadowEffect.Color: получает/устанавливает цвет тени.
- ShadowEffect.Distance: получает/устанавливает расстояние тени в диапазоне от 0 до 200 точек.
- ShadowEffect.PresetType: получает/устанавливает предустановленный тип тени тени.
- ShadowEffect.Size: получает/устанавливает размер тени в диапазоне от 0 до 2,0. Это будет бессмысленно в случае внутренней тени.
- ShadowEffect.Transparency: получает/задает степень прозрачности тени в диапазоне от 0,0 (непрозрачная) до 1,0 (прозрачная).

Вот простой сценарий использования вышеупомянутого свойства.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Работа с теневыми эффектами](/cells/ru/java/working-with-the-shadow-effect-of-shape-or-chart/)

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
### **Поддержка эффектов свечения**
Aspose.Cells 16.10.0 предоставляет свойство Shape.Glow вместе с классом GlowEffect, которые вместе позволяют установить эффект свечения объекта Shape. Класс GlowEffect задает эффект свечения, при котором контур с размытым цветом добавляется за пределы краев объекта с помощью следующих свойств.

- GlowEffect.Size: Получает/устанавливает радиус свечения в единицах точек.
- GlowEffect.Transparency: получает/задает степень прозрачности эффекта свечения в диапазоне от 0,0 (непрозрачный) до 1,0 (прозрачный).

Вот простой сценарий использования свойства Shape.Glow.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Работа с эффектом свечения](/cells/ru/java/working-with-the-glow-effect-of-shape-or-chart/)

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
### **Поддержка формата 3D**
Aspose.Cells 16.10.0 предоставляет свойство Shape.ThreeDFormat вместе с классом ThreeDFormat, которые вместе можно использовать для управления трехмерным форматированием объекта Shape. Класс ThreeDFormat представляет трехмерное форматирование фигуры и имеет следующие свойства.

- ThreeDFormat.BottomBevelHeight: получает/задает высоту нижнего скоса или глубину его применения в фигуре в точках.
- ThreeDFormat.BottomBevelType: получает/задает тип нижнего скоса или глубину его применения в фигуре в точках.
- ThreeDFormat.BottomBevelWidth: получает/задает ширину нижнего скоса или глубину его применения в фигуре в точках.
- ThreeDFormat.ContourColor: получает/задает цвет контура фигуры.
- ThreeDFormat.ContourWidth: получает/задает ширину контура фигуры в точках.
- ThreeDFormat.ExtrusionColor: получает цвет экструзии фигуры.
- ThreeDFormat.ExtrusionHeight: получает/задает высоту экструзии, применяемую к фигуре, в точках.
- ThreeDFormat.LightAngle: получает/задает угол экструзионного освещения.
- ThreeDFormat.Lighting: получает/устанавливает тип установки освещения.
- ThreeDFormat.LightingDirection: получает/задает направление, с которого установка освещения ориентирована по отношению к сцене.
- ThreeDFormat.Material: представляет предустановленный материал, который в сочетании со свойствами освещения придает окончательный вид и ощущение формы.
- ThreeDFormat.Perspective: получает/задает угол, под которым можно просматривать объект ThreeDFormat.
- ThreeDFormat.PresetCameraType: получает/задает предустановленную камеру экструзии.
- ThreeDFormat.RotationX: получает/задает вращение вытянутой формы вокруг оси X в градусах.
- ThreeDFormat.RotationY: получает/задает вращение вытянутой формы вокруг оси Y в градусах.
- ThreeDFormat.RotationZ: получает/задает вращение вытянутой формы вокруг оси Z в градусах.
- ThreeDFormat.TopBevelHeight: получает/задает высоту верхнего скоса или глубину его применения в фигуре в точках.
- ThreeDFormat.TopBevelType: получает/задает тип верхнего скоса или глубину его применения в форме в точках.
- ThreeDFormat.TopBevelWidth: получает/задает ширину верхнего скоса или глубину его применения в фигуре в точках.
- ThreeDFormat.Z: определяет расстояние от земли для трехмерной формы.

Ниже приведен простой сценарий использования свойства Shape.ThreeDFormat.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Работа с форматированием 3D](/cells/ru/java/working-with-the-threedformat-of-shape-or-chart/)

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
### **Поддержка стилей WordArt в тексте фигуры**
Aspose.Cells 16.10.0 предоставляет методы FontSettingCollection.SetWordArtStyle и FontSetting.SetWordArtStyle, чтобы установить предустановленный стиль WordArt для текста объекта Shape.

Вот простой сценарий использования вышеупомянутых методов.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Работа со стилями WordArt](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

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
### **Поддержка встроенных стилей WordArt**
Aspose.Cells 16.10.0 предоставляет метод ShapeCollection.AddWordArt вместе с перечислением PresetWordArtStyle, чтобы обеспечить поддержку добавления предустановленных объектов WordArt, начиная с Excel 2007.

Вот простой сценарий использования метода ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Добавьте WordArt со встроенными стилями](/cells/ru/java/add-word-art-text-with-built-in-styles/)

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
### **Добавлен метод XmlMapCollection.Add.**
Aspose.Cells предоставил метод XmlMapCollection.Add, который позволяет добавить карту Xml в электронную таблицу. Вот простой сценарий использования метода XmlMapCollection.Add.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Добавить XML-карту в электронную таблицу](/cells/ru/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Добавлен метод Cells.LinkToXmlMap.**
Aspose.Cells теперь предоставляет метод Cells.LinkToXmlMap для связывания ячеек с элементами карты XML. Вот простой сценарий использования метода Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Ссылка Cells на элементы карты XML](/cells/ru/java/link-cells-to-xml-map-elements/)

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
### **Добавлено свойство ListColumn.Formula**
Aspose.Cells 16.10.0 предоставило свойство ListColumn.Formula для автоматического распространения формулы на вновь вставленные строки.

Вот простой сценарий использования свойства ListColumn.Formula.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Автоматически распространять формулу в объекте списка](/cells/ru/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

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
