---
title: Benannten Bereich in einer Arbeitsmappe bearbeiten
type: docs
weight: 90
url: /de/cpp/manipulate-named-range-in-a-workbook/
---
##  **Mögliche Nutzungsszenarien**
 Aspose.Cells unterstützt die Bearbeitung vorhandener benannter Bereiche. Auf alle vorhandenen benannten Bereiche kann zugegriffen werden[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/) Sammlung. Sobald Sie auf den benannten Bereich zugreifen, können Sie seine verschiedenen Methoden ändern, z[GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)Und[GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
##  **Benannten Bereich in einer Arbeitsmappe bearbeiten**
 Der folgende Beispielcode liest den ersten benannten Bereich innerhalb von[Quell-Excel-Datei](23167008.xlsx) und druckt es aus[Voller Text](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)Und[Bezieht sich auf](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) Eigenschaften auf der Konsole. Danach wird die Eigenschaft `RefersTo` geändert und gespeichert[Excel-Datei ausgeben](23167009.xlsx).
##  **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
##  **Konsolenausgabe**
 Die folgende Konsolenausgabe gibt die Werte von aus[Voller Text](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)Und[Bezieht sich auf](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) Mitglieder der bestehenden*Benannter Bereich*im obigen Code.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
