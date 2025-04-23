---
title: Formeln von Excel Dateien verwalten
linktitle: Formeln
type: docs
weight: 122
url: /de/python-net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells für Python via .NET kann Formeln in Excel Dateien einfach abrufen, festlegen und berechnen.
description: Erfahren Sie, wie man Formeln in Excel Dateien mit Aspose.Cells für Python via .NET für .NET APIs verwaltet.
keywords: Wie man Formeln in Python berechnet, Formeln und Funktionen mit Python, Python eingebaute Funktionen verwalten, Wie man Add in Funktionen mit Python verwendet, Wie man Array Formeln mit Python verwendet, Wie man R1C1 Formeln in Python nutzt.
---

## **Einführung**

Eine der überzeugenden Funktionen von Microsoft Excel ist die Fähigkeit, Daten mit Formeln und Funktionen zu verarbeiten. Microsoft Excel bietet eine Reihe eingebauter Funktionen und Formeln, die Benutzern helfen, komplexe Berechnungen schnell durchzuführen. Aspose.Cells für Python via .NET bietet ebenfalls eine große Anzahl eingebauter Funktionen und Formeln, die Entwicklern die Werteberechnung erleichtern. Aspose.Cells für Python via .NET unterstützt auch Add-in-Funktionen. Darüber hinaus unterstützt Aspose.Cells für Python via .NET Array- und R1C1-Formeln.

## **Wie man Formeln und Funktionen verwendet**

Aspose.Cells für Python via .NET stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine Sammlung [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine Sammlung [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Jedes Element in der Cells-Sammlung stellt ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) dar.

Es ist möglich, Formeln auf Zellen anzuwenden, indem Eigenschaften und Methoden verwendet werden, die von der Klasse [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) angeboten werden, die im Folgenden näher erläutert werden.

- Verwendung von integrierten Funktionen.
- Verwendung von Add-In-Funktionen.
- Arbeit mit Array-Formeln.
- Erstellen einer R1C1-Formel.

## **Verwendung von integrierten Funktionen**

Eingebaute Funktionen oder Formeln werden als fertig vorbereitete Funktionen bereitgestellt, um den Aufwand und die Zeit der Entwickler zu reduzieren. siehe [Liste der unterstützten eingebauten Funktionen](/cells/de/python-net/supported-formula-functions/), die von Aspose.Cells für Python via .NET unterstützt werden. Die Funktionen sind alphabetisch aufgelistet. In Zukunft werden weitere Funktionen unterstützt.

Aspose.Cells für Python via .NET unterstützt die meisten der von Microsoft Excel angebotenen Formeln oder Funktionen. Entwickler können diese Formeln über die API oder [Designer-Spreadsheet](/cells/de/net/what-is-a-designer-spreadsheet/) verwenden. Aspose.Cells für Python via .NET unterstützt eine große Menge mathematischer, String-, Boolescher, Datum/Uhrzeit-, Statistik-, Datenbank-, Nachschlage- und Referenzformeln.

Verwenden Sie die [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-Eigenschaft der Klasse [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula), um einer Zelle eine Formel hinzuzufügen. **Komplexe Formeln**, zum Beispiel

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, werden auch in Aspose.Cells für Python via .NET unterstützt. Bei der Anwendung einer Formel auf eine Zelle beginnt der String immer mit einem Gleichheitszeichen (=), genau wie beim Erstellen einer Formel in Microsoft Excel, und verwendet ein Komma (,) zur Trennung der Funktionsparameter.

Im nachfolgenden Beispiel wird eine komplexe Formel auf die erste Zelle einer Sammlung [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) eines Arbeitsblatts angewendet. Die Formel verwendet eine eingebaute **WENN**-Funktion, die von Aspose.Cells für Python via .NET bereitgestellt wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingBuiltinfunction-1.py" >}}

## **Verwendung von Add-in-Funktionen**

Es können benutzerdefinierte Formeln definiert werden, die als Excel-Add-In eingebunden werden sollen. Beim Setzen der Zell.Formel-Funktion funktionieren integrierte Funktionen gut, jedoch ist es erforderlich, benutzerdefinierte Funktionen oder Formeln unter Verwendung von Add-In-Funktionen zu setzen.

Aspose.Cells für Python via .NET bietet Funktionen zur Registrierung von Add-in-Funktionen mittels [**worksheets.register_add_in_function()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/register_add_in_function). Danach, wenn wir die Zelle.Formel = eineFunktionAusAddIn setzen, enthält die exportierte Excel-Datei den berechneten Wert aus der AddIn-Funktion.

Die folgende XLAM-Datei soll zum Registrieren der Add-In-Funktion verwendet werden im untenstehenden Beispielcode. Ebenso kann die Ausgabedatei "test_udf.xlsx" heruntergeladen werden, um die Ausgabe zu überprüfen.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-RegisterAndCallFuncFromAddIn-1.py" >}}

## **Verwendung von Array-Formel**

Array-Formeln sind Formeln, die Arrays anstelle von einzelnen Zahlen als Argumente für die Funktionen, die die Formel bilden, verwenden. Wenn eine Array-Formel angezeigt wird, ist sie von geschweiften Klammern ({}) umgeben.

Einige Microsoft Excel-Funktionen geben Arrays von Werten zurück. Um mehrere Ergebnisse mit einer Array-Formel zu berechnen, geben Sie das Array in einen Zellenbereich mit derselben Anzahl von Zeilen und Spalten wie die Array-Argumente ein.

Es ist möglich, einer Zelle eine Array-Formel durch Aufruf der Methode [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula) der Klasse [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) anzuwenden. Die Methode [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula) nimmt die folgenden Parameter an:

- **Array-Formel**, die Array-Formel.
- **Anzahl der Zeilen**, die Anzahl der Zeilen zum Ausfüllen des Ergebnisses der Array-Formel.
- **Anzahl der Spalten**, die Anzahl der Spalten zum Ausfüllen des Ergebnisses der Array-Formel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingArrayFunction-1.py" >}}

## **Verwendung der R1C1-Formel**

Fügen Sie einer Zelle mit der [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) Klasse die Eigenschaft [**r1c1_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/r1c1_formula) hinzu.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingR1C1-1.py" >}}

## **Erweiterte Themen**
- [Vorgänger und Abhängige](/cells/de/python-net/precedents-and-dependents/)
- [Externe Verknüpfungen in Formeln festlegen](/cells/de/python-net/set-external-links-in-formulas/)
- [Formel in Tabelle oder List-Objekt automatisch propagieren, während neue Zeilen eingegeben werden](/cells/de/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Formel für benanntes Bereich setzen](/cells/de/python-net/setting-formula-for-named-range/)
- [Formeln einstellen - Hinweis für nicht englischsprachige Benutzer](/cells/de/python-net/setting-formulas-notice-for-non-english-users/)
- [Gemeinsame Formel festlegen](/cells/de/python-net/setting-shared-formula/)
- [Maximale Zeilen der gemeinsamen Formel angeben](/cells/de/python-net/specify-maximum-rows-of-shared-formula/)
- [Unterstützte Excel-Funktionen](/cells/de/python-net/supported-formula-functions/)


