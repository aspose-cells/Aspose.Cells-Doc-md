---
title: Изменения в открытом API в Aspose.Cells 16.10.0
type: docs
weight: 340
url: /ru/net/public-api-changes-in-aspose-cells-16-10-0/
---

{{% alert color="primary" %}} 

В этом документе описаны изменения в API Aspose.Cells с версии 9.0.0 до 16.10.0, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные открытые методы, добавленные и удаленные классы и т.д., но также описание любых изменений в поведении внутри Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка эффектов отражения**
Aspose.Cells 16.10.0 представил класс ReflectionEffect вместе с свойством Shape.Reflection для управления отражением объекта Shape. Класс ReflectionEffect имеет следующие свойства.

- ReflectionEffect.Blur: Получает/устанавливает радиус размытия в единицах точек.
- ReflectionEffect.Direction: Получает/устанавливает направление альфа-градиента относительно самой формы.
- ReflectionEffect.Distance: Получает/устанавливает расстояние отражения в единицах точек.
- ReflectionEffect.FadeDirection: Получает/устанавливает направление смещения отражения.
- ReflectionEffect.RotWithShape: Получает/устанавливает, должно ли отражение вращаться вместе с формой.
- ReflectionEffect.Size: Получает/устанавливает конечную позицию (вдоль альфа-градиента) конечного значения альфа в процентах.
- ReflectionEffect.Transparency: Получает/устанавливает степень начальной прозрачности отражения в виде значения от 0,0 (непрозрачный) до 1,0 (прозрачный).
- ReflectionEffect.Type: Получает/устанавливает предустановленный эффект отражения.

Вот простой сценарий использования свойства Shape.Reflection.

{{% alert color="primary" %}} 

Проверьте подробную статью по теме [Работа с эффектами отражения](/cells/ru/net/working-with-the-reflection-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Поддержка эффектов тени**
Aspose.Cells 16.10.0 представил свойство Shape.ShadowEffect вместе с классом ShadowEffect, которые вместе позволяют устанавливать эффект тени на объект Shape. Класс ShadowEffect имеет следующие свойства.

- ShadowEffect.Angle: Получает/устанавливает угол освещения в пределах от 0 до 359,9 градусов.
- ShadowEffect.Blur: Получает и устанавливает размытие тени в пределах от 0 до 100 точек.
- ShadowEffect.Color: Получает/устанавливает цвет тени.
- ShadowEffect.Distance: Получает/устанавливает расстояние тени в пределах от 0 до 200 точек.
- ShadowEffect.PresetType: Получает/устанавливает предустановленный тип тени тени.
- ShadowEffect.Size: Получает/устанавливает размер тени в пределах от 0 до 2,0. Будет бессмысленным в случае внутренней тени.
- ShadowEffect.Transparency: Получает/устанавливает степень прозрачности тени в пределах от 0,0 (непрозрачный) до 1,0 (прозрачный).

Вот простой сценарий использования упомянутого свойства.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Работа с эффектами тени](/cells/ru/net/working-with-the-shadow-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Поддержка эффектов свечения**
Aspose.Cells 16.10.0 добавил свойство Shape.Glow вместе с классом GlowEffect, которые вместе позволяют установить эффект свечения объекта формы. Класс GlowEffect указывает свечение, в котором цветной размытый контур добавляется снаружи краев объекта с использованием следующих свойств.

- GlowEffect.Size: Получает/устанавливает радиус свечения в единицах точек.
- GlowEffect.Transparency: Получает/устанавливает степень прозрачности свечения от 0.0 (непрозрачный) до 1.0 (прозрачный).

Вот простой сценарий использования свойства Shape.Glow.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Работа с эффектом свечения](/cells/ru/net/working-with-the-glow-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Поддержка формата 3D**
Aspose.Cells 16.10.0 добавил свойство Shape.ThreeDFormat вместе с классом ThreeDFormat, что вместе можно использовать для управления форматированием 3D объекта формы. Класс ThreeDFormat представляет трехмерное форматирование формы и имеет следующие свойства.

- ThreeDFormat.BottomBevelHeight: Получает/устанавливает высоту нижней фаски или насколько далеко она применяется к форме, в единицах точек.
- ThreeDFormat.BottomBevelType: Получает/устанавливает тип нижней фаски или насколько далеко она применяется к форме, в единицах точек.
- ThreeDFormat.BottomBevelWidth: Получает/устанавляет ширину нижней фаски или насколько далеко она применяется к форме, в единицах точек.
- ThreeDFormat.ContourColor: Получает/устанавливает цвет контура формы.
- ThreeDFormat.ContourWidth: Получает/устанавливает ширину контура на форме, в единицах точек.
- ThreeDFormat.ExtrusionColor: Получает цвет выдавливания на форме.
- ThreeDFormat.ExtrusionHeight: Получает/устанавливает высоту выдавливания, применяемую к форме, в единицах точек.
- ThreeDFormat.LightAngle: Получает/устанавливает угол светового выдавливания.
- ThreeDFormat.Lighting: Получает/устанавливает тип источника света.
- ThreeDFormat.LightingDirection: Получает/устанавливает направление, откуда ориентирован источник света относительно сцены.
- ThreeDFormat.Material: Представляет предустановленный материал, который в сочетании с освещением дает окончательный внешний вид и ощущение формы.
- ThreeDFormat.Perspective: Получает/устанавливает угол, под которым объект ThreeDFormat может быть просмотрен.
- ThreeDFormat.PresetCameraType: Получает/устанавливает предустановленную камеру экструзии.
- ThreeDFormat.RotationX: Получает/устанавливает вращение выдавленной формы вокруг оси X в градусах.
- ThreeDFormat.RotationY: Получает/устанавливает вращение выдавленной формы вокруг оси Y в градусах.
- ThreeDFormat.RotationZ: Получает/устанавливает вращение выдавленной формы вокруг оси Z в градусах.
- ThreeDFormat.TopBevelHeight: Получает/устанавливает высоту верхней фаски или расстояние, на которое она применяется к форме, в пунктах.
- ThreeDFormat.TopBevelType: Получает/устанавливает тип верхней фаски или расстояние, на которое она применяется к форме, в пунктах.
- ThreeDFormat.TopBevelWidth: Получает/устанавливает ширину верхней фаски или расстояние, на которое она применяется к форме, в пунктах.
- ThreeDFormat.Z: Задает расстояние от земли для 3D-формы.

Ниже приведен простой сценарий использования свойства Shape.ThreeDFormat.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Работа с 3D-форматированием](/cells/ru/net/working-with-the-threedformat-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Поддержка стилей WordArt в тексте формы**
Aspose.Cells 16.10.0 добавил методы FontSettingCollection.SetWordArtStyle и FontSetting.SetWordArtStyle для установки предустановленного стиля WordArt в тексте объекта Shape.

Вот пример простого сценария использования указанных выше методов.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Работа со стилями WordArt](/cells/ru/net/set-preset-wordart-style-to-the-text-of-the-shape/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create workbook object

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Create a TextBox with some text

var textBox = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 700);

