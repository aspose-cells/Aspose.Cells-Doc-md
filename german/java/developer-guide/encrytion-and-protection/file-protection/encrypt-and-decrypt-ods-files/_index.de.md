---
title: ODS Dateien verschlüsseln und entschlüsseln
type: docs
weight: 10
url: /de/java/encrypt-and-decrypt-ods-files/
description: Schützen Sie ODS Dateien mit Aspose.Cells for Java, einer reinen Java Bibliothek, durch Passwortschutz und Verschlüsselung.
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

## **Verschlüsseln/Entschlüsseln einer ODS-Datei:**

Um eine ODS-Datei zu verschlüsseln, laden Sie die Datei und geben Sie das tatsächliche Passwort an [**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) an, bevor Sie sie speichern. Die Ausgabe verschlüsselter ODS-Dateien kann nur in OpenOffice geöffnet werden. Um eine ODS-Datei zu entschlüsseln, laden Sie die Datei, indem Sie das Passwort in das [**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password) eingeben. Sobald die Datei geladen ist, rufen Sie die Funktion [**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String)) mit dem tatsächlichen Passwort als Argument auf und geben schließlich null an [**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) weiter.

### **Beispielcode:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
