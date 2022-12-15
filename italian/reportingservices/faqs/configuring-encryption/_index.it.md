---
title: Configurazione della crittografia
type: docs
weight: 40
url: /it/reportingservices/configuring-encryption/
---
{{% alert color="primary" %}} 

 Aspose.Cells for Reporting Services supporta la crittografia ed è possibile eseguire il rendering di file Microsoft Excel crittografati.

{{% /alert %}} 
### **Tipi di crittografia**
Aspose.Cells for Reporting Services supporta la crittografia durante l'esportazione di file Excel. Supporta tre tipi di crittografia:

- XOR
- CRITTOGRAFIA DEBOLE
- Provider di crittografia avanzata Microsoft
### **Informazioni sulla configurazione**
 Sono presenti informazioni di configurazione per la crittografia nel file**Aspose.Cells.ReportingServices.xml** file. Quando il valore di Encryption è impostato su "off", Aspose.Cells.ReportingServices disattiva la crittografia.

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

Quando Encryption è impostato su "on", Aspose.Cells.ReportingServices attiva la crittografia.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

Ci sono quattro parametri nella sezione Encryption: ReportName, Password, EncryptionType e KeyLength.

- ReportName: imposta il report che necessita delle impostazioni di crittografia. Un report utilizza lo stesso metodo di crittografia quando il parametro è vuoto.
- Password: imposta la password. Non può essere lasciato vuoto.
- EncryptionType – Imposta il tipo di crittografia. Non può essere lasciato vuoto.
-  KeyLength – Imposta la lunghezza della chiave. Non può essere lasciato vuoto.

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
