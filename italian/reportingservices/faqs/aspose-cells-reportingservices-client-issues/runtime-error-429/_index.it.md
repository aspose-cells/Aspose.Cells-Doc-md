---
title: Errore di run time 429
type: docs
weight: 60
url: /it/reportingservices/runtime-error-429/
---

##### **Descrizione**
Errore di runtime: '429' 
Impossibile creare l'oggetto componente ActiveX 
La riga che causa l'errore è: 
Set AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient"). 
##### **Soluzione**
{{% alert color="primary" %}} 

Ri-registra **Aspose.Cells.ReportingServices.Client.dll** utilizzando l'utilità **Regasm.exe**: 

1. Esegui cmd.exe come amministratore.
1. cd $(Aspose.Cells for Reporting Services installation folder).
1. Esegui **regasm.exe** per registrare manualmente **Aspose.Cells.ReportingServices.Client.dll**. 

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

Si prega di verificare l'ambiente di esecuzione per il tuo sistema. Ad esempio: 

- Se il tuo Microsoft Office è x64, esegui il comando 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

- Se il tuo Microsoft Office è x86, esegui il comando 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

Si prega di fare riferimento all'esempio/comando seguente:

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
