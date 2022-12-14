---
title: 渲染时间轴
type: docs
weight: 40
url: /zh/net/rendering-timeline/
description: 使用 Aspose.Cells 管理 Excel 文件的时间线。
keywords: Rendering timeline without office 2013, office 2016, office 2019 and office 365
---
## **可能的使用场景**
Aspose.Cells 支持在不使用 office 2013、office 2016、office 2019 和 office 365 的情况下渲染时间线形状。如果将工作表转换为图像或将工作簿保存为 PDF 或 HTML 格式，您将看到，时间线被正确渲染。

## **渲染时间轴**
下面的示例代码加载[示例 Excel 文件](input.xlsx)包含一个现有的时间表。根据时间线的名称获取shape对象，然后通过Shape.ToImage()方法渲染成图片。流动的图像是[输出图像](out.png)显示渲染的时间线。如您所见，时间线已正确呈现，看起来与示例 Excel 文件中的一样。

![待办事项：图片_替代_文本](out.png)
### **示例代码**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Timelines-RenderingTimeline.cs" >}}

