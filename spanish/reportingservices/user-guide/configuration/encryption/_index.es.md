---
title: Cifrado
type: docs
weight: 40
url: /es/reportingservices/encryption/
---
Aspose.Cells for Reporting Services admite tres tipos de cifrado: XOR, CIFRADO DÉBIL y Microsoft Proveedor criptográfico fuerte. Consulte la información de configuración de cifrado en el**Aspose.Cells.ReportingServices.xml** expediente.

 Cuando el valor de Cifrado es**apagado**, Aspose.Cells for Reporting Services desactiva las funciones de cifrado.

{{< highlight "java" >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

 Cuando el valor de Cifrado es**sobre**, Aspose.Cells for Reporting Services activa el cifrado.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

Hay cuatro parámetros en la sección de cifrado:

- **Reportar nombre**: apunta a un informe que necesita cifrado. Si el parámetro se deja en blanco, todos los informes utilizan el mismo método de cifrado.
- **Clave**: establece la contraseña. No puede estar en blanco.
- **Tipo de cifrado**: establece un tipo de cifrado. No puede estar en blanco.
- **Longitud de clave**: establece la longitud de la clave. No puede estar en blanco.

{{< highlight "java" >}}

 <Encryption value="on">

  <Report name="Test" >

      <Password value="12345"/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  	  <Report name="" >

      <Password value="123456"/>

      <EncryptionType value=" XOR "/>

      <KeyLength value="128"/>

    </Report>

 </Encryption>

{{< /highlight >}}
