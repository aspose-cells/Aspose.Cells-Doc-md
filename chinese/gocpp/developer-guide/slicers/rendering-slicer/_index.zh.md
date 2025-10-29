---
title: 使用Golang通过C++渲染切片
type: docs
weight: 40
url: /zh/go-cpp/rendering-slicer/
description: 使用Golang via C++结合Aspose.Cells在Excel文件中渲染切片。
---

## **可能的使用场景**
Aspose.Cells支持对切片器形状进行渲染。如果将工作表转换为图像，或者将工作簿保存为PDF或HTML格式，您会看到切片器被正确地渲染。
## **呈现切片器**
以下示例代码加载包含现有切片器的[示例Excel文件](67338479.xlsx)，通过设置仅覆盖切片器的打印区域将工作表转换为图片。以下图片为[输出图片](67338480.png)，展示渲染的切片器。可以看到，切片器已正确渲染，与示例Excel文件中一样。

![todo:image_alt_text](rendering-slicer_1)
## **示例代码**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderingSlicer.go" >}}
