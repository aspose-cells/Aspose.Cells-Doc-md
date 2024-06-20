---
title: Error de tiempo de ejecución 429
type: docs
weight: 60
url: /es/reportingservices/runtime-error-429/
---

##### **Descripción**
Error de ejecución: '429' 
No se puede crear el componente ActiveX 
La línea que causa el error es: 
Set AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient"). 
##### **Solución**
{{% alert color="primary" %}} 

Vuelve a registrar **Aspose.Cells.ReportingServices.Client.dll** usando la utilidad **Regasm.exe**: 

1. Ejecuta cmd.exe como administrador.
1. cd $(Aspose.Cells for Reporting Services installation folder).
1. Ejecute **regasm.exe** para registrar **Aspose.Cells.ReportingServices.Client.dll** manualmente. 

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

Por favor, verifique el entorno de ejecución de su sistema. Por ejemplo: 

- Si su Microsoft Office es x64, ejecute el comando 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

- Si su Microsoft Office es x86, ejecute el comando 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

Por favor, consulte el siguiente ejemplo/comando:

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
