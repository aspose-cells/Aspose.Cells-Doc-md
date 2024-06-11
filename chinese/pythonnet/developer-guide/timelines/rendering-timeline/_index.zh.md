---
title: 渲染时间轴
type: docs
weight: 40
url: /zh/python-net/rendering-timeline/
description: 使用Aspose.Cells for Python via .NET管理Excel文件的时间轴。
keywords: Aspose.Cells for Python Excel，Python Excel库，Python不使用Excel呈现时间轴，使用Aspose.Cells for Python库呈现时间轴到图像。
---

## **可能的使用场景**
Aspose.Cells for Python via .NET支持在不使用Office 2013、Office 2016、Office 2019和Office 365的情况下呈现时间轴形状。如果您将工作表转换为图像，或者将工作簿保存为PDF或HTML格式，您将看到时间轴被正确呈现。

## **如何使用Aspose.Cells for Python Excel库呈现时间轴**
以下示例代码加载包含现有时间轴的 [示例Excel文件](input.xlsx)。根据时间轴的名称获取形状对象，然后通过Shape.to_image()方法将其呈现为图像。流动的图像是[输出图像](out.png)，显示了呈现的时间轴。正如您所看到的，时间轴已经被正确呈现，并且看起来与示例Excel文件中的时间轴相同。

![todo:image_alt_text](out.png)
### **示例代码**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-RenderingTimeline.py" >}}

