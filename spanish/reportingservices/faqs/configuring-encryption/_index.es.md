---
title: Configuración de encriptación
type: docs
weight: 40
url: /es/reportingservices/configuring-encryption/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services admite encriptación y es posible que pueda renderizar archivos de Microsoft Excel encriptados. 

{{% /alert %}} 
### **Tipos de encriptación**
Aspose.Cells for Reporting Services admite encriptación al exportar archivos de Excel. Admite tres tipos de encriptación:

- XOR
- ENCRIPCIÓN DÉBIL
- Proveedor Criptográfico Fuerte de Microsoft
### **Configuración de información**
Existe información de configuración para encriptación en el archivo **Aspose.Cells.ReportingServices.xml**. Cuando el valor de Encriptación se establece en "off", Aspose.Cells.ReportingServices desactiva la encriptación.

**XML**

{{< highlight csharp >}}

 <Encryption value="off">

<Report name="" >

<Password value=""/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

</ Encryption >



{{< /highlight >}}

Cuando la encriptación se establece en "on", Aspose.Cells.ReportingServices activa la encriptación.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

Hay cuatro parámetros en la sección de Encriptación: NombreInforme, Contraseña, TipoEncriptación y LongitudClave.

- NombreInforme: Establece el informe que necesita ajustes de encriptación. Un informe usa el mismo método de encriptación cuando el parámetro está en blanco.
- Contraseña: Establece la contraseña. No puede dejarse en blanco.
- TipoEncriptación: Establece el tipo de encriptación. No puede dejarse en blanco.
- LongitudClave: Establece la longitud de la clave. No puede dejarse en blanco. 

**XML**

{{< highlight csharp >}}

 <Encryption value="on">

<Report name="Test" >

<Password value="12345"/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

<Report name="" >

<Password value="123456"/>

<EncryptionType value="XOR"/>

<KeyLength value="128"/>

</Report>

</Encryption>



{{< /highlight >}}
