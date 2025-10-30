---
title: Formeln mit Golang über C++ berechnen
linktitle: Berechnung von Formeln
description: Dieser Artikel zeigt, wie man die Aspose.Cells Bibliothek verwendet, um Formeln in Microsoft Excel mit Golang über C++ zu berechnen. Durch das Laden einer bestehenden Excel Datei oder das Erstellen einer neuen Excel Datei können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um die Formel zu berechnen und das Ergebnis zu erhalten. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, Formeln, Berechnungen, Direkte Formelberechnung, Formeln wiederholt berechnen, Formeln hinzufügen.
type: docs
weight: 125
url: /de/go-cpp/calculate-formulas/
---

## **Hinzufügen von Formeln & Berechnen von Ergebnissen**

Aspose.Cells verfügt über eine eingebaute Formelrechnungs-Engine. Es kann nicht nur Formeln, die aus Designer-Vorlagen importiert wurden, neu berechnen, sondern auch die Ergebnisse von Formeln, die zur Laufzeit hinzugefügt wurden, berechnen.

Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die Teil von Microsoft Excel sind (Lesen Sie [eine Liste der von der Rechenmaschine unterstützten Funktionen](/cells/de/cpp/supported-formula-functions/)). Diese Funktionen können über die APIs oder Designer-Tabellen verwendet werden. Aspose.Cells unterstützt eine große Vielfalt an mathematischen, String-, Boolean-, Datums-/Uhrzeit-, Statistik-, Datenbank-, Lookup- und Referenzformeln.

Verwenden Sie die [**GetFormula**](https://reference.aspose.com/cells/go-cpp/cell/getformula/)-Eigenschaft oder [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/)-Methoden der [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse, um eine Formel in eine Zelle einzufügen. Beim Anwenden einer Formel beginnt der String immer mit einem Gleichheitszeichen (=), so wie Sie es beim Erstellen einer Formel in Microsoft Excel tun, und verwenden Sie ein Komma (,) zur Trennung der Funktionsparameter.

Um die Ergebnisse von Formeln zu berechnen, kann der Benutzer die [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)-Methode der [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-Klasse aufrufen, die alle in einer Excel-Datei eingebetteten Formeln verarbeitet. Alternativ kann der Benutzer die [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/)-Methode der [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse aufrufen, die alle in einem Blatt eingebetteten Formeln verarbeitet. Oder der Benutzer kann auch die [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/)-Methode der [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse aufrufen, die die Formel einer einzelnen Zelle verarbeitet:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas.go" >}}
### **Wichtiges zu Formeln**

{{% alert color="primary" %}}

Die **GetFormula**-Eigenschaft und die **SetFormula(...)**-Methoden der [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/)-Klasse arbeiten anders als die **Calculate**-Methoden der [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) und [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/)-Klassen. Die **GetFormula**-Eigenschaft und die **SetFormula(...)**-Methoden fügen die Formel einfach einer Zelle hinzu, berechnen aber das Ergebnis zur Laufzeit nicht. Um das Ergebnis der Formeln zu erhalten, rufen Sie bitte die **Calculate**-Methoden auf.

{{% /alert %}}

## **Direkte Berechnung von Formeln**

Aspose.Cells verfügt über einen eingebetteten Formelberechnungsmotor. Neben der Berechnung von Formeln, die aus einer Designerdatei importiert wurden, kann Aspose.Cells auch Formelergebnisse direkt berechnen.

Manchmal müssen Sie Formelergebnisse direkt berechnen, ohne sie in ein Arbeitsblatt einzufügen. Die Werte der in der Formel verwendeten Zellen sind bereits in einem Arbeitsblatt vorhanden, und alles, was Sie brauchen, ist, das Ergebnis dieser Werte basierend auf einer Microsoft-Excel-Formel zu finden, ohne die Formel ins Arbeitsblatt einzufügen.

Sie können die APIs der Aspose.Cells-Formelberechnung engine für [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) bis [**calculate**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula/) nutzen, um die Ergebnisse solcher Formeln zu ermitteln, ohne sie ins Arbeitsblatt einzufügen:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-1.go" >}}
Der obige Code erzeugt die folgende Ausgabe:
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Wie man Formeln wiederholt berechnet**

Wenn sich viele Formeln im Arbeitsbuch befinden und der Benutzer sie wiederholt berechnen muss, wobei nur ein kleiner Teil geändert wird, kann es für die Leistung hilfreich sein, die Formelberechnungskette zu aktivieren: [**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/go-cpp/formulasettings/getenablecalculationchain/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-2.go" >}}
### **Wichtig zu wissen**

{{% alert color="primary" %}}

Standardmäßig ist die Berechnungskette deaktiviert. Da das Erstellen der Kette zusätzliche Zeit benötigt, kann die erste Berechnung der Formeln ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)) mehr CPU- und Speicherkapazität beanspruchen im Vergleich zur Berechnung ohne Kette. Falls der Benutzer Formeln nicht wiederholt berechnen muss, ist das Standardverhalten (direktes Berechnen der Formel ohne Kette) die bessere Option.

{{% /alert %}}

## **Fortgeschrittene Themen**
- [Zellen zur Microsoft Excel-Formelüberwachung hinzufügen](/cells/de/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Berechnung der IFNA-Funktion mit Aspose.Cells](/cells/de/cpp/calculating-ifna-function-using-aspose-cells/)
- [Berechnung der Arrayformel von Datenblättern](/cells/de/cpp/calculation-of-array-formula-of-data-tables/)
- [Berechnung der Excel 2016 MINIFS- und MAXIFS-Funktionen](/cells/de/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Vermindern der Berechnungszeit der Cell.Calculate-Methode](/cells/de/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Direkte Berechnung einer benutzerdefinierten Funktion ohne Eintragung in ein Arbeitsblatt](/cells/de/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementieren eines benutzerdefinierten Berechnungsmotors zur Erweiterung des Standard-Berechnungsmotors von Aspose.Cells](/cells/de/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Rückgabe eines Bereichs von Werten unter Verwendung von AbstractCalculationEngine](/cells/de/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Festlegen des Formelberechnungsmodus des Arbeitsbuchs](/cells/de/cpp/setting-formula-calculation-mode-of-workbook/)
- [Verwendung der FormulaText-Funktion in Aspose.Cells](/cells/de/cpp/using-formulatext-function-in-aspose-cells/)
