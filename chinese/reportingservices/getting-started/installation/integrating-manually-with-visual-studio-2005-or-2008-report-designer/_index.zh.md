---
title: 与 Visual Studio 2005 或 2008 报表设计器手动集成
type: docs
weight: 30
url: /zh/reportingservices/integrating-manually-with-visual-studio-2005-or-2008-report-designer/
---
{{% alert color="primary" %}} 

如果您想要为 Microsoft Visual Studio Report Designer 手动安装 Aspose.Cells for Reporting Services，请按顺序执行以下步骤，而不使用 MSI 安装程序。我们建议您使用 MSI 安装程序，因为它会自动执行所有必要的安装和配置。但是，如果您使用 MSI 安装程序安装失败，请遵循以下指南。
本节介绍如何在装有 Business Intelligence Development Studio 的计算机上安装 Aspose.Cells for Reporting Services。这将使您能够在设计时从 Microsoft Visual Studio 2005 或 2008 报表设计器将报表导出为 Microsoft Excel 格式。

{{% /alert %}} 
- **整合过程**
1. 复制**Aspose.Cells.ReportingServices.dll**到 Visual Studio 目录。
 1. 与 Visual Studio 2005 Report Designer 集成：复制**Aspose.Cells.ReportingServices.dll**到 C:\Program Files\Microsoft Visual Studio 8\Common7\IDE\PrivateAssemblies 目录。
 1. 与 Visual Studio 2008 Report Designer 集成：复制**Aspose.Cells.ReportingServices.dll**到 C:\Program Files\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssemblies 目录。
1. 将 Reporting Services 的 Aspose.Cells 注册为呈现扩展：
 1.打开**C:\Program Files\Microsoft Visual Studio <版本>\Common7\IDE\PrivateAssemblies\RSReportDesigner.config** 
 （在哪里<Version>对于 Visual Studio 2005 为“8”或对于 Visual Studio 2008 为“9.0”）并将以下行添加到<Render>元素：

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

1. 为 Reporting Services 授予 Aspose.Cells 执行权限：
 1.打开C:\Program Files\Microsoft Visual Studio<Version>\Common7\IDE\PrivateAssemblies\RSPreviewPolicy.config
 （在哪里<Version>对于 Visual Studio 2005 为“8”或对于 Visual Studio 2008 为“9.0”）并将以下内容添加为倒数第二个中的最后一项<CodeGroup>元素（应该是<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">): 

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

1. 验证 Reporting Services 的 Aspose.Cells 是否已成功安装：
 1. 运行或重新启动 Microsoft Visual Studio 2005 或 2008 Report Designer。
您应该注意到导出格式列表中可用的新格式。

**注册组件后，报表设计器中会出现新的导出格式** 

![待办事项：图片_替代_文本](integrating-manually-with-visual-studio-2005-or-2008-report-designer_1.png)
