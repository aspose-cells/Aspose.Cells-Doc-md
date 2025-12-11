---
title: Inserting OLE Objects into the Worksheet
type: docs
weight: 20
url: /cpp/inserting-ole-objects-into-the-worksheet/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Aspose.Cells allows you to insert an OLE object into the worksheet. Please use the [Worksheet.GetOleObjects().Add()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/add/) method for this purpose. You will need an image byte array to be used as the picture representing the OLE object, and OLE object data bytes that contain the actual object to be inserted into the worksheet.

## **Inserting OLE Objects into the Worksheet**
The following sample code creates the workbook object, inserts the OLE object into the first worksheet, and saves it as an [output Excel file](66519074.xlsx). Please see the <a href="66519075.png" download="66519075.png">Aspose Logo</a> used as image bytes and the [input Excel file](66519081.xlsx) used as OLE object data inside the code for reference.

## **Sample Code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
