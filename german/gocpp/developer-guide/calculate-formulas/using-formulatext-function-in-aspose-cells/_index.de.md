---
title: Verwendung der FormulaText Funktion in Aspose.Cells mit Golang über C++
linktitle: Verwendung der FormulaText Funktion
description: In diesem Artikel wird gezeigt, wie man die Funktion FormulaText in der Aspose.Cells Bibliothek verwendet, um Formeln in Microsoft Excel zu verarbeiten. Durch Laden einer vorhandenen Excel Datei oder Erstellen einer neuen Excel Datei können wir die von Aspose.Cells bereitgestellte Methode verwenden, um den Formeltext der Zelle zu erhalten und zu setzen und das Ergebnis zu erhalten. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, FormulaText Funktionen
type: docs
weight: 60
url: /de/go-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText ist eine Funktion von Excel 2013 und späteren Versionen. Sie wird nicht von früheren Versionen wie Excel 2010 oder 2007 usw. unterstützt. Wie der Name schon sagt, druckt sie den Text der Formel, der in einer bestimmten Zelle vorhanden ist. Dieser Artikel zeigt Ihnen, wie Sie diese Funktion mit Aspose.Cells verwenden können.

{{% /alert %}} 

Der folgende Beispielcode zeigt die Verwendung von FormulaText mit Aspose.Cells. Der Code schreibt zuerst eine Formel in Zelle A1 und druckt dann den Text der Formel mit FormulaText in Zelle A2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UsingFormulatextFunctionInAsposeCells.go" >}}
## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
