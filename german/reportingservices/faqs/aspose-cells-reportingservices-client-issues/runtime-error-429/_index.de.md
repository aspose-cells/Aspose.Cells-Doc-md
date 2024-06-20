---
title: Laufzeitfehler 429
type: docs
weight: 60
url: /de/reportingservices/runtime-error-429/
---

##### **Beschreibung**
Laufzeitfehler: '429' 
ActiveX-Komponente kann Objekt nicht erstellen 
Die Zeile, die den Fehler verursacht, ist: 
Set AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient"). 
##### **Lösung**
{{% alert color="primary" %}} 

Registrieren Sie **Aspose.Cells.ReportingServices.Client.dll** erneut mit dem **Regasm.exe**-Dienstprogramm: 

1. Führen Sie cmd.exe als Administrator aus.
1. cd $(Aspose.Cells for Reporting Services installation folder).
1. Führen Sie **regasm.exe** manuell aus, um **Aspose.Cells.ReportingServices.Client.dll** zu registrieren. 

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

Bitte überprüfen Sie die Laufzeitumgebung für Ihr System. Zum Beispiel: 

- Wenn Ihr Microsoft Office x64 ist, führen Sie den Befehl aus 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

- Wenn Ihr Microsoft Office x86 ist, führen Sie den Befehl aus 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

Bitte beachten Sie das folgende Beispiel/den folgenden Befehl:

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
