---
title: Aspose.Cells 16.10.0中的公共API更改
type: docs
weight: 340
url: /zh/net/public-api-changes-in-aspose-cells-16-10-0/
---

{{% alert color="primary" %}} 

本文档描述了Aspose.Cells API从版本9.0.0到16.10.0的更改，可能会引起模块/应用程序开发人员的兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还描述了Aspose.Cells背后行为的任何更改。

{{% /alert %}} 
## **已添加API**
### **支持反射效果**
Aspose.Cells 16.10.0已暴露了ReflectionEffect类以及Shape.Reflection属性，以控制形状对象的反射效果。ReflectionEffect类具有以下属性。

- ReflectionEffect.Blur：以点为单位获取/设置模糊半径。
- ReflectionEffect.Direction：获取/设置Alpha梯度坡相对于形状本身的方向。
- ReflectionEffect.Distance：以点为单位获取/设置反射距离。
- ReflectionEffect.FadeDirection：获取/设置偏移反射的方向。
- ReflectionEffect.RotWithShape：获取/设置反射是否应随形状旋转。
- ReflectionEffect.Size：以百分比为单位获取/设置结束位置(沿Alpha梯度坡)的结束Alpha值。
- ReflectionEffect.Transparency：以从0.0（不透明）到1.0（清晰）的值获取/设置起始反射透明度的程度。
- ReflectionEffect.Type：获取/设置预设反射效果。

这是Shape.Reflection属性的简单使用场景。

{{% alert color="primary" %}} 

在[使用反射效果](/cells/zh/net/working-with-the-reflection-effect-of-shape-or-chart/)的详细文章中查看

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


### **支持阴影效果**
Aspose.Cells 16.10.0已暴露了Shape.ShadowEffect属性，以及ShadowEffect类，可以一起在形状对象上设置阴影效果。ShadowEffect类具有以下属性。

- ShadowEffect.Angle：获取/设置从0到359.9度范围的光照角度。
- ShadowEffect.Blur：获得并设置阴影的模糊范围，范围从0到100点。
- ShadowEffect.Color：获取/设置阴影的颜色。
- ShadowEffect.Distance：获取/设置从0到200点范围的阴影距离。
- ShadowEffect.PresetType：获取/设置阴影的预设阴影类型。
- ShadowEffect.Size：获取/设置范围为0到2.0的阴影尺寸。在内阴影情况下，这将毫无意义。
- ShadowEffect.Transparency：获取/设置阴影的透明度程度，范围从0.0（不透明）到1.0（清晰）。

这是前述属性的简单使用场景。

{{% alert color="primary" %}} 

在[使用阴影效果](/cells/zh/net/working-with-the-shadow-effect-of-shape-or-chart/)的详细文章中查看

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


### **支持发光效果**
Aspose.Cells 16.10.0已暴露了Shape.Glow属性，以及GlowEffect类，可以一起在形状对象上设置发光效果。GlowEffect类指定一种发光效果，通过以下属性添加一个颜色模糊的轮廓在对象的边缘外部。

- GlowEffect.Size：以点为单位获取/设置发光的半径。
- GlowEffect.Transparency: 获取/设置光晕效果的透明度，范围从 0.0（不透明）到 1.0（清晰）。

这里是 Shape.Glow 属性的简单使用场景。

{{% alert color="primary" %}} 

在[使用发光效果](/cells/zh/net/working-with-the-glow-effect-of-shape-or-chart/)的详细文章中查看

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


### **支持 3D 格式**
Aspose.Cells 16.10.0 暴露了 Shape.ThreeDFormat 属性以及 ThreeDFormat 类，可以一起用于控制 Shape 对象的 3D 格式化。ThreeDFormat 类代表形状的三维格式化，并具有以下属性。

