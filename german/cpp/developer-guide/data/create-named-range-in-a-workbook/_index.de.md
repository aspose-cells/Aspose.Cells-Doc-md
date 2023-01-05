---
title: Benannten Bereich in einer Arbeitsmappe erstellen
type: docs
weight: 60
url: /de/cpp/create-named-range-in-a-workbook/
---
## **Mögliche Nutzungsszenarien**
 Aspose.Cells unterstützt die Erstellung eines benannten Bereichs. Es gibt verschiedene Möglichkeiten, einen benannten Bereich zu erstellen. Eine der einfachsten Möglichkeiten besteht darin, zuerst zu erstellen[IRange](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range) Objekt und legen Sie dann seinen Namen mit fest[IRange.SetName()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#a78480b6b6db0f24cffc8acc2b06552eb) Methode. Sie können alle benannten Bereiche in Ihrer Excel-Datei über Microsoft Excel sehen*Name-Manager*Schnittstelle.
## **Benannten Bereich in einer Arbeitsmappe erstellen**
 Im folgenden Beispielcode wird erläutert, wie Sie eine*Benannter Bereich* über Aspose.Cells. Einmal die*Benannter Bereich* erstellt wird, ist es innerhalb der sichtbar[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) Sammlung. Bitte sehen Sie sich ... an[Excel-Datei ausgeben](23167006.xlsx) generiert durch den Code für eine Referenz.
## **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook.cpp" >}}
## **Konsolenausgabe**
 Die folgende Konsolenausgabe gibt die Werte von aus[GetFullText](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563) und `GetRefersTo` Methoden des Erschaffenen*Benannter Bereich*im obigen Code.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
