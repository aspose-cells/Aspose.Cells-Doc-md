---
title: Cryptage de fichiers Excel à l'aide de Aspose.Cells
type: docs
weight: 30
url: /fr/net/encrypting-excel-files-using-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007) vous permet de crypter et de protéger par mot de passe vos feuilles de calcul. Il utilise des algorithmes fournis par un fournisseur de services cryptographiques, ou CSP, un ensemble d'algorithmes cryptographiques aux propriétés différentes. Le CSP par défaut est 'Office 97/2000 Compatible' ou 'Weak Encryption (XOR)'. Il est important de choisir la bonne longueur de clé de chiffrement. Certains CSP ne prennent pas en charge plus de 40 ou 56 bits. C'est considéré comme un cryptage faible. Pour un cryptage fort, une longueur de clé minimale de 128 bits est requise. Microsoft Windows contient des CSP qui offrent également des types de chiffrement fort, par exemple le « Microsoft Strong Cryptographic Provider ». Pour vous donner une idée, le cryptage 128 bits est ce que les banques utilisent pour crypter la connexion avec leurs systèmes bancaires par Internet.

Aspose.Cells vous permet de crypter et de protéger par mot de passe les fichiers Excel Microsoft avec le type de cryptage souhaité.

{{% /alert %}} 
## **Utilisation d'Excel Microsoft**
Pour définir les paramètres de cryptage des fichiers dans Microsoft Excel (ici Microsoft Excel 2003) :

1.  Du**Outils** menu, sélectionnez**Choix**.
 Une boîte de dialogue apparaît.
1.  Sélectionnez le**Sécurité** languette.
1.  Entrez un mot de passe et cliquez**Avancé** 
   **Boîte de dialogue Options** 

![tâche : image_autre_texte](encrypting-excel-files-using-aspose-cells_1.png)




1.  Choisissez le type de cryptage et confirmez le mot de passe.

   **Boîte de dialogue Type de chiffrement** 

![tâche : image_autre_texte](encrypting-excel-files-using-aspose-cells_2.png)



## **Cryptage avec Aspose.Cells**
L'exemple suivant montre comment chiffrer et protéger par mot de passe un fichier Excel en utilisant le Aspose.Cells API.

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string srcFileName = FilePath + "Encrypting Excel Files.xlsx";

string destFileName = FilePath + "Result Encrypting Excel Files.xlsx";

//Open an excel file.

Workbook workbook = new Workbook(srcFileName);

//Specify XOR encryption type.

workbook.SetEncryptionOptions(EncryptionType.XOR, 40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.

workbook.Settings.Password = "1234";

//Save the excel file.

workbook.Save(destFileName);

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Encrypting%20Excel%20Files)

