---
title: 从工作表中提取 OLE 对象
type: docs
weight: 10
url: /zh/cpp/extracting-ole-objects-from-worksheet/
---
##  **可能的使用场景**
Aspose.Cells 允许您从工作表中提取所有类型的 OLE 对象。请用[工作表->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/)方法来访问工作表中的所有 OLE 对象。每个 OLE 对象都有[程序ID](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/)和[对象数据](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/)属性可以帮助您识别 OLE 对象的类型并成功提取它。
##  **从工作表中提取 OLE 对象**
以下示例代码加载[Excel 文件示例](66519077.xlsx)它有三个 OLE 对象。代码识别了OLE对象的类型，并将其一一提取出来，如下文件。

- [输出ExtractOleObject.pptx](66519080.pptx)
- [输出ExtractOleObject.pdf](66519079.pdf)
- [输出ExtractOleObject.docx](66519078.docx)
##  **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
