---
title: ODS Dateien verschlüsseln und entschlüsseln
type: docs
weight: 10
url: /de/python-net/encrypt-and-decrypt-ods-files/
description: Passwortgeschützte und verschlüsselte ODS Dateien mit Aspose.Cells für Python via .NET, einer reinen .NET Bibliothek.
---

{{% alert color="primary" %}}
OpenOffice.org ist eine voll ausgestattete Office-Suite, die die Passwortschutz und Verschlüsselung von Dateien unterstützt. Jedoch kann eine verschlüsselte ODS-Datei nur von OpenOffice geöffnet werden, nachdem das Passwort eingegeben wurde. Excel kann die verschlüsselte ODS-Datei nicht öffnen und möglicherweise eine Warnmeldung anzeigen. Die Verschlüsselungsoptionen sind nicht für ODS-Dateien wie für andere Dateitypen anwendbar. 
Aspose.Cells für Python via .NET ermöglicht die Verschlüsselung und Entschlüsselung von ODS-Dateien. Entschlüsselte ODS-Dateien können sowohl in Excel als auch in OpenOffice geöffnet werden. 
{{% /alert %}}

## **Mit OpenOffice Calc verschlüsseln**
1. Wählen Sie **Speichern unter** und aktivieren Sie das Kästchen **Mit Passwort speichern**.
1. Klicken Sie auf die **Speichern**-Schaltfläche.
1. Geben Sie Ihr gewünschtes Passwort in die Felder **Kennwort eingeben zum Öffnen** und **Kennwort bestätigen** im Fenster **Passwort festlegen** ein, das geöffnet wird. 
1. Klicken Sie auf die Schaltfläche **OK**, um die Datei zu speichern.

## **Ods-Datei mit Aspose.Cells für Python via .NET verschlüsseln**
Für die Verschlüsselung einer ODS-Datei laden Sie die Datei und setzen Sie den Wert [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) auf das tatsächliche Passwort, bevor Sie sie speichern. Die verschlüsselte Ausgabedatei im ODS-Format kann nur in OpenOffice geöffnet werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

## **Ods-Datei mit Aspose.Cells für Python via .NET entsperren**

Für das Entschlüsseln einer ODS-Datei laden Sie die Datei, indem Sie ein Passwort in [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password) angeben. Sobald die Datei geladen ist, setzen Sie den Wert [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) auf null.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
