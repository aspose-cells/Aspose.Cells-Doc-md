---
title: Festlegen signifikanter Stellen, die in einer Excel-Datei gespeichert werden sollen
type: docs
weight: 20
url: /de/java/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **Mögliche Nutzungsszenarien**

Standardmäßig speichert Aspose.Cells 17 signifikante Ziffern von Double-Werten in Tabellenkalkulationen im Gegensatz zur Excel-Anwendung, die nur 15 signifikante Ziffern speichert. Sie können das Standardverhalten von Aspose.Cells für diesen Fall ändern, das heißt; Sie können die Anzahl der signifikanten Stellen von 17 auf 15 ändern, während Sie die verwenden[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)Eigentum.

## **Festlegen signifikanter Stellen, die in einer Excel-Datei gespeichert werden sollen**

 Der folgende Beispielcode erzwingt, dass Aspose.Cells 15 signifikante Ziffern verwendet, während doppelte Werte in der Excel-Datei gespeichert werden. Bitte überprüfen Sie die[Excel-Datei ausgeben](23166982.xlsx) . Ändern Sie die Erweiterung in .zip und entpacken Sie sie, und Sie werden sehen, dass nur 15 signifikante Ziffern in der Excel-Datei gespeichert sind. Der folgende Screenshot erklärt die Wirkung von[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)-Eigenschaft in der Excel-Ausgabedatei.

![todo: Bild_alt_Text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
