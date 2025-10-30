---
title: Angabe von signifikanten Ziffern, die in eine Excel Datei mit Golang via C++ gespeichert werden sollen
linktitle: Festlegung der signifikanten Ziffern
type: docs
weight: 30
url: /de/go-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Erfahren Sie, wie man signifikante Ziffern in Excel Dateien mit Aspose.Cells und Golang via C++ angibt.
---

## **Mögliche Verwendungsszenarien**

Standardmäßig speichert Aspose.Cells 17 signifikante Ziffern von Double-Werten in der Excel-Datei, im Gegensatz zu MS-Excel, das nur 15 signifikante Ziffern speichert. Sie können dieses Standardverhalten von 17 auf 15 signifikante Ziffern mit der [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/) Eigenschaft ändern.

## **Angabe von signifikanten Ziffern, die in der Excel-Datei gespeichert werden sollen**

Der folgende Beispielcode erzwingt, dass Aspose.Cells beim Speichern von Double-Werten in der Excel-Datei 15 signifikante Ziffern verwendet. Überprüfen Sie die [Ausgabe-Excel-Datei](22774105.xlsx). Benennen Sie die Erweiterung in .zip um und entpacken Sie sie, dann sehen Sie, dass nur 15 signifikante Ziffern in der Excel-Datei gespeichert sind. Das folgende Screenshot zeigt die Wirkung der [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/) Eigenschaft auf die Ausgabedatei.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingSignificantDigitsToBeStoredInExcelFile.go" >}}
