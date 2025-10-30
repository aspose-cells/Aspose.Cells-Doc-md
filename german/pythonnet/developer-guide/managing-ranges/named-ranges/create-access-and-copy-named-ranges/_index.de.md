---
title: Zugriff erstellen und benannte Bereiche kopieren
type: docs
weight: 200
url: /de/python-net/create-access-and-copy-named-ranges/
description: In diesem Artikel wird gezeigt, wie Sie benannte Bereiche erstellen, darauf zugreifen und kopieren, mithilfe der Aspose.Cells for Python via .NET API.
keywords: Python Excel Bibliothek, Python Benannte Bereiche erstellen, darauf zugreifen und kopieren, Benannte Bereiche in Python erstellen, Benannte Bereiche in Python kopieren, Auf alle benannten Bereiche in einer Kalkulationstabelle zugreifen Python.
---

## **Einführung**

Normalerweise werden Spalten- und Zeilenbezeichnungen verwendet, um auf individuelle Zellen zu verweisen. Es ist möglich, aussagekräftige Namen zu erstellen, um Zellen, Zellenbereiche, Formeln oder Konstantenwerte zu repräsentieren. Das Wort **Name** kann sich auf eine Zeichenfolge beziehen, die eine Zelle, einen Zellenbereich, eine Formel oder einen Konstantenwert darstellt. Durch Zuweisen eines Namens an einen Bereich kann auf diesen Bereich von seinem Namen aus zugegriffen werden. Verwenden Sie leicht verständliche Namen, wie z.B. Produkte, um auf schwer verständliche Bereiche, wie z.B. Umsatz!C20:C30, zu verweisen. Bezeichnungen können in Formeln verwendet werden, die sich auf Daten im gleichen Arbeitsblatt beziehen; wenn Sie einen Bereich auf einem anderen Arbeitsblatt darstellen möchten, können Sie einen Namen verwenden. *Benannte Bereiche gehören zu den leistungsfähigsten Funktionen von Microsoft Excel, insbesondere wenn sie als Quellbereich für Listensteuerungen, Pivot-Tabellen, Diagramme usw. verwendet werden.

## **Arbeiten mit benannten Bereich unter Verwendung von Microsoft Excel**

### **Benannte Bereiche erstellen**

Die folgenden Schritte beschreiben, wie man eine Zelle oder einen Zellenbereich mit **MS Excel** benennt. Diese Methode gilt für **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** und **2002**.

1. Wählen Sie die Zelle oder den Zellenbereich aus, den Sie benennen möchten.
1. Klicken Sie auf das **Namensfeld** am linken Ende der Formelzeile.
1. Geben Sie den Namen für die Zellen ein.
1. Drücken Sie die EINGABETASTE.

{{% alert color="primary" %}}

Sie können eine Zelle nicht benennen, während Sie den Inhalt der Zelle ändern.

{{% /alert %}}

## **Arbeiten mit benannten Bereichen mit Aspose.Cells für Python Excel-Bibliothek**

