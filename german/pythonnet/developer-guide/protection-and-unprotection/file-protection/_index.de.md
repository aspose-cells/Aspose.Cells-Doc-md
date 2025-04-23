---
title: Excel Dateien verschlüsseln und entschlüsseln
type: docs
weight: 10
url: /de/python-net/encrypt-and-decrypt-excel-files/
description: Wie man Excel Dateien mit Python verschlüsselt und entschlüsselt. Excel Dateien sperren und entsperren.
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

## **Excel-Datei mit Aspose.Cells verschlüsseln**

Das folgende Beispiel zeigt, wie man eine Excel-Datei mit der Aspose.Cells für Python via .NET API verschlüsselt und mit Passwort schützt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **Passwort zum Ändern der Option festlegen**

Das folgende Beispiel zeigt, wie man die **Passwort zum Bearbeiten**-Option für eine bestehende Excel-Datei mit der Aspose.Cells für Python via .NET API festlegt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}


## **Entschlüsselung einer Excel-Datei mit Aspose.Cells**
Es ist sehr einfach, passwortgeschützte Excel-Dateien zu öffnen und mit der Aspose.Cells für Python via .NET API zu entschlüsseln, wie in folgendem Code gezeigt:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-Decrypt-Excel-File.py" >}}


## **Erweiterte Themen**
- [ODS-Dateien verschlüsseln und entschlüsseln](/cells/de/python-net/encrypt-and-decrypt-ods-files/)
- [Festlegen des Verschlüsselungstyps](/cells/de/python-net/setting-strong-encryption-type/)
- [Autor beim Schreibschutz des Arbeitsmappenschreibens spezifizieren](/cells/de/python-net/specify-author-while-write-protecting-workbook/)
- [Passwort von verschlüsselten Dateien überprüfen](/cells/de/python-net/verify-password-of-encrypted-excel-and-ods-files/)

