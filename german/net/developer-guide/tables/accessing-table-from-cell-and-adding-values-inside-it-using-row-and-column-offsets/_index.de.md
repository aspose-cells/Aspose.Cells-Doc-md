---
title: Zugriff auf Tabelle von Zelle und Hinzufügen von Werten in sie unter Verwendung von Zeilen und Spaltenversatz
type: docs
weight: 230
url: /de/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalerweise fügen Sie Werte in die Tabelle oder das Listenobjekt mit der [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)-Methode ein. Manchmal müssen Sie jedoch Werte in die Tabelle oder das Listenobjekt unter Verwendung des Zeilen- und Spaltenoffsets hinzufügen.

Um auf eine Tabelle oder eine Liste aus einer Zelle zuzugreifen, verwenden Sie die [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) Methode. Um Werte unter Verwendung der Zeilen- und Spaltenversätze hinzuzufügen, verwenden Sie die [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) Methode.

{{% /alert %}}

Der folgende Screenshot zeigt die verwendete Excel-Quelldatei im Code. Sie enthält die leere Tabelle und hebt die Zelle D5 hervor, die sich innerhalb der Tabelle befindet. Wir werden auf diese Tabelle von der Zelle D5 aus mit der [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable)-Methode zugreifen und dann die Werte darin mit den [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)- und [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue)-Methoden hinzufügen.

## Beispiel

### Screenshots zum Vergleich der Quell- und Ausgabedateien

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

Der folgende Screenshot zeigt die durch den Code generierte Ausgabedatei. Wie Sie sehen können, hat die Zelle D5 einen Wert und die Zelle F6, die sich im Offset 2,2 der Tabelle befindet, hat ebenfalls einen Wert.

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### C#-Code, um auf die Tabelle aus der Zelle zuzugreifen und Werte mit Zeilen- und Spaltenversätzen hinzuzufügen

Der folgende Beispielcode lädt die oben gezeigte Excel-Quelldatei und fügt Werte in die Tabelle ein, um die oben gezeigte Ausgabedatei zu generieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
{{< app/cells/assistant language="csharp" >}}
