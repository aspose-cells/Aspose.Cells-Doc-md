---
title: 渲染时间轴
type: docs
weight: 40
url: /zh/nodejs-cpp/rendering-timeline/
description: 使用Aspose.Cells for Node.js via C++管理Excel文件的时间线。
keywords: 在没有Office 2013、Office 2016、Office 2019和Office 365的情况下渲染时间轴
---

## **可能的使用场景**
Aspose.Cells for Node.js via C++支持无需使用Office 2013、Office 2016、Office 2019和Office 365即可渲染时间线形状。如果将工作表转换为图片或将工作簿保存为PDF或HTML格式，您会看到时间线被正确渲染。

## **呈现时间轴**
以下示例代码加载包含现有时间轴的[sample Excel file](input.xlsx)，根据时间轴名称获取形状对象，然后通过Shape.ToImage()方法将其呈现为图片。以下图片是[output image](out.png)，显示了已呈现的时间轴。正如你所见，时间轴已正确呈现，并且看起来与示例Excel文件中的相同。

![todo:image_alt_text](out.png)
### **示例代码**
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-RenderingTimeline.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
