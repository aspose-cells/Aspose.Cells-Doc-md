---
title: Mehrere Arbeitsmappen zu einer einzigen Arbeitsmappe mit Golang über C++ zusammenfassen
linktitle: Arbeitsmappen Zusammenführung
type: docs
weight: 66
url: /de/go-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Lernen Sie, wie Sie mehrere Arbeitsmappen mit Aspose.Cells in Golang über C++ zu einer einzigen zusammenfassen.
---

{{% alert color="primary" %}}

Manchmal müssen Sie Arbeitsmappen mit verschiedenen Inhalten wie Bildern, Diagrammen und Daten in eine einzige Arbeitsmappe zusammenfügen. Aspose.Cells unterstützt diese Funktion. Dieser Artikel zeigt, wie man mit Visual Studio eine Konsolenanwendung erstellt und Arbeitsmappen mit wenigen Zeilen Code mit Aspose.Cells kombiniert.

{{% /alert %}}

## **Arbeitsbücher mit Bildern und Diagrammen kombinieren**

Der Beispielcode kombiniert mit Aspose.Cells zwei Arbeitsbücher zu einem einzigen Arbeitsbuch. Der Code lädt die Quell-Arbeitsbücher, verwendet die Methode [**Workbook::Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) zur Kombination und speichert das Ausgabearbeitsbuch.

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeWorkbooks.go" >}}
## **Erweiterte Themen**
- [Mehrere Arbeitsblätter in ein einziges Arbeitsblatt kombinieren](/cells/de/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Dateien zusammenführen](/cells/de/cpp/merge-files/)
