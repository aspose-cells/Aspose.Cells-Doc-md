---
title: Geben Sie die maximalen Zeilen der freigegebenen Formel an
type: docs
weight: 40
url: /de/java/specify-maximum-rows-of-shared-formula/
---
## **Mögliche Nutzungsszenarien**

Die standardmäßige maximale Anzahl von Zeilen der freigegebenen Formel ist 64. Es kann eine beliebige Zahl sein, z. B. 1000. Die Leistung der freigegebenen Formel ändert sich mit einer anderen Anzahl von Zeilen. Daher bietet die Aspose.Cells die[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)Eigenschaft, die verwendet werden kann, um die maximalen Zeilen der freigegebenen Formel anzugeben. Die freigegebene Formel wird auf mehrere freigegebene Formeln aufgeteilt, wenn die Gesamtzahl der Zeilen der freigegebenen Formel größer ist, wie im folgenden Screenshot gezeigt.

![todo: Bild_alt_Text](specify-maximum-rows-of-shared-formula_1.png)

## **Geben Sie die maximalen Zeilen der freigegebenen Formel an**

Der folgende Beispielcode erläutert die Verwendung der[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)Eigentum. Es setzt die maximalen Zeilen der freigegebenen Formel auf 5 und fügt die freigegebene Formel in Zelle D1 für 100 Zeilen hinzu und speichert in[Excel-Datei ausgeben](61767869.xlsx). Wenn Sie den Inhalt der ausgegebenen Excel-Datei extrahieren und die*Blatt1.xml*, sehen Sie die freigegebenen Formelaufteilungen nach jeweils 5 Zeilen, wie im obigen Screenshot hervorgehoben.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
