---
title: ODS-Dateien verschlüsseln und entschlüsseln
type: docs
weight: 10
url: /de/net/encrypt-and-decrypt-ods-files/
description: Schützen und verschlüsseln Sie ODS-Dateien mit einem Kennwort, indem Sie Aspose.Cells für .Net verwenden, das eine reine Netzbibliothek ist.
---
{{% alert color="primary" %}}
OpenOffice.org ist eine Office-Suite mit vollem Funktionsumfang, die den Passwortschutz und die Verschlüsselung von Dateien unterstützt. Die verschlüsselte ODS-Datei kann jedoch nur von OpenOffice geöffnet werden, nachdem das Kennwort angegeben wurde. Excel kann die verschlüsselte ODS-Datei nicht öffnen und gibt möglicherweise eine Warnmeldung aus. Die Verschlüsselungsoptionen gelten im Gegensatz zu anderen Dateitypen nicht für die ODS-Datei.
 Aspose.Cells ermöglicht das Verschlüsseln und Entschlüsseln der Datei ODS. Die entschlüsselte ODS-Datei kann sowohl in Excel als auch in OpenOffice geöffnet werden,
{{% /alert %}}

## **Verschlüsseln mit OpenOffice Calc**
1.  Wählen**Speichern als** und Klicken Sie auf die**Mit Passwort speichern** Kasten.
1.  Drücke den**Speichern** Knopf.
1.  Geben Sie Ihr gewünschtes Passwort in beide ein**Geben Sie das Passwort zum Öffnen ein** und**Kennwort bestätigen** Felder im sich öffnenden Fenster Passwort festlegen.
1.  Drücke den**OK** Schaltfläche, um die Datei zu speichern.

## **ODS-Datei mit Aspose.Cells für .Net verschlüsseln**
 Um eine ODS-Datei zu verschlüsseln, laden Sie die Datei und stellen Sie die[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) Wert auf das eigentliche Passwort, bevor Sie es speichern. Die verschlüsselte Ausgabedatei ODS kann nur in OpenOffice geöffnet werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **Entschlüsseln Sie die ODS-Datei mit Aspose.Cells für .Net**

 Um eine ODS-Datei zu entschlüsseln, laden Sie die Datei, indem Sie ein Passwort in der[**LoadOptions.Passwort**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . Sobald die Datei geladen ist, legen Sie die[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) Zeichenfolge auf null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
