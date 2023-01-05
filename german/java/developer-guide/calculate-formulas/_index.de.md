---
title: Formeln berechnen
type: docs
weight: 110
url: /de/java/calculate-formulas/
---
## **Formeln hinzufügen und Ergebnisse berechnen**

Aspose.Cells hat eine eingebettete Formelberechnungsmaschine. Es kann nicht nur aus Designervorlagen importierte Formeln neu berechnen, sondern unterstützt auch die Berechnung der Ergebnisse von zur Laufzeit hinzugefügten Formeln.

 Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die Teil von Microsoft Excel(Read[eine Liste der Funktionen, die von der Berechnungsmaschine unterstützt werden](/cells/de/java/supported-formula-functions/)). Diese Funktionen können über die APIs oder Designer-Tabellen verwendet werden. Aspose.Cells unterstützt eine große Auswahl an mathematischen, Zeichenfolgen-, booleschen, Datums-/Uhrzeit-, Statistik-, Datenbank-, Such- und Referenzformeln.

 Verwenden Sie die[**Formel**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) Eigentum bzw[**SetFormel(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula(java.lang.String,%20com.aspose.cells.FormulaParseOptions,%20java.lang.Object) ) Methoden der[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)Klasse, um einer Zelle eine Formel hinzuzufügen. Beginnen Sie beim Anwenden einer Formel die Zeichenfolge immer mit einem Gleichheitszeichen (=), wie Sie es beim Erstellen einer Formel in Microsoft Excel tun, und verwenden Sie ein Komma (,), um Funktionsparameter zu trennen.

 Um die Ergebnisse von Formeln zu berechnen, kann der Benutzer aufrufen[**BerechnenFormel**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) Methode der[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)Klasse, die alle in einer Excel-Datei eingebetteten Formeln verarbeitet. Oder der Benutzer kann die anrufen[**BerechnenFormel**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(com.aspose.cells.CalculationOptions,%20boolean)) Methode der[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse, die alle in ein Blatt eingebetteten Formeln verarbeitet. Oder der Benutzer kann auch anrufen[**Berechnung**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate(com.aspose.cells.CalculationOptions)) Methode der[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)Klasse, die die Formel von Cell verarbeitet:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Wichtig zu wissen**

{{% alert color="primary" %}}

 Das**Formel** Eigentum und**SetFormel(...)** Methoden der[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)Klassenarbeit anders als die**Berechnung** Methoden der[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), [**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) und[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) Klassen. Das**Formel** Eigentum und**SetFormel(...)** Methoden fügen einfach die Formel zu einer Zelle hinzu, berechnen aber das Ergebnis nicht zur Laufzeit. Um das Ergebnis der Formeln zu erhalten, rufen Sie bitte an**Berechnung** Methoden.

{{% /alert %}}

## **Direkte Berechnung der Formel**

Aspose.Cells hat eine eingebettete Formelberechnungsmaschine. Neben der Berechnung von Formeln, die aus einer Designerdatei importiert wurden, kann Aspose.Cells Formelergebnisse direkt berechnen.

Manchmal müssen Sie Formelergebnisse direkt berechnen, ohne sie in ein Arbeitsblatt einzufügen. Die Werte der in der Formel verwendeten Zellen sind bereits in einem Arbeitsblatt vorhanden, und alles, was Sie brauchen, ist, das Ergebnis dieser Werte basierend auf einer Microsoft-Excel-Formel zu finden, ohne die Formel in einem Arbeitsblatt hinzuzufügen.

 Sie können die Formelberechnungs-Engine-APIs von Aspose.Cells für verwenden[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) zu[**Berechnung**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(java.lang.String,%20com.aspose.cells.CalculationOptions)) die Ergebnisse solcher Formeln, ohne sie dem Arbeitsblatt hinzuzufügen:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

Der obige Code erzeugt die folgende Ausgabe:
{{< highlight "java" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Formeln wiederholt berechnen**

 Wenn die Arbeitsmappe viele Formeln enthält und der Benutzer sie wiederholt berechnen muss, wobei nur ein kleiner Teil davon geändert werden muss, kann es für die Leistung hilfreich sein, die Formelberechnungskette zu aktivieren:[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **Wichtig zu wissen**

{{% alert color="primary" %}}

Standardmäßig ist die Berechnungskette deaktiviert. Da das Erstellen der Kette auch zusätzliche Zeit benötigt, ist das erstmalige Berechnen von Formeln ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions))) kann im Vergleich zur Berechnung von Formeln ohne Kette mehr CPU-Verarbeitungszeit und Speicher verbrauchen. Wenn der Benutzer Formeln nicht wiederholt berechnen muss, sollte das Standardverhalten (Formel direkt berechnen, ohne Berechnungskette zu erstellen) der bessere Weg sein.

{{% /alert %}}

## **Themen vorantreiben**
- [Fügen Sie Cells zu Microsoft Excel-Formel-Überwachungsfenster hinzu](/cells/de/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells Formelberechnungsmodul](/cells/de/java/aspose-cells-formula-calculation-engine/)
- [Berechnung der IFNA-Funktion mit Aspose.Cells](/cells/de/java/calculating-ifna-function-using-aspose-cells/)
- [Berechnung der Array-Formel von Datentabellen](/cells/de/java/calculation-of-array-formula-of-data-tables/)
- [Berechnung von Excel 2016 MINIFS- und MAXIFS-Funktionen](/cells/de/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Verringern Sie die Berechnungszeit von Cell. Berechnungsmethode](/cells/de/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [Zirkuläre Referenz erkennen](/cells/de/java/detecting-circular-reference/)
- [Direkte Berechnung der benutzerdefinierten Funktion, ohne sie in ein Arbeitsblatt zu schreiben](/cells/de/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementieren Sie eine benutzerdefinierte Berechnungs-Engine, um die Standard-Berechnungs-Engine von Aspose.Cells zu erweitern](/cells/de/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Unterbrechen oder brechen Sie die Formelberechnung der Arbeitsmappe ab](/cells/de/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Zurückgeben eines Wertebereichs mit AbstractCalculationEngine](/cells/de/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [Zurückgeben eines Wertebereichs mit ICustomFunction](/cells/de/java/returning-a-range-of-values-using-icustomfunction/)
- [Verwenden der ICustomFunction-Funktion](/cells/de/java/using-icustomfunction-feature/)
