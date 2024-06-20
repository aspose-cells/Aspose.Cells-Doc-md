---
title: Configurazione della crittografia
type: docs
weight: 40
url: /it/reportingservices/configuring-encryption/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services supporta la crittografia e è possibile rendere crittografati i file di Microsoft Excel. 

{{% /alert %}} 
### **Tipi di crittografia**
Aspose.Cells for Reporting Services supporta la crittografia durante l'esportazione dei file Excel. Supporta tre tipi di crittografia:

- XOR
- CRITTOGRAFIA DEBOLE
- Provider crittografico Microsoft Strong
### **Configurazione delle informazioni**
Nel file **Aspose.Cells.ReportingServices.xml** sono presenti informazioni di configurazione per la crittografia. Quando il valore della crittografia è impostato su "off", Aspose.Cells.ReportingServices disattiva la crittografia.

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

Quando la crittografia è impostata su "on", Aspose.Cells.ReportingServices attiva la crittografia.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

Nella sezione Crittografia ci sono quattro parametri: NomeReport, Password, TipoCrittografia e LunghezzaChiave.

- NomeReport – Imposta il report che necessita delle impostazioni di crittografia. Un report utilizza lo stesso tipo di crittografia quando il parametro è vuoto.
- Password – Imposta la password. Non può essere lasciata vuota.
- TipoCrittografia – Imposta il tipo di crittografia. Non può essere lasciato vuoto.
- LunghezzaChiave – Imposta la lunghezza della chiave. Non può essere lasciata vuota. 

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
