---
title: Crittografia
type: docs
weight: 40
url: /it/reportingservices/encryption/
---

Aspose.Cells for Reporting Services supporta tre tipi di crittografia: XOR, CRITTOGRAFIA DEBOLE e Microsoft Strong Cryptographic Provider. Consultare le informazioni di configurazione della crittografia nel file **Aspose.Cells.ReportingServices.xml**.

Quando il valore della crittografia è **off**, Aspose.Cells for Reporting Services disattiva le funzionalità di crittografia.

{{< highlight java >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

Quando il valore della crittografia è **on**, Aspose.Cells for Reporting Services attiva la crittografia.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

Nella sezione sulla crittografia ci sono quattro parametri:

- **ReportName**: punta a un report che richiede crittografia. Se il parametro è lasciato in bianco, tutti i report utilizzano lo stesso metodo di crittografia.
- **Password**: imposta la password. Non può essere in bianco.
- **EncryptionType**: imposta un tipo di crittografia. Non può essere in bianco.
- **KeyLength**: imposta la lunghezza chiave. Non può essere in bianco.

{{< highlight java >}}

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
