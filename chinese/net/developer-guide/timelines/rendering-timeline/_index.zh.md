---
title: 渲染时间轴
type: docs
weight: 40
url: /zh/net/rendering-timeline/
description: 使用Aspose.Cells管理Excel文件的时间轴。
keywords: 在没有Office 2013、Office 2016、Office 2019和Office 365的情况下渲染时间轴
---

## **可能的使用场景**
Aspose.Cells支持在不使用office 2013、office 2016、office 2019和office 365的情况下呈现时间轴形状。如果将工作表转换为图像，或者将工作簿保存为PDF或HTML格式，就会看到时间轴已正确呈现。

## **呈现时间轴**
以下示例代码加载包含现有时间轴的[sample Excel file](input.xlsx)，根据时间轴名称获取形状对象，然后通过Shape.ToImage()方法将其呈现为图片。以下图片是[output image](out.png)，显示了已呈现的时间轴。正如你所见，时间轴已正确呈现，并且看起来与示例Excel文件中的相同。

![todo:image_alt_text](out.png)
### **示例代码**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Timelines-RenderingTimeline.cs" >}}

{{< app/cells/assistant language="csharp" >}}
