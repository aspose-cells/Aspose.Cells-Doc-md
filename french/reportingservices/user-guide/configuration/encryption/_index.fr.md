---
title: Chiffrement
type: docs
weight: 40
url: /fr/reportingservices/encryption/
---
Aspose.Cells for Reporting Services prend en charge trois types de chiffrement : XOR, WEAK ENCRYPTION et Microsoft Strong Cryptographic Provider. Consultez les informations de configuration du chiffrement dans le**Aspose.Cells.ReportingServices.xml** dossier.

 Lorsque la valeur de Chiffrement est**à l'arrêt**, Aspose.Cells for Reporting Services désactive les fonctionnalités de cryptage.

{{< highlight "java" >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

 Lorsque la valeur de Chiffrement est**au**, Aspose.Cells for Reporting Services active le cryptage.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

Il y a quatre paramètres dans la section de chiffrement :

- **NomRapport**: pointe vers un rapport nécessitant un chiffrement. Si le paramètre est laissé vide, tous les rapports utilisent la même méthode de cryptage.
- **Mot de passe**: définit le mot de passe. Ne peut être vide.
- **Type de chiffrement**: définit un type de cryptage. Ne peut être vide.
- **Longueur de la clé**: définit la longueur de la clé. Ne peut être vide.

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
