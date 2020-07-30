---
title : "Public API Changes in Aspose.Cells 8.6.1" 
description : "" 
weight : 12306 
toc : false
type: docs
url: /java/developerguide/migratingfromearliervs/public+api+changes+in+aspose.cells+8.6.1/
---

# Aspose.Cells for Java : Public API Changes in Aspose.Cells 8.6.1


This document describes the changes to the Aspose.Cells API from version 8.6.0 to 8.6.1 that may be of interest to module/application developers. It includes not only new and updated public methods, added classes, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

## Added APIs

### Support for HTML Link Target Type

This release of Aspose.Cells for Java API has exposed an enumeration namely `HtmlLinkTargetType` along with a new property `HtmlSaveOptions.LinkTargetType` that together allows to [set the target type for the links in spreadsheet while conversion to HTML format](http://www.aspose.com/docs/display/cellsjava/Change+the+HTML+Link+Target+Type). The possible values of the `HtmlLinkTargetType` enumeration as follow where the default value is `SELF`.

1.  `HtmlLinkTargetType.BLANK`: Opens the linked document/page in a new window or tab.
2.  `HtmlLinkTargetType.PARENT`: Opens the linked document/page in parent frame.
3.  `HtmlLinkTargetType.SELF`: Opens the linked document/page in the same frame where the link was clinked.
4.  `HtmlLinkTargetType.TOP`: Opens the linked document/page in the full body of the window.

Following is the simple usage scenario.

**Java**

{{< code lang="java" >}}
//Load a spreadsheet
Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions
HtmlSaveOptions options = new HtmlSaveOptions();
//Set the LinkTargetType property to appropriate value
options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions
workbook.save(outputFilePath, options);
{{< /code >}}

### Method VbaModuleCollection.remove Added

Aspose.Cells for Java 8.6.1 has exposed another overload of the `VbaModuleCollection.remove` method that can now accept an instance of `Worksheet` to remove all the VBA modules associated with the specified `Worksheet`.

Following is the simple usage scenario.

**Java**

{{< code lang="java" >}}
//Load a spreadsheet
Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook
VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet
modules.remove(workbook.getWorksheets().get(0));
{{< /code >}}

### Method RangeCollection.add Added

Aspose.Cells for Java 8.6.1 has exposed the `RangeCollection.Add` method that can be used to add `Range` objects to the collection of ranges for a particular `Worksheet`.

Following is the simple usage scenario.

**Java**

{{< code lang="java" >}}
//Load a spreadsheet
Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook
Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook
RangeCollection ranges = cells.getRanges();

//Add another range to the collection
ranges.add(cells.createRange("A1:B4"));
{{< /code >}}

### Method Cell.setCharacters Added

The `Cell.setCharacters` method can be used to [update the portions of the rich text](http://www.aspose.com/docs/display/cellsjava/Access+and+Update+the+Portions+of+Rich+Text+of+Cell) of a given `Cell` object. The `Cell.getCharacters` method is to be used to access the portions of the text and then amendments can be done using the `Cell.setCharacters` method whereas the **get** method returns an array of `FontSetting` objects which can be manipulated to set various properties font name, font color, boldness etc and **set** method can be used to apply the changes.

Following is the simple usage scenario.

**Java**

{{< code lang="java" >}}
//Load a spreadsheet
Workbook workbook = new Workbook(inputFilePath);
//Access first worksheet of the workbook
Worksheet worksheet = workbook.getWorksheets().get(0);
//Access the cells containing the Rich Text
Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell
FontSetting[] settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 
settings[0].getFont().setName("Arial");

//Set the updated FontSetting
cell.setCharacters(settings);
{{< /code >}}

### Property VbaProject.isSigned Added

Aspose.Cells for Java 8.6.1 has exposed the `VbaProject.isSigned` property that can be used to [test if a `VbaProject` in a `Workbook` is signed or not](http://www.aspose.com/docs/display/cellsjava/Check+if+VBA+project+in+a+Workbook+is+Signed). Boolean type property returns `true` if the project is signed.

Following is the simple usage scenario.

**Java**

{{< code lang="java" >}}
//Load a spreadsheet
Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook
VbaProject project = workbook.getVbaProject();

//Test if VbaProject is signed
if (project.isSigned())
{
    System.out.println("VBA Project is Signed");
}
else
{
	System.out.println("VBA Project is not Signed");
}
{{< /code >}}

## Modified APIs

### Method Cell.getFormatConditions Modified

With the release of v8.6.1, the Aspose.Cells for Java API has modified the return type of the `Cell.getFormatConditions` method that now returns an array of type `FormatConditionCollection`.

## Obsoleted APIs

### Method Workbook.checkWriteProtectedPassword Obsoleted

With the release of v8.6.1, the `Workbook.checkWriteProtectedPassword` method has been marked depreciated. It is advised to use the `WorkbookSettings.WriteProtection.validatePassword` method that can accept a `String` value as parameter and returns `Boolean` if password matches the preset password of the spreadsheet.

