---
title: Laufzeitfehler 429
type: docs
weight: 60
url: /de/reportingservices/runtime-error-429/
---
##### **Beschreibung**
 Laufzeitfehler: '429'
 ActiveX-Komponente kann Objekt nicht erstellen
 Die Zeile, die den Fehler verursacht, lautet:
 Legen Sie AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient") fest.
##### **Lösung**
{{% alert color="primary" %}} 

 Registrieren Sie sich neu**Aspose.Cells.ReportingServices.Client.dll** Verwendung der**Regasm.exe** Dienstprogramm:

1. Führen Sie cmd.exe als Administrator aus.
1. cd $(Aspose.Cells for Reporting Services Installationsordner).
1.  Ausführen**regasm.exe** zu registrieren**Aspose.Cells.ReportingServices.Client.dll** manuell.

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

 Bitte überprüfen Sie die Ausführungsumgebung für Ihr System. Zum Beispiel:

-  Wenn Ihr Microsoft Office x64 ist, führen Sie den Befehl aus

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

-  Wenn Ihr Microsoft Office x86 ist, führen Sie den Befehl aus

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

Bitte beachten Sie das folgende Beispiel/Befehl:

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
