---
title: Firmas digitales
type: docs
weight: 50
url: /es/reportingservices/digital-signatures/
---
Aspose.Cells for Reporting Services admite firmas digitales al exportar archivos Microsoft de Excel 2007 o archivos ODS. Tenemos alguna información de configuración para firmas digitales que se puede establecer en el**Aspose.Cells.ReportingServices.xml** expediente.

 Cuando el valor de DigitalSignature es**apagado**, Aspose.Cells for Reporting Services desactiva las firmas digitales.

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

 Cuando el valor de DigitalSignature es**sobre**, Aspose.Cells for Reporting Services activa las firmas digitales.

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 Hay cuatro parámetros en la sección DigitalSignature. Estos son:

- **nombre**: representa un informe que necesita una firma digital. Cuando el parámetro se deja en blanco, los informes utilizan un archivo PFX para las firmas digitales.
- **pfxNombre de archivo**: se refiere a un archivo PFX. El nombre de archivo debe ser un nombre de archivo completamente calificado, completo con ruta y extensión de archivo. No debe estar en blanco.
- **pfxPwd**: establece la contraseña. No debe estar en blanco.
- **objetivo**: una descripción de para qué sirve la firma. Puede estar en blanco.

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
