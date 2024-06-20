---
title: Verschlüsselung von Excel Dateien
type: docs
weight: 90
url: /de/net/encrypting-excel-files/
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) ermöglicht es Ihnen, Ihre Tabellenkalkulationen zu verschlüsseln und mit einem Passwort zu schützen. Es verwendet Algorithmen, die von einem kryptografischen Dienstanbieter oder CSP bereitgestellt werden, ein Satz kryptografischer Algorithmen mit unterschiedlichen Eigenschaften. Der Standard-CSP ist 'Office 97/2000 Kompatibel' oder 'Schwache Verschlüsselung (XOR)'. Es ist wichtig, die richtige Schlüssellänge zu wählen. Einige CSPs unterstützen nicht mehr als 40 oder 56 Bits. Das gilt als schwache Verschlüsselung. Für starke Verschlüsselung ist eine Mindestschlüssellänge von 128 Bits erforderlich. Microsoft Windows enthält ebenfalls CSPs, die starke Verschlüsselungstypen anbieten, wie z. B. den 'Microsoft Strong Cryptographic Provider'. Um Ihnen eine Vorstellung zu geben, 128-Bit-Verschlüsselung wird von Banken verwendet, um die Verbindung mit ihren Internetbanking-Systemen zu verschlüsseln.

Mit Aspose.Cells können Sie Microsoft Excel-Dateien mit dem gewünschten Verschlüsselungstyp verschlüsseln und mit einem Passwort schützen.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

Um die Dateiverschlüsselungseinstellungen in Microsoft Excel festzulegen (hier Microsoft Excel 2003):

1. Wählen Sie im Menü **Extras** die Option **Optionen** aus. Es wird ein Dialogfeld angezeigt.
1. Wählen Sie den Tab **Sicherheit** aus.
1. Geben Sie ein Passwort ein und klicken Sie auf **Erweitert**
1. Wählen Sie den Verschlüsselungstyp aus und bestätigen Sie das Passwort.

## **Verschlüsselung mit Aspose.Cells**

Das folgende Beispiel zeigt, wie Sie mit dem Aspose.Cells-API eine Excel-Datei verschlüsseln und kennwortgeschützt machen können.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Passwort zum Ändern der Option festlegen**

Das folgende Beispiel zeigt, wie Sie die **Passwort zum Ändern** Microsoft Excel-Option für eine vorhandene Datei mithilfe der Aspose.Cells-API festlegen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **Das Passwort der verschlüsselten Datei verifizieren**

Um das Passwort der verschlüsselten Datei zu verifizieren, bietet Aspose.Cells for .NET die Methode [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword). Diese Methoden akzeptieren zwei Parameter: den Dateistream und das zu verifizierende Passwort.
Der folgende Code-Schnipsel zeigt die Verwendung der Methode [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) zur Überprüfung, ob das angegebene Passwort gültig ist oder nicht.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **Verschlüsselung/Entschlüsselung von ODS-Dateien mit Aspose.Cells**

Aspose.Cells ermöglicht die Verschlüsselung und Entschlüsselung von ODS-Dateien. Die entschlüsselte ODS-Datei kann sowohl in Excel als auch in OpenOffice geöffnet werden. Die verschlüsselte ODS-Datei kann jedoch nur von OpenOffice geöffnet werden, nachdem das Passwort eingegeben wurde. Excel kann die verschlüsselte ODS-Datei nicht öffnen und möglicherweise eine Warnmeldung anzeigen. Die Verschlüsselungsoptionen sind im Gegensatz zu anderen Dateitypen nicht für ODS-Dateien anwendbar. Um eine ODS-Datei zu verschlüsseln, laden Sie die Datei und setzen Sie den [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)-Wert auf das tatsächliche Passwort, bevor Sie sie speichern. Die Ausgabeverschlüsselte ODS-Datei kann nur in OpenOffice geöffnet werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

Für das Entschlüsseln einer ODS-Datei laden Sie die Datei, indem Sie ein Passwort in [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) angeben. Sobald die Datei geladen ist, setzen Sie den Wert [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) auf null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
