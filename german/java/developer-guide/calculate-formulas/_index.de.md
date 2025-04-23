---
title: Berechnung von Formeln
type: docs
weight: 110
url: /de/java/calculate-formulas/
---

## **Hinzufügen von Formeln & Berechnen von Ergebnissen**

Aspose.Cells verfügt über einen eingebetteten Formelberechnungsmotor. Er kann nicht nur Formeln aus Designer-Vorlagen neu berechnen, sondern auch die Ergebnisse von zur Laufzeit hinzugefügten Formeln berechnen.

Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die Teil von Microsoft Excel sind (Lesen Sie [eine Liste der Funktionen, die von der Berechnungsmaschine unterstützt werden](/cells/de/java/supported-formula-functions/)). Diese Funktionen können über die APIs oder Designer-Arbeitsblätter verwendet werden. Aspose.Cells unterstützt eine große Anzahl mathematischer, string-, boolescher, Datum/Uhrzeit-, statistischer, Datenbank-, Such- und Bezug-Formeln.

Verwenden Sie die Eigenschaft [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) oder die Methoden [**SetFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula-java.lang.String-com.aspose.cells.FormulaParseOptions-java.lang.Object-) der Klasse [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell), um einer Zelle eine Formel hinzuzufügen. Bei der Anwendung einer Formel beginnen Sie den String immer mit einem Gleichheitszeichen (=), wie es bei der Erstellung einer Formel in Microsoft Excel der Fall ist, und verwenden ein Komma (,) zur Trennung der Funktionsparameter.

Um die Ergebnisse von Formeln zu berechnen, kann der Benutzer die Methode [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions--) der [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) Klasse aufrufen, die alle in einer Excel-Datei eingebetteten Formeln verarbeitet. Oder der Benutzer kann die Methode [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-com.aspose.cells.CalculationOptions-boolean-) der [**Worsheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse aufrufen, die alle in einem Blatt eingebetteten Formeln verarbeitet. Alternativ kann der Benutzer auch die Methode [**Calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate-com.aspose.cells.CalculationOptions-) der [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) Klasse aufrufen, die die Formel einer einzelnen Zelle verarbeitet:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Wichtig zu wissen**

{{% alert color="primary" %}}

Die **Formel**-Eigenschaft und die **SetFormel(...)**-Methoden der Klasse [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) verhalten sich anders als die **Berechnen**-Methoden der Klassen [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) und [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell). Die **Formel**-Eigenschaft und die **SetFormel(...)**-Methoden fügen einfach die Formel einer Zelle hinzu, berechnen das Ergebnis jedoch nicht zur Laufzeit. Um das Ergebnis der Formeln zu erhalten, rufen Sie bitte die **Berechnen**-Methoden auf.

{{% /alert %}}

## **Direkte Berechnung von Formeln**

Aspose.Cells verfügt über einen eingebetteten Formelberechnungsmotor. Neben der Berechnung von Formeln, die aus einer Designerdatei importiert wurden, kann Aspose.Cells auch Formelergebnisse direkt berechnen.

Manchmal müssen Sie Formelergebnisse direkt berechnen, ohne sie in ein Arbeitsblatt aufzunehmen. Die Werte der Zellen, die in der Formel verwendet werden, existieren bereits in einem Arbeitsblatt, und Sie müssen nur das Ergebnis dieser Werte anhand einiger Microsoft Excel-Formel finden, ohne die Formel in ein Arbeitsblatt aufzunehmen.

Sie können die Formelberechnungsmotor-APIs von Aspose.Cells für [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) bis [**calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-java.lang.String-com.aspose.cells.CalculationOptions-) verwenden, um die Ergebnisse solcher Formeln zu berechnen, ohne sie dem Arbeitsblatt hinzuzufügen:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

Der obige Code erzeugt die folgende Ausgabe:
{{< highlight java >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Formeln wiederholt berechnen**

Wenn es viele Formeln in der Arbeitsmappe gibt und der Benutzer sie wiederholt berechnen muss, wobei nur ein kleiner Teil von ihnen modifiziert wird, kann es für die Leistungsfähigkeit hilfreich sein, die Formelberechnungskette zu aktivieren: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **Wichtig zu wissen**

{{% alert color="primary" %}}

Standardmäßig ist die Berechnungskette deaktiviert. Da das Erstellen der Kette zusätzliche Zeit benötigt, kann die erste Berechnung der Formeln([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions--)) mehr CPU-Verarbeitungszeit und Speicher benötigen im Vergleich zur Berechnung ohne Kette. Wenn der Benutzer keine wiederholte Berechnung der Formeln benötigt, ist das Standardverhalten (direkte Berechnung der Formel ohne Erstellung der Berechnungskette) die bessere Wahl.

{{% /alert %}}

## **Erweiterte Themen**
- [Zellen zur Microsoft Excel-Formelüberwachung hinzufügen](/cells/de/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells Formelberechnungsmotor](/cells/de/java/aspose-cells-formula-calculation-engine/)
- [Berechnung der IFNA-Funktion mit Aspose.Cells](/cells/de/java/calculating-ifna-function-using-aspose-cells/)
- [Berechnung der Arrayformel von Datenblättern](/cells/de/java/calculation-of-array-formula-of-data-tables/)
- [Berechnung der Excel 2016 MINIFS- und MAXIFS-Funktionen](/cells/de/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Vermindern der Berechnungszeit der Cell.Calculate-Methode](/cells/de/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [Erkennen von zirkulären Verweisen](/cells/de/java/detecting-circular-reference/)
- [Direkte Berechnung einer benutzerdefinierten Funktion ohne Eintragung in ein Arbeitsblatt](/cells/de/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementieren eines benutzerdefinierten Berechnungsmotors zur Erweiterung des Standard-Berechnungsmotors von Aspose.Cells](/cells/de/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Unterbrechen oder Abbrechen der Formelberechnung des Arbeitsbuchs](/cells/de/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Rückgabe eines Bereichs von Werten unter Verwendung von AbstractCalculationEngine](/cells/de/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [Rückgabe eines Wertebereichs mit ICustomFunction](/cells/de/java/returning-a-range-of-values-using-icustomfunction/)
- [Verwendung der ICustomFunction-Funktion](/cells/de/java/using-icustomfunction-feature/)
{{< app/cells/assistant language="java" >}}
