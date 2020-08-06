---
title: Public API Changes in Aspose.Cells 16.10.0
type: docs
weight: 340
url: /net/public-api-changes-in-aspose-cells-16-10-0/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 9.0.0 to 16.10.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for Reflection Effects**
Aspose.Cells 16.10.0 has exposed the ReflectionEffect class along with Shape.Reflection property in order to control the reflection effects of a Shape object. The ReflectionEffect class has the following properties.

- ReflectionEffect.Blur: Gets/sets the blur radius in unit of points.
- ReflectionEffect.Direction: Gets/sets the direction of the alpha gradient ramp relative to the shape itself.
- ReflectionEffect.Distance: Gets/sets distance of the reflection in unit of points.
- ReflectionEffect.FadeDirection: Gets/sets the direction to offset the reflection.
- ReflectionEffect.RotWithShape: Gets/sets if the reflection should rotate with the shape.
- ReflectionEffect.Size: Gets/sets the end position (along the alpha gradient ramp) of the end alpha value in unit of percentage .
- ReflectionEffect.Transparency: Gets/sets the degree of the starting reflection transparency as a value from 0.0 (opaque) through 1.0 (clear).
- ReflectionEffect.Type: Gets/sets the preset reflection effect.

Here is simple usage scenario of Shape.Reflection property.

{{% alert color="primary" %}} 

