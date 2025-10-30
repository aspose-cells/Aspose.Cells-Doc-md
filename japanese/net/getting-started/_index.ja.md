---
title: はじめに
type: docs
weight: 10
url: /ja/net/getting-started/
---

{{% alert color="primary" %}} 

このページでは、Aspose Cellsのインストール方法とHello Worldアプリケーションの作成方法を紹介します。

{{% /alert %}}

## **インストール**

### **Aspose.CellsをNuGetを通じてインストール**

NuGet は Aspose.Cells for .NET をダウンロードしてインストールする最も簡単な方法です。 

1. Microsoft Visual Studio を開き、NuGet パッケージマネージャを開きます。 
1. "aspose.cells" を検索して、希望の Aspose.Cells for .NET を見つけます。 
1. "インストール" をクリックすると、Aspose.Cells for .NET がダウンロードされ、プロジェクトに参照されます。
**![NuGet を通じて Aspose Cells をインストール](install-through-nuget.png)**

また、nuget web ページから aspose.cells をダウンロードすることもできます: 
[Aspose.Cells for .NET NuGetパッケージ](https://www.nuget.org/packages/Aspose.Cells/)

[詳細な手順](/cells/ja/net/installation/)

### **Windows に Aspose.Cells をインストール**

1. 次のページから Aspose.Cells.msi をダウンロードします:
[Aspose.Cells.msi をダウンロード](https://downloads.aspose.com/cells/net/)
1. Aspose Cells msi をダブルクリックし、インストール手順に従います:

**![Windows 上で Aspose Cells をインストール](install-on-windows.png)**

[詳細な手順](/cells/ja/net/installing-aspose-cells-on-windows/)

### **Linux 上で Aspose.Cells をインストール**

この例では、Ubuntu を使用して Linux 上で Aspose.Cells を使用する方法を示します。

1. ".netcore application" を作成し、「AsposeCellsTest」と名付けます。
2. 「AsposeCellsTest.csproj」ファイルを開き、Aspose.Cells パッケージの参照に以下の行を追加します。
{{< highlight plain >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="25.10" />
  </ItemGroup>
{{< /highlight >}}
3. Ubuntu 上の VSCode でプロジェクトを開きます。
**![Linux 上で Aspose Cells をインストール](install-on-linux.png)**
4. 次のコードでテストを実行します:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

注: Aspose.Cells For .NetStandard は Linux での要件をサポートできます。

適用対象: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 およびそれ以降のバージョン

### **MAC OS 上で Aspose.Cells をインストール**

この例では、macOS High Sierra を使用して MAC OS 上で Aspose.Cells を使用する方法を示します。

1. ".netcore application" を作成し、「AsposeCellsTest」と名付けます。
2. Visual Studio for Mac でアプリケーションを開き、NuGet を介して Aspose Cells をインストールします。
**![macOS 上で Aspose Cells をインストール](install-on-mac-os.png)**
3. 次のコードでテストを実行します:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. 描画関連の機能を使用する必要がある場合は、macOS に libgdiplus をインストールしてください。詳細は次を参照:
[macOS で libgdiplus のインストール方法](/cells/ja/net/how-to-install-libgdiplus-in-macos/)

Note: Aspose.Cells For .NetStandard はMAC OSでの要件をサポートできます。

適用対象: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 およびそれ以降のバージョン

### [**Run Aspose Cells in Docker**](/cells/ja/net/how-to-run-aspose-cells-in-docker/)

### **Net6以外のプラットフォームでグラフィックスライブラリを使用する方法**

Aspose.Cells for Net6 は今や、[Microsoft の公式声明](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md)で推奨されているSkiaSharpをグラフィックスライブラリとして使用しています。NET6でAspose.Cellsを使用する詳細については、[Aspose.Cells for .Net6 の実行方法](/cells/ja/net/how-to-run-aspose-cells-for-net6/)を参照してください。

## **Hello Worldアプリケーションの作成**

以下の手順により、Aspose.Cells APIを使用してHello Worldアプリケーションを作成できます:

1. ライセンスがある場合は、[適用します](/cells/ja/net/licensing/)。
   評価版を使用している場合は、ライセンスに関連するコード行をスキップします。
1. [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) クラスのインスタンスを作成して新しいExcelファイルを作成するか、既存のExcelファイルを開きます。
1. Excelファイルのワークシートの任意のセルにアクセスします。
1. アクセスしたセルに**Hello World!**の単語を挿入します。
1. 変更されたMicrosoft Excelファイルを生成します。

上記の手順の実装は、以下の例で示されています。

### **コードサンプル: 新しいワークブックの作成**

以下の例では、新しいブックを作成し、その初めのワークシートのセルA1に"Hello World!"を挿入し、Excelファイルとして保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **コードサンプル: 既存のファイルを開く**

以下の例では、既存のMicrosoft Excelテンプレートファイル "Sample.xlsx" を開き、その初めのワークシートのセルA1に"Hello World!"を挿入し、Excelファイルとして保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
