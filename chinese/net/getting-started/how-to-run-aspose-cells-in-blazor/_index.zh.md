---
title: 如何在 Blazor 中运行 Aspose.Cells
type: docs
weight: 138
url: /zh/net/how-to-run-aspose-cells-in-blazor/
description: 了解如何在 Blazor 中运行 Aspose.Cells。
keywords: C# Run Aspose.Cells in Blazor, Use Aspose.Cells in Blazor
---
## 概述

要在 Blazor 中运行 Aspose.Cells，您需要 .NET6（或更高版本）平台，与以前的平台（.netcore31 或之前）相比，一个重要的区别在于图形库。在这个官方[Microsoft 文件](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only)，它解释了.NET6或更高版本的图形库“System.Drawing.Common”将仅在Windows上受支持，并给出了替换图形库的建议。

对于Apose.Cells产品，我们已经进行了评估并完成了图形库的迁移。我们在非 Windows 系统中使用 SkiaSharp 而不是 System.Drawing.Common，如 Microsoft 官方文档中建议的那样。请注意，此重要更改将在 .Net6 的 Aspose.Cells 22.10.1 或更高版本中生效。

## 第一个 Blazor 应用程序，编号为 Aspose.Cells

在此示例中，您将创建一个简单的 blazor 服务器应用程序，该应用程序添加一些数据和图形，并将它们渲染为图像以显示在网页上。在项目创建过程中，您可以根据自己的需要配置选项。例如，当您选中“启用 Docker”选项时，blazor 应用程序就可以在 Docker 中构建并运行。

### 创建第一个 Blazor 应用程序

我们以VS2022工具为例，创建第一个blazor应用程序，编号为Aspose.Cells，步骤如下：
1. 选择文件 -> 新建 -> 项目并使用 blazer 关键字进行过滤以选择相应的项目模板。
<br>
<img src="1.png" width=70% />
1. 将项目名称设置为“BlazorTest”并选择路径。
<br>
<img src="2.png" width=70% />
1. 配置项目中使用的库和其他选项。最后，单击“创建”按钮生成您的第一个西装外套项目。
<br>
<img src="3.png" width=70% />
1. 进入项目后，点击项目下的“依赖项”，选择“管理NuGet包...”添加Aspose.Cells库。
<br>
<img src="4.png" width=70% />
1. 输入关键字进行过滤并安装最新的Aspose.Cells库。同时依赖的库如SkiaSharp也会一起安装。
<br>
<img src="5.png" width=70% />
1. 双击“Index.razor”文件编辑并导入所需的库。添加一些数据和图形，并将其渲染成图形进行显示。
<br>
<img src="5.png" width=70% />
1. 编译并运行该项目，您将得到以下结果。
<br>
<img src="7.png" width=70% />

### 第一个 Blazor 应用程序中的示例代码

Index.razor 文件中包含以下示例代码：
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