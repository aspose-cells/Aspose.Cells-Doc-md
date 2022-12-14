---
title: Zugriff erstellen und benannte Bereiche kopieren
type: docs
weight: 200
url: /de/net/create-access-and-copy-named-ranges/
---
## **Einführung**

Normalerweise beziehen sich Spalten- und Zeilenbeschriftungen auf einzelne Zellen. Es ist möglich, aussagekräftige Namen zu erstellen, um Zellen, Zellbereiche, Formeln oder konstante Werte darzustellen. Das Wort**Name** kann sich auf eine Zeichenfolge beziehen, die eine Zelle, einen Zellbereich, eine Formel oder einen konstanten Wert darstellt. Das Zuweisen eines Namens zu einem Bereich bedeutet, dass auf diesen Zellbereich mit seinem Namen verwiesen werden kann. Verwenden Sie leicht verständliche Namen, z. B. Produkte, um auf schwer verständliche Bereiche zu verweisen, z. B. Sales!C20:C30. Beschriftungen können in Formeln verwendet werden, die auf Daten auf demselben Arbeitsblatt verweisen; Wenn Sie einen Bereich auf einem anderen Arbeitsblatt darstellen möchten, können Sie einen Namen verwenden. *Benannte Bereiche gehören zu den leistungsstärksten Funktionen von Microsoft Excel, insbesondere wenn sie als Quellbereich für Listensteuerelemente, Pivot-Tabellen, Diagramme usw. verwendet werden.

## **Arbeiten mit benannten Bereichen mit Microsoft Excel**

### **Benannte Bereiche erstellen**

 Die folgenden Schritte beschreiben, wie Sie eine Zelle oder einen Zellbereich mit benennen**MS-Excel** . Diese Methode gilt für**Microsoft Office Excel 2003**, **MicrosoftExcel 97**, **2000** und**2002**.

1. Wählen Sie die Zelle oder den Zellbereich aus, den Sie benennen möchten.
1.  Drücke den**Namensfeld** am linken Ende der Bearbeitungsleiste.
1. Geben Sie den Namen für die Zellen ein.
1. Drücken Sie Enter.

{{% alert color="primary" %}}

Sie können eine Zelle nicht benennen, während Sie den Inhalt der Zelle ändern.

{{% /alert %}}

## **Arbeiten mit benanntem Bereich unter Verwendung von Aspose.Cells**

Hier verwenden wir die Aspose.Cells API, um die Aufgabe zu erledigen.
 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung.

### **Benannten Bereich erstellen**

 Es ist möglich, einen benannten Bereich zu erstellen, indem Sie die überladene aufrufen[**Bereich erstellen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung. Eine typische Version von[**Bereich erstellen**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) Die Methode nimmt die folgenden Parameter an:

- Name der oberen linken Zelle, der Name der oberen linken Zelle im Bereich.
- Name der unteren rechten Zelle, der Name der unteren rechten Zelle im Bereich.

 Wenn der[**Bereich erstellen**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) -Methode aufgerufen wird, gibt sie den neu erstellten Bereich als Instanz von zurück[**Bereich**](https://reference.aspose.com/cells/net/aspose.cells/range) Klasse. Benutze das[**Bereich**](https://reference.aspose.com/cells/net/aspose.cells/range) Objekt, um den benannten Bereich zu konfigurieren. Legen Sie beispielsweise den Namen des Bereichs mithilfe von fest[**Name**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name) Eigentum. Das folgende Beispiel zeigt, wie Sie einen benannten Zellbereich erstellen, der sich über B4:G14 erstreckt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **Geben Sie Daten in Cells im benannten Bereich ein**

Sie können Daten nach dem Muster in die einzelnen Zellen eines Bereichs einfügen

- **C#**: Bereich[Zeile,Spalte]
- **VB**: Bereich (Zeile, Spalte)

Angenommen, Sie haben einen benannten Zellbereich, der sich über A1:C4 erstreckt. Die Matrix ergibt 4 * 3 = 12 Zellen. Die einzelnen Range-Zellen sind der Reihe nach angeordnet: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Bereich[2,0], Bereich[2,1], Bereich[2,2], Bereich[3,0], Bereich[3,1], Bereich[3,2].

Verwenden Sie die folgenden Eigenschaften, um die Zellen im Bereich zu identifizieren:

- FirstRow gibt den Index der ersten Zeile im benannten Bereich zurück.
- FirstColumn gibt den Index der ersten Spalte im benannten Bereich zurück.
- RowCount gibt die Gesamtzahl der Zeilen im benannten Bereich zurück.
- ColumnCount gibt die Gesamtzahl der Spalten im benannten Bereich zurück.

Das folgende Beispiel zeigt, wie einige Werte in die Zellen eines bestimmten Bereichs eingegeben werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **Identifizieren Sie Cells im benannten Bereich**

Sie können Daten nach folgendem Muster in die einzelnen Zellen eines Bereichs einfügen:

- **C#**: Bereich[Zeile,Spalte]
- **VB**: Bereich (Zeile, Spalte)

Wenn Sie einen benannten Bereich haben, der A1:C4 umfasst. Die Matrix ergibt 4 * 3 = 12 Zellen. Die einzelnen Range-Zellen sind der Reihe nach angeordnet: Range[0,0], Range[0,1], Range[0,2], Range[1,0] ,Range[1,1], Range[1,2], Bereich[2,0], Bereich[2,1], Bereich[2,2], Bereich[3,0], Bereich[3,1], Bereich[3,2].

Verwenden Sie die folgenden Eigenschaften, um die Zellen im Bereich zu identifizieren:

- FirstRow gibt den Index der ersten Zeile im benannten Bereich zurück.
- FirstColumn gibt den Index der ersten Spalte im benannten Bereich zurück.
- RowCount gibt die Gesamtzahl der Zeilen im benannten Bereich zurück.
- ColumnCount gibt die Gesamtzahl der Spalten im benannten Bereich zurück.

Das folgende Beispiel zeigt, wie einige Werte in die Zellen eines bestimmten Bereichs eingegeben werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **Greifen Sie auf benannte Bereiche zu**

#### **Greifen Sie auf einen bestimmten benannten Bereich zu**

 Ruf den[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) Sammlung[**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) -Methode, um einen Bereich mit dem angegebenen Namen abzurufen. Ein typisches[**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) -Methode nimmt den Namen des benannten Bereichs und gibt den angegebenen benannten Bereich als Instanz von zurück[**Bereich**](https://reference.aspose.com/cells/net/aspose.cells/range) Klasse. Das folgende Beispiel zeigt, wie auf einen angegebenen Bereich über seinen Namen zugegriffen wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **Greifen Sie auf alle benannten Bereiche in einer Tabelle zu**

 Ruf den[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) Sammlung[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) -Methode, um alle benannten Bereiche in einer Tabelle abzurufen. Das[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) -Methode gibt ein Array aller Namensbereiche in der zurück[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) Sammlung.

Das folgende Beispiel zeigt, wie auf alle benannten Bereiche in einer Arbeitsmappe zugegriffen wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **Benannte Bereiche kopieren**

 Aspose.Cells bietet[**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) Methode zum Kopieren eines Zellbereichs mit Formatierung in einen anderen Bereich.

Das folgende Beispiel zeigt, wie Sie einen Quellzellenbereich in einen anderen benannten Bereich kopieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
