---
title: Crittografia
type: docs
weight: 40
url: /it/reportingservices/encryption/
---
Aspose.Cells for Reporting Services supporta tre tipi di crittografia: XOR, WEAK ENCRYPTION e Microsoft Strong Cryptographic Provider. Vedere le informazioni sulla configurazione della crittografia nel file**Aspose.Cells.ReportingServices.xml** file.

 Quando il valore di Encryption è**spento**, Aspose.Cells for Reporting Services disattiva le funzionalità di crittografia.

{{< highlight "java" >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

 Quando il valore di Encryption è**Su**, Aspose.Cells for Reporting Services attiva la crittografia.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

Ci sono quattro parametri nella sezione di crittografia:

- **ReportName**: punta a un report che necessita di crittografia. Se il parametro viene lasciato vuoto, tutti i report utilizzano lo stesso metodo di crittografia.
- **Parola d'ordine**: imposta la password. Non può essere vuoto.
- **Tipo di crittografia**: imposta un tipo di crittografia. Non può essere vuoto.
- **Lunghezza chiave**: imposta la lunghezza della chiave. Non può essere vuoto.

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
