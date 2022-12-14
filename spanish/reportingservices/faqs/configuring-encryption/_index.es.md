---
title: Configuración del cifrado
type: docs
weight: 40
url: /es/reportingservices/configuring-encryption/
---
{{% alert color="primary" %}} 

 Aspose.Cells para Reporting Services admite el cifrado y puede generar archivos Microsoft de Excel cifrados.

{{% /alert %}} 
### **Tipos de cifrado**
Aspose.Cells para Reporting Services admite el cifrado al exportar archivos de Excel. Admite tres tipos de cifrado:

- XOR
- CIFRADO DÉBIL
- Microsoft Proveedor criptográfico fuerte
### **Información de configuración**
 Hay información de configuración para el cifrado en el**Aspose.Cells.ReportingServices.xml** expediente. Cuando el valor de Cifrado se establece en "desactivado", Aspose.Cells.ReportingServices desactiva el cifrado.

**XML**

{{< highlight "csharp" >}}

 <Encryption value="off">

<Report name="" >

<Password value=""/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

</ Encryption >



{{< /highlight >}}

Cuando el cifrado está activado, Aspose.Cells.ReportingServices activa el cifrado.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

Hay cuatro parámetros en la sección Cifrado: ReportName, Password, EncryptionType y KeyLength.

- ReportName: establece el informe que necesita la configuración de cifrado. Un informe utiliza la misma forma de cifrado cuando el parámetro está en blanco.
- Contraseña: establece la contraseña. No se puede dejar en blanco.
- EncryptionType: establece el tipo de cifrado. No se puede dejar en blanco.
-  KeyLength: establece la longitud de la clave. No se puede dejar en blanco.

**XML**

{{< highlight "csharp" >}}

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
