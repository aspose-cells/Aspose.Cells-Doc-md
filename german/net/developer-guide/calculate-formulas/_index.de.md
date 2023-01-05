---
title: Formeln berechnen
type: docs
weight: 125
url: /de/net/calculate-formulas/
---
## **Formeln hinzufügen und Ergebnisse berechnen**

Aspose.Cells hat eine eingebettete Formelberechnungsmaschine. Es kann nicht nur aus Designervorlagen importierte Formeln neu berechnen, sondern unterstützt auch die Berechnung der Ergebnisse von zur Laufzeit hinzugefügten Formeln.

 Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die Teil von Microsoft Excel(Read[eine Liste der Funktionen, die von der Berechnungsmaschine unterstützt werden](/cells/de/net/supported-formula-functions/)). Diese Funktionen können über die APIs oder Designer-Tabellen verwendet werden. Aspose.Cells unterstützt eine große Auswahl an mathematischen, Zeichenfolgen-, booleschen, Datums-/Uhrzeit-, Statistik-, Datenbank-, Such- und Referenzformeln.

 Verwenden Sie die[**Formel**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) Eigentum bzw[**SetFormel(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) Methoden der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse, um einer Zelle eine Formel hinzuzufügen. Beginnen Sie beim Anwenden einer Formel die Zeichenfolge immer mit einem Gleichheitszeichen (=), wie Sie es beim Erstellen einer Formel in Microsoft Excel tun, und verwenden Sie ein Komma (,), um Funktionsparameter zu trennen.

 Um die Ergebnisse von Formeln zu berechnen, kann der Benutzer aufrufen[**BerechnenFormel**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) Methode der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse, die alle in einer Excel-Datei eingebetteten Formeln verarbeitet. Oder der Benutzer kann die anrufen[**BerechnenFormel**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) Methode der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse, die alle in ein Blatt eingebetteten Formeln verarbeitet. Oder der Benutzer kann auch anrufen[**Berechnung**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) Methode der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse, die die Formel von Cell verarbeitet:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

### **Wichtig zu wissen**

{{% alert color="primary" %}}

 Das**Formel** Eigentum und**SetFormel(...)** Methoden der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klassenarbeit anders als die**Berechnung** Methoden der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) und[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klassen. Das**Formel** Eigentum und**SetFormel(...)** Methoden fügen einfach die Formel zu einer Zelle hinzu, berechnen aber das Ergebnis nicht zur Laufzeit. Um das Ergebnis der Formeln zu erhalten, rufen Sie bitte an**Berechnung** Methoden.

{{% /alert %}}

## **Direkte Berechnung der Formel**

Aspose.Cells hat eine eingebettete Formelberechnungsmaschine. Neben der Berechnung von Formeln, die aus einer Designerdatei importiert wurden, kann Aspose.Cells Formelergebnisse direkt berechnen.

Manchmal müssen Sie Formelergebnisse direkt berechnen, ohne sie in ein Arbeitsblatt einzufügen. Die Werte der in der Formel verwendeten Zellen sind bereits in einem Arbeitsblatt vorhanden, und alles, was Sie brauchen, ist, das Ergebnis dieser Werte basierend auf einer Microsoft-Excel-Formel zu finden, ohne die Formel in einem Arbeitsblatt hinzuzufügen.

 Sie können die Formelberechnungs-Engine-APIs von Aspose.Cells für verwenden[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) zu[**Berechnung**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) die Ergebnisse solcher Formeln, ohne sie dem Arbeitsblatt hinzuzufügen:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

Der obige Code erzeugt die folgende Ausgabe:
{{< highlight "net" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Formeln wiederholt berechnen**

 Wenn die Arbeitsmappe viele Formeln enthält und der Benutzer sie wiederholt berechnen muss, wobei nur ein kleiner Teil davon geändert werden muss, kann es für die Leistung hilfreich sein, die Formelberechnungskette zu aktivieren:[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

### **Wichtig zu wissen**

{{% alert color="primary" %}}

Standardmäßig ist die Berechnungskette deaktiviert. Da das Erstellen der Kette auch zusätzliche Zeit benötigt, ist das erstmalige Berechnen von Formeln ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) kann im Vergleich zur Berechnung von Formeln ohne Kette mehr CPU-Verarbeitungszeit und Speicher verbrauchen. Wenn der Benutzer Formeln nicht wiederholt berechnen muss, sollte das Standardverhalten (Formel direkt berechnen, ohne Berechnungskette zu erstellen) der bessere Weg sein.

{{% /alert %}}


## **Themen vorantreiben**
- [Fügen Sie Cells zu Microsoft Excel-Formel-Überwachungsfenster hinzu](/cells/de/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Berechnung der IFNA-Funktion mit Aspose.Cells](/cells/de/net/calculating-ifna-function-using-aspose-cells/)
- [Berechnung der Array-Formel von Datentabellen](/cells/de/net/calculation-of-array-formula-of-data-tables/)
- [Berechnung von Excel 2016 MINIFS- und MAXIFS-Funktionen](/cells/de/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Verringern Sie die Berechnungszeit von Cell. Berechnungsmethode](/cells/de/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Zirkuläre Referenz erkennen](/cells/de/net/detecting-circular-reference/)
- [Direkte Berechnung der benutzerdefinierten Funktion, ohne sie in ein Arbeitsblatt zu schreiben](/cells/de/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementieren Sie eine benutzerdefinierte Berechnungs-Engine, um die Standard-Berechnungs-Engine von Aspose.Cells zu erweitern](/cells/de/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Unterbrechen oder brechen Sie die Formelberechnung der Arbeitsmappe ab](/cells/de/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Zurückgeben eines Wertebereichs mit AbstractCalculationEngine](/cells/de/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [Zurückgeben eines Wertebereichs mit ICustomFunction](/cells/de/net/returning-a-range-of-values-using-icustomfunction/)
- [Festlegen des Formelberechnungsmodus der Arbeitsmappe](/cells/de/net/setting-formula-calculation-mode-of-workbook/)
- [Verwendung der FormulaText-Funktion in Aspose.Cells](/cells/de/net/using-formulatext-function-in-aspose-cells/)
- [Verwenden der ICustomFunction-Funktion](/cells/de/net/using-icustomfunction-feature/)
