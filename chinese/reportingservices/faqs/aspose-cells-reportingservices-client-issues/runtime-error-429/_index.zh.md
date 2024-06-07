---
title: 运行时错误 429
type: docs
weight: 60
url: /zh/reportingservices/runtime-error-429/
---

##### **描述**
运行时错误：'429' 
ActiveX 组件无法创建对象 
导致错误的行是： 
Set AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient")。 
##### **解决方案**
{{% alert color="primary" %}} 

使用 **Regasm.exe** 实用程序重新注册 **Aspose.Cells.ReportingServices.Client.dll**： 

1. 以管理员身份运行 cmd.exe。
1. cd $(Aspose.Cells for Reporting Services安装文件夹)。
1. 手动执行 **regasm.exe** 注册 **Aspose.Cells.ReportingServices.Client.dll**。 

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

请检查系统的运行环境。例如： 

- 如果您的 Microsoft Office 是 x64 版本，请运行命令 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

- 如果您的 Microsoft Office 是 x86 版本，请运行命令 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

请参考以下示例/命令：

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
