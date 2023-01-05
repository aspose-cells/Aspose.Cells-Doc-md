---
title: Runtime Error 429
type: docs
weight: 60
url: /sv/reportingservices/runtime-error-429/
---
##### **Beskrivning**
 Körtidsfel: '429'
 ActiveX-komponenten kan inte skapa objekt
 Raden som orsakar felet är:
 Ställ in AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient").
##### **Lösning**
{{% alert color="primary" %}} 

 Omregistrera dig**Aspose.Cells.ReportingServices.Client.dll** använda**Regasm.exe** verktyg:

1. Kör cmd.exe som administratör.
1. cd $(Aspose.Cells for Reporting Services installationsmapp).
1.  Kör**regasm.exe** att registrera**Aspose.Cells.ReportingServices.Client.dll** manuellt.

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

 Kontrollera körmiljön för ditt system. Till exempel:

-  Om ditt Microsoft Office är x64, kör kommandot

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

-  Om ditt Microsoft Office är x86, kör kommandot

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

Se följande exempel/kommando:

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
