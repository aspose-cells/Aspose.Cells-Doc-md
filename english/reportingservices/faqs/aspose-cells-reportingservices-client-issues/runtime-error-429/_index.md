---
title: Runtime Error 429
type: docs
weight: 60
url: /reportingservices/runtime-error-429/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

##### **Description**
Run-time error: '429' 
ActiveX component can't create object 
The line causing the error is: 
Set AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient"). 
##### **Solution**
{{% alert color="primary" %}} 

Re-register **Aspose.Cells.ReportingServices.Client.dll** using the **Regasm.exe** utility: 

1. Run cmd.exe as administrator.
1. cd $(Aspose.Cells for Reporting Services installation folder).
1. Execute **regasm.exe** to register **Aspose.Cells.ReportingServices.Client.dll** manually. 

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

Please check the running environment for your system. For example: 

- If your Microsoft Office is x64, run the command 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

- If your Microsoft Office is x86, run the command 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

Please refer to the following example/command:

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
