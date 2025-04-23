---
title: Kopieren des VBA Makro UserForm DesignerStorage von der Vorlage in die Zieltabelle
type: docs
weight: 130
url: /de/python-net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells for Python via .NET ermöglicht es, ein VBA-Projekt von einer Excel-Datei in eine andere zu kopieren. Das VBA-Projekt besteht aus verschiedenen Modultypen, z.B. Dokument, Verfahren, Design, usw. Alle Module können mit einfachem Code kopiert werden, aber für das Designer-Modul gibt es zusätzliche Daten namens Designer Storage, auf die zugegriffen oder die kopiert werden müssen. Die folgenden zwei Methoden befassen sich mit Designer Storage.

- [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str)
- [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage/)

## **Kopieren Sie den VBA-Makro UserForm-DesignerStorage von der Vorlage in die Zieldatei**

Bitte sehen Sie den folgenden Beispielcode. Er kopiert das VBA-Projekt aus der [Vorlagen-Excel-Datei](50528345.xlsm) in eine leere Arbeitsmappe und speichert sie als die [Ausgabedatei](50528346.xlsm). Wenn Sie das VBA-Projekt innerhalb der Vorlagen-Excel-Datei öffnen, sehen Sie ein Benutzerformular wie unten gezeigt. Das Benutzerformular besteht aus Designer Storage, daher wird es mithilfe der Methoden [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str) und [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage) kopiert.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

Das nachfolgende Screenshot zeigt die Ausgabedatei und deren Inhalt, die aus der Vorlagen-Excel-Datei kopiert wurden. Wenn Sie auf die Schaltfläche 1 klicken, wird das VBA-Benutzerformular geöffnet, das selbst über eine Befehlsschaltfläche verfügt, die beim Klicken eine Meldungsfeld anzeigt.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.py" >}}

