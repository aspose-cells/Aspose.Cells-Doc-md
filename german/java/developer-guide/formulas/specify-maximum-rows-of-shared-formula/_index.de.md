---
title: Maximale Zeilen der gemeinsamen Formel angeben
type: docs
weight: 40
url: /de/java/specify-maximum-rows-of-shared-formula/
---

## **Mögliche Verwendungsszenarien**

Die Standardmaximalzahl der Zeilen einer gemeinsam genutzten Formel beträgt 64. Es könnte jede Zahl sein, z.B. es könnte 1000 sein. Die Leistung der gemeinsam genutzten Formel ändert sich mit einer unterschiedlichen Anzahl von Zeilen. Daher bietet Aspose.Cells die [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula) Eigenschaft, die verwendet werden kann, um die maximale Anzahl der Zeilen einer gemeinsam genutzten Formel anzugeben. Die gemeinsam genutzte Formel wird in mehrere gemeinsam genutzte Formeln aufgeteilt, wenn die Gesamtzahl der Zeilen der gemeinsam genutzten Formel größer ist als in der folgenden Bildschirmaufnahme gezeigt.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Maximale Zeilen der gemeinsamen Formel angeben**

Der folgende Beispielcode erläutert die Verwendung der [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula) Eigenschaft. Es setzt die maximale Anzahl der Zeilen einer gemeinsam genutzten Formel auf 5 und fügt die gemeinsam genutzte Formel in Zelle D1 für 100 Zeilen hinzu und speichert sie in der [Ausgabedatei Excel] (61767869.xlsx). Wenn Sie den Inhalt der Ausgabedatei Excel extrahieren und die *sheet1.xml* überprüfen, sehen Sie, dass die gemeinsam genutzte Formel nach jeweils 5 Zeilen aufgeteilt wird, wie in der obigen Bildschirmaufnahme hervorgehoben.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
{{< app/cells/assistant language="java" >}}
