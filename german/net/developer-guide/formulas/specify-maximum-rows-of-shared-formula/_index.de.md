---
title: Maximale Zeilen der gemeinsamen Formel angeben
type: docs
weight: 40
url: /de/net/specify-maximum-rows-of-shared-formula/
---

## **Mögliche Verwendungsszenarien**

Die Standard-Maximalzeilen der gemeinsamen Formel sind 64. Es könnte jede beliebige Zahl sein, z.B. 1000. Die Leistung der gemeinsamen Formel ändert sich mit einer unterschiedlichen Anzahl von Zeilen. Daher bietet Aspose.Cells die Eigenschaft [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula), die verwendet werden kann, um die maximalen Zeilen der gemeinsamen Formel festzulegen. Die gemeinsame Formel wird auf mehrere gemeinsame Formeln aufgeteilt, wenn die Gesamtzeilen der gemeinsamen Formel größer sind als in der folgenden Bildschirmaufnahme gezeigt.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Maximale Zeilen der gemeinsamen Formel angeben**

Der folgende Beispielcode erläutert die Verwendung der Eigenschaft [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula). Es setzt die maximalen Zeilen der gemeinsamen Formel auf 5 und fügt die gemeinsame Formel in Zelle D1 für 100 Zeilen hinzu und speichert sie in der [Ausgabedatei für Excel](61767856.xlsx). Wenn Sie die Inhalte der Ausgabedatei für Excel extrahieren und die *sheet1.xml* überprüfen, sehen Sie, dass die gemeinsame Formel nach jeweils 5 Zeilen aufgeteilt ist, wie in der obigen Bildschirmaufnahme hervorgehoben.

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-SpecifyMaximumRowsOfSharedFormula.cs" >}}
{{< app/cells/assistant language="csharp" >}}
