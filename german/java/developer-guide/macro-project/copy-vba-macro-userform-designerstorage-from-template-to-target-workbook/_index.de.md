---
title: Kopieren Sie VBA Macro UserForm DesignerStorage aus der Vorlage in die Zielarbeitsmappe
type: docs
weight: 60
url: /de/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells ermöglicht es Ihnen, das VBA-Projekt von einer Excel-Datei in eine andere Excel-Datei zu kopieren. Das VBA-Projekt besteht aus verschiedenen Arten von Modulen, z. B. Dokument, Verfahren, Designer usw. Alle Module können mit einfachem Code kopiert werden, aber für das Designer-Modul gibt es einige zusätzliche Daten namens Designer Storage, auf die zugegriffen oder kopiert werden muss. Die folgenden zwei Methoden befassen sich mit Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String))
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[]))

## **Kopieren Sie VBA Macro UserForm DesignerStorage aus der Vorlage in die Zielarbeitsmappe**

Bitte sehen Sie sich den folgenden Beispielcode an. Es kopiert das VBA-Projekt aus der[Vorlage Excel-Datei](50528367.xlsm)in eine leere Arbeitsmappe und speichert sie als[Excel-Datei ausgeben](50528366.xlsm). Wenn Sie das VBA-Projekt in der Excel-Vorlagendatei öffnen, sehen Sie ein Benutzerformular wie unten gezeigt. Das Benutzerformular besteht aus Designer Storage, daher wird es mit kopiert[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String)) und[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[])) Methoden.

![todo: Bild_alt_Text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

Der folgende Screenshot zeigt die Excel-Ausgabedatei und deren Inhalt, die aus der Excel-Vorlagendatei kopiert wurden. Wenn Sie auf die Schaltfläche 1 klicken, wird das VBA-Benutzerformular geöffnet, das selbst über eine Befehlsschaltfläche verfügt, die beim Klicken ein Meldungsfeld anzeigt.

![todo: Bild_alt_Text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
