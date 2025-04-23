---
title: Mehrere Arbeitsbücher zu einem einzelnen Arbeitsbuch zusammenführen
linktitle: Arbeitsmappen Zusammenführung
type: docs
weight: 66
url: /de/net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}}

Manchmal müssen Arbeitsbücher mit verschiedenen Inhalten wie Bilder, Diagramme und Daten in einem einzigen Arbeitsbuch zusammengeführt werden. Aspose.Cells unterstützt diese Funktion. Dieser Artikel zeigt, wie man eine Konsolenanwendung in Visual Studio erstellt und Arbeitsbücher mit ein paar einfachen Zeilen Code mithilfe von Aspose.Cells zusammenführt.

{{% /alert %}}

## **Arbeitsbücher mit Bildern und Diagrammen kombinieren**

Der Beispielcode kombiniert mit Aspose.Cells zwei Arbeitsbücher zu einem einzigen Arbeitsbuch. Der Code lädt die Quell-Arbeitsbücher, verwendet die Methode [**Workbook.combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) zur Kombination und speichert das Ausgabearbeitsbuch.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CombineMultipleWorkbooksSingleWorkbook-1.cs" >}}

## **Erweiterte Themen**
- [Mehrere Arbeitsblätter in ein einziges Arbeitsblatt kombinieren](/cells/de/net/combine-multiple-worksheets-into-a-single-worksheet/)
- [Dateien zusammenführen](/cells/de/net/merge-files/)
{{< app/cells/assistant language="csharp" >}}
