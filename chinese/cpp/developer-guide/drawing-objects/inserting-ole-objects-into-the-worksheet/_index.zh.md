---
title: 将 OLE 对象插入工作表
type: docs
weight: 20
url: /zh/cpp/inserting-ole-objects-into-the-worksheet/
---
## **可能的使用场景**
Aspose.Cells 允许您在工作表中插入 OLE 对象。请用[IWorksheet->GetIOleObjects()->Add()](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object_collection#af230dd65a00cefabcc4b9f165b5dc7ba)为此目的的方法。您将需要一个用于将 OLE 对象插入到工作表中的图像字节数组和将成为您的实际对象的 Ole 对象数据字节。以将 OLE 对象插入到工作表中。
## **将 OLE 对象插入工作表**
以下示例代码创建工作簿对象并将 Ole 对象插入第一个工作表并将其另存为[输出Excel文件](66519074.xlsx).请参阅[Aspose 徽标](66519075.png)用作图像字节和[输入Excel文件](66519081.xlsx)用作代码内部的 Ole 对象数据以供参考。
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet.cpp" >}}
