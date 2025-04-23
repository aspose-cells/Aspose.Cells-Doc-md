---
title: BlazorでAspose.Cellsを実行する方法
type: docs
weight: 138
url: /ja/net/how-to-run-aspose-cells-in-blazor/
description: Blazor WebAssemblyアプリやBlazorサーバーアプリでAspose.Cellsを実行する方法を学びましょう。
keywords: C# Aspose.CellsをBlazor WebAssemblyで実行、Blazor WebAssemblyでAspose.Cellsを使用、Aspose.Cellsを使用したBlazor WebAssemblyアプリケーション
---

## 概要

BlazorはMicrosoftが開発したウェブフレームワークで、開発者がJavaScriptを使わずにC#と.NETを使用してインタラクティブなクライアントサイドウェブアプリケーションを構築できるようにします。Blazorには主に二つのホスティングモデルがあります：**Blazor WebAssembly**と**Blazor Server**です。**Aspose.Cells for .NET**を直接両方のモデルで使用できます。

## Aspose.Cellsを使用したBlazor WebAssemblyアプリケーション

Blazor WebAssemblyはWebAssemblyを使ってクライアント側でブラウザ内で動作します。これにより開発者はサーバーに依存せずに.NETアプリケーションをブラウザ上で直接実行できます。**Aspose.Cells for .NET 25.1**から、Aspose.CellsはBlazor WebAssemblyアプリに直接使用可能です。この例では、Aspose.Cellsを使ったシンプルなBlazor WebAssemblyを作成し、テキストと図形を含むExcelファイルをPNG画像に変換し、その画像をページに表示します。

### Blazor WebAssemblyアプリケーションの作成

VS2022ツールを例にして、Aspose.Cellsを使用した最初のBlazor WebAssemblyアプリを作成する手順は次のとおりです：

1. **Blazor WebAssemblyスタンドアロンアプリ**テンプレートで新しいプロジェクトを作成します。

   ![webassembly_project_template.jpg](webassembly_project_template.jpg)

2. ターゲットフレームワークを選択してください。推奨は.NET 8.0以上です。

   ![webassembly_framework_net9.jpg](webassembly_framework_net9.jpg)

3. プロジェクト作成後、Aspose.Cellsパッケージを追加します。Aspose.CellsはSkiaSharpを参照しているため、WebAssemblyでSkiaSharpを動作させるには「SkiaSharp.Views.Blazor」パッケージが必要です。

   ```
   <PackageReference Include="Aspose.Cells" Version="25.1.1" />
   <PackageReference Include="SkiaSharp.Views.Blazor" Version="3.116.1" />
   ```

   *追加する「SkiaSharp.Views.Blazor」パッケージのバージョンは、参照されている「SkiaSharp」のバージョンと対応している必要があります。 Aspose.Cells for .NETが参照する「SkiaSharp」のバージョンと対応バージョンは次のとおりです:*

   | Aspose.Cells for .NET |                SkiaSharp                |
   | :-------------------: | :-------------------------------------: |
   |       = 25.1.1        |                 3.116.1                 |
   |       >=25.1.2        | 2.88.9（net6.0、net8.0）、3.116.1（net9.0） |

4. プロジェクトの「Pages」フォルダ内の「Home.razor」ファイルに移動し、いくつかのデータと図形を追加し、画像にレンダリングして表示するコードを記述します。

   ![webassembly_code.jpg](webassembly_code.jpg)

5. プロジェクトを右クリックし、「公開...」を選択します。その後、AOTオプションの有無にかかわらず、フォルダに公開します。

   ![webassembly_publish.jpg](webassembly_publish.jpg)

6. 公開後、出力ファイルは `publish/wwwroot` フォルダに配置されます。これらのファイルは静的ファイル（HTML、JS、CSSなど）ですので、次のような方法でホストできます：

   - **ローカルWebサーバー**（例：`dotnet serve`、`nginx`、`Apache`）。
   - **クラウドホスティング**（例：Azure、AWS、Netlify、GitHub Pages）。

   例として`dotnet serve`を取り上げると：

   - `dotnet-serve`ツールをインストール（まだインストールしていない場合）：

     ```bash
     dotnet tool install -g dotnet-serve
     ```

   - 公開された`wwwroot`ディレクトリに移動します。

   - サーバーを起動します：

     ```bash
     dotnet serve
     ```