- ThreeDFormat.BottomBevelHeight: 获取/设置底部斜角的高度或应用于形状的深度，单位为 Points。
- ThreeDFormat.BottomBevelType: 获取/设置底部斜角的类型或应用于形状的深度，单位为 Points。
- ThreeDFormat.BottomBevelWidth: 获取/设置底部斜角的宽度或应用于形状的深度，单位为 Points。
- ThreeDFormat.ContourColor: 获取/设置形状的轮廓颜色。
- ThreeDFormat.ContourWidth: 获取/设置形状的轮廓宽度，单位为 Points。
- ThreeDFormat.ExtrusionColor: 获取形状的挤出颜色。
- ThreeDFormat.ExtrusionHeight: 获取/设置应用于形状的挤出高度，单位为 Points。
- ThreeDFormat.LightAngle: 获取/设置挤出灯光的角度。
- ThreeDFormat.Lighting: 获取/设置灯光光源的类型。
- ThreeDFormat.LightingDirection: 获取/设置灯光光源在场景中朝向的方向。
- ThreeDFormat.Material: 代表与光照属性结合以给出形状最终外观的预设材质。
- ThreeDFormat.Perspective: 获取/设置 ThreeDFormat 对象的可查看角度。
- ThreeDFormat.PresetCameraType: 获取/设置挤出预设摄像机。
- ThreeDFormat.RotationX: 获取/设置绕 X 轴旋转的挤出形状的旋转，单位为度。
- ThreeDFormat.RotationY: 获取/设置绕 Y 轴旋转的挤出形状的旋转，单位为度。
- ThreeDFormat.RotationZ: 获取/设置绕 Z 轴旋转的挤出形状的旋转，单位为度。
- ThreeDFormat.TopBevelHeight: 获取/设置顶部斜角的高度或应用于形状的深度，单位为 Points。
- ThreeDFormat.TopBevelType: 获取/设置顶部斜角的类型或应用于形状的深度，单位为 Points。
- ThreeDFormat.TopBevelWidth: 获取/设置顶部斜角的宽度或应用于形状的深度，单位为 Points。
- ThreeDFormat.Z: 定义 3D 形状离地面的距离。

以下是 Shape.ThreeDFormat 属性的简单使用场景。

{{% alert color="primary" %}} 

在[使用三维格式](/cells/zh/net/working-with-the-threedformat-of-shape-or-chart/)的详细文章中查看

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


### **支持 Shape 文本中的 WordArt 样式**
Aspose.Cells 16.10.0 暴露了 FontSettingCollection.SetWordArtStyle 和 FontSetting.SetWordArtStyle 方法，以便为 Shape 对象的文本设置预设 WordArt 样式。

以下是上述方法的简单使用场景。

{{% alert color="primary" %}} 

在[WordArt样式](/cells/zh/net/set-preset-wordart-style-to-the-text-of-the-shape/)的详细文章中查看

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


### **支持WordArt内置样式**
Aspose.Cells 16.10.0已经公开了ShapeCollection.AddWordArt方法，同时还暴露了PresetWordArtStyle枚举，以便在Excel 2007中添加预设的WordArt对象。

这里是ShapeCollection.AddWordArt方法的简单使用情景。

{{% alert color="primary" %}} 

在[使用内置样式添加WordArt](/cells/zh/net/add-word-art-text-with-built-in-styles/)的详细文章中查看

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


### **新增了XmlMapCollection.Add方法**
Aspose.Cells现在暴露了XmlMapCollection.Add方法，允许向电子表格添加Xml Map。这里是XmlMapCollection.Add方法的简单使用情景。

{{% alert color="primary" %}} 

在[电子表格中添加XML映射](/cells/zh/net/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)的详细文章中查看

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Add xml map from the sample.xml to the workbook

book.Worksheets.XmlMaps.Add("sample.xml");

{{< /highlight >}}


### **新增了Cells.LinkToXmlMap方法**
现在Aspose.Cells暴露了Cells.LinkToXmlMap方法，以将单元格链接到XML映射元素。

这里是Cells.LinkToXmlMap方法的简单使用情景。

{{% alert color="primary" %}} 

在[将单元格链接到XML映射元素](/cells/zh/net/link-cells-to-xml-map-elements/)的详细文章中查看

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


### **新增了ListColumn.Formula属性**
Aspose.Cells 16.10.0现在暴露了ListColumn.Formula属性，以便自动将公式传播到新插入的行。

这里是ListColumn.Formula属性的简单使用情景。

{{% alert color="primary" %}} 

在[表格或列表对象中自动传播公式](/cells/zh/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)的详细文章中查看

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


### **支持使用GridWeb计算自定义函数**
Aspose.Cells.GridWeb 16.10.0现在暴露了GridWeb.CustomCalculationEngine属性以及GridAbstractCalculationEngine类，可以一起在GridWeb组件内定义和计算自定义函数。

这里是上述API的简单使用情景。

{{% alert color="primary" %}} 

在[GridWeb中计算自定义函数](/cells/zh/net/calculate-custom-functions-in-gridweb/)的详细文章中查看

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
