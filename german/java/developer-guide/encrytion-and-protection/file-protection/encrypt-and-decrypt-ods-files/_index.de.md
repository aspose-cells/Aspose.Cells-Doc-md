---
title: ODS-Dateien verschlüsseln und entschlüsseln
type: docs
weight: 10
url: /de/java/encrypt-and-decrypt-ods-files/
description: Schützen und verschlüsseln Sie ODS-Dateien mit Aspose.Cells for Java, einer reinen Java-Bibliothek.
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

## **ODS-Datei verschlüsseln/entschlüsseln:**

 Um eine ODS-Datei zu verschlüsseln, laden Sie die Datei und übergeben Sie das tatsächliche Passwort an[**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) bevor Sie es speichern. Die ausgegebene verschlüsselte ODS-Datei kann nur in OpenOffice geöffnet werden. Laden Sie zum Entschlüsseln einer ODS-Datei die Datei, indem Sie das Kennwort in der Datei angeben[**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password) . Sobald die Datei geladen ist, rufen Sie die Funktion auf[**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String) ) mit dem tatsächlichen Passwort als Argument und übergeben Sie schließlich null an[**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **Beispielcode:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
