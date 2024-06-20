---
title: Angabe von signifikanten Ziffern, die in der Excel Datei gespeichert werden sollen
type: docs
weight: 30
url: /de/net/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **Mögliche Verwendungsszenarien**

Standardmäßig speichert Aspose.Cells 17 signifikante Ziffern von Gleitkommazahlen in der Excel-Datei, im Gegensatz zu MS-Excel, das nur 15 signifikante Ziffern speichert. Sie können das Standardverhalten von Aspose.Cells von 17 signifikanten Ziffern auf 15 signifikante Ziffern ändern, indem Sie die Eigenschaft [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits) verwenden.

## **Angabe von signifikanten Ziffern, die in der Excel-Datei gespeichert werden sollen**

Der folgende Beispielcode erzwingt Aspose.Cells, 15 signifikante Ziffern beim Speichern von Gleitkommazahlen in der Excel-Datei zu verwenden. Bitte überprüfen Sie die [Ausgabedatei](22774105.xlsx). Ändern Sie die Erweiterung in .zip, entpacken Sie sie und Sie sehen, dass nur 15 signifikante Ziffern in der Excel-Datei gespeichert sind. Der folgende Screenshot erklärt die Auswirkung der Eigenschaft [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits) auf die Ausgabedatei.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}
