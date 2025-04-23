---
title: 如何在 Blazor 中运行 Aspose.Cells
type: docs
weight: 138
url: /zh/net/how-to-run-aspose-cells-in-blazor/
description: 了解如何在 Blazor WebAssembly 和 Blazor Server 应用中运行 Aspose.Cells。
keywords: C# 在 Blazor WebAssembly 中运行 Aspose.Cells， 在 Blazor WebAssembly 中使用 Aspose.Cells，带有 Aspose.Cells 的 Blazor WebAssembly 应用
---

## 概述

Blazor 是由微软开发的一个网页框架，允许开发者使用 C# 和 .NET 构建交互式客户端网页应用，而无需使用 JavaScript。Blazor 有两种主要的托管模式：**Blazor WebAssembly** 和 **Blazor Server**。你可以在这两种模式中直接使用 **Aspose.Cells for .NET**。

## 带有 Aspose.Cells 的 Blazor WebAssembly 应用

Blazor WebAssembly 在浏览器端使用 WebAssembly 运行。这允许开发者在浏览器中直接运行 .NET 应用，而无需依赖服务器进行渲染。从 **Aspose.Cells for .NET 25.1** 开始，Aspose.Cells 可以直接在 Blazor WebAssembly 应用中使用。在这个例子中，你将创建一个简单的带有 Aspose.Cells 的 Blazor WebAssembly，渲染一个包含文本和形状的 Excel 文件成 png 图像，然后在页面上显示该图像。

### 创建 Blazor WebAssembly 应用

以 VS2022 工具为例，按照以下步骤创建第一个带有 Aspose.Cells 的 Blazor WebAssembly 应用：

1. 使用 **Blazor WebAssembly 独立应用**模板创建新项目。

   ![webassembly_project_template.jpg](webassembly_project_template.jpg)

2. 选择目标框架，推荐使用 .NET 8.0 或更高版本。

   ![webassembly_framework_net9.jpg](webassembly_framework_net9.jpg)

3. 项目创建后，添加 Aspose.Cells 包到项目中。因为 Aspose.Cells 引用 SkiaSharp，为了让 SkiaSharp 在 WebAssembly 中工作，还需要添加 "SkiaSharp.Views.Blazor" 包。

   ```
   <PackageReference Include="Aspose.Cells" Version="25.1.1" />
   <PackageReference Include="SkiaSharp.Views.Blazor" Version="3.116.1" />
   ```

   *请注意，所添加包 "SkiaSharp.Views.Blazor" 的版本应对应于 Aspose.Cells for .NET 引用的 "SkiaSharp" 版本。Aspose.Cells for .NET 和相应引用的 "SkiaSharp" 版本的描述如下：*

   | Aspose.Cells for .NET |                SkiaSharp                |
   | :-------------------: | :-------------------------------------: |
   |       = 25.1.1        |                 3.116.1                 |
   |       >=25.1.2        | 2.88.9（net6.0、net8.0），3.116.1（net9.0） |

4. 在 "Pages" 文件夹中的 "Home.razor" 文件中编写代码，添加一些数据和图形，并渲染成图片以显示。

   ![webassembly_code.jpg](webassembly_code.jpg)

5. 右键项目，选择 "发布..."，然后将项目发布到有或没有 AOT 选项的文件夹中。

   ![webassembly_publish.jpg](webassembly_publish.jpg)

6. 发布后，输出文件将位于 `publish/wwwroot` 文件夹中。这些文件是静态文件（HTML、JS、CSS等），可使用以下方式托管：

   - **本地网页服务器**（如 `dotnet serve`、`nginx` 或 `Apache`）。
   - **云托管**（如 Azure、AWS、Netlify、GitHub Pages）。

   以 `dotnet serve` 为例：

   - 安装 `dotnet-serve` 工具（如果尚未安装）：

     ```bash
     dotnet tool install -g dotnet-serve
     ```

   - 进入已发布的 `wwwroot` 目录。

   - 启动服务器：

     ```bash
     dotnet serve
     ```

7. 打开浏览器，访问显示的地址（例如 `http://localhost:1970`），输出的图片会显示在页面上。

   ![webassembly_output.jpg](webassembly_output.jpg)

### Blazor WebAssembly 应用中的示例代码

以下示例代码包含在 Home.razor 文件中：

```cs
@page "/"
@using Aspose.Cells
@using Aspose.Cells.Drawing
@using Aspose.Cells.Rendering

<PageTitle>Home</PageTitle>

<h1>Aspose.Cells works in Blazor WebAssembly App</h1>

@if (imageSrc is not null)
{
    <img src="@imageSrc" alt="Output Image" style="float: left; margin-right: 10px;" />
}
else
{
    <p>Loading image...</p>
}

@code
{
    private string? imageSrc;

    protected override void OnInitialized()
    {
        imageSrc = "data:image/png;base64, " + Convert.ToBase64String(CreateFile());
    }

    private byte[] CreateFile()
    {
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        sheet.Cells["A1"].Value = "Aspose.Cells works in Blazor WebAssembly App!";

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

### 疑难解答

Currently(Jan 2025) there is a known issue of `dotnet` in the case that publishing a Blazor WebAssembly project which targets to net8.0 with .NET 9.0 SDK(.NET 9.0 SDK is installed and .NET 8.0 SDK is uninstalled if you upgraded Visual Studio to the version v17.12.x). For more info, check the link: <https://github.com/dotnet/runtime/issues/109951>.

```
System.PlatformNotSupportedException: PlatformNotSupported_HybridGlobalization, HashCode
   at System.Globalization.CompareInfo.GetHashCodeOfStringCore(ReadOnlySpan`1 , CompareOptions )
   at System.Globalization.CompareInfo.GetHashCode(ReadOnlySpan`1 , CompareOptions )
   at System.Globalization.CompareInfo.GetHashCode(String , CompareOptions )
   at System.CultureAwareComparer.GetHashCode(String )
   at System.StringComparer.GetHashCode(Object )
```

如果是你的情况，有三个选择：

1. 重新安装 .NET 8.0 SDK（如果已卸载），并在解决方案级别（与 .sln 文件同一文件夹）使用 "global.json" 文件指定所用 SDK。以下是 "global.json" 文件的示例：

   ```
   {
     "sdk": {
       "version": "8.0.300",
       "rollForward": "latestFeature"
     }
   }
   ```



2. 更新项目文件以目标为 net9.0。

3. Update Visual Studio to the version v17.12.4.(The issue <https://github.com/dotnet/runtime/issues/109951> is fixed.(updated on Jan 15, 2025))

## 使用Aspose.Cells创建Blazor服务器应用程序

在此示例中，你将创建一个简单的 Blazor Server 应用，添加一些数据和图形，并将它们渲染成图片显示在网页上。在项目创建过程中，可以根据自己的需要配置选项。例如，勾选 "启用 Docker" 选项，则可以在 Docker 中构建和运行这个 Blazor 应用。

### 创建Blazor服务器应用程序

以 VS2022 工具为例，按照以下步骤创建第一个带有 Aspose.Cells 的 Blazor Server 应用：
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
<img src="6.png" width=70% />
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
{{< app/cells/assistant language="csharp" >}}
