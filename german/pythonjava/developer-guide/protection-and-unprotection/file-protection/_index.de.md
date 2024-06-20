---
title: Excel Dateien verschlüsseln und entschlüsseln
type: docs
weight: 10
url: /de/python-java/encrypt-and-decrypt-excel-files/
description: Wie man Excel Dateien mit Python verschlüsselt und entschlüsselt. Excel Dateien sperren und entsperren.
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) ermöglicht es Ihnen, Ihre Tabellenkalkulationen zu verschlüsseln und mit einem Passwort zu schützen. Es verwendet Algorithmen, die von einem kryptografischen Dienstanbieter oder CSP bereitgestellt werden, ein Satz kryptografischer Algorithmen mit unterschiedlichen Eigenschaften. Der Standard-CSP ist 'Office 97/2000 Kompatibel' oder 'Schwache Verschlüsselung (XOR)'. Es ist wichtig, die richtige Schlüssellänge zu wählen. Einige CSPs unterstützen nicht mehr als 40 oder 56 Bits. Das gilt als schwache Verschlüsselung. Für starke Verschlüsselung ist eine Mindestschlüssellänge von 128 Bits erforderlich. Microsoft Windows enthält ebenfalls CSPs, die starke Verschlüsselungstypen anbieten, wie z. B. den 'Microsoft Strong Cryptographic Provider'. Um Ihnen eine Vorstellung zu geben, 128-Bit-Verschlüsselung wird von Banken verwendet, um die Verbindung mit ihren Internetbanking-Systemen zu verschlüsseln.

Mit Aspose.Cells for Python können Sie Microsoft Excel-Dateien mit Ihrem gewünschten Verschlüsselungstyp verschlüsseln und mit einem Passwort schützen.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

Um die Dateiverschlüsselungseinstellungen in Microsoft Excel festzulegen (hier Microsoft Excel 2003):

1. Wählen Sie im Menü **Extras** die Option **Optionen** aus. Es wird ein Dialogfeld angezeigt.
1. Wählen Sie den Tab **Sicherheit** aus.
1. Geben Sie ein Passwort ein und klicken Sie auf **Erweitert**
1. Wählen Sie den Verschlüsselungstyp aus und bestätigen Sie das Passwort.

## **Excel-Datei mit Aspose.Cells verschlüsseln**

Das folgende Beispiel zeigt, wie Sie mit dem Aspose.Cells-API eine Excel-Datei verschlüsseln und kennwortgeschützt machen können.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-CSharp-Files-Utility-EncryptingFiles-1.py" >}}

## **Entschlüsselung einer Excel-Datei mit Aspose.Cells**
Es ist sehr einfach, eine passwortgeschützte Excel-Datei zu öffnen und mit den folgenden Codes zu entschlüsseln, die Aspose.Cells-API zu verwenden:

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Decrypt-Excel-File.py" >}}


