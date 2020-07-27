+++
title = "Public API Changes in Aspose.Cells 16.10.0" 
description = "" 
weight = 12320 
+++

Aspose.Cells for Java : Public API Changes in Aspose.Cells 16.10.0  

# Aspose.Cells for Java : Public API Changes in Aspose.Cells 16.10.0


This document describes the changes to the Aspose.Cells API from version 9.0.0 to 16.10.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

## Added APIs

### Support for Reflection Effects

Aspose.Cells 16.10.0 has exposed the `ReflectionEffect` class along with `Shape.Reflection` property in order to control the reflection effects of a `Shape` object. The `ReflectionEffect` class has the following properties.

*   `ReflectionEffect.Blur`: Gets/sets the blur radius in unit of points.
*   `ReflectionEffect.Direction`: Gets/sets the direction of the alpha gradient ramp relative to the shape itself.
*   `ReflectionEffect.Distance`: Gets/sets distance of the reflection in unit of points.
*   `ReflectionEffect.FadeDirection`: Gets/sets the direction to offset the reflection.
*   `ReflectionEffect.RotWithShape`: Gets/sets if the reflection should rotate with the shape.
*   `ReflectionEffect.Size`: Gets/sets the end position (along the alpha gradient ramp) of the end alpha value in unit of percentage .
*   `ReflectionEffect.Transparency`: Gets/sets the degree of the starting reflection transparency as a value from 0.0 (opaque) through 1.0 (clear).
*   `ReflectionEffect.Type`: Gets/sets the preset reflection effect.

Here is simple usage scenario of `Shape.Reflection` property.

