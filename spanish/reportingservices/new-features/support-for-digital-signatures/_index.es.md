---
title: Soporte para firmas digitales
type: docs
weight: 70
url: /es/reportingservices/support-for-digital-signatures/
---
{{% alert color="primary" %}} 

Una firma digital garantiza que un libro de trabajo es válido y que nadie lo ha alterado. Adjuntar una firma digital es similar a sellar un sobre. Si un sobre llega sellado, tiene cierto nivel de seguridad de que nadie ha manipulado su contenido.

 Puede crear una firma digital personal utilizando Microsoft Selfcert.exe o cualquier otra herramienta, o puede comprar una firma digital. Para firmar una hoja de cálculo, adjunte una firma a sus libros de trabajo una vez que haya creado una firma digital.

 Aspose.Cells for Reporting Services admite firmas digitales.

{{% /alert %}} 
### **Trabajar con firmas digitales**
#### **Formatos de Excel admitidos para firmas digitales**
Aspose.Cells for Reporting Services admite firmas digitales al exportar a formatos de archivo Excel 2007 y ODS.
#### **Configuración de firmas digitales**
 Él**Aspose.Cells.ReportingServices.xml** El archivo contiene la información de configuración y el texto de una firma digital en el<DigitalSignature> etiqueta:

- Cuando DigitalSignature está desactivado, Aspose.Cells for Reporting Services desactiva la función de firma digital.
Por ejemplo:

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- Cuando el valor de DigitalSignature está activado, Aspose.Cells.ReportingServices activa la funcionalidad de la firma digital.
Por ejemplo:

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 Hay cuatro parámetros en la sección DigitalSignature. Estos son :

- nombre: apunta a un informe que necesita una firma digital. El informe utiliza un archivo PFX para la firma digital cuando el parámetro está en blanco.
- pfxFilename: apunta al archivo PFX. El nombre de archivo debe ser un nombre de archivo completo. No se puede establecer en un valor en blanco.
- pfxPwd: establece la contraseña. No se puede dejar en blanco.
- Propósito: explica el propósito de la firma. Puede estar en blanco.
Por ejemplo:

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
