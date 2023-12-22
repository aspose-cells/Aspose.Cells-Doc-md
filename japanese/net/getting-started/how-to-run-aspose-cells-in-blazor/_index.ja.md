---
title: Blazor で Aspose.Cells を実行する方法
type: docs
weight: 138
url: /ja/net/how-to-run-aspose-cells-in-blazor/
description: Blazor で Aspose.Cells を実行する方法を学習します。
keywords: C# Run Aspose.Cells in Blazor, Use Aspose.Cells in Blazor
---
## 概要

 Blazor で Aspose.Cells を実行するには、.NET6 (以降) プラットフォームが必要です。以前のプラットフォーム (.netcore31 以前) と比較して、重要な違いはグラフィック ライブラリに関するものです。この公式では[Microsoft 文書](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only)では、.NET6 以降のリリースでは、グラフィックス ライブラリ「System.Drawing.Common」が Windows でのみサポートされることについて説明し、グラフィックス ライブラリを置き換える推奨事項を示します。

Apose.Cells 製品については、評価を実施し、グラフィックス ライブラリの移行を完了しました。 Microsoft の公式ドキュメントで示唆されているように、Windows 以外のシステムでは System.Drawing.Common の代わりに SkiaSharp を使用します。この重要な変更は、.Net6 の Aspose.Cells 22.10.1 以降で有効になることに注意してください。

## Aspose.Cells を使用した最初の Blazor アプリケーション

この例では、いくつかのデータとグラフィックスを追加し、それらを画像にレンダリングして Web ページに表示する単純な blazor サーバー アプリケーションを作成します。プロジェクトの作成プロセス中に、独自のニーズに応じてオプションを構成できます。たとえば、[Docker を有効にする] オプションをオンにすると、Blazor アプリケーションを Docker で構築して実行できるようになります。

### 最初の Blazor アプリケーションを作成する

例として VS2022 ツールを使用して、Aspose.Cells の最初の blazor アプリケーションを作成してみましょう。以下の手順に従います。
1. [ファイル] -> [新規] -> [プロジェクト] を選択し、ブレザー キーワードを使用してフィルタリングして、対応するプロジェクト テンプレートを選択します。
<br>
<img src="1.png" width=70% />
1. プロジェクト名を「BlazorTest」に設定し、パスを選択します。
<br>
<img src="2.png" width=70% />
1. プロジェクトで使用されるライブラリとその他のオプションを構成します。最後に、[作成] ボタンをクリックして最初のブレザー プロジェクトを生成します。
<br>
<img src="3.png" width=70% />
1. プロジェクトを入力した後、プロジェクトの下の「依存関係」をクリックし、「NuGet パッケージの管理...」を選択して Aspose.Cells ライブラリを追加します。
<br>
<img src="4.png" width=70% />
1. フィルタリング用のキーワードを入力し、最新の Aspose.Cells ライブラリをインストールします。 SkiaSharp などの依存ライブラリも同時にインストールされます。
<br>
<img src="5.png" width=70% />
1. 「Index.razor」ファイルをダブルクリックして、必要なライブラリを編集してインポートします。データとグラフィックスを追加し、それらを表示用のグラフィックスにレンダリングします。
<br>
<img src="5.png" width=70% />
1. プロジェクトをコンパイルして実行すると、次の結果が得られます。
<br>
<img src="7.png" width=70% />

### 最初の Blazor アプリケーションのサンプル コード

次のサンプル コードは Index.razor ファイルに含まれています。
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