Check the detailed article on [Working with Reflection Effects](http://www.aspose.com/docs/display/cellsjava/Working+with+the+Reflection+Effect+of+Shape+or+Chart)

**Java**

{{< code lang="java" >}}
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
{{< /code >}}

### Support for Shadow Effects

Aspose.Cells 16.10.0 has exposed the `Shape.ShadowEffect` property along with `ShadowEffect` class which all together allows to set the shadow effect on a `Shape` object. The `ShadowEffect` class has the following properties.

*   `ShadowEffect.Angle`: Gets/sets the lighting angle ranging from 0 to 359.9 degrees.
*   `ShadowEffect.Blur`: Gets and sets the blur of the shadow ranging from 0 to 100 points.
*   `ShadowEffect.Color`: Gets/sets the color of the shadow.
*   `ShadowEffect.Distance`: Gets/sets the distance of the shadow ranging from 0 to 200 points.
*   `ShadowEffect.PresetType`: Gets/sets the preset shadow type of the shadow.
*   `ShadowEffect.Size`: Gets/sets the size of the shadow ranging from 0 to 2.0. It will be meaningless in case of inner shadow.
*   `ShadowEffect.Transparency`: Gets/sets the degree of transparency of the shadow ranging from 0.0 (opaque) to 1.0 (clear).

Here is simple usage scenario of aforementioned property.

Check the detailed article on [Working with Shadow Effects](http://www.aspose.com/docs/display/cellsjava/Working+with+the+Shadow+Effect+of+Shape+or+Chart)

**Java**

{{< code lang="java" >}}
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
{{< /code >}}

### Support for Glow Effects

Aspose.Cells 16.10.0 has exposed the `Shape.Glow` property along with `GlowEffect` class which all together allows to set the glow effect of a `Shape` object. The `GlowEffect` class specifies a glow effect, in which a color blurred outline is added outside the edges of the object using the following properties.

*   `GlowEffect.Size`: Gets/sets the radius of the glow in unit of points.
*   `GlowEffect.Transparency`: Gets/sets the degree of transparency of the glow effect ranging from 0.0 (opaque) to 1.0 (clear).

Here is simple usage scenario of `Shape.Glow` property.

Check the detailed article on [Working with Glow Effect](http://www.aspose.com/docs/display/cellsjava/Working+with+the+Glow+Effect+of+Shape+or+Chart)

**Java**

{{< code lang="java" >}}
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
{{< /code >}}

### Support for 3D Format

Aspose.Cells 16.10.0 has exposed the `Shape.ThreeDFormat` property along with the `ThreeDFormat` class which together can be used to control the 3D formatting of the `Shape` object. The `ThreeDFormat` class represents a shape's three-dimensional formatting and has the following properties.

*   `ThreeDFormat.BottomBevelHeight`: Gets/sets the height of the bottom bevel or how far into the shape it is applied, in unit of Points.
*   `ThreeDFormat.BottomBevelType`: Gets/sets the type of the bottom bevel or how far into the shape it is applied, in unit of Points.
*   `ThreeDFormat.BottomBevelWidth`: Gets/sets the width of the bottom bevel or how far into the shape it is applied, in unit of Points.
*   `ThreeDFormat.ContourColor`: Gets/sets the contour color of a shape.
*   `ThreeDFormat.ContourWidth`: Gets/sets the contour width on the shape, in unit of Points.
*   `ThreeDFormat.ExtrusionColor`: Gets the extrusion color on a shape.
*   `ThreeDFormat.ExtrusionHeight`: Gets/sets the extrusion height of the applied to the shape, in unit of Points.
*   `ThreeDFormat.LightAngle`: Gets/sets the angle of the extrusion lights.
*   `ThreeDFormat.Lighting`: Gets/sets type of light rig.
*   `ThreeDFormat.LightingDirection`: Gets/sets the direction from which the light rig is oriented in relation to the scene.
*   `ThreeDFormat.Material`: Represents the preset material which is combined with the lighting properties to give the final look and feel of a shape.
*   `ThreeDFormat.Perspective`: Gets/sets the angle at which a ThreeDFormat object can be viewed.
*   `ThreeDFormat.PresetCameraType`: Gets/sets the extrusion preset camera.
*   `ThreeDFormat.RotationX`: Gets/sets the rotation of the extruded shape around the X-axis in unit of Degrees.
*   `ThreeDFormat.RotationY`: Gets/sets the rotation of the extruded shape around the Y-axis in unit of Degrees.
*   `ThreeDFormat.RotationZ`: Gets/sets the rotation of the extruded shape around the Z-axis in unit of Degrees.
*   `ThreeDFormat.TopBevelHeight`: Gets/sets the height of the top bevel or how far into the shape it is applied, in unit of Points.
*   `ThreeDFormat.TopBevelType`: Gets/sets the type of the top bevel or how far into the shape it is applied, in unit of Points.
*   `ThreeDFormat.TopBevelWidth`: Gets/sets the width of the top bevel or how far into the shape it is applied, in unit of Points.
*   `ThreeDFormat.Z`: Defines the distance from ground for the 3D shape.

Following is the simple usage scenario of `Shape.ThreeDFormat` property.

Check the detailed article on [Working with 3D Formatting](http://www.aspose.com/docs/display/cellsjava/Working+with+the+ThreeDFormat+of+Shape+or+Chart)

**Java**

{{< code lang="java" >}}
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
{{< /code >}}

### Support for WordArt Styles in Shape's Text

Aspose.Cells 16.10.0 has exposed the `FontSettingCollection.SetWordArtStyle` & `FontSetting.SetWordArtStyle` methods in order to set the preset WordArt style to the text of the `Shape` object.

Here is simple usage scenario of aforementioned methods.

Check the detailed article on [Working with WordArt Styles](http://www.aspose.com/docs/display/cellsjava/Set+preset+WordArt+style+to+the+text+of+the+shape)

**Java**

{{< code lang="java" >}}
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
{{< /code >}}

### Support for WordArt Built-in Styles

Aspose.Cells 16.10.0 has exposed the `ShapeCollection.AddWordArt` method along with `PresetWordArtStyle` enumeration in order to provide the support for adding preset WordArt objects since Excel 2007.

Here is simple usage scenario of `ShapeCollection.AddWordArt` method.

Check the detailed article on [Add WordArt with Built-in Styles](http://www.aspose.com/docs/display/cellsjava/Add+Word+Art+Text+with+Built-in+Styles)

**Java**

{{< code lang="java" >}}
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
{{< /code >}}

### Added XmlMapCollection.Add Method

Aspose.Cells has exposed the `XmlMapCollection.Add` method that allows to add Xml Map to a spreadsheet. Here is simple usage scenario of `XmlMapCollection.Add` method.

Check the detailed article on [Add XML Map to Spreadsheet](http://www.aspose.com/docs/display/cellsjava/Add+XML+Map+inside+the+Workbook+using+XmlMapCollection.Add+method)

**Java**

{{< code lang="java" >}}
//Create an instance of Workbook
Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook
book.getWorksheets().getXmlMaps().add("sample.xml");
{{< /code >}}

### Added Cells.LinkToXmlMap Method

Aspose.Cells has now exposed the `Cells.LinkToXmlMap` method in order to link the cells with the XML map elements. Here is simple usage scenario of `Cells.LinkToXmlMap` method.

Check the detailed article on [Link Cells to XML Map Elements](http://www.aspose.com/docs/display/cellsjava/Link+Cells+to+Xml+Map+Elements)

**Java**

{{< code lang="java" >}}
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
{{< /code >}}

### Added ListColumn.Formula Property

Aspose.Cells 16.10.0 has exposed the `ListColumn.Formula` property in order automatically propagate the formula to newly inserted rows.

Here is simple usage scenario of `ListColumn.Formula` property.

Check the detailed article on [Automatically Propagate Formula in List Object](http://www.aspose.com/docs/display/cellsjava/Propagate+Formula+in+Table+or+List+Object+automatically+while+entering+data+in+new+rows)

**Java**

{{< code lang="java" >}}
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
{{< /code >}}

