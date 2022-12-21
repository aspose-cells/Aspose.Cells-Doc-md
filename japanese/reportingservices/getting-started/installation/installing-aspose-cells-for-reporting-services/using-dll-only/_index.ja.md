---
title: DLL のみを使用する
type: docs
weight: 20
url: /ja/reportingservices/using-dll-only/
---
## DLL のみを使用して Aspose.Cells for Reporting Services をインストールする方法:

- 訪問 Aspose.Cells for Reporting Services[ダウンロードページ](https://downloads.aspose.com/cells/reportingservices)をダウンロードして、**Aspose.Cells for Reporting Services (zip)**コンポーネントの最新バージョンとインストールされたドキュメントを含むアーカイブ。
 - Aspose.Cells.ReportingServices.DLLs_xx.xx.zip 内の Aspose.Cells.ReprotingSerivces.dll のバージョンは 7 種類あります。これらは、さまざまな Microsoft レポート サーバー製品をサポートしています。
 - SSRS2005 フォルダーの Aspose.Cells.ReportingServices.dll は、Microsoft SQL Server 2005 Reporting Services をサポートします。
 - SSRS2008 フォルダーの Aspose.Cells.ReportingServices.dll は、Microsoft SQL Server 2008 Reporting Services をサポートします。
 - SSRS2008R2 フォルダーの Aspose.Cells.ReportingServices.dll は、Microsoft SQL Server 2008R2/2012/2014 Reporting Services をサポートします。
 - SSRS2016 フォルダーの Aspose.Cells.ReportingServices.dll は、Microsoft SQL Server 2016/2017/2019 Reporting Services をサポートします。
   
- アーカイブをハード ドライブのディレクトリに解凍します。

- Aspose.Cells for Reporting Services レポート デザイナーをインストールします。
 - 登録**Aspose.Cells.ReportingServices.Client.dll**Regasm.exe ユーティリティを使用します。
 - Excel に Aspose.Cells for Reporting Services アドインを追加します。
   
- Microsoft SQL Server Reporting Services サービス コンポーネントの Aspose.Cells for Reporting Services をインストールします。
 - 置く**Aspose.Cells.ReportingServices.dll**${Microsoft SQL Server Reporting Services インストール フォルダー}\ReportServer\bin フォルダーに移動します。
 - Aspose.Cells for Reporting Services レンダラー拡張機能を追加:
 - 開ける**${Microsoft SQL Server Reporting Services インストール フォルダー}\ReportServer\rsreportserver.config**
 - 次の行を<Render>……</Render>エレメント：
{{< highlight "xml" >}}

 <Render>

...

<!--Start here.-->

<Extension Name="ACXLS" Type="Aspose.Cells.ReportingServices.XlsRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXLSX" Type="Aspose.Cells.ReportingServices.Excel2007XlsxRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXLSX(Data Only)" Type="Aspose.Cells.ReportingServices.Excel2007SimpleXlsxRenderer,Aspose.Cells.ReportingServices"/>

<Extension Name="ACXLSB" Type="Aspose.Cells.ReportingServices.XlsbRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXLSM" Type="Aspose.Cells.ReportingServices.Excel2007XlsmRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXML" Type="Aspose.Cells.ReportingServices.SpreadsheetMLRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACHTML" Type="Aspose.Cells.ReportingServices.HtmlRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACCSV" Type="Aspose.Cells.ReportingServices.CSVRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACODS" Type="Aspose.Cells.ReportingServices.ODSRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACTXT" Type="Aspose.Cells.ReportingServices.TabDelimitedRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXPS" Type="Aspose.Cells.ReportingServices.XpsRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACMD" Type="Aspose.Cells.ReportingServices.MarkdownRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACTIFF" Type="Aspose.Cells.ReportingServices.TIFFRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACPDF" Type="Aspose.Cells.ReportingServices.PDFRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACPNG" Type="Aspose.Cells.ReportingServices.PNGRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACJPG" Type="Aspose.Cells.ReportingServices.JPGRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACEMF" Type="Aspose.Cells.ReportingServices.EMFRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACDIF" Type="Aspose.Cells.ReportingServices.DifRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACSVG" Type="Aspose.Cells.ReportingServices.SvgRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACJSON" Type="Aspose.Cells.ReportingServices.JsonRenderer,Aspose.Cells.ReportingServices" />
<!--End here.-->

</Render>

{{< /highlight >}}
 - 実行するための Aspose.Cells for Reporting Services 権限を追加します。
 - 開ける**${Microsoft SQL Server Reporting Services インストール フォルダー}\ReportServer\rssrvpolicy.config**そして
 外側の 2 番目の最後の項目として次を追加します。<CodeGroup>要素 (これは<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. "> ): 

{{< highlight "xml" >}}

 <CodeGroup>

...

<CodeGroup>

...

<!--Start here.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust" Name="Aspose.Cells_for_Reporting_Services" Description="This code group grants full trust to the Aspose.Cells for Reporting Services assembly.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001002780c08eaa89aedfb00b1b96137cca3e15f32826e0e4fd1da3c98d1e3968a03a019aa7b7228b151f6e5dae4dcb00f98479770f507626b04e786e5e93ec3757c1cc4ed1ac4b72c7649c4438e9d3a5f44d8b7522043686a2e8c2a495e04b917e0505d3201015c828e3c15afc8a46ab78293574b9e0475df68627bbabc5b564addd" />

</CodeGroup>

<!--End here.-->

</CodeGroup>

</CodeGroup>

{{< /highlight >}}

## Aspose.Cells for Reporting Services が正常にインストールされたことを確認します。
1. レポート マネージャーを開き、レポートで使用できるエクスポート タイプのリストを確認します。 (ブラウザを開いて Report Manager を起動し、Report Manager の URL をアドレス バーに入力します。(デフォルトでは、URL は http://<ComputerName>/レポート)。
 1. サーバー上のレポートの 1 つを選択し、**フォーマットを選択**リスト。
Aspose.Cells for Reporting Services が提供するエクスポート形式のリストが表示されます。
 1. 選択**XLS – Aspose.Cells 経由の Excel ワークブック**.
 1. クリック**輸出**.
選択した形式でレポートが生成されます。
 1. クライアントに送信し、適切なアプリケーションで開きます。この場合、レポートは Microsoft Excel で開きます。

おめでとうございます。Aspose.Cells for Reporting Services が正常にインストールされ、レポートが Microsoft Excel ファイルとして生成されました。


 Aspose.Cells.ReportingServices.DLLs_xx.xx.zipの中にAspose.Cells.ReprotingSerivces.dllの7種類のバージョンがあります。これらは、さまざまな Microsoft レポート サーバー製品をサポートしています。