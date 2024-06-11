---
title: Aspose.Cells 16.10.0中的公共API更改
type: docs
weight: 350
url: /zh/java/public-api-changes-in-aspose-cells-16-10-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本9.0.0到16.10.0的Aspose.Cells API的更改，可能会对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、已添加和已删除的类等，还描述了在Aspose.Cells背后的行为中的任何更改。

{{% /alert %}} 
## **添加的 API**
### **反射效果支持**
Aspose.Cells 16.10.0已经暴露了ReflectionEffect类以及Shape.Reflection属性，以控制形状对象的反射效果。ReflectionEffect类具有以下属性。

- ReflectionEffect.Blur: 获取/设置点单位中的模糊半径。
- ReflectionEffect.Direction: 获取/设置与形状本身相关的Alpha梯度坡的方向。
- ReflectionEffect.Distance: 获取/设置点单位中的反射距离。
- ReflectionEffect.FadeDirection: 获取/设置偏移反射的方向。
- ReflectionEffect.RotWithShape: 获取/设置是否应该让反射效果随形状旋转。
- ReflectionEffect.Size: 获取/设置结束位置（沿 alpha 渐变坡度）中结束 alpha 值的单位百分比。
- ReflectionEffect.Transparency: 获取/设置起始反射透明度的程度，值从 0.0（不透明）至 1.0（清晰）。
- ReflectionEffect.Type: 获取/设置预设的反射效果。

Shape.Reflection 属性的简单使用场景如下。

{{% alert color="primary" %}} 

查看[使用倒影效果](/cells/zh/java/working-with-the-reflection-effect-of-shape-or-chart/)的详细文章

{{% /alert %}} 

Java

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
### **支持阴影效果**
Aspose.Cells 16.10.0 已经暴露了 Shape.ShadowEffect 属性，以及 ShadowEffect 类，它们一起允许在形状对象上设置阴影效果。ShadowEffect 类具有以下属性。

- ShadowEffect.Angle: 获取/设置光照角度，范围从 0 到 359.9 度。
- ShadowEffect.Blur: 获取/设置阴影的模糊程度，范围从 0 到 100 点。
- ShadowEffect.Color: 获取/设置阴影的颜色。
- ShadowEffect.Distance: 获取/设置阴影的距离，范围从 0 到 200 点。
- ShadowEffect.PresetType: 获取/设置阴影的预设类型。
- ShadowEffect.Size: 获取/设置阴影的大小，范围从 0 到 2.0。在内阴影的情况下将毫无意义。
- ShadowEffect.Transparency: 获取/设置阴影的透明度，范围从 0.0（不透明）到 1.0（清晰）。

前述属性的简单使用场景如下。

{{% alert color="primary" %}} 

查看[使用阴影效果](/cells/zh/java/working-with-the-shadow-effect-of-shape-or-chart/)的详细文章

{{% /alert %}} 

Java

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
### **支持辉光效果**
Aspose.Cells 16.10.0 已经暴露了 Shape.Glow 属性，以及 GlowEffect 类，它们一起允许设置形状对象的辉光效果。GlowEffect 类指定了辉光效果，通过以下属性进行设置。

- GlowEffect.Size: 获取/设置辉光的半径，单位为点。
- GlowEffect.Transparency: 获取/设置发光效果的透明度，取值范围从0.0（不透明）到1.0（透明）。

这是 Shape.Glow 属性的简单使用场景。

{{% alert color="primary" %}} 

查看[使用发光效果](/cells/zh/java/working-with-the-glow-effect-of-shape-or-chart/)的详细文章

{{% /alert %}} 

Java

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
### **对3D格式的支持**
Aspose.Cells 16.10.0已经暴露了 Shape.ThreeDFormat 属性以及 ThreeDFormat 类，它们可以共同用于控制Shape对象的3D格式。ThreeDFormat 类表示形状的三维格式，具有以下属性。

