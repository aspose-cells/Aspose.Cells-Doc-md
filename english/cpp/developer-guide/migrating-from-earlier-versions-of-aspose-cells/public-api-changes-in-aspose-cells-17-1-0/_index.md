---
title: Public API Changes in Aspose.Cells 17.1.0
type: docs
weight: 20
url: /cpp/public-api-changes-in-aspose-cells-17-1-0/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 16.12.0 to 17.1.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for Named Ranges**
Aspose.Cells for C++ now supports creation as well as the manipulation of the Named Ranges. The following code snippet demonstrates how simple is to use Aspose.Cells for C++ API to [create named ranges](/cells/cpp/create-named-range-in-a-workbook/).

**C++**

{{< highlight csharp >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of output excel file

StringPtr outCreateNamedRange = (new String(dirPath))->Append(new String("outCreateNamedRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Create a range

intrusive_ptr<IRange> rng = ws->GetICells()->CreateIRange((intrusive_ptr<String>)new String("A5:C10"));

//Set its name to make it named range

rng->SetName((intrusive_ptr<String>)new String("MyNamedRange"));

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Save the workbook in xlsx format

wb->Save(outCreateNamedRange, SaveFormat_Xlsx);

{{< /highlight >}}

Besides creating new Named Ranges, Aspose.Cells for C++ APIs also support to manipulate existing Named Ranges. The following code snippet uses the Aspose.Cells for C++ API to [manipulate an existing named range](/cells/cpp/manipulate-named-range-in-a-workbook/).

**C++**

{{< highlight csharp >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of source excel file

StringPtr srcManipulateRange = (new String(dirPath))->Append(new String("srcManipulateRange.xlsx"));

//Path of output excel file

StringPtr outManipulateRange = (new String(dirPath))->Append(new String("outManipulateRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(srcManipulateRange);

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Manipulate the RefersTo property of NamedRange

nm->SetRefersTo((intrusive_ptr<String>)new String("=Sheet1!$D$5:$J$10"));

//Save the workbook in xlsx format

wb->Save(outManipulateRange, SaveFormat_Xlsx);

{{< /highlight >}}
### **Added ICells::LinkToXmlMap Method**
The LinkToXmlMap method has been added to the ICells class which is useful in linking an XML map.
### **Added ICells::ImportCSV Method**
The ImportCSV method has been added to the ICells class which is useful importing a CSV file onto the cells of a worksheet.
### **Added ICells::ImportTwoDimensionArray Method**
The GetIProtectedRangeCollection method has been added to the ICells class which is useful importing a two-dimensional array of data onto a worksheet.
### **Added IWorksheet::GetIProtectedRangeCollection Method**
The GetIProtectedRangeCollection method has been added to the IWorksheet class which is useful in retrieving the collection of IProtectedRange objects.
### **Added IWorksheet::GetIProtectedRangeCollection Method**
The GetIProtectedRangeCollection method has been added to the IWorksheet class which is useful in retrieving the edit range collection from the worksheet.
### **Added IWorkbookSettings::ClearPivottables Method**
The ClearPivottables method has been added to the IWorkbookSettings class which is useful in clearing all Pivot Tables from a given spreadsheet.
### **Added IWorksheetCollection::CreateIRange Method**
The CreateIRange method has been added to the IWorksheetCollection class which is useful in creating an object of the IRange by passing cell references in string format.
### **Added IExternalLink::IsVisible Method**
The IsVisible method gets the visibility status of an external link in Excel application.
### **Added GetScaleCrop & SetScaleCrop Methods**
Aspose.Cells for C++ 17.1.0 has exposed the GetScaleCrop & SetScaleCrop methods to the IBuiltInDocumentPropertyCollection class. These methods are useful to get or set the ScaleCrop property which indicates the display mode of the document thumbnail.
### **Added GetLinksUpToDate & SetLinksUpToDate Methods**
Aspose.Cells for C++ 17.1.0 has exposed the GetLinksUpToDate & SetLinksUpToDate methods to the IBuiltInDocumentPropertyCollection class. These methods are useful to get or set the LinkUpToDate property which indicates whether hyperlinks in a document are up-to-date.
### **Added GetAbsolutePath & SetAbsolutePath Methods**
Aspose.Cells for C++ 17.1.0 has exposed the GetAbsolutePath & SetAbsolutePath methods to the IWorkbook class. These methods are useful to get or set the absolute path of the file which can only be used for external links.
### **Added GetFormula & SetFormula Methods**
This release of Aspose.Cells for C++ has exposed the GetFormula & SetFormula methods for the IListColumn class. These methods are useful to get or set the formula of a list column.
### **Added GetCheckCompatibility & SetCheckCompatibility Methods**
This release of Aspose.Cells for C++ has exposed the GetCheckCompatibility & GetCheckCompatibility methods for the IWorkbookSettings class. These methods are useful to get or set the compatibility check property indicating if the API should check the compatibility when saving workbook. The default value is true, and can be set to false if application requirement is not to check the compatibility.
### **Added GetILightCellsDataHandler & SetILightCellsDataHandler Methods**
Aspose.Cells for C++ has now exposed the GetILightCellsDataHandler & SetILightCellsDataHandler methods for the ILoadOptions class. These methods denotes the data handler for processing cells data while reading template file.
### **Added GetCultureInfo & SetCultureInfo Methods**
Aspose.Cells for C++ has exposed the GetCultureInfo & SetCultureInfo methods for the ILoadOptions class. These methods can get or set the system culture info at the time file loading.
## **Removed APIs**
### **Removed ICells::MaxDataRowInColumn Method**
It is advised to use the ICells::GetLastDataRow method instead.
### **Removed ICell::GetConditionalIStyle Method**
It is advised to use the ICell::GetIConditionalFormattingResult method instead.
### **Removed IPageSetup::GetDraft & SetDraft Methods**
It is advised to use the IPageSetup::GetPrintDraft & IPageSetup::SetPrintDraft methods instead.

{{% alert color="primary" %}} 

With the release of Aspose.Cells for C++ 17.1.0, we have removed a few method which were not in use therefore deemed unnecessary. Here is the list of all such methods.

- IPaneCollection::GetAcitvePaneType & SetAcitvePaneType Methods
- IRange::ToString Method
- IRow::Equals Method
- IWorkbook::SetISettings Method
- ICell::ToString() Method
- ICell::Equals(ObjectPtr) Method
- ICell::GetHashCode Method
- IWorksheet::ToString Method

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
