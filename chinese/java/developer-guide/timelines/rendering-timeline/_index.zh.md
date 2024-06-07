---
title: 渲染时间轴
type: docs
weight: 40
url: /zh/java/rendering-timeline/
description: 使用Aspose.Cells For Java管理Excel文件的时间轴。
keywords: 在不使用office 2013、office 2016、office 2019和office 365的情况下渲染时间表
---

## **可能的使用场景**
Aspose.Cells支持在不使用office 2013、office 2016、office 2019和office 365的情况下渲染时间表形状。如果将工作表转换为图片，或将工作簿保存为PDF或HTML格式，您将看到时间轴会被正确地渲染。

## **渲染时间轴**
以下示例代码加载包含现有时间表的[示例Excel文件](input.xlsx)。根据时间轴的名称获取形状对象，然后通过Shape.ToImage()方法将其渲染为图片。下方图像是显示渲染时间轴的[输出图片](out.png)。如您所见，时间轴已被正确渲染，并且与示例Excel文件中的样式相同。

![todo:image_alt_text](out.png)
### **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-RenderingTimeline.java" >}}

