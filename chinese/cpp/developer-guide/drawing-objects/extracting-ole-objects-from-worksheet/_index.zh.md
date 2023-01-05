---
title: 从工作表中提取 OLE 对象
type: docs
weight: 10
url: /zh/cpp/extracting-ole-objects-from-worksheet/
---
## **可能的使用场景**
Aspose.Cells 允许您从工作表中提取所有类型的 OLE 对象。请用[IWorksheet->GetIOleObjects()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4c59d95cdd871ecfe18274480831a728)方法来访问工作表中的所有 OLE 对象。每个 OLE 对象都有[程序ID](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#abb2ea6872025fe4724d9613cd6b81752)和[对象数据](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#a4a200a03478d3553798360cd6a911d70)可以帮助您识别 OLE 对象的类型并成功提取它的属性。
## **从工作表中提取 OLE 对象**
下面的示例代码加载[示例 Excel 文件](66519077.xlsx)其中包含三个 OLE 对象。代码识别OLE对象的类型，并一一提取为如下文件。

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet.cpp" >}}
