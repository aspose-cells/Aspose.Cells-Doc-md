---
title: Aspose.Cells 16.10.0中的公共API更改
type: docs
weight: 350
url: /zh/java/public-api-changes-in-aspose-cells-16-10-0/
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

查看[使用反射效果操作](/cells/zh/java/working-with-the-reflection-effect-of-shape-or-chart/)的详细文章

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

查看[使用阴影效果操作](/cells/zh/java/working-with-the-shadow-effect-of-shape-or-chart/)的详细文章

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
### **支持发光效果**
Aspose.Cells 16.10.0已暴露了Shape.Glow属性，以及GlowEffect类，可以一起在形状对象上设置发光效果。GlowEffect类指定一种发光效果，通过以下属性添加一个颜色模糊的轮廓在对象的边缘外部。

- GlowEffect.Size：以点为单位获取/设置发光的半径。
- GlowEffect.Transparency: 获取/设置光晕效果的透明度，范围从 0.0（不透明）到 1.0（清晰）。

这里是 Shape.Glow 属性的简单使用场景。

{{% alert color="primary" %}} 

查看[使用发光效果操作](/cells/zh/java/working-with-the-glow-effect-of-shape-or-chart/)的详细文章

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

查看[使用3D格式化操作](/cells/zh/java/working-with-the-threedformat-of-shape-or-chart/)的详细文章

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
### **支持 Shape 文本中的 WordArt 样式**
Aspose.Cells 16.10.0 暴露了 FontSettingCollection.SetWordArtStyle 和 FontSetting.SetWordArtStyle 方法，以便为 Shape 对象的文本设置预设 WordArt 样式。

以下是上述方法的简单使用场景。

{{% alert color="primary" %}} 

在[使用WordArt样式](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)中查看详细文章

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
### **支持WordArt内置样式**
Aspose.Cells 16.10.0已经公开了ShapeCollection.AddWordArt方法，同时还暴露了PresetWordArtStyle枚举，以便在Excel 2007中添加预设的WordArt对象。

这里是ShapeCollection.AddWordArt方法的简单使用情景。

{{% alert color="primary" %}} 

在[/cells/zh/java/add-word-art-text-with-built-in-styles/]中查看[添加使用内置样式的WordArt](/cells/zh/java/add-word-art-text-with-built-in-styles/)的详细文章

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
### **新增了XmlMapCollection.Add方法**
Aspose.Cells现在暴露了XmlMapCollection.Add方法，允许向电子表格添加Xml Map。这里是XmlMapCollection.Add方法的简单使用情景。

{{% alert color="primary" %}} 

在[/cells/zh/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/]中查看[向电子表格添加XML映射](/cells/zh/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)的详细文章

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **新增了Cells.LinkToXmlMap方法**
Aspose.Cells现在公开了Cells.LinkToXmlMap方法，以便将单元格与XML映射元素链接起来。以下是Cells.LinkToXmlMap方法的简单使用场景。

{{% alert color="primary" %}} 

在[/cells/zh/java/link-cells-to-xml-map-elements/]中查看[将单元格链接到XML映射元素](/cells/zh/java/link-cells-to-xml-map-elements/)的详细文章

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
### **新增了ListColumn.Formula属性**
Aspose.Cells 16.10.0现在暴露了ListColumn.Formula属性，以便自动将公式传播到新插入的行。

这里是ListColumn.Formula属性的简单使用情景。

{{% alert color="primary" %}} 

在[/cells/zh/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/]中查看[在列表对象中自动传播公式](/cells/zh/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)的详细文章

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
