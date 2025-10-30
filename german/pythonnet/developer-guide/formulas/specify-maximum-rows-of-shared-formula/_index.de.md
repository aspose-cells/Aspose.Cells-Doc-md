---
title: Maximale Zeilen der gemeinsamen Formel angeben
type: docs
weight: 40
url: /de/python-net/specify-maximum-rows-of-shared-formula/
---

## **Mögliche Verwendungsszenarien**

Die Standard-Höchstzahl der Zeilen für die gemeinsame Formel beträgt 64. Es kann auch jede andere Zahl sein, z.B. 1000. Die Leistung der gemeinsamen Formel ändert sich mit der unterschiedlichen Anzahl von Zeilen. Daher bietet Aspose.Cells für Python via .NET die [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula)-Eigenschaft, die verwendet werden kann, um die maximale Anzahl der Zeilen der gemeinsamen Formel festzulegen. Die gemeinsame Formel wird in mehrere geteilte Formeln aufgespalten, falls die Gesamtzahl der Zeilen der gemeinsamen Formel größer ist, wie in folgendem Screenshot gezeigt.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Maximale Zeilen der gemeinsamen Formel angeben**

Der folgende Beispielcode erläutert die Verwendung der Eigenschaft [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula). Es setzt die maximalen Zeilen der gemeinsamen Formel auf 5 und fügt die gemeinsame Formel in Zelle D1 für 100 Zeilen hinzu und speichert sie in der [Ausgabedatei für Excel](61767856.xlsx). Wenn Sie die Inhalte der Ausgabedatei für Excel extrahieren und die *sheet1.xml* überprüfen, sehen Sie, dass die gemeinsame Formel nach jeweils 5 Zeilen aufgeteilt ist, wie in der obigen Bildschirmaufnahme hervorgehoben.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SpecifyMaximumRowsOfSharedFormula.py" >}}

{{< app/cells/assistant language="python-net" >}}
