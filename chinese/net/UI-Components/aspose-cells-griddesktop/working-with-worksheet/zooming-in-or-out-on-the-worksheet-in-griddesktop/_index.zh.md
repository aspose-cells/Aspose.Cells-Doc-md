---
title: 在 GridDesktop 中放大或缩小工作表
type: docs
weight: 160
url: /zh/net/aspose-cells-griddesktop/zoom-in-or-out-on-the-worksheet-in-griddesktop/
keywords: GridDesktop，缩放，放大，缩小
description: 本文介绍了在 GridDesktop 中如何缩放。
---

{{% alert color="primary" %}} 

有时，在处理数据时，您可能希望在屏幕上放大内容，而不实际更改字体大小。例如，您可能已经格式化了文本，以便使用较小的字体。然而，在工作表中工作时，由于字体太小而难以阅读。

在 Microsoft Excel 中，一个缩放滑块可快速且轻松地放大和缩小文档。缩放滑块通常位于软件窗口的右下角。

Aspose.Cells 还允许开发人员设置工作表的缩放系数，以便内容显示为所需的百分比值。

{{% /alert %}} 
## **使用 Aspose.Cells.GridDesktop 进行放大或缩小**
Aspose.Cells 提供了 Aspose.Cells.GridDesktop.Worksheet 类，该类具有广泛的属性和方法来管理工作表。要设置工作表的缩放系数，请使用 Worksheet 类的 Zoom 属性。通过将一个数字（整数）值分配给 Zoom 属性来设置缩放系数。

我们使用 TrackBar (.NET) 控件构建了一个类似于 MS Excel 的缩放滑块。在 WinForm 项目中，我们将 Aspose.Cells.GridDesktop 控件从工具箱放置到窗体上，并根据需要指定一些属性来设置其名称、大小或其他方面。现在，我们将 TrackBar 控件放置在 GridDesktop 控件下方右下角，还在其下放置一个标签控件，该控件将显示通过 TrackBar 控件的滑块指定的百分比值。我们在 TrackBar 的滚动事件中添加了相关代码行，这样当滚动 Trackbar 控件时，GridDesktop 应该放大或缩小以显示其中的数据/内容。

下面给出一个完整的示例，演示如何使用 Zoom 属性设置 GridDesktop 的活动工作表的缩放系数。我们首先将一个模板 Excel 文件导入到 GridDesktop。

在窗体的加载事件中编写以下代码，将模板 Excel 文件设置为 GridDesktop 并跟踪条值。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


现在将以下代码复制到跟踪滚动事件中并运行应用程序。您将注意到移动跟踪条将更改工作表的缩放属性。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
