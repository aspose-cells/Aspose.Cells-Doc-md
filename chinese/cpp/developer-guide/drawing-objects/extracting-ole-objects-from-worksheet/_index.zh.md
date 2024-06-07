---
title: 从工作表中提取OLE对象
type: docs
weight: 10
url: /zh/cpp/extracting-ole-objects-from-worksheet/
---

## **可能的使用场景**
Aspose.Cells允许您从工作表中提取所有类型的OLE对象。请使用Worksheet-> GetOleObjects()方法访问工作表中的所有OLE对象。每个OLE对象都具有ProgID和ObjectData属性，可帮助您识别OLE对象的类型并成功提取它们。
## **从工作表中提取OLE对象**
以下示例代码加载了具有三个OLE对象的示例Excel文件。该代码识别了OLE对象的类型，并逐个提取它们作为以下文件。

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **示例代码**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
