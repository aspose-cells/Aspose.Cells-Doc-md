---
title: はじめる
type: docs
weight: 10
url: /ja/net/getting-started/
---
{{% alert color="primary" %}} 

このページでは、Aspose Cells をインストールし、Hello World アプリケーションを作成する方法を説明します。

{{% /alert %}}

##  **インストール**

###  **Aspose.Cells ～ NuGet をインストールします**

NuGet は、Aspose.Cells for .NET をダウンロードしてインストールする最も簡単な方法です。

1. Microsoft Visual Studio および NuGet パッケージ マネージャーを開きます。
1.  「aspose.cells」を検索して、目的の Aspose.Cells for .NET を見つけます。
1. 「インストール」をクリックすると、Aspose.Cells for .NET がダウンロードされ、プロジェクト内で参照されます。
**![Aspose Cells ～ NuGet をインストール](install-through-nuget.png)**

 aspose.cells の Web ページ nuget からダウンロードすることもできます。
[Aspose.Cells for .NET NuGet パッケージ](https://www.nuget.org/packages/Aspose.Cells/)

[詳細については、さらなるステップをご覧ください](/cells/ja/net/installation/)

###  **Aspose.Cells を Windows にインストールする**

1. 次のページから Aspose.Cells.msi をダウンロードします。
[Aspose.Cells.msiをダウンロード](https://downloads.aspose.com/cells/net/)
1. Aspose Cells msi をダブルクリックし、指示に従ってインストールします。

**![Aspose Cells を Windows にインストール](install-on-windows.png)**

[詳細については、さらなるステップをご覧ください](/cells/ja/net/installing-aspose-cells-on-windows/)

###  **Linux に Aspose.Cells をインストールする**

この例では、Ubuntu を使用して、Linux 上で Aspose.Cells の使用を開始する方法を示します。

1. 「AsposeCellsTest」という名前の .netcore アプリケーションを作成します。
2. ファイル「AsposeCellsTest.csproj」を開き、Aspose.Cells パッケージ参照として次の行を追加します。
{{< highlight "plain" >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="24.3" />
  </ItemGroup>
{{< /highlight >}}
3. Ubuntu 上の VSCode でプロジェクトを開きます。
**![Aspose Cells を Linux にインストール](install-on-linux.png)**
4. 次のコードでテストを実行します。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

注: Aspose.Cells .NetStandard の場合、Linux 上の要件をサポートできます。

適用対象: NetStandard2.0、NetCore2.1、NetCore3.1、Net5.0、Net6.0 およびアドバンスト バージョン。

###  **Aspose.Cells を MAC OS にインストールする**

この例では、macOS High Sierra を使用して、MAC OS で Aspose.Cells の使用を開始する方法を示します。

1. 「AsposeCellsTest」という名前の .netcore アプリケーションを作成します。
2. Visual Studio for Mac でアプリケーションを開き、Aspose Cells ～ NuGet をインストールします。
**![macOS に Aspose Cells をインストール](install-on-mac-os.png)**
3. 次のコードでテストを実行します。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. 描画関連の機能を使用する必要がある場合は、macOS に libgdiplus をインストールしてください。次を参照してください。
[macOS に libgdiplus をインストールする方法](/cells/ja/net/how-to-install-libgdiplus-in-macos/)

注: Aspose.Cells .NetStandard の場合、MAC OS 上の要件をサポートできます。

適用対象: NetStandard2.0、NetCore2.1、NetCore3.1、Net5.0、Net6.0 およびアドバンスト バージョン。

###  **[Docker で Aspose Cells を実行](/cells/net/how-to-run-aspose-cells-in-docker/)**

###  **Net6 を使用して Windows 以外のプラットフォームでグラフィックス ライブラリを使用する方法**

Net6 の Aspose.Cells は、で推奨されているように、グラフィックス ライブラリとして SkiaSharp を使用するようになりました。[Microsoftの公式声明](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md)。 NET6 での Aspose.Cells の使用の詳細については、次を参照してください。[.Net6 で Aspose.Cells を実行する方法](/cells/ja/net/how-to-run-aspose-cells-for-net6/).

##  **Hello World アプリケーションの作成**

以下の手順では、Aspose.Cells API を使用して Hello World アプリケーションを作成します。

1. 免許をお持ちであれば、[それを適用してください](/cells/ja/net/licensing/).
評価版を使用している場合は、ライセンス関連のコード行をスキップしてください。
1. のインスタンスを作成します。[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを使用して新しい Excel ファイルを作成するか、既存の Excel ファイルを開きます。
1. Excel ファイル内のワークシートの任意のセルにアクセスします。
1. 言葉を挿入する**Hello World!**アクセスされたセルに。
1. 変更した Microsoft Excel ファイルを生成します。

上記のステップの実装を以下の例で示します。

###  **コードサンプル: 新しいワークブックの作成**

次の例では、新しいワークブックを最初から作成し、「Hello World!」を挿入します。最初のワークシートのセル A1 にコピーし、Excel ファイルとして保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **コードサンプル: 既存のファイルを開く**

次の例では、既存の Microsoft Excel テンプレート ファイル「Sample.xlsx」を開き、「Hello World!」を挿入します。最初のワークシートのセル A1 にコピーし、Excel ファイルとして保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
