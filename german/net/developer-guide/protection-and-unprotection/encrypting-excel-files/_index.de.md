---
title: Verschlüsseln von Excel-Dateien
type: docs
weight: 90
url: /de/net/encrypting-excel-files/
---
{{% alert color="primary" %}}

Microsoft Excel (97 - 365) ermöglicht es Ihnen, Ihre Tabellenkalkulationen zu verschlüsseln und mit einem Passwort zu schützen. Es verwendet Algorithmen, die von einem Kryptografiedienstanbieter oder CSP bereitgestellt werden, eine Reihe von Kryptografiealgorithmen mit unterschiedlichen Eigenschaften. Der Standard-CSP ist „Office 97/2000-kompatibel“ oder „Schwache Verschlüsselung (XOR)“. Es ist wichtig, die richtige Länge des Verschlüsselungsschlüssels zu wählen. Einige CSPs unterstützen nicht mehr als 40 oder 56 Bit. Das gilt als schwache Verschlüsselung. Für eine starke Verschlüsselung ist eine Mindestschlüssellänge von 128 Bit erforderlich. Microsoft Windows enthält CSPs, die ebenfalls starke Verschlüsselungstypen anbieten, beispielsweise den 'Microsoft Strong Cryptographic Provider'. Um Ihnen eine Vorstellung zu geben: Banken verwenden eine 128-Bit-Verschlüsselung, um die Verbindung mit ihren Internet-Banking-Systemen zu verschlüsseln.

Mit Aspose.Cells können Sie Microsoft Excel-Dateien mit Ihrem gewünschten Verschlüsselungstyp verschlüsseln und mit einem Kennwort schützen.

{{% /alert %}}

## **Mit Microsoft Excel**

So legen Sie die Dateiverschlüsselungseinstellungen in Microsoft Excel fest (hier Microsoft Excel 2003):

1.  Von dem**Werkzeug** Menü, auswählen**Optionen**Ein Dialogfeld wird angezeigt.
1.  Wähle aus**Sicherheit** Tab.
1.  Geben Sie ein Passwort ein und klicken Sie auf**Fortschrittlich**
1. Wählen Sie den Verschlüsselungstyp und bestätigen Sie das Passwort.

## **Verschlüsselung mit Aspose.Cells**

Das folgende Beispiel zeigt, wie eine Excel-Datei mit Aspose.Cells API verschlüsselt und mit einem Kennwort geschützt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Festlegen des Kennworts zum Ändern der Option**

 Das folgende Beispiel zeigt, wie die eingestellt wird**Zu änderndes Passwort** Microsoft Excel-Option für eine vorhandene Datei mit der Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **Überprüfen Sie das Passwort der verschlüsselten Datei**

 Um das Passwort der verschlüsselten Datei zu überprüfen, bietet Aspose.Cells for .NET die[**Passwort bestätigen**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) Methode. Diese Methoden akzeptieren zwei Parameter, den Dateistream und das zu verifizierende Passwort.
 Das folgende Code-Snippet demonstriert die Verwendung von[**Passwort bestätigen**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) Methode, um zu überprüfen, ob das angegebene Passwort gültig ist oder nicht.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **Verschlüsselung/Entschlüsselung der ODS-Datei mit Aspose.Cells**

Aspose.Cells ermöglicht das Verschlüsseln und Entschlüsseln der Datei ODS. Die entschlüsselte ODS-Datei kann sowohl in Excel als auch in OpenOffice geöffnet werden, die verschlüsselte ODS-Datei kann jedoch nur von OpenOffice geöffnet werden, nachdem das Kennwort angegeben wurde. Excel kann die verschlüsselte ODS-Datei nicht öffnen und gibt möglicherweise eine Warnmeldung aus. Die Verschlüsselungsoptionen gelten im Gegensatz zu anderen Dateitypen nicht für die Datei ODS. Um eine ODS-Datei zu verschlüsseln, laden Sie die Datei und stellen Sie die[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) Wert auf das eigentliche Passwort, bevor Sie es speichern. Die verschlüsselte Ausgabedatei ODS kann nur in OpenOffice geöffnet werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

 Um eine ODS-Datei zu entschlüsseln, laden Sie die Datei, indem Sie ein Passwort in der[**LoadOptions.Passwort**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . Sobald die Datei geladen ist, legen Sie die[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) Zeichenfolge auf null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
