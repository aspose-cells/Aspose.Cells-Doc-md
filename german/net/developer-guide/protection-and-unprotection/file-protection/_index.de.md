---
title: Excel-Dateien verschlüsseln und entschlüsseln
type: docs
weight: 10
url: /de/net/encrypt-and-decrypt-excel-files/
description: So verschlüsseln und entschlüsseln Sie Excel-Dateien mit C#. Sperren und entsperren Sie Excel-Dateien.
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

## **Excel-Datei mit Aspose.Cells verschlüsseln**

Das folgende Beispiel zeigt, wie eine Excel-Datei mit Aspose.Cells API verschlüsselt und mit einem Kennwort geschützt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Festlegen des Kennworts zum Ändern der Option**

 Das folgende Beispiel zeigt, wie die eingestellt wird**Zu änderndes Passwort** Microsoft Excel-Option für eine vorhandene Datei mit der Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}


## **Excel-Datei mit Aspose.Cells entschlüsseln**
Es ist sehr wichtig, eine passwortgeschützte Excel-Datei zu öffnen und mit den folgenden Codes Aspose.Cells API zu entschlüsseln:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Decrypt-Excel-File.cs" >}}


## **Themen vorantreiben**
- [ODS-Dateien verschlüsseln und entschlüsseln](/cells/de/net/encrypt-and-decrypt-ods-files/)
- [Festlegen des starken Verschlüsselungstyps](/cells/de/net/setting-strong-encryption-type/)
- [Geben Sie beim Schreibschutz der Arbeitsmappe den Autor an](/cells/de/net/specify-author-while-write-protecting-workbook/)
- [Überprüfen Sie das Passwort verschlüsselter Dateien](/cells/de/net/verify-password-of-encrypted-excel-and-ods-files/)

