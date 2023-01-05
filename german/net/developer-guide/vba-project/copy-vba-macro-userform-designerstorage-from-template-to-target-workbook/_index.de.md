---
title: Kopieren Sie VBA Macro UserForm DesignerStorage aus der Vorlage in die Zielarbeitsmappe
type: docs
weight: 130
url: /de/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells ermöglicht das Kopieren eines VBA-Projekts aus einer Excel-Datei in eine andere Excel-Datei. Ein VBA-Projekt besteht aus verschiedenen Arten von Modulen, z. B. Dokument, Prozedur, Designer usw. Alle Module können mit einfachem Code kopiert werden, aber für das Designer-Modul gibt es einige zusätzliche Daten namens Designer Storage, auf die zugegriffen oder kopiert werden muss. Die folgenden zwei Methoden befassen sich mit Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **Kopieren Sie VBA Macro UserForm DesignerStorage aus der Vorlage in die Zielarbeitsmappe**

Bitte sehen Sie sich den folgenden Beispielcode an. Es kopiert das VBA-Projekt aus der[Vorlage Excel-Datei](50528345.xlsm) in eine leere Arbeitsmappe und speichert sie als[Excel-Datei ausgeben](50528346.xlsm). Wenn Sie das VBA-Projekt in der Excel-Vorlagendatei öffnen, sehen Sie ein Benutzerformular wie unten gezeigt. Das Benutzerformular besteht aus Designer Storage, daher wird es mit kopiert[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)und[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)Methoden.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

Der folgende Screenshot zeigt die Excel-Ausgabedatei und deren Inhalt, die aus der Excel-Vorlagendatei kopiert wurden. Wenn Sie auf die Schaltfläche 1 klicken, wird das VBA-Benutzerformular geöffnet, das selbst über eine Befehlsschaltfläche verfügt, die beim Klicken ein Meldungsfeld anzeigt.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
