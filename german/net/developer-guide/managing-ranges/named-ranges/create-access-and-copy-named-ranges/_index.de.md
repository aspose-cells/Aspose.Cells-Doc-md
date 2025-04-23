---
title: Zugriff erstellen und benannte Bereiche kopieren
type: docs
weight: 200
url: /de/net/create-access-and-copy-named-ranges/
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

## **Arbeiten mit benannten Bereich unter Verwendung von Aspose.Cells**

Hier verwenden wir die Aspose.Cells API, um die Aufgabe zu erledigen.
Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jede Arbeitsmappe in einer Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung.

### **Benannten Bereich erstellen**

Es ist möglich, einen benannten Bereich zu erstellen, indem die überladene [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index)-Methode der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung aufgerufen wird. Eine typische Version der [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3)-Methode nimmt die folgenden Parameter:

- Name der oberen linken Zelle, Name der oberen linken Zelle im Bereich.
- Name der unteren rechten Zelle, Name der unteren rechten Zelle im Bereich.

Wenn die Methode [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) aufgerufen wird, wird der neu erstellte Bereich als Instanz der Klasse [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) zurückgegeben. Verwenden Sie dieses Objekt [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range), um den benannten Bereich zu konfigurieren. Setzen Sie beispielsweise den Namen des Bereichs mit der [**Name**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name)-Eigenschaft. Das folgende Beispiel zeigt, wie man einen benannten Bereich von Zellen erstellt, der sich über B4:G14 erstreckt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **Zugriff auf benannte Bereiche**

#### **Auf einen bestimmten benannten Bereich zugreifen**

Rufen Sie die Methode [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) der [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)-Sammlung auf, um einen Bereich nach dem angegebenen Namen zu erhalten. Eine typische [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname)-Methode nimmt den Namen des benannten Bereichs entgegen und gibt den angegebenen benannten Bereich als Instanz der [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)-Klasse zurück. Das folgende Beispiel zeigt, wie auf einen bestimmten Bereich nach seinem Namen zugegriffen wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **Zugriff auf alle benannten Bereiche in einer Arbeitsmappe**

Rufen Sie die Methode [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) der [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)-Sammlung auf, um alle benannten Bereiche in einer Arbeitsmappe zu erhalten. Die [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges)-Methode gibt ein Array aller benannten Bereiche in der [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)-Sammlung zurück.

Das folgende Beispiel zeigt, wie auf alle benannten Bereiche in einer Arbeitsmappe zugegriffen wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **Benannte Bereiche kopieren**

Aspose.Cells bietet die [**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index)-Methode zum Kopieren eines Zellenbereichs mit Formatierung in einen anderen Bereich.

Das folgende Beispiel zeigt, wie ein Quellbereich von Zellen in einen anderen benannten Bereich kopiert wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
