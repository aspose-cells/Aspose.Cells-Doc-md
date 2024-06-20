---
title: Benannter Bereich in einer Arbeitsmappe erstellen
type: docs
weight: 60
url: /de/cpp/create-named-range-in-a-workbook/
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells unterstützt die Erstellung eines benannten Bereichs. Es gibt verschiedene Möglichkeiten, einen benannten Bereich zu erstellen. Eine der einfachsten Möglichkeiten ist, zuerst ein [Range](https://de.reference.aspose.com/cells/cpp/aspose.cells/range)-Objekt zu erstellen und dann seinen Namen mithilfe der Methode [Range.SetName()](https://de.reference.aspose.com/cells/cpp/aspose.cells/range/setname) zu setzen. Sie können alle benannten Bereiche in Ihrer Excel-Datei über die Schnittstelle *Namensmanager* von Microsoft Excel sehen.
## **Benannten Bereich in einem Arbeitsbuch erstellen**
Der folgende Beispielscode erläutert, wie ein *benannter Bereich* über Aspose.Cells erstellt wird. Sobald der *benannte Bereich* erstellt ist, ist er in der Sammlung [Workbook.GetWorksheets().GetNames()](https://de.reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames) sichtbar. Bitte beachten Sie die [Ausgabedatei der Excel-Datei](23167006.xlsx), die vom Code für eine Referenz generiert wurde.
## **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
## **Konsolenausgabe**
Die folgende Konsolenausgabe gibt die Werte der Methoden [GetFullText](https://de.reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) und [GetRefersTo](https://de.reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) des erstellten *benannten Bereichs* im obigen Code aus.

{{< highlight java >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
