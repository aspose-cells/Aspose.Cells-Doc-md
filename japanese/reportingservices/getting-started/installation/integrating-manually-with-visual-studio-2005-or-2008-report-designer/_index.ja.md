---
title: Visual Studio 2005 または 2008 Report Designer との手動統合
type: docs
weight: 30
url: /ja/reportingservices/integrating-manually-with-visual-studio-2005-or-2008-report-designer/
---
{{% alert color="primary" %}} 

MSI インストーラーを使用せずに、Microsoft Visual Studio Report Designer に対して Aspose.Cells for Reporting Services を手動でインストールする場合は、次の手順を順番に実行してください。必要なすべてのインストールと構成が自動的に実行されるため、MSI インストーラーを使用することをお勧めします。ただし、MSI インストーラーでのインストールに失敗した場合は、次のガイドラインに従ってください。
このセクションでは、Business Intelligence Development Studio を使用してコンピューターに Aspose.Cells for Reporting Services をインストールする方法について説明します。これにより、設計時に Microsoft Visual Studio 2005 または 2008 Report Designer からレポートを Microsoft Excel 形式にエクスポートできます。

{{% /alert %}} 
- **統合プロセス**
1. コピー**Aspose.Cells.ReportingServices.dll**Visual Studio ディレクトリに。
 1. Visual Studio 2005 Report Designer と統合するには:**Aspose.Cells.ReportingServices.dll** C:\Program Files\Microsoft Visual Studio 8\Common7\IDE\PrivateAssemblies ディレクトリに移動します。
 1. Visual Studio 2008 Report Designer と統合するには:**Aspose.Cells.ReportingServices.dll**C:\Program Files\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssemblies ディレクトリにコピーします。
1.  Aspose.Cells for Reporting Services を表示拡張機能として登録します。
 1.開く**C:\Program Files\Microsoft Visual Studio <バージョン>\Common7\IDE\PrivateAssemblies\ RSReportDesigner.config** 
 （どこ<Version>Visual Studio 2005 の場合は「8」、Visual Studio 2008 の場合は「9.0」です)、次の行を<Render>エレメント：

**XML**

{{< highlight "csharp" >}}

 <Extension Name="ACXLS" Type="Aspose.Cells.ReportingServices.XlsRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACXLSX" Type="Aspose.Cells.ReportingServices.Excel2007XlsxRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACXLSB" Type="Aspose.Cells.ReportingServices.XlsbRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACXLSM" Type="Aspose.Cells.ReportingServices.Excel2007XlsmRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACXML" Type="Aspose.Cells.ReportingServices.SpreadsheetMLRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACHTML" Type="Aspose.Cells.ReportingServices.HtmlRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACCSV" Type="Aspose.Cells.ReportingServices.CSVRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACODS" Type="Aspose.Cells.ReportingServices.ODSRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACTXT" Type="Aspose.Cells.ReportingServices.TabDelimitedRenderer,Aspose.Cells.ReportingServices" />



{{< /highlight >}}

1. Aspose.Cells for Reporting Services に実行権限を与えます:
 1. C:\Program Files\Microsoft Visual Studio を開きます<Version>\Common7\IDE\PrivateAssemblies\RSPreviewPolicy.config
 （どこ<Version>は、Visual Studio 2005 の場合は「8」、Visual Studio 2008 の場合は「9.0」です)、outer の 2 番目の最後の項目として次を追加します。<CodeGroup>要素 (これは<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">): 

**XML**

{{< highlight "csharp" >}}

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

1.  Aspose.Cells for Reporting Services が正常にインストールされたことを確認します。
 1. Microsoft Visual Studio 2005 または 2008 Report Designer を実行または再起動します。
エクスポート形式のリストで利用可能な新しい形式に気付くはずです。

**コンポーネントが登録されると、新しいエクスポート形式がレポート デザイナーに表示されます** 

![todo:画像_代替_文章](integrating-manually-with-visual-studio-2005-or-2008-report-designer_1.png)
