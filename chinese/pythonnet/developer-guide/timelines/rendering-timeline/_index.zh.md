---
title: 渲染时间轴
type: docs
weight: 40
url: /zh/python-net/rendering-timeline/
description: 使用 Aspose.Cells for Python via .NET 管理 Excel 文件的时间线。
keywords: Rendering timeline without office 2013, office 2016, office 2019 and office 365
---
##  **可能的使用场景**
Aspose.Cells for Python via .NET 支持时间线形状的渲染，而无需使用 Office 2013、office 2016、office 2019 和 Office 365。如果将工作表转换为图像或将工作簿保存为 PDF 或 HTML 格式，您将看到，时间线已正确渲染。

##  **渲染时间轴**
以下示例代码加载[Excel 文件示例](input.xlsx)包含现有的时间线。根据时间轴名称获取shape对象，然后通过Shape.to_image()方法渲染成图片。流动的图像是[输出图像](out.png)显示渲染的时间线。如您所见，时间线已正确呈现，并且看起来与示例 Excel 文件中的相同。

![待办事项：图像_替代_文本](out.png)
###  **示例代码**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-RenderingTimeline.py" >}}

