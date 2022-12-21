---
title: 入門
type: docs
weight: 10
url: /ja/net/getting-started/
---
{{% alert color="primary" %}} 

このページでは、Aspose Cells をインストールし、Hello World アプリケーションを作成する方法を説明します。

{{% /alert %}}

## **インストール**

### **Aspose.Cells から NuGet をインストールします。**

NuGet は、Aspose.Cells for .NET をダウンロードしてインストールする最も簡単な方法です。

1.  Microsoft Visual Studio と NuGet パッケージ マネージャーを開きます。
1.  「aspose.cells」を検索して、目的の Aspose.Cells for .NET を見つけます。
1. 「インストール」をクリックすると、Aspose.Cells for .NET がダウンロードされ、プロジェクトで参照されます。
**![インストール Aspose Cells ～ NuGet](install-through-nuget.png)**

 aspose.cells の nuget Web ページからダウンロードすることもできます。
[Aspose.Cells for .NET NuGet パッケージ](https://www.nuget.org/packages/Aspose.Cells/)

[詳細については、さらに手順を実行してください](/cells/ja/net/installation/)

### **Windows に Aspose.Cells をインストールします。**

1. 次のページから Aspose.Cells.msi をダウンロードします。
[Aspose.Cells.msi をダウンロード](https://downloads.aspose.com/cells/net/)
1. Aspose Cells msi をダブルクリックし、指示に従ってインストールします。

**![Windows に Aspose Cells をインストール](install-on-windows.png)**

[詳細については、さらに手順を実行してください](/cells/ja/net/installing-aspose-cells-on-windows/)

### **Linux に Aspose.Cells をインストールします。**

この例では、Ubuntu を使用して、Linux で Aspose.Cells の使用を開始する方法を示します。

1. 「AsposeCellsTest」という名前の .netcore アプリケーションを作成します。
2. ファイル「AsposeCellsTest.csproj」を開き、Aspose.Cells パッケージ参照用に次の行を追加します。
{{< highlight "plain" >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="22.12" />
  </ItemGroup>
{{< /highlight >}}
3. Ubuntu で VSCode を使用してプロジェクトを開きます。
**![Linux に Aspose Cells をインストール](install-on-linux.png)**
4. 次のコードでテストを実行します。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

注: .NetStandard の場合、Aspose.Cells は Linux での要件をサポートできます。

適用対象: NetStandard2.0、NetCore2.1、NetCore3.1、Net5.0、Net6.0、および高度なバージョン。

### **MAC OS に Aspose.Cells をインストール**

この例では、macOS High Sierra を使用して、MAC OS で Aspose.Cells の使用を開始する方法を示します。

1. 「AsposeCellsTest」という名前の .netcore アプリケーションを作成します。
2. Visual Studio for Mac でアプリケーションを開き、Aspose Cells から NuGet をインストールします。
**![macOS に Aspose Cells をインストール](install-on-mac-os.png)**
3. 次のコードでテストを実行します。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. 描画関連の機能を使用する必要がある場合は、macOS に libgdiplus をインストールしてください。以下を参照してください。
[macOS に libgdiplus をインストールする方法](/cells/ja/net/how-to-install-libgdiplus-in-macos/)

注: Aspose.Cells .NetStandard は、MAC OS での要件をサポートできます。

適用対象: NetStandard2.0、NetCore2.1、NetCore3.1、Net5.0、Net6.0、および高度なバージョン。

### **[Docker で Aspose Cells を実行](/cells/net/how-to-run-aspose-cells-in-docker/)**

### **Windows 以外のプラットフォームで Net6 を使用してグラフィック ライブラリを使用する方法**

Net6 の Aspose.Cells では、推奨されているように、SkiaSharp をグラフィック ライブラリとして使用するようになりました。[Microsoftの公式声明](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md) NET6 で Aspose.Cells を使用する方法の詳細については、次を参照してください。[.Net6 で Aspose.Cells を実行する方法](/cells/ja/net/how-to-run-aspose-cells-for-net6/).

## **Hello World アプリケーションの作成**

以下の手順では、Aspose.Cells API を使用して Hello World アプリケーションを作成します。

1. 免許をお持ちの方は、[それを適用する](/cells/ja/net/licensing/).
評価版を使用している場合は、ライセンス関連のコード行をスキップしてください。
1. のインスタンスを作成します[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを使用して、新しい Excel ファイルを作成するか、既存の Excel ファイルを開きます。
1. Excel ファイル内のワークシートの目的のセルにアクセスします。
1. 単語を挿入する**Hello World!**アクセスされたセルに。
1. 変更された Microsoft Excel ファイルを生成します。

上記の手順の実装は、以下の例で示されています。

### **コード サンプル: 新しいワークブックの作成**

次の例では、新しいワークブックをゼロから作成し、"Hello World!" を挿入します。最初のワークシートのセル A1 に入力し、Excel ファイルとして保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **コード サンプル: 既存のファイルを開く**

次の例では、既存の Microsoft Excel テンプレート ファイル "Sample.xlsx" を開き、"Hello World!" を挿入します。最初のワークシートのセル A1 に入力し、Excel ファイルとして保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
