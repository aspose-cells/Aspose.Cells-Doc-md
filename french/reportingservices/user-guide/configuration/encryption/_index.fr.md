---
title: Chiffrement
type: docs
weight: 40
url: /fr/reportingservices/encryption/
---

Aspose.Cells for Reporting Services prend en charge trois types de chiffrement : XOR, WEAK ENCRYPTION et Microsoft Strong Cryptographic Provider. Voir les informations de configuration de chiffrement dans le fichier **Aspose.Cells.ReportingServices.xml**.

Lorsque la valeur de Encryption est **off**, Aspose.Cells for Reporting Services désactive les fonctionnalités de chiffrement.

{{< highlight java >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

Lorsque la valeur du chiffrement est **activée**, Aspose.Cells for Reporting Services active le chiffrement.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

Il y a quatre paramètres dans la section chiffrement:

- **ReportName**: pointe vers un rapport qui nécessite un chiffrement. Si le paramètre est laissé en blanc, tous les rapports utilisent la même méthode de chiffrement.
- **Mot de passe**: définit le mot de passe. Ne peut pas être laissé en blanc.
- **Type de chiffrement**: définit un type de chiffrement. Ne peut pas être laissé en blanc.
- **Longueur de la clé**: définit la longueur de la clé. Ne peut pas être laissé en blanc.

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
