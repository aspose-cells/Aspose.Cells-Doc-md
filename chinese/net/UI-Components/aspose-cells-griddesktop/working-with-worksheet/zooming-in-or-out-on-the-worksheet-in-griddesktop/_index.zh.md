---
title: 在GridDesktop工作表中放大或缩小视图
type: docs
weight: 160
url: /zh/net/aspose-cells-griddesktop/zoom-in-or-out-on-the-worksheet-in-griddesktop/
keywords: GridDesktop，缩放，放大视图，缩小视图
description: 本文介绍如何在GridDesktop中放大或缩小视图。
---

{{% alert color="primary" %}} 

有时，在处理数据时，您可能希望在屏幕上放大内容，而实际上并不更改字体大小。例如，您可能已经格式化了文本，以便使用小字体。（这通常是为了使所有信息都能打印出来。）但是，在工作表中工作时，字体太小，很难阅读。

在Microsoft Excel中，有一个缩放滑块可快速轻松地放大和缩小文档。 缩放滑块通常位于软件窗口的右下角。

Aspose.Cells还允许开发人员设置工作表的缩放因子，因此内容应根据您需求的百分比值出现。

{{% /alert %}} 
## **使用Aspose.Cells.GridDesktop进行放大或缩小视图**
Aspose.Cells提供Aspose.Cells.GridDesktop.Worksheet类，该类具有广泛的属性和方法，用于管理工作表。 要设置工作表的缩放因子，请使用工作表类的Zoom属性。 通过向Zoom属性分配数字（整数）值来设置缩放因子。

我们使用TrackBar（.NET）控件构建类似于MS Excel的缩放滑块。 在WinForm项目中，我们将工具箱中的Aspose.Cells.GridDesktop控件放置到表单中，并指定一些属性以设置其名称，大小或其他方面。 现在，我们将TrackBar控件放置在位于GridDesktop控件下方的右下角，还会放置一个Label控件，用于显示通过TrackBar控件的手柄指定的百分比值。 我们在TrackBar的滚动事件中添加相关代码线，因此当您滚动Trackbar控件时，GridDesktop应放大或缩小以显示其中的数据/内容。

下面提供了一个完整的示例，演示如何使用Zoom属性来设置GridDesktop的活动工作表的缩放因子。 我们首先将一个模板Excel文件导入到GridDesktop中。

写下面的代码在窗体的Load事件中，将模板Excel文件设置为GridDesktop和trackbar值。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


现在将下面的代码复制到跟踪滚动事件中并运行应用程序。 您会注意到移动跟踪条会更改工作表的缩放属性。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
