---
title: ODS Dateien verschlüsseln und entschlüsseln
type: docs
weight: 10
url: /de/net/encrypt-and-decrypt-ods-files/
description: Passwortschutz und Verschlüsselung von ODS Dateien mit Aspose.Cells für .Net, das eine reine .NET Bibliothek ist.
---

{{% alert color="primary" %}}
OpenOffice.org ist eine voll ausgestattete Office-Suite, die die Passwortschutz und Verschlüsselung von Dateien unterstützt. Jedoch kann eine verschlüsselte ODS-Datei nur von OpenOffice geöffnet werden, nachdem das Passwort eingegeben wurde. Excel kann die verschlüsselte ODS-Datei nicht öffnen und möglicherweise eine Warnmeldung anzeigen. Die Verschlüsselungsoptionen sind nicht für ODS-Dateien wie für andere Dateitypen anwendbar. 
Aspose.Cells ermöglicht es, ODS-Dateien zu verschlüsseln und zu entschlüsseln. Entschlüsselte ODS-Dateien können sowohl in Excel als auch in OpenOffice geöffnet werden. 
{{% /alert %}}

## **Mit OpenOffice Calc verschlüsseln**
1. Wählen Sie **Speichern unter** und aktivieren Sie das Kästchen **Mit Passwort speichern**.
1. Klicken Sie auf die **Speichern**-Schaltfläche.
1. Geben Sie Ihr gewünschtes Passwort in die Felder **Kennwort eingeben zum Öffnen** und **Kennwort bestätigen** im Fenster **Passwort festlegen** ein, das geöffnet wird. 
1. Klicken Sie auf die Schaltfläche **OK**, um die Datei zu speichern.

## **ODS-Datei mit Aspose.Cells für .Net verschlüsseln**
Für die Verschlüsselung einer ODS-Datei laden Sie die Datei und setzen Sie den Wert [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) auf das tatsächliche Passwort, bevor Sie sie speichern. Die verschlüsselte Ausgabedatei im ODS-Format kann nur in OpenOffice geöffnet werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **ODS-Datei mit Aspose.Cells für .Net entschlüsseln**

Für das Entschlüsseln einer ODS-Datei laden Sie die Datei, indem Sie ein Passwort in [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) angeben. Sobald die Datei geladen ist, setzen Sie den Wert [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) auf null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
