---
title: Public API Changes in Aspose.Cells 8.6.1
type: docs
weight: 210
url: /java/public-api-changes-in-aspose-cells-8-6-1/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.6.0 to 8.6.1 that may be of interest to module/application developers. It includes not only new and updated public methods, added classes, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for HTML Link Target Type**
This release of Aspose.Cells for Java API has exposed an enumeration namely HtmlLinkTargetType along with a new property HtmlSaveOptions.LinkTargetType that together allows to [set the target type for the links in spreadsheet while conversion to HTML format](/cells/java/change-the-html-link-target-type/). The possible values of the HtmlLinkTargetType enumeration are as follows, with the default value being SELF.

1. HtmlLinkTargetType.BLANK: Opens the linked document/page in a new window or tab.  
2. HtmlLinkTargetType.PARENT: Opens the linked document/page in the parent frame.  
3. HtmlLinkTargetType.SELF: Opens the linked document/page in the same frame where the link was clicked.  
4. HtmlLinkTargetType.TOP: Opens the linked document/page in the full body of the window.  

The following is a simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.save(outputFilePath, options);

{{< /highlight >}}
### **Added VbaModuleCollection.remove Method**
Aspose.Cells for Java 8.6.1 has exposed another overload of the VbaModuleCollection.remove method that can now accept an instance of Worksheet to remove all the VBA modules associated with the specified Worksheet.

The following is a simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from a specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **Added RangeCollection.add Method**
Aspose.Cells for Java 8.6.1 has exposed the RangeCollection.Add method that can be used to add Range objects to the collection of ranges for a particular Worksheet.

The following is a simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from the first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **Added Cell.setCharacters Method**
The Cell.setCharacters method can be used to [update the portions of the rich text](/cells/java/access-and-update-the-portions-of-rich-text-of-cell/) of a given Cell object. The Cell.getCharacters method is used to access the portions of the text, and then amendments can be made using the Cell.setCharacters method. The **get** method returns an array of FontSetting objects that can be manipulated to set various properties such as font name, font color, boldness, etc., and the **set** method applies the changes.

The following is a simple usage scenario.

**Java**

{{< highlight csharp >}}

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

{{< /highlight >}}
### **Added VbaProject.isSigned Property**
Aspose.Cells for Java 8.6.1 has exposed the VbaProject.isSigned property that can be used to [test if a VbaProject in a Workbook is signed or not](/cells/java/check-if-vba-project-in-a-workbook-is-signed/). This Boolean property returns true if the project is signed.

The following is a simple usage scenario.

**Java**

{{< highlight csharp >}}

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

{{< /highlight >}}
## **Modified APIs**
### **Modified Cell.getFormatConditions Method**
With the release of v8.6.1, the Aspose.Cells for Java API has modified the return type of the Cell.getFormatConditions method so that it now returns an array of type FormatConditionCollection.
## **Obsoleted APIs**
### **Obsoleted Workbook.checkWriteProtectedPassword Method**
With the release of v8.6.1, the Workbook.checkWriteProtectedPassword method has been marked deprecated. It is advised to use the WorkbookSettings.WriteProtection.validatePassword method, which can accept a `String` value as a parameter and returns a Boolean indicating whether the password matches the preset password of the spreadsheet.
{{< app/cells/assistant language="java" >}}
