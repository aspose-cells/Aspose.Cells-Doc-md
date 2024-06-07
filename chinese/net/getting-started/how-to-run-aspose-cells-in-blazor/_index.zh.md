---
title: 如何在Blazor中运行Aspose.Cells
type: docs
weight: 138
url: /zh/net/how-to-run-aspose-cells-in-blazor/
description: 学习如何在Blazor中运行Aspose.Cells。
keywords: 在Blazor中运行Aspose.Cells，使用Aspose.Cells在Blazor中，Blazor服务器应用程序与Aspose.Cells
---

## 概述

要在Blazor中运行Aspose.Cells，您需要.NET6（或更高版本）平台，与之前的平台（.netcore31或更早版本）相比，一个重要的区别是关于图形库。在此官方[Microsoft文档](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only)中，它解释了对于.NET6或更高版本，图形库"System.Drawing.Common"将仅在Windows上受支持，并建议替换图形库。

对于Apose.Cells产品，我们已经进行了评估并完成了图形库的迁移。在非Windows系统中，我们使用SkiaSharp代替System.Drawing.Common，正如Microsoft官方文档建议的那样。请注意，这个关键性的变化将在Aspose.Cells 22.10.1或更高版本中对.NET6生效。

## 在Blazor服务器应用程序中使用Aspose.Cells

在此示例中，您将创建一个简单的Blazor服务器应用程序，添加一些数据和图形，并将它们呈现为图像以显示在网页上。在项目创建过程中，您可以根据自己的需求配置选项。例如，当您选中"启用Docker"选项时，Blazor应用程序可以在Docker中构建和运行。

### 创建Blazor服务器应用程序

让我们以VS2022工具为例，创建第一个带有Aspose.Cells的Blazor应用程序，按照以下步骤进行：
1. 选择文件 ->新建 ->项目，并使用blazer关键字过滤以选择相应的项目模板。
<br>
<img src="1.png" width=70% />
1. 将项目命名为"BlazorTest"并选择路径。
<br>
<img src="2.png" width=70% />
1. 配置项目中使用的库和其他选项。最后，点击"创建"按钮生成你的第一个Blazer项目。
<br>
<img src="3.png" width=70% />
1. 进入项目后，单击项目下的"依赖项"，选择"管理NuGet软件包..."以添加Aspose.Cells库。
<br>
<img src="4.png" width=70% />
1. 输入关键字进行过滤，安装最新的Aspose.Cells库。同时将安装一同依赖的库，比如SkiaSharp。
<br>
<img src="5.png" width=70% />
1. 双击"Index.razor"文件进行编辑，并导入所需的库。添加一些数据和图形，并将它们呈现为图形以供显示。
<br>
<img src="5.png" width=70% />
1. 编译并运行该项目，您将获得以下结果。
<br>
<img src="7.png" width=70% />

### Blazor服务器应用程序中的示例代码

以下示例代码包括在Index.razor文件中：
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
