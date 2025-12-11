---
title: Public API Changes in Aspose.Cells 16.10.0
type: docs
weight: 350
url: /java/public-api-changes-in-aspose-cells-16-10-0/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 9.0.0 to 16.10.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for Reflection Effects**
Aspose.Cells 16.10.0 has exposed the ReflectionEffect class along with the Shape.Reflection property in order to control the reflection effects of a Shape object. The ReflectionEffect class has the following properties.

- ReflectionEffect.Blur: Gets/sets the blur radius in units of points.  
- ReflectionEffect.Direction: Gets/sets the direction of the alpha gradient ramp relative to the shape itself.  
- ReflectionEffect.Distance: Gets/sets the distance of the reflection in units of points.  
- ReflectionEffect.FadeDirection: Gets/sets the direction to offset the reflection.  
- ReflectionEffect.RotWithShape: Gets/sets whether the reflection should rotate with the shape.  
- ReflectionEffect.Size: Gets/sets the end position (along the alpha gradient ramp) of the end alpha value in units of percentage.  
- ReflectionEffect.Transparency: Gets/sets the degree of the starting reflection transparency as a value from 0.0 (opaque) through 1.0 (clear).  
- ReflectionEffect.Type: Gets/sets the preset reflection effect.  

Here is a simple usage scenario of the Shape.Reflection property.

{{% alert color="primary" %}} 

Check the detailed article on [Working with Reflection Effects](/cells/java/working-with-the-reflection-effect-of-shape-or-chart/)

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
### **Support for Shadow Effects**
Aspose.Cells 16.10.0 has exposed the Shape.ShadowEffect property along with the ShadowEffect class, which altogether allows you to set the shadow effect on a Shape object. The ShadowEffect class has the following properties.

- ShadowEffect.Angle: Gets/sets the lighting angle ranging from 0 to 359.9 degrees.  
- ShadowEffect.Blur: Gets and sets the blur of the shadow ranging from 0 to 100 points.  
- ShadowEffect.Color: Gets/sets the color of the shadow.  
- ShadowEffect.Distance: Gets/sets the distance of the shadow ranging from 0 to 200 points.  
- ShadowEffect.PresetType: Gets/sets the preset shadow type of the shadow.  
- ShadowEffect.Size: Gets/sets the size of the shadow ranging from 0 to 2.0. It will be meaningless in case of inner shadow.  
- ShadowEffect.Transparency: Gets/sets the degree of transparency of the shadow ranging from 0.0 (opaque) to 1.0 (clear).  

Here is a simple usage scenario of the aforementioned property.

{{% alert color="primary" %}} 

Check the detailed article on [Working with Shadow Effects](/cells/java/working-with-the-shadow-effect-of-shape-or-chart/)

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
### **Support for Glow Effects**
Aspose.Cells 16.10.0 has exposed the Shape.Glow property along with the GlowEffect class, which altogether allows you to set the glow effect of a Shape object. The GlowEffect class specifies a glow effect, in which a color‑blurred outline is added outside the edges of the object using the following properties.

- GlowEffect.Size: Gets/sets the radius of the glow in units of points.  
- GlowEffect.Transparency: Gets/sets the degree of transparency of the glow effect ranging from 0.0 (opaque) to 1.0 (clear).  

Here is a simple usage scenario of the Shape.Glow property.

{{% alert color="primary" %}} 

Check the detailed article on [Working with Glow Effect](/cells/java/working-with-the-glow-effect-of-shape-or-chart/)

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
### **Support for 3D Format**
Aspose.Cells 16.10.0 has exposed the Shape.ThreeDFormat property along with the ThreeDFormat class, which together can be used to control the 3D formatting of the Shape object. The ThreeDFormat class represents a shape's three‑dimensional formatting and has the following properties.

