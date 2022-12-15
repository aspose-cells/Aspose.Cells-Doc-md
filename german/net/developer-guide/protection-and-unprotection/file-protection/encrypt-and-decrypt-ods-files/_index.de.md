---
title: ODS-Dateien verschlüsseln und entschlüsseln
type: docs
weight: 10
url: /de/net/encrypt-and-decrypt-ods-files/
description: ODS-Dateien mit Passwort schützen und verschlüsseln, indem Aspose.Cells für .Net verwendet wird, das eine reine Netzbibliothek ist.
---
{{% alert color="primary" %}}
 OpenOffice.org ist eine Office-Suite mit vollem Funktionsumfang, die den Passwortschutz und die Verschlüsselung von Dateien unterstützt. Die verschlüsselte ODS-Datei kann jedoch nur von OpenOffice geöffnet werden, nachdem das Kennwort angegeben wurde. Excel kann die verschlüsselte ODS-Datei nicht öffnen und gibt möglicherweise eine Warnmeldung aus. Die Verschlüsselungsoptionen gelten im Gegensatz zu anderen Dateitypen nicht für ODS-Dateien.
 Aspose.Cells ermöglicht das Verschlüsseln und Entschlüsseln von ODS-Dateien. Entschlüsselte ODS-Datei kann sowohl in Excel als auch in OpenOffice geöffnet werden,
{{% /alert %}}

## **Verschlüsseln mit OpenOffice Calc**
1.  Auswählen**Speichern als** und Klicken Sie auf die**Mit Passwort speichern** Kasten.
1.  Drücke den**Speichern** Taste.
1.  Geben Sie Ihr gewünschtes Passwort in beide ein**Geben Sie das Passwort zum Öffnen ein** und**Passwort bestätigen** Felder im sich öffnenden Fenster Passwort festlegen.
1.  Drücke den**OK** Schaltfläche, um die Datei zu speichern.

## **ODS-Datei mit Aspose.Cells für .Net verschlüsseln**
 Um eine ODS-Datei zu verschlüsseln, laden Sie die Datei und stellen Sie die[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) Wert auf das eigentliche Passwort, bevor Sie es speichern. Die ausgegebene verschlüsselte ODS-Datei kann nur in OpenOffice geöffnet werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **ODS-Datei mit Aspose.Cells für .Net entschlüsseln**

 Laden Sie zum Entschlüsseln einer ODS-Datei die Datei, indem Sie ein Kennwort in der Datei angeben[**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . Sobald die Datei geladen ist, legen Sie die[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) Zeichenfolge auf null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
