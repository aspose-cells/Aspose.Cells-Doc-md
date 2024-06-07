---
title: 在Visual Studio 2005或2008报表设计器中手动集成
type: docs
weight: 30
url: /zh/reportingservices/integrating-manually-with-visual-studio-2005-or-2008-report-designer/
---

{{% alert color="primary" %}} 

如果您希望在Microsoft Visual Studio报表设计器上手动安装Aspose.Cells for Reporting Services，请按照以下步骤操作。我们建议您使用MSI安装程序，因为它可以自动执行所有必要的安装和配置。但是，如果使用MSI安装程序安装失败，请按照以下指南操作。 
本部分介绍如何在具有Business Intelligence Development Studio的计算机上安装Aspose.Cells for Reporting Services。这将使您能够在Microsoft Visual Studio 2005或2008报表设计器中在设计时将报告导出到Microsoft Excel格式。 

{{% /alert %}} 
- **集成流程**
1. 将**Aspose.Cells.ReportingServices.dll**复制到Visual Studio目录。 
   1. 要与Visual Studio 2005报表设计器集成：将**Aspose.Cells.ReportingServices.dll**复制到C:\Program Files\Microsoft Visual Studio 8\Common7\IDE\PrivateAssemblies目录。
   1. 要与Visual Studio 2008报表设计器集成：将**Aspose.Cells.ReportingServices.dll**复制到C:\Program Files\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssemblies目录。
1. 将Aspose.Cells for Reporting Services注册为渲染扩展程序： 
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

1. 授予Aspose.Cells for Reporting Services执行权限： 
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

1. 验证Aspose.Cells for Reporting Services是否成功安装： 
   1. 运行或重新启动Microsoft Visual Studio 2005或2008报表设计器。
      您应该在导出格式列表中看到新的格式可用。 

**组件注册后，报表设计器中会出现新的导出格式** 

![todo:image_alt_text](integrating-manually-with-visual-studio-2005-or-2008-report-designer_1.png)
