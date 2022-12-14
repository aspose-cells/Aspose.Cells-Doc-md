---
title: 公共 API Aspose.Cells 16.10.0 的变化
type: docs
weight: 350
url: /zh/java/public-api-changes-in-aspose-cells-16-10-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 9.0.0 到 16.10.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持反射效果**
Aspose.Cells 16.10.0 公开了 ReflectionEffect 类和 Shape.Reflection 属性，以控制 Shape 对象的反射效果。 ReflectionEffect 类具有以下属性。

- ReflectionEffect.Blur：获取/设置以点为单位的模糊半径。
- ReflectionEffect.Direction：获取/设置 alpha 渐变渐变相对于形状本身的方向。
- ReflectionEffect.Distance：获取/设置以点为单位的反射距离。
- ReflectionEffect.FadeDirection：获取/设置偏移反射的方向。
- ReflectionEffect.RotWithShape：获取/设置反射是否应随形状旋转。
- ReflectionEffect.Size：获取/设置以百分比为单位的结束 alpha 值的结束位置（沿着 alpha 渐变斜坡）。
- ReflectionEffect.Transparency：获取/设置起始反射透明度的程度，值为从 0.0（不透明）到 1.0（透明）的值。
- ReflectionEffect.Type：获取/设置预设反射效果。

这是 Shape.Reflection 属性的简单使用场景。

{{% alert color="primary" %}} 

查看详细文章[使用反射效果](/cells/zh/java/working-with-the-reflection-effect-of-shape-or-chart/)

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
### **支持阴影效果**
Aspose.Cells 16.10.0 公开了 Shape.ShadowEffect 属性和 ShadowEffect 类，它们一起允许在 Shape 对象上设置阴影效果。 ShadowEffect 类具有以下属性。

- ShadowEffect.Angle：获取/设置光照角度，范围为0到359.9度。
- ShadowEffect.Blur：获取和设置阴影的模糊度，范围为0到100点。
- ShadowEffect.Color：获取/设置阴影的颜色。
- ShadowEffect.Distance：获取/设置阴影的距离，取值范围为0到200点。
- ShadowEffect.PresetType：获取/设置阴影的预设阴影类型。
- ShadowEffect.Size：获取/设置阴影的大小，范围从0到2.0。如果有内阴影，它将毫无意义。
- ShadowEffect.Transparency：获取/设置阴影的透明度，范围从0.0（不透明）到1.0（透明）。

这是上述属性的简单使用场景。

{{% alert color="primary" %}} 

查看详细文章[使用阴影效果](/cells/zh/java/working-with-the-shadow-effect-of-shape-or-chart/)

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
### **支持发光效果**
Aspose.Cells 16.10.0 公开了 Shape.Glow 属性和 GlowEffect 类，它们一起允许设置 Shape 对象的发光效果。 GlowEffect 类指定发光效果，其中使用以下属性在对象边缘外添加颜色模糊轮廓。

- GlowEffect.Size：获取/设置以点为单位的发光半径。
- GlowEffect.Transparency：获取/设置发光效果的透明度，范围从0.0（不透明）到1.0（透明）。

这是 Shape.Glow 属性的简单使用场景。

{{% alert color="primary" %}} 

查看详细文章[使用发光效果](/cells/zh/java/working-with-the-glow-effect-of-shape-or-chart/)

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
### **支持 3D 格式**
Aspose.Cells 16.10.0 公开了 Shape.ThreeDFormat 属性以及 ThreeDFormat 类，它们一起可用于控制 Shape 对象的 3D 格式设置。 ThreeDFormat 类表示形状的三维格式并具有以下属性。

