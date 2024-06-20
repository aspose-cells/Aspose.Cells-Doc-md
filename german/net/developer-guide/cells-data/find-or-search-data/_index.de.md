---
title: Daten finden oder suchen
type: docs
weight: 50
url: /de/net/find-or-search-data/
description: Erfahren Sie, wie Sie Zellen in einem Arbeitsblatt finden oder durch die Aspose.Cells for .NET API nach spezifischen Daten suchen können
keywords: Suchen Sie Daten, Suchen Sie Zellen mit einer Formel, Suchen Sie Zellen mit einer Formel, Finden Sie Daten oder Formeln mit FindOptions, Suchen Sie Daten oder Formeln mit FindOptions, Finden oder Suchen Sie Zellen mit einem bestimmten Zeichenwert oder einer Zahl, Finden oder Suchen Sie Zellen mit bestimmten Daten
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Benutzern, in einem Arbeitsblatt Zellen zu finden, die bestimmte Daten enthalten.

{{% /alert %}}

## **Suchen von Zellen, die bestimmte Daten enthalten**

### **Verwendung von Microsoft Excel**

Microsoft Excel ermöglicht es Benutzern, in einem Arbeitsblatt Zellen zu finden, die bestimmte Daten enthalten. Wenn Sie **Bearbeiten** im **Suchen**-Menü in Microsoft Excel auswählen, wird ein Dialogfeld angezeigt, in dem Sie den Suchwert angeben können.

Hier suchen wir nach dem Wert "Orangen". Aspose.Cells ermöglicht es Entwicklern auch, in einem Arbeitsblatt Zellen mit bestimmten Werten zu finden.

### **Verwendung von Aspose.Cells**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine Sammlung von [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) stellt eine Sammlung von [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) dar, die alle Zellen im Arbeitsblatt repräsentiert. Die Sammlung [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) bietet mehrere Methoden zum Finden von Zellen in einem Arbeitsblatt, die vom Benutzer spezifizierte Daten enthalten. Einige dieser Methoden werden im Folgenden genauer erläutert.

{{% alert color="primary" %}}

Alle Find-Methoden geben die Verweise auf die Zellen zurück, die die angegebenen Daten enthalten.

{{% /alert %}}

## **Suchen von Zellen, die eine Formel enthalten**

Entwickler können eine bestimmte Formel im Arbeitsblatt finden, indem sie die Methode [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) der Sammlung [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) aufrufen. Typischerweise akzeptiert die Methode [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) drei Parameter:

- **Objekt:** Das gesuchte Objekt. Der Typ sollte int, double, DateTime, string oder bool sein.
- **Vorherige Zelle:** Vorherige Zelle mit demselben Objekt. Dieser Parameter kann auf null gesetzt werden, wenn die Suche vom Anfang aus durchgeführt wird.
- FindOptions: Optionen zum Auffinden des gesuchten Objekts.

Die folgenden Beispiele verwenden Arbeitsblattdaten, um die Find-Methoden zu üben:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **Suchen von Daten oder Formeln mithilfe von FindOptions**

Es ist möglich, angegebene Werte mithilfe der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Methode der [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)-Sammlung mit verschiedenen [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) zu finden. Normalerweise akzeptiert die Methode [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) die folgenden Parameter:

- **Suchwert**, die Daten oder der Wert, nach dem gesucht werden soll.
- **Vorherige Zelle**, die letzte Zelle, die den gleichen Wert enthielt. Dieser Parameter kann auf null gesetzt werden, wenn von Anfang an gesucht wird.
- **Suchoptionen**, die Suchoptionen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **Zellen finden, die den angegebenen Zeichenfolgenwert oder die angegebene Zahl enthalten**

Es ist möglich, angegebene Zeichenfolgenwerte zu finden, indem dieselbe [**Find**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)-Methode in der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung mit verschiedenen [**FindOptions**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) aufgerufen wird.

Geben Sie die [**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype)- und [**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype)-Eigenschaften an. Das folgende Beispielcode veranschaulicht die Verwendung dieser Eigenschaften zum Auffinden von Zellen mit verschiedener Anzahl von Zeichenfolgen am **Anfang** oder in der **Mitte** oder am **Ende** der Zellzeichenfolge.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **Erweiterte Themen**
- [Zellen mit bestimmtem Stil finden](/cells/de/net/find-cells-with-specific-style/)
- [Finden, ob der Zellenwert mit einem einzelnen Anführungszeichen beginnt](/cells/de/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Daten mithilfe der Originalwerte suchen](/cells/de/net/search-data-using-original-values/)
