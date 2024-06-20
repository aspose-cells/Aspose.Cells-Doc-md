---
title: DLLのみを使用
type: docs
weight: 20
url: /ja/reportingservices/using-dll-only/
---

## Aspose.Cells for Reporting ServicesのみをDLLでインストールする方法:

- Aspose.Cells for Reporting Services [ダウンロードページ](https://downloads.aspose.com/cells/reportingservices)を訪れ、最新バージョンのコンポーネントとインストール済みドキュメントが含まれる**Aspose.Cells for Reporting Services (zip)**アーカイブをダウンロードします。
   - Aspose.Cells.ReportingServices.DLLs_xx.xx.zipには7種類のバージョンのAspose.Cells.ReprotingSerivces.dllが含まれています。これらは異なるMicrosoftリポートサーバー製品をサポートしています。
       - SSRS2005フォルダーのAspose.Cells.ReportingServices.dllはMicrosoft SQL Server 2005 Reporting Servicesをサポートしています。
       - SSRS2008フォルダーのAspose.Cells.ReportingServices.dllはMicrosoft SQL Server 2008 Reporting Servicesをサポートしています。
       - SSRS2008R2フォルダーのAspose.Cells.ReportingServices.dllはMicrosoft SQL Server 2008R2/2012/2014 Reporting Servicesをサポートしています。
       - SSRS2016フォルダーのAspose.Cells.ReportingServices.dllはMicrosoft SQL Server 2016/2017/2019 Reporting Servicesをサポートしています。

- アーカイブをハードドライブ上のディレクトリに展開します。

- Aspose.Cells for Reporting Servicesレポートデザイナーをインストールします:
   - Regasm.exeユーティリティを使用して**Aspose.Cells.ReportingServices.Client.dll**を登録します。
   - ExcelにAspose.Cells for Reporting Servicesアドインを追加します。

- Microsoft SQL Server Reporting ServicesのAspose.Cells for Reporting Servicesサービスコンポーネントをインストールします:
   - **Aspose.Cells.ReportingServices.dll**を${Microsoft SQL Server Reporting Servicesインストールフォルダー}\ReportServer\binフォルダーに入れます。 
   - Aspose.Cells for Reporting Servicesのレンダラーエクステンションを追加します:  
      - **${Microsoft SQL Server Reporting Servicesインストールフォルダー}\ReportServer\rsreportserver.config**を開きます。
      - Add the following lines into the <Render>……</Render> element: 
{{< highlight xml >}}

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
   - Aspose.Cells for Reporting Servicesの実行権限を追加します:
      - **${Microsoft SQL Server Reporting Servicesのインストールフォルダー}\ReportServer\rssrvpolicy.config** を開きます。
      - Add the following as the last item in the second to the outer <CodeGroup> element (which should be <CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. "> ): 

{{< highlight xml >}}

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

## Aspose.Cells for Reporting Services が正常にインストールされたことを確認します:
   1. Open the Report Manager and check the list of available export types for a report. (Launch Report Manager by opening a browser and type the Report Manager URL into the address bar. (By default, the URL is http://<ComputerName>/Reports).
   1. サーバー上のレポートのいずれかを選択して、**フォーマットの選択**リストを開きます。
      Aspose.Cells for Reporting Services が提供するエクスポート形式のリストが表示されるはずです。
   1. **XLS – Aspose.Cells を使用して Excel ワークブック** を選択します。
   1. **エクスポート** をクリックします。
      選択した形式でレポートが生成されます。
   1. クライアントに送信し、適切なアプリケーションで開きます。この場合、レポートは Microsoft Excel で開きます。

おめでとうございます。Aspose.Cells for Reporting Services を正常にインストールし、Microsoft Excel ファイルとしてレポートを生成しました!


Aspose.Cells.ReportingServices.DLLs_xx.xx.zip には7種類の Aspose.Cells.ReprotingSerivces.dll のバージョンが含まれています。これらは異なるMicrosoftレポートサーバー製品をサポートしています。 
