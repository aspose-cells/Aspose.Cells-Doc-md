---
title: Excel Dateien mit Aspose.Cells verschlüsseln
type: docs
weight: 30
url: /de/net/encrypting-excel-files-using-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007) ermöglicht es Ihnen, Ihre Tabellenkalkulationen zu verschlüsseln und mit einem Passwort zu schützen. Dabei verwendet es von einem kryptografischen Dienstanbieter bereitgestellte Algorithmen - eine Reihe kryptografischer Algorithmen mit unterschiedlichen Eigenschaften. Der Standard-Kryptodienstanbieter ist 'Office 97/2000-kompatibel' oder 'Schwache Verschlüsselung (XOR)'. Es ist wichtig, die geeignete Verschlüsselungsschlüssellänge zu wählen. Einige Kryptodienstanbieter unterstützen nicht mehr als 40 oder 56 Bits. Das gilt als schwache Verschlüsselung. Für starke Verschlüsselung ist eine Mindestschlüssellänge von 128 Bits erforderlich. Microsoft Windows enthält auch Kryptodienstanbieter, die starke Verschlüsselungstypen unterstützen, z.B. der 'Microsoft Strong Cryptographic Provider'. Zur Veranschaulichung: 128-Bit-Verschlüsselung ist das, was Banken zur Verschlüsselung der Verbindung mit ihren Internet-Banking-Systemen verwenden.

Mit Aspose.Cells können Sie Microsoft Excel-Dateien mit dem gewünschten Verschlüsselungstyp verschlüsseln und mit einem Passwort schützen.

{{% /alert %}} 
## **Verwendung von Microsoft Excel**
Um die Dateiverschlüsselungseinstellungen in Microsoft Excel festzulegen (hier Microsoft Excel 2003):

1. Wählen Sie im **Extras**-Menü die Option **Optionen** aus.
   Ein Dialogfeld wird angezeigt.
1. Wählen Sie den Tab **Sicherheit** aus.
1. Geben Sie ein Passwort ein und klicken Sie auf **Erweitert** 
   **Dialogfeld Optionen** 

![todo:image_alt_text](encrypting-excel-files-using-aspose-cells_1.png)




1. Wählen Sie den Verschlüsselungstyp aus und bestätigen Sie das Passwort. 

   **Dialogfeld Verschlüsselungstyp** 

![todo:image_alt_text](encrypting-excel-files-using-aspose-cells_2.png)



## **Verschlüsselung mit Aspose.Cells**
Das folgende Beispiel zeigt, wie Sie mit dem Aspose.Cells-API eine Excel-Datei verschlüsseln und kennwortgeschützt machen können.

**C#**

{{< highlight csharp >}}

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
## **Laufenden Code herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
## **Beispielcode herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Encrypting%20Excel%20Files)