textBox.Text = "Aspose File Format APIs";

textBox.Font.Size = 44;

// Set preset WordArt style to the text of the shape

FontSetting fntSetting = textBox.GetCharacters()[0] as FontSetting;

fntSetting.SetWordArtStyle(PresetWordArtStyle.WordArtStyle3);

{{< /highlight >}}


### **Поддержка встроенных стилей WordArt**
Aspose.Cells 16.10.0 добавил метод ShapeCollection.AddWordArt вместе с перечислением PresetWordArtStyle для добавления поддержки предустановленных объектов WordArt начиная с Excel 2007.

Ниже приведен простой сценарий использования метода ShapeCollection.AddWordArt.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Добавлению WordArt с встроенными стилями](/cells/ru/net/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Добавлен метод XmlMapCollection.Add**
Aspose.Cells теперь предоставляет метод XmlMapCollection.Add, позволяющий добавлять Xml Map в электронную таблицу. Вот простой сценарий использования метода XmlMapCollection.Add.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Добавлению XML-карты к электронной таблице](/cells/ru/net/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Add xml map from the sample.xml to the workbook

book.Worksheets.XmlMaps.Add("sample.xml");

{{< /highlight >}}


### **Добавлен метод Cells.LinkToXmlMap**
Aspose.Cells теперь предоставляет метод Cells.LinkToXmlMap для связи ячеек с элементами XML-карты.

Вот простой сценарий использования метода Cells.LinkToXmlMap.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Связыванию ячеек с элементами XML-карты](/cells/ru/net/link-cells-to-xml-map-elements/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Добавлено свойство ListColumn.Formula**
Aspose.Cells 16.10.0 предоставляет свойство ListColumn.Formula для автоматической передачи формулы в новые вставленные строки.

Вот простой сценарий использования свойства ListColumn.Formula.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Автоматическому распространению формул в объекте списка](/cells/ru/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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

listObject.ListColumns[1].Formula = "=[Column A] + 1";

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **Поддержка вычисления пользовательских функций с GridWeb**
Aspose.Cells.GridWeb 16.10.0 теперь предоставляет свойство GridWeb.CustomCalculationEngine вместе с классом GridAbstractCalculationEngine, что вместе позволяет определять и вычислять пользовательские функции в компоненте GridWeb.

Вот простой сценарий использования упомянутых API.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Вычислению пользовательских функций с GridWeb](/cells/ru/net/calculate-custom-functions-in-gridweb/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
