---
title: Runtime Error 429
type: docs
weight: 60
url: /sv/reportingservices/runtime-error-429/
---

##### **Beskrivning**
Run-time error: '429' 
ActiveX-komponenten kan inte skapa objekt 
Radet som orsakar felet är: 
Set AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient"). 
##### **Lösning**
{{% alert color="primary" %}} 

Omförregistrera **Aspose.Cells.ReportingServices.Client.dll** med hjälp av verktyget **Regasm.exe**: 

1. Kör cmd.exe som administratör.
1. cd $(Aspose.Cells for Reporting Services installation folder).
1. Kör **regasm.exe** för att manuellt registrera **Aspose.Cells.ReportingServices.Client.dll**. 

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

Vänligen kontrollera körmiljön för ditt system. Exempelvis: 

- Om ditt Microsoft Office är x64, kör kommandot 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

- Om ditt Microsoft Office är x86, kör kommandot 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

Vänligen se följande exempel/kommando:

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
