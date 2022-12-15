---
title: Excel-Dateien verschlüsseln und entschlüsseln
type: docs
weight: 40
url: /de/java/encrypt-and-decrypt-excel-files/
description: So verschlüsseln und entschlüsseln Sie Excel-Dateien mit Java. Sperren und Entsperren von Excel-Dateien.
---
{{% alert color="primary" %}}
Microsoft Excel (97 - 365 ) ermöglicht es Ihnen, Ihre Tabellenkalkulationen zu verschlüsseln / mit einem Passwort zu schützen. Es verwendet Algorithmen, die vom Crypto Service Provider bereitgestellt werden. Ein Crypto Service Provider oder CSP ist eine Reihe von kryptografischen Algorithmen mit unterschiedlichen Eigenschaften. Der Standard-CSP ist „Office 97/2000-kompatibel“ oder „Wochenverschlüsselung (XOR)“. Es ist auch wichtig, eine geeignete Länge des Verschlüsselungsschlüssels zu wählen. Einige der Kryptodienstanbieter unterstützen nicht mehr als 40 oder 56 Bit. Dies gilt als schwacher Verschlüsselungstyp. Für starke Verschlüsselungstypen ist jedoch eine Mindestschlüssellänge von 128 Bit erforderlich. Microsoft Windows enthält Crypto Service Provider, die ebenfalls starke Verschlüsselungstypen anbieten, zum Beispiel 'Microsoft Strong Cryptographic Provider'. Um eine Vorstellung zu geben, verwenden Banken eine 128-Bit-Verschlüsselung, um die Verbindung mit ihren Internet-Banking-Systemen zu verschlüsseln. Aspose.Cells ermöglicht es Ihnen, Ihre Excel-Dateien mit Ihrem gewünschten Verschlüsselungstyp zu verschlüsseln / mit einem Passwort zu schützen.

{{% /alert %}}

## **Mit MS-Excel**

In MS Excel (z. B. MS Excel 2003) können Sie zum Implementieren von Dateiverschlüsselungseinstellungen Folgendes versuchen:

-  Von dem**Werkzeug** Menü, auswählen**Optionen** , und wählen Sie dann die aus**Sicherheit** Tab.
-  Eingang**Passwort zum Öffnen** und klicken Sie auf die**Fortschrittlich** Taste.
- Wählen Sie den Verschlüsselungstyp und bestätigen Sie das Passwort.

![todo: Bild_alt_Text](encrypting-excel-files_1.png)

**Abbildung: Dialog Optionen**

![todo: Bild_alt_Text](encrypting-excel-files_2.png)

**Abbildung: Dialog Verschlüsselungstyp**

## **Excel-Datei verschlüsseln**
Das folgende Beispiel zeigt, wie Sie eine Excel-Datei mit der Aspose.Cells API verschlüsseln / mit einem Passwort schützen können.

### **Beispielcode:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **Excel-Datei mit Aspose.Cells entschlüsseln**
Es ist sehr wichtig, eine passwortgeschützte Excel-Datei zu öffnen und mit den folgenden Codes Aspose.Cells API zu entschlüsseln:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



