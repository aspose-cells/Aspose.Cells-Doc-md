---
title: Inserting OLE Objects into the Worksheet
type: docs
weight: 20
url: /go-cpp/inserting-ole-objects-into-the-worksheet/
---

## **Possible Usage Scenarios**
Aspose.Cells allows you to insert an OLE object into the worksheet. Please use the [Worksheet.GetOleObjects().Add()](https://reference.aspose.com/cells/go-cpp/oleobjectcollection/add_int_int_int_int_stream/) method for this purpose. You will need an image byte array to be used as the picture representing the OLE object, and OLE object data bytes that contain the actual object to be inserted into the worksheet.

## **Inserting OLE Objects into the Worksheet**
The following sample code creates the workbook object, inserts the OLE object into the first worksheet, and saves it as an [output Excel file](66519074.xlsx). Please see the <a href="66519075.png" download="66519075.png">Aspose Logo</a> used as image bytes and the [input Excel file](66519081.xlsx) used as OLE object data inside the code for reference.

## **Sample Code**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingOleObjectsIntoTheWorksheet.go" >}}
{{< app/cells/assistant language="go" >}}