- ThreeDFormat.BottomBevelHeight：获取/设置底部斜面的高度或应用形状的深度，以点为单位。
- ThreeDFormat.BottomBevelType：获取/设置底部斜面的类型或应用形状的深度，以点为单位。
- ThreeDFormat.BottomBevelWidth：获取/设置底部斜面的宽度或应用形状的深度，以点为单位。
- ThreeDFormat.ContourColor：获取/设置形状的轮廓颜色。
- ThreeDFormat.ContourWidth：获取/设置形状上的轮廓宽度，以Points为单位。
- ThreeDFormat.ExtrusionColor：获取形状上的挤出颜色。
- ThreeDFormat.ExtrusionHeight：获取/设置应用于形状的挤出高度，单位为Points。
- ThreeDFormat.LightAngle：获取/设置挤出灯的角度。
- ThreeDFormat.Lighting：获取/设置光照装置的类型。
- ThreeDFormat.LightingDirection：获取/设置灯光装置相对于场景的方向。
- ThreeDFormat.Material：表示预设材质，它与照明属性相结合以提供形状的最终外观和感觉。
- ThreeDFormat.Perspective：获取/设置可以查看 ThreeDFormat 对象的角度。
- ThreeDFormat.PresetCameraType：获取/设置挤压预设相机。
- ThreeDFormat.RotationX：获取/设置拉伸形状绕 X 轴的旋转度，单位为 Degrees。
- ThreeDFormat.RotationY：获取/设置拉伸形状绕 Y 轴的旋转度，单位为 Degrees。
- ThreeDFormat.RotationZ：获取/设置拉伸形状绕 Z 轴的旋转度，单位为 Degrees。
- ThreeDFormat.TopBevelHeight：获取/设置顶部斜面的高度或应用到形状中的深度，以点为单位。
- ThreeDFormat.TopBevelType：获取/设置顶部斜面的类型或它应用到形状中的程度，以点为单位。
- ThreeDFormat.TopBevelWidth：获取/设置顶部斜角的宽度或应用到形状中的距离，以点为单位。
- ThreeDFormat.Z：定义 3D 形状与地面的距离。

以下是 Shape.ThreeDFormat 属性的简单使用场景。

{{% alert color="primary" %}} 

查看详细文章[使用 3D 格式](/cells/zh/java/working-with-the-threedformat-of-shape-or-chart/)

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
### **支持形状文本中的艺术字样式**
Aspose.Cells 16.10.0 公开了 FontSettingCollection.SetWordArtStyle 和 FontSetting.SetWordArtStyle 方法，以便将预设艺术字样式设置为 Shape 对象的文本。

下面是上述方法的简单使用场景。

{{% alert color="primary" %}} 

查看详细文章[使用艺术字样式](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

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
### **支持艺术字内置样式**
Aspose.Cells 16.10.0 公开了 ShapeCollection.AddArt 方法以及 PresetWordArtStyle 枚举，以提供对自 Excel 2007 以来添加预设艺术字对象的支持。

下面是 ShapeCollection.AddWordArt 方法的简单使用场景。

{{% alert color="primary" %}} 

查看详细文章[添加具有内置样式的艺术字](/cells/zh/java/add-word-art-text-with-built-in-styles/)

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
### **添加了 XmlMapCollection.Add 方法**
Aspose.Cells 公开了允许将 Xml 映射添加到电子表格的 XmlMapCollection.Add 方法。下面是 XmlMapCollection.Add 方法的简单使用场景。

{{% alert color="primary" %}} 

查看详细文章[将 XML 映射添加到电子表格](/cells/zh/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **添加了 Cells.LinkToXmlMap 方法**
Aspose.Cells 现在公开了 Cells.LinkToXmlMap 方法，以便将单元格与 XML 地图元素链接起来。下面是 Cells.LinkToXmlMap 方法的简单使用场景。

{{% alert color="primary" %}} 

查看详细文章[将 Cells 链接到 XML 映射元素](/cells/zh/java/link-cells-to-xml-map-elements/)

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
### **添加了 ListColumn.Formula 属性**
Aspose.Cells 16.10.0 公开了 ListColumn.Formula 属性，以便自动将公式传播到新插入的行。

这是 ListColumn.Formula 属性的简单使用场景。

{{% alert color="primary" %}} 

查看详细文章[在列表对象中自动传播公式](/cells/zh/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

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
