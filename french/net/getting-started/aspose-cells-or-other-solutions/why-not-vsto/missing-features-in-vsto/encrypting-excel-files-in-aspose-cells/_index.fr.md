---
title: Chiffrer les fichiers Excel dans Aspose.Cells
type: docs
weight: 90
url: /fr/net/encrypting-excel-files-in-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007) vous permet de chiffrer et de protéger par mot de passe vos feuilles de calcul. Il utilise des algorithmes fournis par un fournisseur de services cryptographiques, ou CSP, un ensemble d'algorithmes cryptographiques aux propriétés différentes. Le CSP par défaut est 'Compatible Office 97/2000' ou 'Chiffrement faible (XOR)'. Il est important de choisir la bonne longueur de clé de cryptage. Certains CSP ne prennent pas en charge plus de 40 ou 56 bits. Cela est considéré comme un chiffrement faible. Pour un chiffrement fort, une longueur de clé minimale de 128 bits est requise. Microsoft Windows contient des CSP offrant également des types de chiffrement forts, par exemple le 'Fournisseur cryptographique fort de Microsoft'. Pour vous donner une idée, un chiffrement de 128 bits est ce que les banques utilisent pour crypter la connexion avec leurs systèmes de banque en ligne.

Aspose.Cells vous permet de chiffrer et de protéger par mot de passe des fichiers Microsoft Excel avec le type de chiffrement de votre choix.

{{% /alert %}} 
## **Utilisation de Microsoft Excel**
Pour définir les paramètres de chiffrement de fichier dans Microsoft Excel (ici Microsoft Excel 2003) :

1. Dans le menu **Outils**, sélectionnez **Options**.
   Une boîte de dialogue apparaît.
1. Sélectionnez l'onglet **Sécurité**.
1. Saisissez un mot de passe et cliquez sur **Avancé** 
   **Boîte de dialogue Options** 

![todo:image_alt_text](encrypting-excel-files-in-aspose-cells_1.png)




1. Choisissez le type de chiffrement et confirmez le mot de passe. 

   **Dialogue de type de chiffrement** 

![todo:image_alt_text](encrypting-excel-files-in-aspose-cells_2.png)



## **Chiffrement avec Aspose.Cells**
L'exemple suivant montre comment chiffrer et protéger par mot de passe un fichier Excel à l'aide de l'API Aspose.Cells.

**C#**

{{< highlight csharp >}}

 //Instantiate a Workbook object.

//Open an excel file.

Workbook workbook = new Workbook("Book1.xls");

//Specify XOR encryption type.

workbook.SetEncryptionOptions(EncryptionType.XOR,40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.

workbook.Settings.Password = "1234";

//Save the excel file.

workbook.Save("encryptedBook1.xls");



{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Encrypting%20Excel%20Files)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1))
{{< app/cells/assistant language="csharp" >}}
