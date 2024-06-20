---
title: Excel Dateien verschlüsseln und entschlüsseln
type: docs
weight: 40
url: /de/java/encrypt-and-decrypt-excel-files/
description: Wie man Excel Dateien mit Java verschlüsselt und entschlüsselt. Excel Dateien sperren und entsperren.
---

{{% alert color="primary" %}}
Microsoft Excel (97 - 365 ) ermöglicht es Ihnen, Ihre Tabellenkalkulationen zu verschlüsseln / mit einem Passwort zu schützen. Es verwendet Algorithmen, die vom Crypto Service Provider bereitgestellt werden. Ein Crypto Service Provider oder CSP ist eine Gruppe von kryptografischen Algorithmen mit unterschiedlichen Eigenschaften. Der Standard-CSP ist "Office 97/2000 kompatibel" oder "Schwache Verschlüsselung (XOR)". Es ist auch wichtig, eine geeignete Verschlüsselungsschlüssellänge zu wählen. Einige der Crypto Service Provider unterstützen nicht mehr als 40 oder 56 Bits. Dies gilt als schwache Verschlüsselungsart. Für eine starke Verschlüsselungsart ist eine Mindestschlüssellänge von 128 Bits erforderlich. Microsoft Windows enthält auch Crypto Service Provider, die starke Verschlüsselungsarten anbieten, z. B. den 'Microsoft Strong Cryptographic Provider'. Zur Veranschaulichung, 128-Bit-Verschlüsselung wird von Banken zur Verschlüsselung der Verbindung mit ihren Internet-Banking-Systemen verwendet. Aspose.Cells ermöglicht es Ihnen, Ihre Excel-Dateien mit Ihrem gewünschten Verschlüsselungstyp zu verschlüsseln / passwortgeschützt zu machen.

{{% /alert %}}

## **Verwendung von MS Excel**

In MS Excel (z. B. MS Excel 2003) können Sie versuchen, Dateiverschlüsselungseinstellungen zu implementieren:

- Wählen Sie im **Extras**-Menü **Optionen** und dann die Registerkarte **Sicherheit**.
- Geben Sie **Kennwort zum Öffnen** ein und klicken Sie auf die Schaltfläche **Erweitert**.
- Wählen Sie den Verschlüsselungstyp und bestätigen Sie das Kennwort.

![todo:image_alt_text](encrypting-excel-files_1.png)

**Abbildung: Optionsdialog**

![todo:image_alt_text](encrypting-excel-files_2.png)

**Abbildung: Dialogfeld Verschlüsselungstyp**

## **Verschlüsselung einer Excel-Datei**
Das folgende Beispiel zeigt, wie Sie eine Excel-Datei mithilfe der Aspose.Cells-API verschlüsseln/passwortgeschützt machen können.

### **Beispielcode:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **Entschlüsselung einer Excel-Datei mit Aspose.Cells**
Es ist sehr einfach, eine passwortgeschützte Excel-Datei zu öffnen und mit den folgenden Codes zu entschlüsseln, die Aspose.Cells-API zu verwenden:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



