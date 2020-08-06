---
title: Inserting OLE Objects into the Worksheet
type: docs
weight: 20
url: /cpp/inserting-ole-objects-into-the-worksheet/
---

## **Possible Usage Scenarios**
Aspose.Cells allows you to insert an OLE object inside the worksheet. Please use [IWorksheet->GetIOleObjects()->Add()](https://apireference.aspose.com/cpp/cells/class/aspose.cells.drawing.i_ole_object_collection/#af230dd65a00cefabcc4b9f165b5dc7ba) method for this purpose. You will need an image byte array that will be used to insert the OLE object inside the worksheet and Ole object data bytes that will be your actual object.to insert the Ole object inside the worksheet. 
## **Inserting OLE Objects into the Worksheet**
The following sample code creates the workbook object and inserts the Ole object inside the first worksheet and saves it as [output Excel file](attachments/66257162/66519074.xlsx). Please see the [Aspose Logo](attachments/66257162/66519075.png) used as image bytes and [input Excel file](attachments/66257162/66519081.xlsx) used as Ole object data inside the code for reference.
## **Sample Code**
{{< gist "aspose-com-gists" "0edd1c91ebaa6cd099be1200b1ec7480" "DrawingObjects-InsertingOLEObjectsIntoWorksheet.cpp" >}}
