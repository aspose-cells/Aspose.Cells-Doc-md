---
title: Zugriff auf die Tabelle von Cell und Hinzufügen von Werten darin mithilfe von Zeilen- und Spalten-Offsets
type: docs
weight: 110
url: /de/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 Normalerweise fügen Sie Werte innerhalb des Tabellen- oder Listenobjekts hinzu, indem Sie verwenden[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)) Methode. Aber manchmal müssen Sie möglicherweise Werte innerhalb des Tabellen- oder Listenobjekts hinzufügen, indem Sie die Zeilen- und Spalten-Offsets verwenden.

Um von einer Zelle aus auf Tabellen- oder Listenobjekte zuzugreifen, verwenden Sie die[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ) Methode. Und um darin Werte mithilfe der Zeilen- und Spalten-Offsets hinzuzufügen, verwenden Sie die[**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) Methode.

{{% /alert %}}

## Beispiel

### Screenshots, die die Quell- und Ausgabedateien vergleichen

 Der folgende Screenshot zeigt die im Code verwendete Excel-Quelldatei. Sie enthält die leere Tabelle und hebt die Zelle D5 hervor, die innerhalb der Tabelle liegt. Auf diese Tabelle greifen wir von Zelle D5 aus mit zu[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ) Methode und fügen Sie dann die darin enthaltenen Werte mit beiden hinzu[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean) ) und[**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) Methoden.

![todo: Bild_alt_Text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

Der folgende Screenshot zeigt die vom Code generierte Excel-Ausgabedatei. Wie Sie sehen können, hat Zelle D5 einen Wert und Zelle F6, die sich am Offset 2,2 der Tabelle befindet, hat einen Wert.

![todo: Bild_alt_Text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Java-Code für den Zugriff auf die Tabelle aus der Zelle und das Hinzufügen von Werten darin mithilfe von Zeilen- und Spalten-Offsets

Der folgende Beispielcode lädt die Excel-Quelldatei, wie im obigen Screenshot gezeigt, fügt Werte in die Tabelle ein und generiert die Excel-Ausgabedatei, wie oben gezeigt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