Hier verwenden wir die Aspose.Cells for Python via .NET API, um die Aufgabe zu erledigen.
Aspose.Cells für Python via .NET bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) stellt eine [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung bereit.

### **Benannten Bereich erstellen**

Es ist möglich, einen benannten Bereich zu erstellen, indem die überladene [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str)-Methode der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung aufgerufen wird. Eine typische Version der [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str)-Methode nimmt die folgenden Parameter:

- Name der oberen linken Zelle, Name der oberen linken Zelle im Bereich.
- Name der unteren rechten Zelle, Name der unteren rechten Zelle im Bereich.

Wenn die Methode [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) aufgerufen wird, wird der neu erstellte Bereich als Instanz der Klasse [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) zurückgegeben. Verwenden Sie dieses Objekt [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range), um den benannten Bereich zu konfigurieren. Setzen Sie beispielsweise den Namen des Bereichs mit der [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/range/name)-Eigenschaft. Das folgende Beispiel zeigt, wie man einen benannten Bereich von Zellen erstellt, der sich über B4:G14 erstreckt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CreateNamedRangeofCells-1.py" >}}

### **Daten in die Zellen des benannten Bereichs eingeben**

Sie können Daten in die einzelnen Zellen eines Bereichs einfügen, indem Sie dem Muster folgen

- **C#**: Range[row,column]
- **VB**: Range(row,column)

Angenommen, Sie haben einen benannten Bereich von Zellen, der sich über A1:C4 erstreckt. Die Matrix enthält 4 * 3 = 12 Zellen. Die einzelnen Bereichszellen sind sequentiell angeordnet: Bereich[0,0], Bereich[0,1], Bereich[0,2], Bereich[1,0], Bereich[1,1], Bereich[1,2], Bereich[2,0], Bereich[2,1], Bereich[2,2], Bereich[3,0], Bereich[3,1], Bereich[3,2].

Verwenden Sie die folgenden Eigenschaften, um die Zellen im Bereich zu identifizieren:

- FirstRow gibt den Index der ersten Zeile im benannten Bereich zurück.
- FirstColumn gibt den Index der ersten Spalte im benannten Bereich zurück.
- RowCount gibt die Gesamtanzahl der Zeilen im benannten Bereich zurück.
- ColumnCount gibt die Gesamtanzahl der Spalten im benannten Bereich zurück.

Das folgende Beispiel zeigt, wie einige Werte in die Zellen eines bestimmten Bereichs eingegeben werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-InputDataInCellsInRange-1.py" >}}

### **Zellen im benannten Bereich identifizieren**

Sie können Daten in die einzelnen Zellen eines Bereichs einfügen, indem Sie dem Muster folgen:

- **C#**: Range[row,column]
- **VB**: Range(row,column)

Wenn Sie einen benannten Bereich haben, der A1:C4 umfasst. Die Matrix umfasst 4 * 3 = 12 Zellen. Die einzelnen Bereichszellen sind sequentiell angeordnet: Bereich[0,0], Bereich[0,1], Bereich[0,2], Bereich[1,0] ,Bereich[1,1], Bereich[1,2], Bereich[2,0], Bereich[2,1], Bereich[2,2], Bereich[3,0], Bereich[3,1], Bereich[3,2].

Verwenden Sie die folgenden Eigenschaften, um die Zellen im Bereich zu identifizieren:

- FirstRow gibt den Index der ersten Zeile im benannten Bereich zurück.
- FirstColumn gibt den Index der ersten Spalte im benannten Bereich zurück.
- RowCount gibt die Gesamtanzahl der Zeilen im benannten Bereich zurück.
- ColumnCount gibt die Gesamtanzahl der Spalten im benannten Bereich zurück.

Das folgende Beispiel zeigt, wie einige Werte in die Zellen eines bestimmten Bereichs eingegeben werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IdentifyCellsinNamedRange-1.py" >}}

### **Zugriff auf benannte Bereiche**

#### **Auf einen bestimmten benannten Bereich zugreifen**

Rufen Sie die Methode [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str) der [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)-Sammlung auf, um einen Bereich nach dem angegebenen Namen zu erhalten. Eine typische [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str)-Methode nimmt den Namen des benannten Bereichs entgegen und gibt den angegebenen benannten Bereich als Instanz der [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)-Klasse zurück. Das folgende Beispiel zeigt, wie auf einen bestimmten Bereich nach seinem Namen zugegriffen wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessSpecificNamedRange-1.py" >}}

#### **Zugriff auf alle benannten Bereiche in einer Arbeitsmappe**

Rufen Sie die Methode [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#) der [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)-Sammlung auf, um alle benannten Bereiche in einer Arbeitsmappe zu erhalten. Die [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#)-Methode gibt ein Array aller benannten Bereiche in der [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)-Sammlung zurück.

Das folgende Beispiel zeigt, wie auf alle benannten Bereiche in einer Arbeitsmappe zugegriffen wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessAllNamedRanges-1.py" >}}

### **Benannte Bereiche kopieren**

Aspose.Cells für Python via .NET bietet die Methode [**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range) zum Kopieren eines Zellenbereichs mit Formatierung in einen anderen Bereich an.

Das folgende Beispiel zeigt, wie ein Quellbereich von Zellen in einen anderen benannten Bereich kopiert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CopyNamedRanges-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
