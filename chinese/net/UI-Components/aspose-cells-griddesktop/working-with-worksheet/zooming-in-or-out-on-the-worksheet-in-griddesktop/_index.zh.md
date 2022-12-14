---
title: 在 GridDesktop 中放大或缩小工作表
type: docs
weight: 160
url: /zh/net/zooming-in-or-out-on-the-worksheet-in-griddesktop/
---
{{% alert color="primary" %}} 

有时，在处理数据时，您可能希望在不实际更改字体大小的情况下放大屏幕上的内容。例如，您可能已将文本格式化为使用小字体。 （这通常是在打印输出上获取所有信息所必需的。）但是，在工作表中工作时，字体太小，难以阅读。

在 Microsoft Excel 中，缩放滑块可用于快速轻松地放大和缩小文档。缩放滑块通常位于软件窗口的右下角。

Aspose.Cells 还允许开发人员设置工作表的缩放系数，因此内容应该按照您想要的百分比值显示。

{{% /alert %}} 
## **使用 Aspose.Cells.GridDesktop 放大或缩小**
Aspose.Cells 提供 Aspose.Cells.GridDesktop.Worksheet 类，该类具有用于管理工作表的广泛属性和方法。要设置工作表的缩放系数，请使用 Worksheet 类的 Zoom 属性。缩放系数通过为 Zoom 属性分配一个数字（整数）值来设置。

我们使用 TrackBar (.NET) 控件构建类似 MS Excel 的缩放滑块。在 WinForm 项目中，我们将工具箱中的 Aspose.Cells.GridDesktop 控件放置到窗体中，并指定一些属性以相应地设置其名称、大小或其他方面。现在，我们将 TrackBar 控件放置在 GridDesktop 控件下方的右下角，我们还放置了一个 Label 控件，该控件将显示您通过 TrackBar 控件的句柄指定的百分比值。我们在 TrackBar 的 Scroll 事件中添加了相关的代码行，因此当您滚动 Trackbar 控件时，GridDesktop 应该放大或缩小以显示其中的数据/内容。

下面给出一个完整的示例，演示如何使用 Zoom 属性设置 GridDesktop 的活动工作表的缩放因子。我们首先将模板 Excel 文件导入 GridDesktop。

在窗体的 Load 事件中编写以下代码以设置 GridDesktop 中的模板 Excel 文件和轨迹栏值。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


现在将下面的代码复制到轨道滚动事件中并运行应用程序。您会注意到移动轨迹栏会改变工作表的缩放属性。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
