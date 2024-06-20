---
title: Benannten Bereich in einer Arbeitsmappe manipulieren
type: docs
weight: 90
url: /de/cpp/manipulate-named-range-in-a-workbook/
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells unterstützt die Manipulation bestehender benannter Bereiche. Alle bestehenden benannten Bereiche können aus der [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/) Sammlung abgerufen werden. Sobald Sie den benannten Bereich zugreifen, können Sie seine verschiedenen Methoden ändern, z. B. [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) und [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
## **Benannten Bereich in einer Arbeitsmappe manipulieren**
Der folgende Beispielcode liest den ersten benannten Bereich in der [Quellexceldatei](23167008.xlsx) und gibt seine [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) und [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) Eigenschaften auf der Konsole aus. Danach ändert er die Eigenschaft `RefersTo` und speichert die [Ausgabeexceldatei](23167009.xlsx).
## **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
## **Konsolenausgabe**
Die folgende Konsolenausgabe gibt die Werte von [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) und [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) der vorhandenen *Benannten Bereich* im obigen Code aus.

{{< highlight java >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
