---
title: Mehrere Arbeitsbücher zu einem einzelnen Arbeitsbuch zusammenführen
linktitle: Arbeitsmappen Zusammenführung
type: docs
weight: 66
url: /de/python-net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}}

Manchmal müssen Sie Arbeitsmappen mit verschiedenen Inhalten wie Bildern, Diagrammen und Daten in eine einzige Arbeitsmappe zusammenfügen. Aspose.Cells für Python via .NET unterstützt diese Funktion. Dieser Artikel zeigt, wie man eine Konsolenanwendung in Visual Studio erstellt und Arbeitsmappen mit wenigen einfachen Codezeilen mithilfe von Aspose.Cells für Python via .NET zusammenführt.

{{% /alert %}}

## **Arbeitsbücher mit Bildern und Diagrammen kombinieren**

Das Beispielcode verbindet zwei Arbeitsmappen zu einer einzigen Arbeitsmappe mit Aspose.Cells für Python via .NET. Der Code lädt die Quellarbeitsmappen, verwendet die Methode [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) zum Zusammenfügen und speichert die Ausgabearbeitsmappe.

### **Quell-Arbeitsbücher**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Ausgabearbeitsbücher**

- [combined.xlsx](5473095.xlsx)

### **Screenshots**

Nachfolgend finden Sie Screenshots der Quell- und Ausgabearbeitsbücher.

{{% alert color="primary" %}}

Sie können beliebige Quellarbeitsmappen verwenden. Diese Bilder dienen nur zur Veranschaulichung.

{{% /alert %}}

**Die erste Arbeitsblatt der Diagramme Arbeitsmappe - gestapelt** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Zweites Arbeitsblatt der Diagramme Arbeitsmappe - Linie** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Erstes Arbeitsblatt der Bild Arbeitsmappe - Bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Alle drei Arbeitsblätter in der kombinierten Arbeitsmappe - gestapelt, Linie, Bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CombineMultipleWorkbooksSingleWorkbook-1.py" >}}

## **Erweiterte Themen**
- [Mehrere Arbeitsblätter in ein einziges Arbeitsblatt kombinieren](/cells/de/python-net/combine-multiple-worksheets-into-a-single-worksheet/)
- [Dateien zusammenführen](/cells/de/python-net/merge-files/)

{{< app/cells/assistant language="python-net" >}}
