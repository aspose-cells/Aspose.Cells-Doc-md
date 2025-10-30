---
title: Zugriff auf Tabelle von Zelle und Hinzufügen von Werten in sie unter Verwendung von Zeilen und Spaltenversatz
type: docs
weight: 230
url: /de/python-net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalerweise fügen Sie Werte in die Tabelle oder das Listenobjekt mit der [**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool)-Methode ein. Manchmal müssen Sie jedoch Werte in die Tabelle oder das Listenobjekt unter Verwendung des Zeilen- und Spaltenoffsets hinzufügen.

Um auf eine Tabelle oder eine Liste aus einer Zelle zuzugreifen, verwenden Sie die [**Cell.get_table()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_table/#) Methode. Um Werte unter Verwendung der Zeilen- und Spaltenversätze hinzuzufügen, verwenden Sie die [**ListObject.put_cell_value**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/put_cell_value/#int-int-any) Methode.

{{% /alert %}}

Der folgende Screenshot zeigt die verwendete Excel-Quelldatei im Code. Sie enthält die leere Tabelle und hebt die Zelle D5 hervor, die sich innerhalb der Tabelle befindet. Wir werden auf diese Tabelle von der Zelle D5 aus mit der [**Cell.get_table()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_table/#)-Methode zugreifen und dann die Werte darin mit den [**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool)- und [**ListObject.put_cell_value**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/put_cell_value/#int-int-any)-Methoden hinzufügen.

## Beispiel

### Screenshots zum Vergleich der Quell- und Ausgabedateien

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

Der folgende Screenshot zeigt die durch den Code generierte Ausgabedatei. Wie Sie sehen können, hat die Zelle D5 einen Wert und die Zelle F6, die sich im Offset 2,2 der Tabelle befindet, hat ebenfalls einen Wert.

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### Python-Code zum Zugriff auf Tabelle aus Zelle und zum Hinzufügen von Werten innerhalb der Tabelle unter Verwendung von Zeilen- und Spaltenoffsets

Der folgende Beispielcode lädt die oben gezeigte Excel-Quelldatei und fügt Werte in die Tabelle ein, um die oben gezeigte Ausgabedatei zu generieren.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-AccessTableFromCellAndAddValue.py" >}}
{{< app/cells/assistant language="python-net" >}}
