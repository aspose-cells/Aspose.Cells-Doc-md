---
title: 运行时错误 429
type: docs
weight: 60
url: /zh/reportingservices/runtime-error-429/
---

##### **描述**
运行时错误: '429' 
无法创建ActiveX组件 
导致错误的行是: 
Set AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient")。 
##### **Solution**
{{% alert color="primary" %}} 

使用**Regasm.exe**实用程序重新注册**Aspose.Cells.ReportingServices.Client.dll**: 

1. 以管理员身份运行cmd.exe。
1. 切换到$(Aspose.Cells for Reporting Services安装文件夹)。
1. 手动执行**regasm.exe**注册**Aspose.Cells.ReportingServices.Client.dll**。 

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

请检查系统运行环境。例如: 

- 如果你的 Microsoft Office 是 x64，运行以下命令 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

- 如果你的 Microsoft Office 是 x86，运行以下命令 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

请参考以下示例/命令:

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