- ThreeDFormat.BottomBevelHeight: Gets/sets the height of the bottom bevel, in units of points.  
- ThreeDFormat.BottomBevelType: Gets/sets the type of the bottom bevel, in units of points.  
- ThreeDFormat.BottomBevelWidth: Gets/sets the width of the bottom bevel, in units of points.  
- ThreeDFormat.ContourColor: Gets/sets the contour color of a shape.  
- ThreeDFormat.ContourWidth: Gets/sets the contour width on the shape, in units of points.  
- ThreeDFormat.ExtrusionColor: Gets the extrusion color on a shape.  
- ThreeDFormat.ExtrusionHeight: Gets/sets the extrusion height applied to the shape, in units of points.  
- ThreeDFormat.LightAngle: Gets/sets the angle of the extrusion lights.  
- ThreeDFormat.Lighting: Gets/sets the type of light rig.  
- ThreeDFormat.LightingDirection: Gets/sets the direction from which the light rig is oriented in relation to the scene.  
- ThreeDFormat.Material: Represents the preset material which is combined with the lighting properties to give the final look and feel of a shape.  
- ThreeDFormat.Perspective: Gets/sets the angle at which a ThreeDFormat object can be viewed.  
- ThreeDFormat.PresetCameraType: Gets/sets the extrusion preset camera.  
- ThreeDFormat.RotationX: Gets/sets the rotation of the extruded shape around the X‑axis, in units of degrees.  
- ThreeDFormat.RotationY: Gets/sets the rotation of the extruded shape around the Y‑axis, in units of degrees.  
- ThreeDFormat.RotationZ: Gets/sets the rotation of the extruded shape around the Z‑axis, in units of degrees.  
- ThreeDFormat.TopBevelHeight: Gets/sets the height of the top bevel, in units of points.  
- ThreeDFormat.TopBevelType: Gets/sets the type of the top bevel, in units of points.  
- ThreeDFormat.TopBevelWidth: Gets/sets the width of the top bevel, in units of points.  
- ThreeDFormat.Z: Defines the distance from the ground for the 3D shape.  

Following is a simple usage scenario of the Shape.ThreeDFormat property.

{{% alert color="primary" %}} 

Check the detailed article on [Working with 3D Formatting](/cells/java/working-with-the-threedformat-of-shape-or-chart/)

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
### **Support for WordArt Styles in Shape's Text**
Aspose.Cells 16.10.0 has exposed the `FontSettingCollection.setWordArtStyle` & `FontSetting.setWordArtStyle` methods in order to set the preset WordArt style to the text of the Shape object.

Here is a simple usage scenario of the aforementioned methods.

{{% alert color="primary" %}} 

Check the detailed article on [Working with WordArt Styles](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

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
### **Support for WordArt Built‑in Styles**
Aspose.Cells 16.10.0 has exposed the `ShapeCollection.addWordArt` method along with the `PresetWordArtStyle` enumeration in order to provide support for adding preset WordArt objects since Excel 2007.

Here is a simple usage scenario of the `ShapeCollection.addWordArt` method.

{{% alert color="primary" %}} 

Check the detailed article on [Add WordArt with Built‑in Styles](/cells/java/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access ShapeCollection of first worksheet

ShapeCollection shapes = sheet.getShapes();

//Add WordArt with built‑in styles

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_1, "Aspose File Format APIs", 0, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **Added XmlMapCollection.add Method**
Aspose.Cells has exposed the `XmlMapCollection.add` method that allows adding an XML Map to a spreadsheet. Here is a simple usage scenario of the `XmlMapCollection.add` method.

{{% alert color="primary" %}} 

Check the detailed article on [Add XML Map to Spreadsheet](/cells/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Added Cells.linkToXmlMap Method**
Aspose.Cells has now exposed the `Cells.linkToXmlMap` method in order to link cells with the XML map elements. Here is a simple usage scenario of the `Cells.linkToXmlMap` method.

{{% alert color="primary" %}} 

Check the detailed article on [Link Cells to XML Map Elements](/cells/java/link-cells-to-xml-map-elements/)

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
### **Added ListColumn.formula Property**
Aspose.Cells 16.10.0 has exposed the `ListColumn.formula` property in order to automatically propagate the formula to newly inserted rows.

Here is a simple usage scenario of the `ListColumn.formula` property.

{{% alert color="primary" %}} 

Check the detailed article on [Automatically Propagate Formula in List Object](/cells/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

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

//Set the formula of the second column so that it automatically propagates to new rows while entering data

listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
