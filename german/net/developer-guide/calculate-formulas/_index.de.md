---
title: Berechnung von Formeln
description: Dieser Artikel zeigt, wie die Aspose.Cells Bibliothek zum Berechnen von Formeln in Microsoft Excel verwendet werden kann. Durch Laden einer vorhandenen Excel Datei oder Erstellen einer neuen Excel Datei können die Methoden von Aspose.Cells zur Berechnung der Formel und zum Erhalten des Ergebnisses verwendet werden. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, Formeln, Berechnungen, Direkte Formelberechnung, Formeln wiederholt berechnen, Formeln hinzufügen.
type: docs
weight: 125
url: /de/net/calculate-formulas/
---

## **Hinzufügen von Formeln & Berechnen von Ergebnissen**

Aspose.Cells verfügt über einen eingebetteten Formelberechnungsmotor. Er kann nicht nur Formeln aus Designer-Vorlagen neu berechnen, sondern auch die Ergebnisse von zur Laufzeit hinzugefügten Formeln berechnen.

Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die Teil von Microsoft Excel sind (siehe [eine Liste der vom Berechnungsmotor unterstützten Funktionen](/cells/de/net/supported-formula-functions/)). Diese Funktionen können über die APIs oder Designer-Tabellenkalkulationen verwendet werden. Aspose.Cells unterstützt eine große Anzahl mathematischer, Zeichenfolgen-, Boolescher, Datum/Uhrzeit-, statistischer, Datenbank-, Such-, und Verweisformeln.

Verwenden Sie die Eigenschaft [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) oder die Methoden [**SetFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) der Klasse [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell), um einer Zelle eine Formel hinzuzufügen. Bei der Anwendung einer Formel beginnen Sie den String immer mit einem Gleichheitszeichen (=), wie es bei der Erstellung einer Formel in Microsoft Excel der Fall ist, und verwenden ein Komma (,) zur Trennung der Funktionsparameter.

Um die Ergebnisse von Formeln zu berechnen, kann der Benutzer die Methode [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) der Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) aufrufen, die alle in einer Excel-Datei eingebetteten Formeln verarbeitet. Alternativ kann der Benutzer die Methode [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) der Klasse [**Worsheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) aufrufen, die alle in einem Tabellenblatt eingebetteten Formeln verarbeitet. Oder der Benutzer kann auch die Methode [**Calculate**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) der Klasse [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) aufrufen, die die Formel einer Zelle verarbeitet:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

### **Wichtiges zu Formeln**

{{% alert color="primary" %}}

Die **Formel**-Eigenschaft und die **SetFormel(...)**-Methoden der Klasse [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) verhalten sich anders als die **Berechnen**-Methoden der Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) und [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Die **Formel**-Eigenschaft und die **SetFormel(...)**-Methoden fügen einfach die Formel einer Zelle hinzu, berechnen das Ergebnis jedoch nicht zur Laufzeit. Um das Ergebnis der Formeln zu erhalten, rufen Sie bitte die **Berechnen**-Methoden auf.

{{% /alert %}}

## **Direkte Berechnung von Formeln**

Aspose.Cells verfügt über einen eingebetteten Formelberechnungsmotor. Neben der Berechnung von Formeln, die aus einer Designerdatei importiert wurden, kann Aspose.Cells auch Formelergebnisse direkt berechnen.

Manchmal müssen Sie Formelergebnisse direkt berechnen, ohne sie in ein Arbeitsblatt aufzunehmen. Die Werte der Zellen, die in der Formel verwendet werden, existieren bereits in einem Arbeitsblatt, und Sie müssen nur das Ergebnis dieser Werte anhand einiger Microsoft Excel-Formel finden, ohne die Formel in ein Arbeitsblatt aufzunehmen.

Sie können die Formelberechnungsmotor-APIs von Aspose.Cells für [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bis [**calculate**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) verwenden, um die Ergebnisse solcher Formeln zu berechnen, ohne sie dem Arbeitsblatt hinzuzufügen:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

Der obige Code erzeugt die folgende Ausgabe:
{{< highlight net >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Wie man Formeln wiederholt berechnet**

Wenn es viele Formeln in der Arbeitsmappe gibt und der Benutzer sie wiederholt berechnen muss, wobei nur ein kleiner Teil von ihnen modifiziert wird, kann es für die Leistungsfähigkeit hilfreich sein, die Formelberechnungskette zu aktivieren: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

### **Wichtig zu wissen**

{{% alert color="primary" %}}

Standardmäßig ist die Berechnungskette deaktiviert. Da das Erstellen der Kette zusätzliche Zeit benötigt, kann das erstmalige Berechnen von Formeln ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) mehr CPU-Verarbeitungszeit und Speicher in Anspruch nehmen im Vergleich zur Berechnung von Formeln ohne Kette. Wenn der Benutzer keine wiederholten Formelberechnungen benötigt, sollte das Standardverhalten (direkte Berechnung der Formel ohne Erstellung einer Berechnungskette) der bessere Weg sein.

{{% /alert %}}


## **Erweiterte Themen**
- [Zellen zur Microsoft Excel-Formelüberwachung hinzufügen](/cells/de/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Berechnung der IFNA-Funktion mit Aspose.Cells](/cells/de/net/calculating-ifna-function-using-aspose-cells/)
- [Berechnung der Arrayformel von Datenblättern](/cells/de/net/calculation-of-array-formula-of-data-tables/)
- [Berechnung der Excel 2016 MINIFS- und MAXIFS-Funktionen](/cells/de/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Vermindern der Berechnungszeit der Cell.Calculate-Methode](/cells/de/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Erkennen von zirkulären Verweisen](/cells/de/net/detecting-circular-reference/)
- [Direkte Berechnung einer benutzerdefinierten Funktion ohne Eintragung in ein Arbeitsblatt](/cells/de/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementieren eines benutzerdefinierten Berechnungsmotors zur Erweiterung des Standard-Berechnungsmotors von Aspose.Cells](/cells/de/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Unterbrechen oder Abbrechen der Formelberechnung des Arbeitsbuchs](/cells/de/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Rückgabe eines Bereichs von Werten unter Verwendung von AbstractCalculationEngine](/cells/de/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [Rückgabe eines Wertebereichs mit ICustomFunction](/cells/de/net/returning-a-range-of-values-using-icustomfunction/)
- [Festlegen des Formelberechnungsmodus des Arbeitsbuchs](/cells/de/net/setting-formula-calculation-mode-of-workbook/)
- [Verwendung der FormulaText-Funktion in Aspose.Cells](/cells/de/net/using-formulatext-function-in-aspose-cells/)
- [Verwendung der ICustomFunction-Funktion](/cells/de/net/using-icustomfunction-feature/)
{{< app/cells/assistant language="csharp" >}}
