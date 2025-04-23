---
title: Festlegung von Signifikanten Stellen, die in Excel Datei gespeichert werden sollen
type: docs
weight: 20
url: /de/java/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **Mögliche Verwendungsszenarien**

Standardmäßig speichert Aspose.Cells 17 signifikante Stellen von Double-Werten in Tabellenkalkulationen, im Gegensatz zur Excel-Anwendung, die nur 15 signifikante Stellen speichert. Sie können das Standardverhalten von Aspose.Cells für diesen Fall ändern, d.h. Sie können die Anzahl der signifikanten Stellen von 17 auf 15 ändern, während Sie die Eigenschaft [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits) verwenden.

## **Festlegung von Signifikanten Stellen, die in Excel-Datei gespeichert werden sollen**

Der folgende Beispielcode zwingt Aspose.Cells dazu, 15 signifikante Stellen zu verwenden, während Double-Werte in der Excel-Datei gespeichert werden. Bitte überprüfen Sie die [ausgegebene Excel-Datei](23166982.xlsx). Ändern Sie ihre Erweiterung in .zip und entpacken Sie sie. Sie werden sehen, dass nur 15 signifikante Stellen in der Excel-Datei gespeichert sind. Der folgende Screenshot erläutert die Wirkung der Eigenschaft [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits) auf die ausgegebene Excel-Datei.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
{{< app/cells/assistant language="java" >}}
