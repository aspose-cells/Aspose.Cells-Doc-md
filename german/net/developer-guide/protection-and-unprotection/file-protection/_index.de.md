---
title: Excel Dateien verschlüsseln und entschlüsseln
type: docs
weight: 10
url: /de/net/encrypt-and-decrypt-excel-files/
description: So verschlüsseln und entschlüsseln Sie Excel Dateien in C#. Excel Dateien sperren und entsperren.
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

## **Excel-Datei mit Aspose.Cells verschlüsseln**

Das folgende Beispiel zeigt, wie Sie mit dem Aspose.Cells-API eine Excel-Datei verschlüsseln und kennwortgeschützt machen können.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Passwort zum Ändern der Option festlegen**

Das folgende Beispiel zeigt, wie Sie die **Passwort zum Ändern** Microsoft Excel-Option für eine vorhandene Datei mithilfe der Aspose.Cells-API festlegen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}


## **Entschlüsselung einer Excel-Datei mit Aspose.Cells**
Es ist sehr einfach, eine passwortgeschützte Excel-Datei zu öffnen und mit den folgenden Codes zu entschlüsseln, die Aspose.Cells-API zu verwenden:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Decrypt-Excel-File.cs" >}}


## **Erweiterte Themen**
- [ODS-Dateien verschlüsseln und entschlüsseln](/cells/de/net/encrypt-and-decrypt-ods-files/)
- [Festlegen des Verschlüsselungstyps](/cells/de/net/setting-strong-encryption-type/)
- [Autor beim Schreibschutz des Arbeitsmappenschreibens spezifizieren](/cells/de/net/specify-author-while-write-protecting-workbook/)
- [Passwort von verschlüsselten Dateien überprüfen](/cells/de/net/verify-password-of-encrypted-excel-and-ods-files/)

