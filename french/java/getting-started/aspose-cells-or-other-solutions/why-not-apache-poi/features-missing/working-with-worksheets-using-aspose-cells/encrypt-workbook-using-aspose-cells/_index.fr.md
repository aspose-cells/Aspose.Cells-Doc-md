---
title: Chiffrer le classeur à l aide d Aspose.Cells
type: docs
weight: 60
url: /fr/java/encrypt-workbook-using-aspose-cells/
---

## **Aspose.Cells - Chiffrer le classeur**
L'exemple suivant montre comment vous pouvez chiffrer / protéger par mot de passe un fichier Excel à l'aide de l'API Aspose.Cells.

**Java**

{{< highlight java >}}

 //Instantiate a Workbook object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Password protect the file.

workbook.getSettings().setPassword("1234");

//Specify XOR encryption type.

workbook.setEncryptionOptions(EncryptionType.XOR, 40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.setEncryptionOptions(EncryptionType.STRONG_CRYPTOGRAPHIC_PROVIDER, 128);

//Save the excel file.

workbook.save(dataDir + "AsposeEncryptedWorkBook.xls");

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeEncryptSpreadsheets.java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Chiffrer les fichiers Excel](/cells/fr/java/chiffrer-les-fichiers-excel/).

{{% /alert %}}
