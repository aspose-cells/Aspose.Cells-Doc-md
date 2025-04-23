---
title: Kopieren des VBA Makro UserForm DesignerStorage von der Vorlage in die Zieltabelle
type: docs
weight: 60
url: /de/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es Ihnen, das VBA-Projekt von einer Excel-Datei in eine andere Excel-Datei zu kopieren. Das VBA-Projekt besteht aus verschiedenen Arten von Modulen, d.h. Dokument, Prozedur, Designer usw. Alle Module können mit einfachem Code kopiert werden, aber für das Designermodul gibt es zusätzliche Daten namens Designer Storage, auf die zugegriffen oder kopiert werden muss. Die folgenden beiden Methoden behandeln das Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-)

## **Kopieren Sie den VBA-Makro UserForm-DesignerStorage von der Vorlage in die Zieldatei**

Bitte sehen Sie sich den folgenden Beispielscode an. Er kopiert das VBA-Projekt von der [Vorlagen-Excel-Datei](50528367.xlsm) in eine leere Arbeitsmappe und speichert sie als die [Ausgabe-Excel-Datei](50528366.xlsm). Wenn Sie das VBA-Projekt in der Vorlagen-Excel-Datei öffnen, sehen Sie ein User-Formular wie unten gezeigt. Das User-Formular besteht aus dem Designer Storage, der mithilfe der [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-)- und [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-)-Methoden kopiert wird.

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

Der folgende Screenshot zeigt die Ausgabe-Excel-Datei und ihre Inhalte, die von der Vorlagen-Excel-Datei kopiert wurden. Wenn Sie auf Button 1 klicken, öffnet sich das VBA-Benutzerformular, das selbst eine Befehlsschaltfläche hat, die beim Klicken eine Meldungsfeld anzeigt.

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