7. ブラウザを開き、表示されているアドレス（例：`http://localhost:1970`）にアクセスしてください。出力画像がページに表示されます。

   ![webassembly_output.jgp](webassembly_output.jpg)

### Blazor WebAssemblyアプリケーションのサンプルコード

以下のサンプルコードはHome.razorファイルに含まれています：

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

### トラブルシューティング

Currently(Jan 2025) there is a known issue of `dotnet` in the case that publishing a Blazor WebAssembly project which targets to net8.0 with .NET 9.0 SDK(.NET 9.0 SDK is installed and .NET 8.0 SDK is uninstalled if you upgraded Visual Studio to the version v17.12.x). For more info, check the link: <https://github.com/dotnet/runtime/issues/109951>.

```
System.PlatformNotSupportedException: PlatformNotSupported_HybridGlobalization, HashCode
   at System.Globalization.CompareInfo.GetHashCodeOfStringCore(ReadOnlySpan`1 , CompareOptions )
   at System.Globalization.CompareInfo.GetHashCode(ReadOnlySpan`1 , CompareOptions )
   at System.Globalization.CompareInfo.GetHashCode(String , CompareOptions )
   at System.CultureAwareComparer.GetHashCode(String )
   at System.StringComparer.GetHashCode(Object )
```

この場合、次の3つのオプションから選択できます：

1. .NET 8.0 SDKを再インストール（アンインストールされている場合）し、ソリューションレベル（.slnファイルと同じフォルダ）に「global.json」ファイルを置いて使用するSDKを指定します。以下は「global.json」ファイルの例です：

   ```
   {
     "sdk": {
       "version": "8.0.300",
       "rollForward": "latestFeature"
     }
   }
   ```



2. プロジェクトファイルを更新してnet9.0をターゲットにします。

3. Update Visual Studio to the version v17.12.4.(The issue <https://github.com/dotnet/runtime/issues/109951> is fixed.(updated on Jan 15, 2025))

## Aspose.CellsでのBlazorサーバーアプリケーション

この例では、いくつかのデータとグラフィックを追加し、それらを画像にレンダリングしてWebページに表示するシンプルなBlazor Serverアプリを作成します。プロジェクト作成時には、ご自身のニーズに応じてオプションを設定してください。たとえば、「Dockerを有効にする」オプションを選択すると、BlazorアプリケーションをDocker内でビルドおよび実行できます。

### Blazorサーバーアプリケーションの作成

例としてVS2022ツールを使用して、Aspose.Cellsを含む最初のBlazor Serverアプリを作成する手順は次のとおりです：
1. ファイル -> 新規 -> プロジェクトを選択し、Blazerキーワードを使用して対応するプロジェクトテンプレートを選択します。
<br>
<img src="1.png" width=70% />
1. プロジェクト名を"BlazorTest"に設定し、パスを選択します。
<br>
<img src="2.png" width=70% />
1. プロジェクトで使用するライブラリやその他のオプションを構成します。最後に"作成"ボタンをクリックして最初のBlazerプロジェクトを生成します。
<br>
<img src="3.png" width=70% />
1. プロジェクトに入った後、プロジェクトの下にある"依存関係"をクリックし、「NuGetパッケージの管理...」を選択してAspose.Cellsライブラリを追加します。
<br>
<img src="4.png" width=70% />
1. フィルタリング用のキーワードを入力し、最新のAspose.Cellsライブラリをインストールします。同時にSkiaSharpなどの依存ライブラリも一緒にインストールされます。
<br>
<img src="5.png" width=70% />
1. "Index.razor"ファイルをダブルクリックして編集し、必要なライブラリをインポートします。データやグラフィックを追加し、それらを表示用のグラフィックにレンダリングします。
<br>
<img src="6.png" width=70% />
1. プロジェクトをコンパイルして実行すると、以下の結果が得られます。
<br>
<img src="7.png" width=70% />

### Blazorサーバーアプリケーションのサンプルコード

次のサンプルコードはIndex.razorファイルに含まれています:
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
