---
title: Zugriff auf die Tabelle von Cell und Hinzufügen von Werten darin mithilfe von Zeilen- und Spalten-Offsets
type: docs
weight: 230
url: /de/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 Normalerweise fügen Sie Werte innerhalb des Tabellen- oder Listenobjekts hinzu, indem Sie verwenden[**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)Methode. Aber manchmal müssen Sie möglicherweise Werte innerhalb des Tabellen- oder Listenobjekts hinzufügen, indem Sie die Zeilen- und Spalten-Offsets verwenden.

Um von einer Zelle aus auf Tabellen- oder Listenobjekte zuzugreifen, verwenden Sie die[**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) Methode. Um darin Werte mithilfe der Zeilen- und Spalten-Offsets hinzuzufügen, verwenden Sie die[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) Methode.

{{% /alert %}}

 Der folgende Screenshot zeigt die im Code verwendete Excel-Quelldatei. Sie enthält die leere Tabelle und hebt die Zelle D5 hervor, die innerhalb der Tabelle liegt. Auf diese Tabelle greifen wir von Zelle D5 aus mit zu[**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) -Methode und fügen Sie dann die darin enthaltenen Werte mit beiden hinzu[**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) und[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue)Methoden.

## Beispiel

### Screenshots, die die Quell- und Ausgabedateien vergleichen

|![todo: Bild_alt_Text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
|:- |

Der folgende Screenshot zeigt die vom Code generierte Excel-Ausgabedatei. Wie Sie sehen können, hat Zelle D5 einen Wert und Zelle F6, die sich am Offset 2,2 der Tabelle befindet, hat einen Wert.

|![todo: Bild_alt_Text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
|:- |

### C#-Code für den Zugriff auf die Tabelle aus der Zelle und das Hinzufügen von Werten darin mithilfe von Zeilen- und Spalten-Offsets

Der folgende Beispielcode lädt die Excel-Quelldatei, wie im obigen Screenshot gezeigt, fügt Werte in die Tabelle ein und generiert die Excel-Ausgabedatei, wie oben gezeigt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
