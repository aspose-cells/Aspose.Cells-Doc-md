---
title: 如何在 Blazor 中运行 Aspose.Cells
type: docs
weight: 138
url: /zh/net/how-to-run-aspose-cells-in-blazor/
description: 学习如何在 Blazor 中运行 Aspose.Cells。
keywords: C# 在 Blazor 中运行 Aspose.Cells，使用 Aspose.Cells 在 Blazor 中，具有 Aspose.Cells 的 Blazor 服务器应用程序
---

## 概述

要在 Blazor 中运行 Aspose.Cells，您需要.net6(或更高版本)平台，与之前的平台(.NetCore31或之前)相比，一个重要的区别是关于图形库。在这份官方[Microsoft文档](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only)中，它解释了对于.net6或以后版本，图形库“System.Drawing.Common”将仅支持在Windows上，并建议替换图形库。

对于Apose.Cells产品，我们已经进行了评估并已完成了图形库的迁移。在非Windows系统中，我们使用SkiaSharp代替System.Drawing.Common，这是在微软官方文档中建议的。请注意，这个重要的更改将在Aspose.Cells 22.10.1或更高版本的.Net6中生效。

## 使用Aspose.Cells创建Blazor服务器应用程序

在这个示例中，您将创建一个简单的Blazor服务器应用程序，向其中添加一些数据和图形，并将它们渲染成图像以在网页上显示。在项目创建过程中，您可以根据自己的需求配置选项。例如，当您勾选"启用Docker"选项时，Blazor应用程序可以在Docker中构建和运行。

### 创建Blazor服务器应用程序

让我们以VS2022工具作为示例，按照以下步骤创建第一个带有Aspose.Cells的Blazor应用程序：
1. 选择文件 -> 新建 -> 项目，并使用Blazor关键词进行过滤，选择相应的项目模板。
<br>
<img src="1.png" width=70% />
1. 将项目名称设置为"BlazorTest"，并选择路径。
<br>
<img src="2.png" width=70% />
1. 配置项目中使用的库和其他选项。最后，点击"创建"按钮生成您的第一个Blazor项目。
<br>
<img src="3.png" width=70% />
1. 进入项目后，点击项目下的"依赖项"，选择"管理NuGet软件包"，添加Aspose.Cells库。
<br>
<img src="4.png" width=70% />
1. 输入关键字进行过滤并安装最新的Aspose.Cells库。同时，相应依赖库如SkiaSharp也会被一同安装。
<br>
<img src="5.png" width=70% />
1. 双击"Index.razor"文件进行编辑并导入所需的库。添加一些数据和图形，将其渲染成图形进行显示。
<br>
<img src="5.png" width=70% />
1. 编译并运行项目，您将得到以下结果。
<br>
<img src="7.png" width=70% />

### Blazor服务器应用程序示例代码

以下示例代码包含在Index.razor文件中：
```
@page "/"
@using SkiaSharp;
@using Aspose.Cells;
@using Aspose.Cells.Drawing;
@using Aspose.Cells.Rendering;


<PageTitle>Index</PageTitle>

<h1>Hello, world!</h1>

Welcome to your new app.

<SurveyPrompt Title="How is Blazor working for you?" />

<img src="@imageSrc" />

@code
{
    private string imageSrc;

    public Index()
    {
        imageSrc = "data:image/png;base64, " + Convert.ToBase64String(CreateFile());
    }

    private byte[] CreateFile()
    {
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        sheet.Cells["A1"].Value = "test data for blazor";

        sheet.PageSetup.PrintGridlines = true;
        sheet.PageSetup.PrintArea = "A1:F20";

        ShapeCollection shapes = sheet.Shapes;

        //Add rectangle shape
        shapes.AddRectangle(1, 0, 1, 0, 100, 150);

        //Add line shape
        shapes.AddLine(8, 0, 1, 0, 100, 150);

        //Add oval shape
        shapes.AddOval(13, 0, 1, 0, 100, 150);

        using MemoryStream ms = new();

        SheetRender render = new SheetRender(sheet, new ImageOrPrintOptions());
        render.ToImage(0, ms);

        return ms.ToArray();
    }
}

```
