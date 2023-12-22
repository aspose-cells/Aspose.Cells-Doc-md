---
title: Erstellen Sie einen benannten Bereich in einer Arbeitsmappe
type: docs
weight: 60
url: /de/cpp/create-named-range-in-a-workbook/
---
##  **Mögliche Nutzungsszenarien**
 Aspose.Cells unterstützt die Erstellung eines benannten Bereichs. Es gibt verschiedene Möglichkeiten, einen benannten Bereich zu erstellen. Eine der einfachsten Möglichkeiten besteht darin, zunächst etwas zu erstellen[Reichweite](https://reference.aspose.com/cells/cpp/aspose.cells/range) Objekt und legen Sie dann seinen Namen mit fest[Range.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname) Methode. Sie können alle benannten Bereiche in Ihrer Excel-Datei über Microsoft Excel sehen*Namensmanager*Schnittstelle.
##  **Erstellen Sie einen benannten Bereich in einer Arbeitsmappe**
 Der folgende Beispielcode erklärt, wie man einen erstellt*Benannter Bereich* über Aspose.Cells. Einmal, die*Benannter Bereich* erstellt wird, ist es im Inneren sichtbar[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames) Sammlung. Bitte sehen Sie sich ... an[Excel-Datei ausgeben](23167006.xlsx) vom Code als Referenz generiert.
##  **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
##  **Konsolenausgabe**
 Die folgende Konsolenausgabe gibt die Werte von aus[GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) Und[GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) Methoden des Geschaffenen*Benannter Bereich*im obigen Code.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