- ThreeDFormat.BottomBevelHeight: 获取/设置底部倒角的高度或应用到形状的距离，单位为磅。
- ThreeDFormat.BottomBevelType: 获取/设置底部倒角的类型或应用到形状的距离，单位为磅。
- ThreeDFormat.BottomBevelWidth: 获取/设置底部倒角的宽度或应用到形状的距离，单位为磅。
- ThreeDFormat.ContourColor: 获取/设置形状的轮廓颜色。
- ThreeDFormat.ContourWidth: 获取/设置形状上轮廓的宽度，单位为磅。
- ThreeDFormat.ExtrusionColor: 获取形状上挤出的颜色。
- ThreeDFormat.ExtrusionHeight: 获取/设置应用于形状的挤出高度，单位为磅。
- ThreeDFormat.LightAngle: 获取/设置挤出光线的角度。
- ThreeDFormat.Lighting: 获取/设置灯光类型。
- ThreeDFormat.LightingDirection: 获取/设置光源照射的方向与场景的关系。
- ThreeDFormat.Material: 代表与灯光属性结合以给出形状最终外观的预设材料。
- ThreeDFormat.Perspective: 获取/设置可以查看 ThreeDFormat 对象的角度。
- ThreeDFormat.PresetCameraType: 获取/设置挤出预设摄像头。
- ThreeDFormat.RotationX: 获取/设置绕X轴旋转的挤出形状的旋转角度，单位为度。
- ThreeDFormat.RotationY: 获取/设置绕Y轴旋转的挤出形状的旋转角度，单位为度。
- ThreeDFormat.RotationZ: 获取/设置围绕 Z 轴的挤出形状的旋转，单位为度。
- ThreeDFormat.TopBevelHeight: 获取/设置顶部斜角的高度或应用于形状的距离，单位为点。
- ThreeDFormat.TopBevelType: 获取/设置顶部斜角的类型或应用于形状的距离，单位为点。
- ThreeDFormat.TopBevelWidth: 获取/设置顶部斜角的宽度或应用于形状的距离，单位为点。
- ThreeDFormat.Z: 定义 3D 形状离地的距离。

以下是 Shape.ThreeDFormat 属性的简单使用场景。

{{% alert color="primary" %}} 

查看[使用3D格式设置](/cells/zh/java/working-with-the-threedformat-of-shape-or-chart/)的详细文章

{{% /alert %}} 

Java

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
### **支持 Shape 的文本中的 WordArt 样式**
Aspose.Cells 16.10.0 现已公开了 FontSettingCollection.SetWordArtStyle 和 FontSetting.SetWordArtStyle 方法，以便为 Shape 对象的文本设置预置的 WordArt 样式。

以下是上述方法的简单使用场景。

{{% alert color="primary" %}} 

查看[使用WordArt样式](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)的详细文章

{{% /alert %}} 

Java

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
### **支持内置 WordArt 样式**
Aspose.Cells 16.10.0 现已公开了 ShapeCollection.AddWordArt 方法以及 PresetWordArtStyle 枚举，以便自 Excel 2007 以来提供对预设 WordArt 对象的支持。

以下是 ShapeCollection.AddWordArt 方法的简单使用场景。

{{% alert color="primary" %}} 

查看[添加具有内置样式的WordArt](/cells/zh/java/add-word-art-text-with-built-in-styles/)的详细文章

{{% /alert %}} 

Java

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
### **添加了 XmlMapCollection.Add 方法**
Aspose.Cells 现已公开了 XmlMapCollection.Add 方法，允许向电子表格中添加 Xml 映射。以下是 XmlMapCollection.Add 方法的简单使用场景。

{{% alert color="primary" %}} 

查看[在电子表格中添加XML映射](/cells/zh/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)的详细文章

{{% /alert %}} 

Java

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **添加了 Cells.LinkToXmlMap 方法**
Aspose.Cells现已公开了Cells.LinkToXmlMap方法，以便将单元格与XML映射元素关联。以下是Cells.LinkToXmlMap方法的简单用法场景。

{{% alert color="primary" %}} 

查看[将单元格链接到XML映射元素](/cells/zh/java/link-cells-to-xml-map-elements/)的详细文章

{{% /alert %}} 

Java

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
### **添加了 ListColumn.Formula 属性。**
Aspose.Cells 16.10.0 已公开了 ListColumn.Formula 属性，以便自动将公式传播到新插入的行。

这里是 ListColumn.Formula 属性的简单使用场景。

{{% alert color="primary" %}} 

查看[自动传播列表对象中的公式](/cells/zh/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)的详细文章

{{% /alert %}} 

Java

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
