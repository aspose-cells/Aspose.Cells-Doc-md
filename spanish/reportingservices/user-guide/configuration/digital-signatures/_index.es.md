---
title: Firmas digitales
type: docs
weight: 50
url: /es/reportingservices/digital-signatures/
---

Aspose.Cells for Reporting Services admite firmas digitales al exportar archivos de Microsoft Excel 2007 o archivos ODS. Tenemos alguna información de configuración para firmas digitales que se pueden establecer en el archivo **Aspose.Cells.ReportingServices.xml**.

Cuando el valor de DigitalSignature es **apagado**, Aspose.Cells for Reporting Services desactiva las firmas digitales.

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

Cuando el valor de DigitalSignature es **encendido**, Aspose.Cells for Reporting Services activa las firmas digitales.

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

Hay cuatro parámetros en la sección de DigitalSignature. Estos son: 

- **nombre**: representa un informe que necesita una firma digital. Cuando el parámetro se deja en blanco, los informes utilizan un archivo PFX para las firmas digitales.
- **pfxFilename**: se refiere a un archivo PFX. El nombre de archivo debe ser un nombre completo calificado, completo con la ruta y la extensión del archivo. No debe estar en blanco.
- **pfxPwd**: establece la contraseña. No debe estar en blanco.
- **propósito**: una descripción de para qué es la firma. Puede estar en blanco.

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