Check the detailed article on [Working with Reflection Effects](http://www.aspose.com/docs/display/cellsnet/Working+with+the+Reflection+Effect+of+Shape+or+Chart)

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


### **Support for Shadow Effects**
Aspose.Cells 16.10.0 has exposed the Shape.ShadowEffect property along with ShadowEffect class which all together allows to set the shadow effect on a Shape object. The ShadowEffect class has the following properties.

- ShadowEffect.Angle: Gets/sets the lighting angle ranging from 0 to 359.9 degrees.
- ShadowEffect.Blur: Gets and sets the blur of the shadow ranging from 0 to 100 points.
- ShadowEffect.Color: Gets/sets the color of the shadow.
- ShadowEffect.Distance: Gets/sets the distance of the shadow ranging from 0 to 200 points.
- ShadowEffect.PresetType: Gets/sets the preset shadow type of the shadow.
- ShadowEffect.Size: Gets/sets the size of the shadow ranging from 0 to 2.0. It will be meaningless in case of inner shadow.
- ShadowEffect.Transparency: Gets/sets the degree of transparency of the shadow ranging from 0.0 (opaque) to 1.0 (clear).

Here is simple usage scenario of aforementioned property.

{{% alert color="primary" %}} 

Check the detailed article on [Working with Shadow Effects](http://www.aspose.com/docs/display/cellsnet/Working+with+the+Shadow+Effect+of+Shape+or+Chart)

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


### **Support for Glow Effects**
Aspose.Cells 16.10.0 has exposed the Shape.Glow property along with GlowEffect class which all together allows to set the glow effect of a Shape object. The GlowEffect class specifies a glow effect, in which a color blurred outline is added outside the edges of the object using the following properties.

- GlowEffect.Size: Gets/sets the radius of the glow in unit of points.
- GlowEffect.Transparency: Gets/sets the degree of transparency of the glow effect ranging from 0.0 (opaque) to 1.0 (clear).

Here is simple usage scenario of Shape.Glow property.

{{% alert color="primary" %}} 

Check the detailed article on [Working with Glow Effect](http://www.aspose.com/docs/display/cellsnet/Working+with+the+Glow+Effect+of+Shape+or+Chart)

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


### **Support for 3D Format**
Aspose.Cells 16.10.0 has exposed the Shape.ThreeDFormat property along with the ThreeDFormat class which together can be used to control the 3D formatting of the Shape object. The ThreeDFormat class represents a shape's three-dimensional formatting and has the following properties.

- ThreeDFormat.BottomBevelHeight: Gets/sets the height of the bottom bevel or how far into the shape it is applied, in unit of Points.
- ThreeDFormat.BottomBevelType: Gets/sets the type of the bottom bevel or how far into the shape it is applied, in unit of Points.
- ThreeDFormat.BottomBevelWidth: Gets/sets the width of the bottom bevel or how far into the shape it is applied, in unit of Points.
- ThreeDFormat.ContourColor: Gets/sets the contour color of a shape.
- ThreeDFormat.ContourWidth: Gets/sets the contour width on the shape, in unit of Points.
- ThreeDFormat.ExtrusionColor: Gets the extrusion color on a shape.
- ThreeDFormat.ExtrusionHeight: Gets/sets the extrusion height of the applied to the shape, in unit of Points.
- ThreeDFormat.LightAngle: Gets/sets the angle of the extrusion lights.
- ThreeDFormat.Lighting: Gets/sets type of light rig.
- ThreeDFormat.LightingDirection: Gets/sets the direction from which the light rig is oriented in relation to the scene.
- ThreeDFormat.Material: Represents the preset material which is combined with the lighting properties to give the final look and feel of a shape.
- ThreeDFormat.Perspective: Gets/sets the angle at which a ThreeDFormat object can be viewed.
- ThreeDFormat.PresetCameraType: Gets/sets the extrusion preset camera.
- ThreeDFormat.RotationX: Gets/sets the rotation of the extruded shape around the X-axis in unit of Degrees.
- ThreeDFormat.RotationY: Gets/sets the rotation of the extruded shape around the Y-axis in unit of Degrees.
- ThreeDFormat.RotationZ: Gets/sets the rotation of the extruded shape around the Z-axis in unit of Degrees.
- ThreeDFormat.TopBevelHeight: Gets/sets the height of the top bevel or how far into the shape it is applied, in unit of Points.
- ThreeDFormat.TopBevelType: Gets/sets the type of the top bevel or how far into the shape it is applied, in unit of Points.
- ThreeDFormat.TopBevelWidth: Gets/sets the width of the top bevel or how far into the shape it is applied, in unit of Points.
- ThreeDFormat.Z: Defines the distance from ground for the 3D shape.

Following is the simple usage scenario of Shape.ThreeDFormat property.

{{% alert color="primary" %}} 

Check the detailed article on [Working with 3D Formatting](http://www.aspose.com/docs/display/cellsnet/Working+with+the+ThreeDFormat+of+Shape+or+Chart)

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


### **Support for WordArt Styles in Shape's Text**
Aspose.Cells 16.10.0 has exposed the FontSettingCollection.SetWordArtStyle & FontSetting.SetWordArtStyle methods in order to set the preset WordArt style to the text of the Shape object.

Here is simple usage scenario of aforementioned methods.

{{% alert color="primary" %}} 

Check the detailed article on [Working with WordArt Styles](http://www.aspose.com/docs/display/cellsnet/Set+preset+WordArt+style+to+the+text+of+the+shape)

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


### **Support for WordArt Built-in Styles**
Aspose.Cells 16.10.0 has exposed the ShapeCollection.AddWordArt method along with PresetWordArtStyle enumeration in order to provide the support for adding preset WordArt objects since Excel 2007.

Here is simple usage scenario of ShapeCollection.AddWordArt method.

{{% alert color="primary" %}} 

Check the detailed article on [Add WordArt with Built-in Styles](http://www.aspose.com/docs/display/cellsnet/Add+Word+Art+Text+with+Built-in+Styles)

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


### **Added XmlMapCollection.Add Method**
Aspose.Cells has exposed the XmlMapCollection.Add method that allows to add Xml Map to a spreadsheet. Here is simple usage scenario of XmlMapCollection.Add method.

{{% alert color="primary" %}} 

Check the detailed article on [Add XML Map to Spreadsheet](http://www.aspose.com/docs/display/cellsnet/Add+XML+Map+inside+the+Workbook+using+XmlMapCollection.Add+method)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Add xml map from the sample.xml to the workbook

book.Worksheets.XmlMaps.Add("sample.xml");

{{< /highlight >}}


### **Added Cells.LinkToXmlMap Method**
Aspose.Cells has now exposed the Cells.LinkToXmlMap method in order to link the cells with the XML map elements.

Here is simple usage scenario of Cells.LinkToXmlMap method.

{{% alert color="primary" %}} 

Check the detailed article on [Link Cells to XML Map Elements](http://www.aspose.com/docs/display/cellsnet/Link+Cells+to+Xml+Map+Elements)

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


### **Added ListColumn.Formula Property**
Aspose.Cells 16.10.0 has exposed the ListColumn.Formula property in order automatically propagate the formula to newly inserted rows.

Here is simple usage scenario of ListColumn.Formula property.

{{% alert color="primary" %}} 

Check the detailed article on [Automatically Propagate Formula in List Object](http://www.aspose.com/docs/display/cellsnet/Propagate+Formula+in+Table+or+List+Object+automatically+while+entering+data+in+new+rows)

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


### **Support for Calculating Custom Functions with GridWeb**
Aspose.Cells.GridWeb 16.10.0 has exposed the GridWeb.CustomCalculationEngine property along with GridAbstractCalculationEngine class which all together allows to define & calculate the custom functions from within the GridWeb component.

Here is simple usage scenario of aforementioned APIs.

{{% alert color="primary" %}} 

Check the detailed article on [Calculating Custom Functions with GridWeb](http://www.aspose.com/docs/display/cellsnet/Calculate+Custom+Functions+in+GridWeb)

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
