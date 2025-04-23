---
title: Zugriff auf Tabelle von Zelle und Hinzufügen von Werten in sie unter Verwendung von Zeilen und Spaltenversatz
type: docs
weight: 110
url: /de/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalerweise fügen Sie Werte in die Tabelle oder das Listenobjekt mit der [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue-boolean-)-Methode ein. Manchmal müssen Sie jedoch Werte in die Tabelle oder das Listenobjekt unter Verwendung des Zeilen- und Spaltenoffsets hinzufügen.

Verwenden Sie die [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--)-Methode, um auf die Tabelle oder das Listenobjekt von einer Zelle aus zuzugreifen. Und verwenden Sie die [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue-int-int-java.lang.Object-)-Methode, um Werte darin unter Verwendung des Zeilen- und Spaltenoffsets hinzuzufügen.

{{% /alert %}}

## Beispiel

### Screenshots zum Vergleich der Quell- und Ausgabedateien

Der folgende Screenshot zeigt die verwendete Excel-Quelldatei im Code. Sie enthält die leere Tabelle und hebt die Zelle D5 hervor, die sich innerhalb der Tabelle befindet. Wir werden auf diese Tabelle von der Zelle D5 aus mit der [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--)-Methode zugreifen und dann die Werte darin mit den [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue-boolean-)- und [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue-int-int-java.lang.Object-)-Methoden hinzufügen.

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

Der folgende Screenshot zeigt die durch den Code generierte Ausgabedatei. Wie Sie sehen können, hat die Zelle D5 einen Wert und die Zelle F6, die sich im Offset 2,2 der Tabelle befindet, hat ebenfalls einen Wert.

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Java-Code zum Zugriff auf die Tabelle von der Zelle und zum Hinzufügen von Werten darin unter Verwendung von Zeilen- und Spaltenoffsets

Der folgende Beispielcode lädt die oben gezeigte Excel-Quelldatei und fügt Werte in die Tabelle ein, um die oben gezeigte Ausgabedatei zu generieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
{{< app/cells/assistant language="java" >}}
