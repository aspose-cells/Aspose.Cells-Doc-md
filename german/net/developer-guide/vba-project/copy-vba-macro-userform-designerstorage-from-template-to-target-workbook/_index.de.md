---
title: Kopieren des VBA Makro UserForm DesignerStorage von der Vorlage in die Zieltabelle
type: docs
weight: 130
url: /de/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es Ihnen, ein VBA-Projekt aus einer Excel-Datei in eine andere Excel-Datei zu kopieren. Das VBA-Projekt besteht aus verschiedenen Arten von Modulen, z. B. Dokument-, Prozedur- oder Designer-Modulen. Alle Module können mit einem einfachen Code kopiert werden, aber für das Designer-Modul gibt es zusätzliche Daten namens Designer Storage, die benötigt werden, um darauf zuzugreifen oder es zu kopieren. Die folgenden beiden Methoden beschäftigen sich mit Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **Kopieren Sie den VBA-Makro UserForm-DesignerStorage von der Vorlage in die Zieldatei**

Bitte sehen Sie den folgenden Beispielcode. Er kopiert das VBA-Projekt aus der [Vorlagen-Excel-Datei](50528345.xlsm) in eine leere Arbeitsmappe und speichert sie als die [Ausgabedatei](50528346.xlsm). Wenn Sie das VBA-Projekt innerhalb der Vorlagen-Excel-Datei öffnen, sehen Sie ein Benutzerformular wie unten gezeigt. Das Benutzerformular besteht aus Designer Storage, daher wird es mithilfe der Methoden [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage) und [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage) kopiert.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

Das nachfolgende Screenshot zeigt die Ausgabedatei und deren Inhalt, die aus der Vorlagen-Excel-Datei kopiert wurden. Wenn Sie auf die Schaltfläche 1 klicken, wird das VBA-Benutzerformular geöffnet, das selbst über eine Befehlsschaltfläche verfügt, die beim Klicken eine Meldungsfeld anzeigt.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
