---
title: Soporte para Firmas Digitales
type: docs
weight: 70
url: /es/reportingservices/support-for-digital-signatures/
---

{{% alert color="primary" %}} 

Una firma digital proporciona la seguridad de que un libro de trabajo es válido y que nadie lo ha alterado. Adjuntar una firma digital es similar a sellar un sobre. Si un sobre llega sellado, tiene cierto nivel de seguridad de que nadie ha manipulado su contenido. 

Puede crear una firma digital personal utilizando el Microsoft Selfcert.exe o cualquier otra herramienta, o puede comprar una firma digital. Para firmar una hoja de cálculo, adjunte una firma a sus libros de trabajo una vez que haya creado una firma digital. 

Aspose.Cells for Reporting Services admite firmas digitales. 

{{% /alert %}} 
### **Trabajando con Firmas Digitales**
#### **Formatos Excel Soportados para Firmas Digitales**
Aspose.Cells for Reporting Services admite firmas digitales al exportar a los formatos de Excel 2007 y ODS.
#### **Configuración de Firmas Digitales**
The **Aspose.Cells.ReportingServices.xml** file holds the configuration information and text of a digital signature in the <DigitalSignature> tag:

- Cuando DigitalSignature está desactivado, Aspose.Cells for Reporting Services desactiva la funcionalidad de firma digital.
  Por ejemplo: 

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- Cuando el valor de DigitalSignature está activado, Aspose.Cells.ReportingServices activa la funcionalidad de firma digital.
  Por ejemplo: 

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

Hay cuatro parámetros en la sección de Firma Digital. Estos son: 

- name - Apunta a un informe que necesita una firma digital. El informe utiliza un archivo PFX para la firma digital cuando el parámetro está en blanco.
- pfxFilename – Apunta al archivo PFX. El nombre de archivo debe ser un nombre completo. No se puede establecer en un valor en blanco.
- pfxPwd – Establece la contraseña. No se puede dejar en blanco.
- purpose – Explica el propósito de la firma. Puede estar en blanco.
  Por ejemplo: 

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
