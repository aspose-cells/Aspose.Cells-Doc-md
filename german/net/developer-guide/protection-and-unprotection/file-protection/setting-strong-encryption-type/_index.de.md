---
title: Festlegen des starken Verschlüsselungstyps
type: docs
weight: 60
url: /de/net/setting-strong-encryption-type/
---
{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) ermöglicht es Ihnen, Tabellenkalkulationen zu verschlüsseln und mit einem Passwort zu schützen. Es verwendet Algorithmen, die von einem Crypto Service Provider bereitgestellt werden. Ein Crypto Service Provider (oder CSP) ist eine Reihe von kryptografischen Algorithmen mit unterschiedlichen Eigenschaften. Der Standard-CSP ist „Office 97/2000-kompatibel“. Dies ist ein CSP mit einigen öffentlich bekannten Sicherheitsproblemen. Tabellenkalkulationen, die mit dem Verschlüsselungstyp „schwache Verschlüsselung (XOR)“ oder mit dem Verschlüsselungstyp „Office 97/2000 kompatibel“ gesichert sind, können leicht geknackt werden.

Um dieses Problem zu umgehen, verwenden Sie einen der starken Verschlüsselungstypen, die von Microsoft Excel bereitgestellt werden. Sie können den Verschlüsselungstyp auf den stärksten verfügbaren CSP ändern. Für eine starke Verschlüsselung ist eine Mindestschlüssellänge von 128 Bit erforderlich, zum Beispiel „Microsoft Strong Cryptographic Provider“.

Sie können Excel-Dateien auch mit starkem Verschlüsselungstyp verschlüsseln und mit einem Kennwort schützen, indem Sie die Aspose.Cells API verwenden.

{{% /alert %}} 
## **Anwenden der Verschlüsselung mit Microsoft Excel**
So implementieren Sie die Dateiverschlüsselung in Microsoft Excel (z. B. 2007):

1.  Von dem**Werkzeug** Menü, auswählen**Optionen**.
1.  Wähle aus**Sicherheit** Tab.
1.  Geben Sie einen Wert für die ein**Passwort zum Öffnen** aufstellen.
1.  Klicken**Fortschrittlich**.
1. Wählen Sie den Verschlüsselungstyp und bestätigen Sie das Passwort.
## **Anwenden der Verschlüsselung mit Aspose.Cells**
Die folgenden Codebeispiele wenden eine starke Verschlüsselung auf eine Datei an und legen ein Kennwort fest.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingStrongEncryptionType-1.cs" >}}
