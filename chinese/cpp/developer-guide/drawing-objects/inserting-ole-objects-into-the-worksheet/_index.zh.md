---
title: 将 OLE 对象插入工作表
type: docs
weight: 20
url: /zh/cpp/inserting-ole-objects-into-the-worksheet/
---
##  **可能的使用场景**
Aspose.Cells 允许您在工作表中插入 OLE 对象。请用[工作表->GetOleObjects()->Add()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/add/)用于此目的的方法。您将需要一个图像字节数组，该数组将用于在工作表中插入 OLE 对象，并且 Ole 对象数据字节将成为您的实际对象。要在工作表中插入 Ole 对象。
##  **将 OLE 对象插入工作表**
以下示例代码创建工作簿对象并将 Ole 对象插入第一个工作表中并将其另存为[输出Excel文件](66519074.xlsx)。请参阅<a href="66519075.png" download="66519075.png">Aspose 标志</a>用作图像字节和[输入Excel文件](66519081.xlsx)代码内部用作Ole对象数据以供参考。
##  **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet-new.cpp" >}}
