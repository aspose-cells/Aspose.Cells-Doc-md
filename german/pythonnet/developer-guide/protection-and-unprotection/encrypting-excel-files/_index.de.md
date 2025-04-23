---
title: Verschlüsselung von Excel Dateien
type: docs
weight: 90
url: /de/python-net/encrypting-excel-files/
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) ermöglicht es Ihnen, Ihre Tabellenkalkulationen zu verschlüsseln und mit einem Passwort zu schützen. Es verwendet Algorithmen, die von einem kryptografischen Dienstanbieter oder CSP bereitgestellt werden, ein Satz kryptografischer Algorithmen mit unterschiedlichen Eigenschaften. Der Standard-CSP ist 'Office 97/2000 Kompatibel' oder 'Schwache Verschlüsselung (XOR)'. Es ist wichtig, die richtige Schlüssellänge zu wählen. Einige CSPs unterstützen nicht mehr als 40 oder 56 Bits. Das gilt als schwache Verschlüsselung. Für starke Verschlüsselung ist eine Mindestschlüssellänge von 128 Bits erforderlich. Microsoft Windows enthält ebenfalls CSPs, die starke Verschlüsselungstypen anbieten, wie z. B. den 'Microsoft Strong Cryptographic Provider'. Um Ihnen eine Vorstellung zu geben, 128-Bit-Verschlüsselung wird von Banken verwendet, um die Verbindung mit ihren Internetbanking-Systemen zu verschlüsseln.

Aspose.Cells für Python via .NET ermöglicht es Ihnen, Microsoft Excel-Dateien mit Ihrer gewünschten Verschlüsselungsmethode zu verschlüsseln und mit Passwort zu schützen.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

Um die Dateiverschlüsselungseinstellungen in Microsoft Excel festzulegen (hier Microsoft Excel 2003):

1. Wählen Sie im Menü **Extras** die Option **Optionen** aus. Es wird ein Dialogfeld angezeigt.
1. Wählen Sie den Tab **Sicherheit** aus.
1. Geben Sie ein Passwort ein und klicken Sie auf **Erweitert**
1. Wählen Sie den Verschlüsselungstyp aus und bestätigen Sie das Passwort.

## **Verschlüsselung mit Aspose.Cells**

Das folgende Beispiel zeigt, wie man eine Excel-Datei mit der Aspose.Cells für Python via .NET API verschlüsselt und mit Passwort schützt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **Passwort zum Ändern der Option festlegen**

Das folgende Beispiel zeigt, wie man die **Passwort zum Bearbeiten**-Option für eine bestehende Excel-Datei mit der Aspose.Cells für Python via .NET API festlegt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}

## **Das Passwort der verschlüsselten Datei verifizieren**

Um das Passwort der verschlüsselten Datei zu überprüfen, bietet Aspose.Cells für Python via .NET die [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password)-Methode. Diese Methoden akzeptieren zwei Parameter, den Dateistream und das zu überprüfende Passwort.
Der folgende Code-Schnipsel zeigt die Verwendung der Methode [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) zur Überprüfung, ob das angegebene Passwort gültig ist oder nicht.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}

## **Verschlüsselung/Entschlüsselung von ODS-Dateien**

Aspose.Cells für Python via .NET ermöglicht es, ODS-Dateien zu verschlüsseln und zu entschlüsseln. Entschlüsselte ODS-Dateien können sowohl in Excel als auch in OpenOffice geöffnet werden. Verschlüsselte ODS-Dateien können nur in OpenOffice geöffnet werden, nachdem das Passwort eingegeben wurde. Excel kann die verschlüsselte ODS-Datei nicht öffnen und gibt möglicherweise eine Warnmeldung aus. Die Verschlüsselungsoptionen sind bei ODS-Dateien im Gegensatz zu anderen Dateitypen nicht anwendbar. Um eine ODS-Datei zu verschlüsseln, laden Sie die Datei, setzen Sie den [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password)-Wert auf das tatsächliche Passwort und speichern Sie die Datei. Die verschlüsselte ODS-Ausgabe kann nur in OpenOffice geöffnet werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

Für das Entschlüsseln einer ODS-Datei laden Sie die Datei, indem Sie ein Passwort in [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password) angeben. Sobald die Datei geladen ist, setzen Sie den Wert [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) auf null.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

