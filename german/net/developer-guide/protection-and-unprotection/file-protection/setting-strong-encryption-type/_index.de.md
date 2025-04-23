---
title: Festlegen des starken Verschlüsselungstyps
type: docs
weight: 60
url: /de/net/setting-strong-encryption-type/
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) ermöglicht es Ihnen, Arbeitsmappen zu verschlüsseln und mit einem Passwort zu schützen. Es verwendet Algorithmen, die von einem kryptografischen Dienstanbieter bereitgestellt werden. Ein kryptografischer Dienstanbieter (oder CSP) ist eine Reihe von kryptografischen Algorithmen mit unterschiedlichen Eigenschaften. Der Standard-CSP ist "Office 97/2000 Compatible". Dies ist ein CSP mit einigen öffentlich bekannten Sicherheitsproblemen. Arbeitsmappen, die mit der "schwachen Verschlüsselung (XOR)" oder dem Verschlüsselungstyp "Office 97/2000 Compatible" gesichert sind, können leicht geknackt werden.

Um dieses Problem zu überwinden, verwenden Sie eine der starken Verschlüsselungstypen, die von Microsoft Excel bereitgestellt werden. Sie können den Verschlüsselungstyp auf den stärksten verfügbaren CSP ändern. Für starke Verschlüsselung ist eine Mindestschlüssellänge von 128 Bits erforderlich, zum Beispiel 'Microsoft Strong Cryptographic Provider'.

Sie können auch Excel-Dateien mit starkem Verschlüsselungstyp mithilfe der Aspose.Cells-API verschlüsseln und mit einem Passwort schützen.

{{% /alert %}} 
## **Verschlüsselung mit Microsoft Excel anwenden**
Um die Dateiverschlüsselung in Microsoft Excel (zum Beispiel 2007) zu implementieren:

1. Wählen Sie im **Extras**-Menü die Option **Optionen** aus.
1. Wählen Sie den Tab **Sicherheit** aus.
1. Geben Sie einen Wert für das Feld **Kennwort zum Öffnen** ein.
1. Klicken Sie auf **Erweitert**.
1. Wählen Sie den Verschlüsselungstyp aus und bestätigen Sie das Passwort.
## **Verschlüsselung mit Aspose.Cells anwenden**
Die unten stehenden Codebeispiele wenden eine starke Verschlüsselung auf eine Datei an und setzen ein Passwort.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingStrongEncryptionType-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
