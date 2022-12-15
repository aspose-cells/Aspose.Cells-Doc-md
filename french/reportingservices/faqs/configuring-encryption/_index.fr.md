---
title: Configuration du chiffrement
type: docs
weight: 40
url: /fr/reportingservices/configuring-encryption/
---
{{% alert color="primary" %}} 

 Aspose.Cells for Reporting Services prend en charge le cryptage et vous pouvez afficher des fichiers Excel Microsoft cryptés.

{{% /alert %}} 
### **Types de chiffrement**
Aspose.Cells for Reporting Services prend en charge le cryptage lors de l'exportation de fichiers Excel. Il prend en charge trois types de chiffrement :

- XOR
- CHIFFREMENT FAIBLE
- Microsoft Fournisseur cryptographique puissant
### **Configuration des informations**
 Il y a des informations de configuration pour le cryptage dans le**Aspose.Cells.ReportingServices.xml** dossier. Lorsque la valeur de Encryption est définie sur "off", Aspose.Cells.ReportingServices désactive le cryptage.

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

Lorsque le chiffrement est défini sur "on", Aspose.Cells.ReportingServices active le chiffrement.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

Il y a quatre paramètres dans la section Encryption : ReportName, Password, EncryptionType et KeyLength.

- ReportName – Définit le rapport qui nécessite des paramètres de cryptage. Un rapport utilise le même mode de cryptage lorsque le paramètre est vide.
- Mot de passe – Définit le mot de passe. Il ne peut pas être laissé vide.
- EncryptionType – Définit le type de chiffrement. Il ne peut pas être laissé vide.
-  KeyLength – Définit la longueur de la clé. Il ne peut pas être laissé vide.

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
