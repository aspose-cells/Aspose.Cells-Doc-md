---
title: Benannten Bereich in einer Arbeitsmappe bearbeiten
type: docs
weight: 90
url: /de/cpp/manipulate-named-range-in-a-workbook/
---
## **Mögliche Nutzungsszenarien**
 Aspose.Cells unterstützt die Manipulation bestehender benannter Bereiche. Auf alle vorhandenen benannten Bereiche kann zugegriffen werden[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) Sammlung. Sobald Sie auf den benannten Bereich zugreifen, können Sie seine verschiedenen Methoden ändern, z[GetFullText](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)und[GetRefersTo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36).
## **Benannten Bereich in einer Arbeitsmappe bearbeiten**
 Der folgende Beispielcode liest den ersten benannten Bereich innerhalb der[Excel-Quelldatei](23167008.xlsx) und druckt seine[Voller Text](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)und[Bezieht sich auf](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) Eigenschaften auf der Konsole. Danach ändert es die Eigenschaft `RefersTo` und speichert die[Excel-Datei ausgeben](23167009.xlsx).
## **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook.cpp" >}}
## **Konsolenausgabe**
 Die folgende Konsolenausgabe gibt die Werte von aus[Voller Text](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)und[Bezieht sich auf](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) Mitglieder der bestehenden*Benannter Bereich*im obigen Code.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
