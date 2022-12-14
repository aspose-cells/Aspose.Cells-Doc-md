---
title: Daten finden oder suchen
type: docs
weight: 50
url: /de/net/find-or-search-data/
---
{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Benutzern, Zellen in einem Arbeitsblatt zu finden, das bestimmte Daten enthält.

{{% /alert %}}

## **Suche nach Cells mit spezifizierten Daten**

### **Mit Microsoft Excel**

Microsoft Excel ermöglicht es Benutzern, Zellen in einem Arbeitsblatt zu finden, das bestimmte Daten enthält. Wenn Sie auswählen**Bearbeiten** von dem**Finden** Menü in Microsoft Excel, sehen Sie einen Dialog, in dem Sie den Suchwert angeben können.

Hier suchen wir nach dem Wert „Oranges“. Aspose.Cells ermöglicht es Entwicklern auch, Zellen im Arbeitsblatt zu finden, die bestimmte Werte enthalten.

### **Mit Aspose.Cells**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Auflistung, die alle Zellen im Arbeitsblatt darstellt. Das[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Die Sammlung bietet mehrere Methoden zum Suchen von Zellen in einem Arbeitsblatt, das benutzerdefinierte Daten enthält. Einige dieser Verfahren werden nachstehend ausführlicher erörtert.

{{% alert color="primary" %}}

Alle Find-Methoden geben die Referenzen der Zellen zurück, die die angegebenen zu durchsuchenden Daten enthalten.

{{% /alert %}}

## **Suche nach Cells mit einer Formel**

 Entwickler können eine bestimmte Formel im Arbeitsblatt finden, indem sie die aufrufen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung[**Finden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) Methode. Typischerweise die[**Finden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)Die Methode akzeptiert drei Parameter:

- **Objekt:**Das Objekt, nach dem gesucht werden soll. Der Typ sollte int,double,DateTime,string,bool sein.
- **Vorherige Zelle:**Vorherige Zelle mit demselben Objekt. Dieser Parameter kann auf null gesetzt werden, wenn von Anfang an gesucht wird.
- FindOptions: Optionen zum Auffinden des gewünschten Objekts.

Die folgenden Beispiele verwenden Arbeitsblattdaten zum Üben von Suchmethoden:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **Suchen von Daten oder Formeln mit FindOptions**

 Es ist möglich, bestimmte Werte mithilfe von zu finden[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung[**Finden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) Methode mit verschiedenen[**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) . Typischerweise die[**Finden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)Die Methode akzeptiert die folgenden Parameter:

- **Suchwert**, die zu suchenden Daten oder Werte.
- **Vorherige Zelle**, die letzte Zelle, die denselben Wert enthielt. Dieser Parameter kann bei der Suche von Anfang an auf null gesetzt werden.
- **Optionen finden**, die Suchoptionen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **Es wird Cells gefunden, der den angegebenen Zeichenfolgenwert oder die angegebene Zahl enthält**

 Es ist möglich, bestimmte String-Werte zu finden, indem Sie diese aufrufen[**Finden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) Methode gefunden in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung mit diversen[**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

 Präzisiere das[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) und[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype)Eigenschaften. Der folgende Beispielcode veranschaulicht, wie diese Eigenschaften verwendet werden, um Zellen mit einer unterschiedlichen Anzahl von Zeichenfolgen zu finden**Anfang** oder bei der**Center** oder bei der**Ende** der Zeichenfolge der Zelle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **Themen vorantreiben**
- [Finden Sie Cells mit einem bestimmten Stil](/cells/de/net/find-cells-with-specific-style/)
- [Finden Sie heraus, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt](/cells/de/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Suchen Sie Daten mit Originalwerten](/cells/de/net/search-data-using-original-values/)
