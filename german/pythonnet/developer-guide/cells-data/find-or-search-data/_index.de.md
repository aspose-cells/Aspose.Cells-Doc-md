---
title: Daten finden oder suchen
type: docs
weight: 50
url: /de/python-net/find-or-search-data/
description: Erfahren Sie, wie Sie in einem Arbeitsblatt Zellen finden oder suchen, die bestimmte Daten über die Aspose.Cells for Python via .NET API enthalten.
keywords: Python Excel Bibliothek, Python Daten finden, Python Daten suchen, Python Zellen finden, die eine Formel enthalten, Python Zellen suchen, die eine Formel enthalten, Python Daten oder Formeln mit FindOptions finden, Python Daten oder Formeln mit FindOptions suchen, Python Zellen finden oder suchen, die bestimmte Zeichenfolgen oder Zahlwerte enthalten, Python Zellen finden oder suchen, die bestimmte Daten enthalten
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Benutzern, in einem Arbeitsblatt Zellen zu finden, die bestimmte Daten enthalten.

{{% /alert %}}

## **Suchen von Zellen, die bestimmte Daten enthalten**

### **Verwendung von Microsoft Excel**

Microsoft Excel ermöglicht es Benutzern, in einem Arbeitsblatt Zellen zu finden, die bestimmte Daten enthalten. Wenn Sie **Bearbeiten** im **Suchen**-Menü in Microsoft Excel auswählen, wird ein Dialogfeld angezeigt, in dem Sie den Suchwert angeben können.

Hier suchen wir nach dem Wert "Orangen". Aspose.Cells ermöglicht es Entwicklern auch, in einem Arbeitsblatt Zellen mit bestimmten Werten zu finden.

### **Verwendung von Aspose.Cells**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine Sammlung von [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) stellt eine Sammlung von [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) dar, die alle Zellen im Arbeitsblatt repräsentiert. Die Sammlung [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) bietet mehrere Methoden zum Finden von Zellen in einem Arbeitsblatt, die vom Benutzer spezifizierte Daten enthalten. Einige dieser Methoden werden im Folgenden genauer erläutert.

{{% alert color="primary" %}}

Alle Find-Methoden geben die Verweise auf die Zellen zurück, die die angegebenen Daten enthalten.

{{% /alert %}}

## **Suchen von Zellen, die eine Formel enthalten**

Entwickler können eine bestimmte Formel im Arbeitsblatt finden, indem sie die Methode [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) der Sammlung [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) aufrufen. Typischerweise akzeptiert die Methode [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) drei Parameter:

- **what:** Das zu suchende Objekt. Der Typ sollte int, double, DateTime, string, bool sein.
- **previous_cell:** Vorherige Zelle mit demselben Objekt. Dieser Parameter kann auf null gesetzt werden, wenn von Anfang an gesucht wird.
- **find_options:** Optionen zum Auffinden des erforderlichen Objekts.

Die folgenden Beispiele verwenden Arbeitsblattdaten, um die Find-Methoden zu üben:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingFormula-1.py" >}}

## **Suchen von Daten oder Formeln mithilfe von FindOptions**

Es ist möglich, angegebene Werte mithilfe der [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-Methode der [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions)-Sammlung mit verschiedenen [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions) zu finden. Normalerweise akzeptiert die Methode [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions) die folgenden Parameter:

- **was:**, die zu suchenden Daten oder Werte.
- **previous_cell**, die letzte Zelle, die denselben Wert enthielt. Dieser Parameter kann auf Null gesetzt werden, wenn von Anfang an gesucht wird.
- **find_options**, die Suchoptionen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingDataOrFormulasUsingFindOptions-1.py" >}}

## **Zellen finden, die den angegebenen Zeichenfolgenwert oder die angegebene Zahl enthalten**

Es ist möglich, angegebene Zeichenfolgenwerte zu finden, indem dieselbe [**find**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/find/#any-aspose.cells.Cell-aspose.cells.FindOptions)-Methode in der [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-Sammlung mit verschiedenen [**FindOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions) aufgerufen wird.

Geben Sie die [**FindOptions.look_in_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_in_type/)- und [**FindOptions.look_at_type**](https://reference.aspose.com/cells/python-net/aspose.cells/findoptions/look_at_type/)-Eigenschaften an. Das folgende Beispielcode veranschaulicht die Verwendung dieser Eigenschaften zum Auffinden von Zellen mit verschiedener Anzahl von Zeichenfolgen am **Anfang** oder in der **Mitte** oder am **Ende** der Zellzeichenfolge.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindingCellsContainingStringValueOrNumber-1.py" >}}

## **Erweiterte Themen**
- [Zellen mit bestimmtem Stil finden](/cells/de/python-net/find-cells-with-specific-style/)
- [Finden, ob der Zellenwert mit einem einzelnen Anführungszeichen beginnt](/cells/de/python-net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Daten mithilfe der Originalwerte suchen](/cells/de/python-net/search-data-using-original-values/)
