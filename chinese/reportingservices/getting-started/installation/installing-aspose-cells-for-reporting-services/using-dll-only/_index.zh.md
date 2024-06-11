---
title: 仅使用 DLL
type: docs
weight: 20
url: /zh/reportingservices/using-dll-only/
---

## 如何仅使用 DLL 安装 Aspose.Cells for Reporting Services：

- 访问 Aspose.Cells for Reporting Services [下载页面](https://downloads.aspose.com/cells/reportingservices)，并下载包含最新版本组件和安装文档的 **Aspose.Cells for Reporting Services (zip)** 归档文件。
   - Aspose.Cells.ReportingServices.DLLs_xx.xx.zip 中包含 7 种版本的 Aspose.Cells.ReprotingSerivces.dll，支持不同的 Microsoft 报表服务器产品。
       - 在 SSRS2005 文件夹中的 Aspose.Cells.ReportingServices.dll 支持 Microsoft SQL Server 2005 Reporting Services。
       - 在 SSRS2008 文件夹中的 Aspose.Cells.ReportingServices.dll 支持 Microsoft SQL Server 2008 Reporting Services。
       - 在 SSRS2008R2 文件夹中的 Aspose.Cells.ReportingServices.dll 支持 Microsoft SQL Server 2008R2/2012/2014 Reporting Services。
       - 在 SSRS2016 文件夹中的 Aspose.Cells.ReportingServices.dll 支持 Microsoft SQL Server 2016/2017/2019 Reporting Services。

- 将归档文件解压缩到硬盘上的一个目录中。

- 安装 Aspose.Cells for Reporting Services 报表设计器：
   - 使用 Regasm.exe 实用程序注册 **Aspose.Cells.ReportingServices.Client.dll**。
   - 在 Excel 中添加 Aspose.Cells for Reporting Services 插件。

- 安装 Aspose.Cells for Reporting Services 用于 Microsoft SQL Server Reporting Services 服务组件：
   - 将 **Aspose.Cells.ReportingServices.dll** 放入 ${Microsoft SQL Server Reporting Services安装目录}\ReportServer\bin文件夹。 
   - 添加 Aspose.Cells for Reporting Services 渲染扩展：  
      - 打开 **${Microsoft SQL Server Reporting Services安装目录}\ReportServer\rsreportserver.config**
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
   - 添加 Aspose.Cells for Reporting Services 权限以执行：
      - 打开 **${Microsoft SQL Server Reporting Services安装目录}\ReportServer\rssrvpolicy.config** 和 a
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

## 验证Aspose.Cells for Reporting Services是否安装成功：
   1. Open the Report Manager and check the list of available export types for a report. (Launch Report Manager by opening a browser and type the Report Manager URL into the address bar. (By default, the URL is http://<ComputerName>/Reports).
   1. 选择服务器上的报告之一，并打开**选择格式**列表。
      您应该看到Aspose.Cells为Reporting Services提供的导出格式列表。
   1. 选择**XLS - 通过Aspose.Cells生成的Excel工作簿**。
   1. 点击**导出**。
      报告以所选格式生成。
   1. 发送给客户并在适当的应用程序中打开。在本例中，报告在 Microsoft Excel 中打开。

恭喜，您已成功安装了Aspose.Cells for Reporting Services并生成了以Microsoft Excel文件形式的报告！


Aspose.Cells.ReportingServices.DLLs_xx.xx.zip 中有7种版本的 Aspose.Cells.ReprotingSerivces.dll。它们支持不同的 Microsoft 报告服务器产品。 
