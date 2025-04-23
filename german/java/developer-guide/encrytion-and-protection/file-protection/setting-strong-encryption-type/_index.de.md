---
title: Festlegen des starken Verschlüsselungstyps
type: docs
weight: 10
url: /de/java/setting-strong-encryption-type/
---

{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) ermöglicht es Ihnen, Tabellenkalkulationen zu verschlüsseln und mit einem Passwort zu schützen. Es verwendet Algorithmen, die von einem kryptografischen Dienstanbieter bereitgestellt werden. Ein kryptografischer Dienstanbieter (oder CSP) ist eine Reihe von kryptografischen Algorithmen mit unterschiedlichen Eigenschaften. Der Standard-CSP ist "Office 97/2000 Compatible". Dies ist ein CSP mit einigen bekannten Sicherheitsproblemen. Tabellenkalkulationen, die mit der "schwachen Verschlüsselung (XOR)" oder mit dem Verschlüsselungstyp "Office 97/2000 Compatible" gesichert sind, können leicht geknackt werden.

Um dieses Problem zu überwinden, verwenden Sie einen der starken Verschlüsselungstypen, die von Microsoft Excel bereitgestellt werden. Sie können den Verschlüsselungstyp auf den stärksten verfügbaren CSP ändern. Für eine starke Verschlüsselung ist eine Mindestschlüssellänge von 128 Bits erforderlich, z.B. 'Microsoft Strong Cryptographic Provider'.

Sie können auch Excel-Dateien mit starkem Verschlüsselungstyp mithilfe der Aspose.Cells-API verschlüsseln und mit einem Passwort schützen.

{{% /alert %}}

## **Verschlüsselung mit Microsoft Excel anwenden**

Um die Dateiverschlüsselung in Microsoft Excel (zum Beispiel 2007) zu implementieren:

1. Wählen Sie im **Extras**-Menü die Option **Optionen** aus.
1. Wählen Sie den Tab **Sicherheit** aus.
1. Geben Sie einen Wert für das Feld **Kennwort zum Öffnen** ein.
1. Klicken Sie auf **Erweitert**.
1. Wählen Sie den Verschlüsselungstyp aus und bestätigen Sie das Passwort.

   **Verschlüsselung in Microsoft Excel festlegen**

![todo:image_alt_text](setting-strong-encryption-type_1.png)

## **Verschlüsselung mit Aspose.Cells anwenden**

In dem untenstehenden Codebeispiel wird eine starke Verschlüsselung auf eine Datei angewendet und ein Passwort festgelegt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyingEncryption-ApplyingEncryption.java" >}}
{{< app/cells/assistant language="java" >}}
