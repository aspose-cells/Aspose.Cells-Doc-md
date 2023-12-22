---
title: Verwendung der FormulaText-Funktion in Aspose.Cells
description: In diesem Artikel wird erläutert, wie Sie die FormulaText-Funktion in der Aspose.Cells-Bibliothek verwenden, um Formeln in Microsoft Excel zu verarbeiten. Indem wir eine vorhandene Excel-Datei laden oder eine neue Excel-Datei erstellen, können wir die von Aspose.Cells bereitgestellte Methode verwenden, um den Formeltext der Zelle abzurufen und festzulegen und das Ergebnis zu erhalten. Abschließend speichern wir die geänderte Excel-Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, FormulaText functions
type: docs
weight: 60
url: /de/net/using-formulatext-function-in-aspose-cells/
---
{{% alert color="primary" %}} 

FormulaText ist eine Funktion von Excel 2013 und höher. Es wird von früheren Versionen wie Excel 2010 oder 2007 usw. nicht unterstützt. Wie der Name schon sagt, druckt es den Text der Formel, der in einer bestimmten Zelle vorhanden ist. In diesem Artikel erfahren Sie, wie Sie diese Funktion mit Aspose.Cells nutzen.

{{% /alert %}} 

Der folgende Beispielcode zeigt die Verwendung von FormulaText mit Aspose.Cells. Der Code schreibt zunächst eine Formel in Zelle A1 und druckt dann den Text der Formel mithilfe von FormulaText in Zelle A2.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingFormulaTextFunction-UsingFormulaTextFunction.cs" >}}
##  **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

 =SUM(B1:B10)

{{< /highlight >}}
