---
title: Text in Spalten konvertieren mithilfe von Aspose.Cells
type: docs
weight: 30
url: /de/net/convert-text-to-columns-using-aspose-cells/
---

## **Mögliche Verwendungsszenarien**

Sie können Ihren Text in Spalten mit Microsoft Excel umwandeln. Diese Funktion ist unter dem Register *Daten* in den *Datentools* verfügbar. Um den Inhalt einer Spalte in mehrere Spalten aufzuteilen, sollte die Daten einen spezifischen Trennzeichen wie ein Komma (oder ein anderes Zeichen) enthalten, anhand dessen Microsoft Excel den Inhalt einer Zelle in mehrere Zellen aufteilt. Aspose.Cells bietet diese Funktion auch über die [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)-Methode.

## **Text in Spalten konvertieren mit Aspose.Cells**

Der folgende Beispielscode erläutert die Verwendung der [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) Methode. Der Code fügt zuerst einige Personennamen in Spalte A des ersten Arbeitsblatts hinzu. Der Vor- und Nachname ist durch ein Leerzeichen getrennt. Dann wendet er die [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) Methode auf Spalte A an und speichert es als Ausgabedatei Excel. Wenn Sie die [Ausgabedatei Excel](25395213.xlsx) öffnen, sehen Sie, dass die Vornamen in Spalte A stehen, während die Nachnamen in Spalte B stehen, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}
{{< app/cells/assistant language="csharp" >}}
