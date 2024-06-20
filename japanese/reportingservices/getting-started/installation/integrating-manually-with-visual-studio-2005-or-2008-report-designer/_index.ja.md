---
title: Visual Studio 2005または2008レポートデザイナと手動で統合
type: docs
weight: 30
url: /ja/reportingservices/integrating-manually-with-visual-studio-2005-or-2008-report-designer/
---

{{% alert color="primary" %}} 

次の手順を実行して、MSIインストーラを使用せずにMicrosoft Visual StudioレポートデザイナのためにAspose.Cells for Reporting Servicesを手動でインストールする場合に実行してください。MSIインストーラを使用することをお勧めしますが、MSIインストーラでインストールに失敗した場合は、以下のガイドラインに従ってください。 
このセクションでは、Business Intelligence Development Studioを使用したコンピューターにAspose.Cells for Reporting Servicesをインストールする方法について説明します。これにより、Microsoft Visual Studio 2005または2008レポートデザイナから、デザイン時にレポートをMicrosoft Excel形式でエクスポートできるようになります。 

{{% /alert %}} 
- 統合プロセス
1. **Aspose.Cells.ReportingServices.dll**をVisual Studioディレクトリにコピーします。 
   1. Visual Studio 2005レポートデザイナと統合するには：**Aspose.Cells.ReportingServices.dll**をC:\Program Files\Microsoft Visual Studio 8\Common7\IDE\PrivateAssembliesディレクトリにコピーしてください。
   1. Visual Studio 2008レポートデザイナと統合するには：**Aspose.Cells.ReportingServices.dll**をC:\Program Files\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssembliesディレクトリにコピーしてください。
1. レンダリング拡張としてAspose.Cells for Reporting Servicesを登録します： 
   1. Open **C:\Program Files\Microsoft Visual Studio <Version>\Common7\IDE\PrivateAssemblies\ RSReportDesigner.config** 
      (where <Version> is “8” for Visual Studio 2005 or “9.0” for Visual Studio 2008) and add the following lines into the <Render> element: 

**XML**

{{< highlight csharp >}}

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

1. Aspose.Cells for Reporting Servicesに実行権限を与えます： 
   1. Open C:\Program Files\Microsoft Visual Studio <Version>\Common7\IDE\PrivateAssemblies\RSPreviewPolicy.config
      (where <Version> is “8” for Visual Studio 2005 or “9.0” for Visual Studio 2008) and add the following as the last item in the second to outer <CodeGroup> element (which should be <CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">): 

**XML**

{{< highlight csharp >}}

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

1. Aspose.Cells for Reporting Servicesが正常にインストールされたことを確認します： 
   1. Microsoft Visual Studio 2005または2008レポートデザイナを実行または再起動します。
      エクスポート形式のリストで新しい形式が利用可能になったことに気付くはずです。 

コンポーネントが登録されると、レポートデザイナに新しいエクスポート形式が表示されます。 

![todo:image_alt_text](integrating-manually-with-visual-studio-2005-or-2008-report-designer_1.png)
