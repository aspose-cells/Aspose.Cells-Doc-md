---
title: Configuration du cryptage
type: docs
weight: 40
url: /fr/reportingservices/configuring-encryption/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services prend en charge le cryptage et vous pouvez rendre des fichiers Microsoft Excel cryptés. 

{{% /alert %}} 
### **Types de cryptage**
Aspose.Cells for Reporting Services prend en charge le cryptage lors de l'exportation de fichiers Excel. Il prend en charge trois types de cryptage :

- XOR
- CRYPTAGE FAIBLE
- Fournisseur Cryptographique Fort de Microsoft
### **Configuration des informations**
Il y a des informations de configuration pour le cryptage dans le fichier **Aspose.Cells.ReportingServices.xml**. Lorsque la valeur de Cryptage est définie sur "désactivé", Aspose.Cells.ReportingServices désactive le cryptage.

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

Lorsque le cryptage est défini sur "activé", Aspose.Cells.ReportingServices active le cryptage.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

Il y a quatre paramètres dans la section Cryptage : NomRapport, MotDePasse, TypeCryptage et LongueurClé.

- NomRapport – Définit le rapport qui nécessite des paramètres de cryptage. Un rapport utilise la même méthode de cryptage lorsque le paramètre est vide.
- MotDePasse – Définit le mot de passe. Il ne peut pas être laissé vide.
- TypeCryptage – Définit le type de cryptage. Il ne peut pas être laissé vide.
- LongueurClé – Définit la longueur de la clé. Il ne peut pas être laissé vide. 

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
