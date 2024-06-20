---
title: Formeln von Excel Dateien verwalten
linktitle: Formeln
type: docs
weight: 122
url: /de/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells kann ganz einfach Formeln von Excel Dateien abrufen, setzen und berechnen.
description: Erfahren Sie, wie Sie Formeln von Excel Dateien über die Aspose.Cells for NET APIs verwalten können.
keywords: Wie man Formeln in C# berechnet, Formeln und Funktionen in C# verwendet, C# eingebaute Funktionen verwalten, wie man Add In Funktionen mit C# verwendet, wie man Arrayformeln über C# verwendet, wie man R1C1 Formeln in C# verwendet.
---

## **Einführung**

Eine der überzeugendsten Funktionen von Microsoft Excel ist die Fähigkeit, Daten mit Formeln und Funktionen zu verarbeiten. Microsoft Excel bietet eine Reihe von integrierten Funktionen und Formeln, die Benutzern helfen, komplexe Berechnungen schnell durchzuführen. Aspose.Cells bietet ebenfalls eine große Anzahl von integrierten Funktionen und Formeln, die Entwicklern die Berechnung von Werten erleichtern. Aspose.Cells unterstützt auch Add-In-Funktionen. Darüber hinaus unterstützt Aspose.Cells Array- und R1C1-Formeln in Aspose.Cells.

## **Wie man Formeln und Funktionen verwendet**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung. Jedes Element in der Cells-Sammlung repräsentiert ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Es ist möglich, Formeln auf Zellen anzuwenden, indem Eigenschaften und Methoden verwendet werden, die von der Klasse [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) angeboten werden, die im Folgenden näher erläutert werden.

- Verwendung von integrierten Funktionen.
- Verwendung von Add-In-Funktionen.
- Arbeit mit Array-Formeln.
- Erstellen einer R1C1-Formel.

## **Verwendung von integrierten Funktionen**

Integrierte Funktionen oder Formeln werden als fertige Funktionen bereitgestellt, um die Bemühungen und die Zeit der Entwickler zu reduzieren. Siehe [eine Liste der integrierten Funktionen](/cells/de/net/supported-formula-functions/), die von Aspose.Cells unterstützt werden. Die Funktionen sind alphabetisch aufgelistet. In Zukunft werden weitere Funktionen unterstützt.

Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die von Microsoft Excel angeboten werden. Entwickler können diese Formeln über die API oder die [Designtabelle](/cells/de/net/what-is-a-designer-spreadsheet/) verwenden. Aspose.Cells unterstützt eine große Anzahl von mathematischen, alphanumerischen, logischen, Datum/Zeit-, statistischen, Datenbank-, Such- und Verweisformeln.

Verwenden Sie die [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-Eigenschaft der Klasse [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula), um einer Zelle eine Formel hinzuzufügen. **Komplexe Formeln**, zum Beispiel

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, werden auch von Aspose.Cells unterstützt. Beim Anwenden einer Formel auf eine Zelle beginnen Sie immer die Zeichenfolge mit einem Gleichheitszeichen (=), wie Sie es bei der Erstellung einer Formel in Microsoft Excel tun, und verwenden ein Komma (,) zur Trennung der Funktionsparameter.

Im folgenden Beispiel wird eine komplexe Formel auf die erste Zelle der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung eines Arbeitsblatts angewendet. Die Formel verwendet eine integrierte **IF**-Funktion von Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **Verwendung von Add-in-Funktionen**

Es können benutzerdefinierte Formeln definiert werden, die als Excel-Add-In eingebunden werden sollen. Beim Setzen der Zell.Formel-Funktion funktionieren integrierte Funktionen gut, jedoch ist es erforderlich, benutzerdefinierte Funktionen oder Formeln unter Verwendung von Add-In-Funktionen zu setzen.

Aspose.Cells bietet Funktionen zur Registrierung von Add-In-Funktionen mit [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Anschließend, wenn wir cell.Formula = anyFunctionFromAddIn setzen, enthält die Ausgabedatei Excel den berechneten Wert aus der AddIn-Funktion.

Die folgende XLAM-Datei soll zum Registrieren der Add-In-Funktion verwendet werden im untenstehenden Beispielcode. Ebenso kann die Ausgabedatei "test_udf.xlsx" heruntergeladen werden, um die Ausgabe zu überprüfen.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **Verwendung von Array-Formel**

Array-Formeln sind Formeln, die Arrays anstelle von einzelnen Zahlen als Argumente für die Funktionen, die die Formel bilden, verwenden. Wenn eine Array-Formel angezeigt wird, ist sie von geschweiften Klammern ({}) umgeben.

Einige Microsoft Excel-Funktionen geben Arrays von Werten zurück. Um mehrere Ergebnisse mit einer Array-Formel zu berechnen, geben Sie das Array in einen Zellenbereich mit derselben Anzahl von Zeilen und Spalten wie die Array-Argumente ein.

Es ist möglich, einer Zelle eine Array-Formel durch Aufruf der Methode [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) der Klasse [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) anzuwenden. Die Methode [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) nimmt die folgenden Parameter an:

- **Array-Formel**, die Array-Formel.
- **Anzahl der Zeilen**, die Anzahl der Zeilen zum Ausfüllen des Ergebnisses der Array-Formel.
- **Anzahl der Spalten**, die Anzahl der Spalten zum Ausfüllen des Ergebnisses der Array-Formel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **Verwendung der R1C1-Formel**

Fügen Sie einer Zelle mit der [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse die Eigenschaft [**R1C1Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) hinzu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **Erweiterte Themen**
- [Vorgänger und Abhängige](/cells/de/net/precedents-and-dependents/)
- [Externe Verknüpfungen in Formeln festlegen](/cells/de/net/set-external-links-in-formulas/)
- [Formel in Tabelle oder List-Objekt automatisch propagieren, während neue Zeilen eingegeben werden](/cells/de/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Formel für benanntes Bereich setzen](/cells/de/net/setting-formula-for-named-range/)
- [Formeln einstellen - Hinweis für nicht englischsprachige Benutzer](/cells/de/net/setting-formulas-notice-for-non-english-users/)
- [Gemeinsame Formel festlegen](/cells/de/net/setting-shared-formula/)
- [Maximale Zeilen der gemeinsamen Formel angeben](/cells/de/net/specify-maximum-rows-of-shared-formula/)
- [Unterstützte Excel-Funktionen](/cells/de/net/supported-formula-functions/)

