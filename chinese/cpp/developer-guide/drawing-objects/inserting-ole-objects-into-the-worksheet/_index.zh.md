---
title: 向工作表中插入OLE对象
type: docs
weight: 20
url: /zh/cpp/inserting-ole-objects-into-the-worksheet/
---

## **可能的使用场景**
Aspose.Cells允许您在工作表中插入OLE对象。请使用Worksheet->GetOleObjects()->Add()方法实现此目的。您将需要一个图像字节数组，用于在工作表中插入OLE对象，以及将用于在工作表中插入OLE对象的实际对象的Ole对象数据字节数。 
## **将OLE对象插入工作表**
The following sample code creates the workbook object and inserts the Ole object inside the first worksheet and saves it as [output Excel file](66519074.xlsx). Please see the <a href="66519075.png" download="66519075.png">Aspose Logo</a> used as image bytes and [input Excel file](66519081.xlsx) used as Ole object data inside the code for reference.
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet-new.cpp" >}}
