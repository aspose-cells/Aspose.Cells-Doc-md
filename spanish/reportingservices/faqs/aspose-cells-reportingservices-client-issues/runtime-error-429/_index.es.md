---
title: Error de tiempo de ejecución 429
type: docs
weight: 60
url: /es/reportingservices/runtime-error-429/
---
##### **Descripción**
 Error en tiempo de ejecución: '429'
 El componente ActiveX no puede crear un objeto
 La línea que causa el error es:
 Establezca AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient").
##### **Solución**
{{% alert color="primary" %}} 

 volver a registrarse**Aspose.Cells.ReportingServices.Client.dll** utilizando la**Regasm.exe** utilidad:

1. Ejecute cmd.exe como administrador.
1. cd $(Aspose.Cells for Reporting Services carpeta de instalación).
1.  Ejecutar**regasm.exe** registrarse**Aspose.Cells.ReportingServices.Client.dll** a mano.

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

 Compruebe el entorno de ejecución de su sistema. Por ejemplo:

-  Si su Office Microsoft es x64, ejecute el comando

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

-  Si su Office Microsoft es x86, ejecute el comando

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

Consulte el siguiente ejemplo/comando:

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
