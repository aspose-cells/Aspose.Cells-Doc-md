---
title: 将OLE对象插入工作表
type: docs
weight: 20
url: /zh/cpp/inserting-ole-objects-into-the-worksheet/
---

## **可能的使用场景**
Aspose.Cells允许您在工作表中插入OLE对象。请使用[Worksheet->GetOleObjects()->Add()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/add/)方法来实现此目的。您需要一个图像字节数组，将用于在工作表中插入OLE对象，以及Ole对象数据字节，将是您实际要插入工作表中的对象。 
## **将OLE对象插入工作表**
The following sample code creates the workbook object and inserts the Ole object inside the first worksheet and saves it as [output Excel file](66519074.xlsx). Please see the <a href="66519075.png" download="66519075.png">Aspose标志</a> used as image bytes and [input Excel file](66519081.xlsx) used as Ole object data inside the code for reference.
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
