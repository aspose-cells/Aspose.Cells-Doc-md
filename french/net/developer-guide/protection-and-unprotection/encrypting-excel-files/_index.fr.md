---
title: Chiffrement des fichiers Excel
type: docs
weight: 90
url: /fr/net/encrypting-excel-files/
---
{{% alert color="primary" %}}

Microsoft Excel (97 - 365) vous permet de crypter et de protéger par mot de passe vos feuilles de calcul. Il utilise des algorithmes fournis par un fournisseur de services cryptographiques, ou CSP, un ensemble d'algorithmes cryptographiques aux propriétés différentes. Le CSP par défaut est 'Office 97/2000 Compatible' ou 'Weak Encryption (XOR)'. Il est important de choisir la bonne longueur de clé de chiffrement. Certains CSP ne prennent pas en charge plus de 40 ou 56 bits. C'est considéré comme un cryptage faible. Pour un cryptage fort, une longueur de clé minimale de 128 bits est requise. Microsoft Windows contient des CSP qui offrent également des types de chiffrement fort, par exemple le « Microsoft Strong Cryptographic Provider ». Pour vous donner une idée, le cryptage 128 bits est ce que les banques utilisent pour crypter la connexion avec leurs systèmes bancaires par Internet.

Aspose.Cells vous permet de crypter et de protéger par mot de passe les fichiers Excel Microsoft avec le type de cryptage souhaité.

{{% /alert %}}

## **Utilisation d'Excel Microsoft**

Pour définir les paramètres de cryptage des fichiers dans Microsoft Excel (ici Microsoft Excel 2003) :

1.  Du**Outils** menu, sélectionnez**Choix**Une boîte de dialogue apparaîtra.
1.  Sélectionnez le**Sécurité** languette.
1.  Entrez un mot de passe et cliquez**Avancé**
1. Choisissez le type de cryptage et confirmez le mot de passe.

## **Cryptage avec Aspose.Cells**

L'exemple suivant montre comment chiffrer et protéger par mot de passe un fichier Excel en utilisant le Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Spécification du mot de passe pour modifier l'option**

 L'exemple suivant montre comment régler le**Mot de passe à modifier** Microsoft Option Excel pour un fichier existant utilisant le Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **Vérifier le mot de passe du fichier crypté**

 Pour vérifier le mot de passe du fichier crypté, Aspose.Cells for .NET fournit le[**Vérifier le mot de passe**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) méthode. Ces méthodes acceptent deux paramètres, le flux du fichier et le mot de passe qui doit être vérifié.
L'extrait de code suivant illustre l'utilisation de[**Vérifier le mot de passe**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) méthode pour vérifier si le mot de passe fourni est valide ou non.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **Cryptage/Décryptage du fichier ODS avec Aspose.Cells**

Aspose.Cells permet de chiffrer et de déchiffrer le fichier ODS. Le fichier ODS décrypté peut être ouvert à la fois dans Excel et OpenOffice, mais le fichier ODS crypté ne peut être ouvert par OpenOffice qu'après avoir fourni le mot de passe. Excel ne peut pas ouvrir le fichier ODS crypté et peut générer un message d'avertissement. Les options de cryptage ne s'appliquent pas au fichier ODS contrairement aux autres types de fichiers. Pour chiffrer un fichier ODS, chargez le fichier et définissez le[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) valeur au mot de passe réel avant de l'enregistrer. Le fichier ODS crypté de sortie ne peut être ouvert que dans OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

 Pour déchiffrer un fichier ODS, chargez le fichier en fournissant un mot de passe dans le[**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . Une fois le fichier chargé, réglez le[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) chaîne à null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
