---
title: Errore di runtime 429
type: docs
weight: 60
url: /it/reportingservices/runtime-error-429/
---
##### **Descrizione**
Errore di runtime: '429'
 Il componente ActiveX non può creare l'oggetto
 La riga che causa l'errore è:
 Impostare AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient").
##### **Soluzione**
{{% alert color="primary" %}} 

 Registrati di nuovo**Aspose.Cells.ReportingServices.Client.dll** usando il**Regasm.exe** utilità:

1. Eseguire cmd.exe come amministratore.
1. cd $(Aspose.Cells for Reporting Services cartella di installazione).
1.  Eseguire**regasm.exe** registrare**Aspose.Cells.ReportingServices.Client.dll** manualmente.

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

 Controlla l'ambiente in esecuzione per il tuo sistema. Per esempio:

-  Se il tuo Microsoft Office è x64, esegui il comando

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

-  Se il tuo Microsoft Office è x86, esegui il comando

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

Fare riferimento al seguente esempio/comando:

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
