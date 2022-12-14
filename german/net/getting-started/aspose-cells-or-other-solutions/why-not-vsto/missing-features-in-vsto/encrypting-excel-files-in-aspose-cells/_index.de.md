---
title: Verschlüsseln von Excel-Dateien in Aspose.Cells
type: docs
weight: 90
url: /de/net/encrypting-excel-files-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007) ermöglicht es Ihnen, Ihre Tabellenkalkulationen zu verschlüsseln und mit einem Kennwort zu schützen. Es verwendet Algorithmen, die von einem Kryptografiedienstanbieter oder CSP bereitgestellt werden, eine Reihe von Kryptografiealgorithmen mit unterschiedlichen Eigenschaften. Der Standard-CSP ist „Office 97/2000-kompatibel“ oder „Schwache Verschlüsselung (XOR)“. Es ist wichtig, die richtige Länge des Verschlüsselungsschlüssels zu wählen. Einige CSPs unterstützen nicht mehr als 40 oder 56 Bit. Das gilt als schwache Verschlüsselung. Für eine starke Verschlüsselung ist eine Mindestschlüssellänge von 128 Bit erforderlich. Microsoft Windows enthält CSPs, die ebenfalls starke Verschlüsselungstypen anbieten, beispielsweise den 'Microsoft Strong Cryptographic Provider'. Um Ihnen eine Vorstellung zu geben: Banken verwenden eine 128-Bit-Verschlüsselung, um die Verbindung mit ihren Internet-Banking-Systemen zu verschlüsseln.

Mit Aspose.Cells können Sie Microsoft Excel-Dateien mit Ihrem gewünschten Verschlüsselungstyp verschlüsseln und mit einem Kennwort schützen.

{{% /alert %}} 
## **Mit Microsoft Excel**
So legen Sie die Dateiverschlüsselungseinstellungen in Microsoft Excel fest (hier Microsoft Excel 2003):

1.  Von dem**Werkzeug** Menü, auswählen**Optionen**.
 Ein Dialogfeld wird angezeigt.
1.  Wähle aus**Sicherheit** Tab.
1.  Geben Sie ein Passwort ein und klicken Sie auf**Fortschrittlich** 
   **Dialogfeld „Optionen“.** 

![todo: Bild_alt_Text](encrypting-excel-files-in-aspose-cells_1.png)




1.  Wählen Sie den Verschlüsselungstyp und bestätigen Sie das Passwort.

   **Dialogfeld „Verschlüsselungstyp“.** 

![todo: Bild_alt_Text](encrypting-excel-files-in-aspose-cells_2.png)



## **Verschlüsselung mit Aspose.Cells**
Das folgende Beispiel zeigt, wie eine Excel-Datei mit Aspose.Cells API verschlüsselt und mit einem Kennwort geschützt wird.

**C#**

{{< highlight "csharp" >}}

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
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Encrypting%20Excel%20Files)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1))
