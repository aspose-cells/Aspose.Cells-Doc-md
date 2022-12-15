---
title: 仅使用 DLL
type: docs
weight: 20
url: /zh/reportingservices/using-dll-only/
---
## 如何仅使用 DLL 安装 Aspose.Cells for Reporting Services：

- 参观 Aspose.Cells for Reporting Services[下载页面](https://downloads.aspose.com/cells/reportingservices)并下载**Aspose.Cells for Reporting Services（邮编）**包含最新版本组件和已安装文档的存档。
 - Aspose.Cells.ReportingServices.DLLs_xx.xx.zip中有7种版本Aspose.Cells.ReprotingSerivces.dll。它们支持不同的 Microsoft 报表服务器产品。
 - SSRS2005 文件夹中的 Aspose.Cells.ReportingServices.dll 支持 Microsoft SQL Server 2005 Reporting Services。
 - SSRS2008 文件夹中的 Aspose.Cells.ReportingServices.dll 支持 Microsoft SQL Server 2008 Reporting Services。
 - SSRS2008R2 文件夹中的 Aspose.Cells.ReportingServices.dll 支持 Microsoft SQL Server 2008R2/2012/2014 Reporting Services。
 - SSRS2016 文件夹中的 Aspose.Cells.ReportingServices.dll 支持 Microsoft SQL Server 2016/2017/2019 Reporting Services。
   
- 将存档解压缩到硬盘驱动器上的目录中。

- 安装 Aspose.Cells for Reporting Services 报表设计器：
 - 登记**Aspose.Cells.ReportingServices.Client.dll**使用 Regasm.exe 实用程序。
 - 添加 Aspose.Cells for Reporting Services Excel 插件。
   
- 为 Microsoft SQL Server Reporting Services 安装 Aspose.Cells for Reporting Services 服务组件：
 - 放在**Aspose.Cells.ReportingServices.dll**进入 ${Microsoft SQL Server Reporting Services 安装文件夹}\ReportServer\bin 文件夹。
 - 添加 Aspose.Cells for Reporting Services 渲染器扩展：
 - 打开**${Microsoft SQL Server Reporting Services 安装文件夹}\ReportServer\rsreportserver.config**
 - 将以下行添加到<Render>……</Render>元素：
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
 - 添加Aspose.Cells for Reporting Services权限执行：
 - 打开**${Microsoft SQL Server Reporting Services 安装文件夹}\ReportServer\rssrvpolicy.config**和一个
 将以下内容作为第二个中的最后一项添加到外部<CodeGroup>元素（应该是<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. "> ): 

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

## 验证Aspose.Cells for Reporting Services是否安装成功：
1. 打开报告管理器并检查报告的可用导出类型列表。 （通过打开浏览器启动 Report Manager，然后在地址栏中键入 Report Manager URL。（默认情况下，URL 为 http://<ComputerName>/报告）。
 1. 选择服务器上的一份报告并打开**选择格式**列表。
您应该看到 Aspose.Cells for Reporting Services 提供的导出格式列表。
1. 选择**XLS – Excel 工作簿来自 Aspose.Cells**.
 1.点击**出口**.
报告以选定的格式生成。
 1. 将其发送给客户并在适当的应用程序中打开它。在这种情况下，报表将在 Microsoft Excel 中打开。

恭喜，您已成功安装 Aspose.Cells for Reporting Services 并生成了一份 Microsoft Excel 文件格式的报告！


 Aspose.Cells.ReportingServices.DLLs_xx.xx.zip中有7种版本Aspose.Cells.ReprotingSerivces.dll。它们支持不同的 Microsoft 报表服务器产品。