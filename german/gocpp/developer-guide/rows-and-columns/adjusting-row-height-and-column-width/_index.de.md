---
title: Anpassen der Zeilenhöhe und Spaltenbreite
type: docs
weight: 10
url: /de/go-cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}}

Wenn Sie mit Tabellenkalkulationen arbeiten und Daten zu Zeilen oder Spalten hinzufügen, müssen Sie möglicherweise die Höhe von Zeilen oder die Breite von Spalten ändern. Manchmal muss die aktuelle Höhe oder Breite geändert werden, um Daten anzuzeigen, wenn Formatierungen auf Zeilen oder Spalten angewendet werden. Normalerweise passen Benutzer die Zeilenhöhen und Spaltenbreiten in einer WYSIWYG-Umgebung mit Microsoft Excel an. Aber mit Aspose.Cells können Entwickler diese Operationen zur Laufzeit durchführen.

{{% /alert %}}

## **Arbeiten mit Zeilen**

### **Anpassen der Zeilenhöhe**

Aspose.Cells stellt eine Klasse bereit, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse enthält eine [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/), die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) dargestellt. Die [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) Klasse bietet eine [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung, die alle Zellen im Arbeitsblatt repräsentiert. Die [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung stellt mehrere Methoden zur Verwaltung von Zeilen oder Spalten in einem Arbeitsblatt bereit. Einige davon werden im Folgenden detaillierter besprochen.

#### **Die Höhe einer Zeile festlegen**

Es ist möglich, die Höhe einer einzelnen Zeile festzulegen, indem die [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung's [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) Methode aufgerufen wird. Die [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) Methode nimmt die folgenden Parameter entgegen:

- **Zeilenindex**, der Index der Zeile, deren Höhe geändert wird.
- **Zeilenhöhe**, die auf die Zeile anzuwendende Zeilenhöhe.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-GPP-SettingHeightOfRow.go" >}}

#### **Die Höhe aller Zeilen in einem Arbeitsblatt festlegen**

Wenn Entwickler die gleiche Zeilenhöhe für alle Zeilen im Arbeitsblatt festlegen müssen, können sie dies mit der [SetStandardHeight](https://reference.aspose.com/cells/go-cpp/cells/setstandardheight/) Methode der [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung tun.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingHeightOfAllRowsInWorksheet.go" >}}

## **Arbeiten mit Spalten**

### **Einstellen der Breite einer Spalte**

Setzen Sie die Spaltenbreite, indem Sie die [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung mit der [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) Methode aufrufen. Die [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) Methode akzeptiert die folgenden Parameter:

- **Spaltenindex**, der Index der Spalte, deren Breite geändert wird.
- **Spaltenbreite**, die gewünschte Spaltenbreite.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfColumn.go" >}}

### **Einstellen der Breite aller Spalten in einem Arbeitsblatt**

Um die gleiche Spaltenbreite für alle Spalten im Arbeitsblatt festzulegen, verwenden Sie die [Cells](https://reference.aspose.com/cells/go-cpp/cells/) Sammlung mit der [SetStandardWidth](https://reference.aspose.com/cells/go-cpp/cells/setstandardwidth/) Methode.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfAllColumnsInWorksheet.go" >}}
