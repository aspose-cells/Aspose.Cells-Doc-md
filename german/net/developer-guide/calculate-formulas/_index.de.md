---
title: Formeln berechnen
description: In diesem Artikel wird erläutert, wie Sie die Bibliothek Aspose.Cells zum Berechnen von Formeln in Microsoft Excel verwenden. Durch das Laden einer vorhandenen Excel-Datei oder das Erstellen einer neuen Excel-Datei können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um die Formel zu berechnen und das Ergebnis zu erhalten. Abschließend speichern wir die geänderte Excel-Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, formulas, calculations, Direct Calculation of Formula, Calculate Formulas repeatedly, add formulas.
type: docs
weight: 125
url: /de/net/calculate-formulas/
---
##  **Formeln hinzufügen und Ergebnisse berechnen**

Aspose.Cells verfügt über eine eingebettete Formelberechnungs-Engine. Es kann nicht nur aus Designer-Vorlagen importierte Formeln neu berechnen, sondern unterstützt auch die Berechnung der Ergebnisse von zur Laufzeit hinzugefügten Formeln.

 Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die Teil von Microsoft Excel sind (Read[eine Liste der von der Berechnungs-Engine unterstützten Funktionen](/cells/de/net/supported-formula-functions/)). Diese Funktionen können über die APIs oder Designer-Tabellen verwendet werden. Aspose.Cells unterstützt eine große Auswahl an mathematischen, Zeichenfolgen-, booleschen, Datums-/Uhrzeit-, Statistik-, Datenbank-, Such- und Referenzformeln.

 Benutzen Sie die[**Formel**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) Eigentum bzw[**SetFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) Methoden der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse, um einer Zelle eine Formel hinzuzufügen. Wenn Sie eine Formel anwenden, beginnen Sie die Zeichenfolge immer mit einem Gleichheitszeichen (=), wie Sie es beim Erstellen einer Formel in Microsoft Excel tun, und verwenden Sie ein Komma (,), um Funktionsparameter zu trennen.

 Um die Ergebnisse von Formeln zu berechnen, kann der Benutzer Folgendes aufrufen:[**BerechnenFormel**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) Methode der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse, die alle in einer Excel-Datei eingebetteten Formeln verarbeitet. Oder der Benutzer ruft an[**BerechnenFormel**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) Methode der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse, die alle in einem Blatt eingebetteten Formeln verarbeitet. Oder der Benutzer kann auch anrufen[**Berechnung**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) Methode der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse, die die Formel von einem Cell verarbeitet:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

###  **Wichtig zu wissen für Formeln**

{{% alert color="primary" %}}

 Der**Formel** Eigentum und**SetFormula(...)** Methoden der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klassenarbeit anders als die**Berechnung** Methoden der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Und[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klassen. Der**Formel** Eigentum und**SetFormula(...)** Methoden fügen einfach die Formel zu einer Zelle hinzu, berechnen das Ergebnis jedoch nicht zur Laufzeit. Um das Ergebnis der Formeln zu erhalten, rufen Sie bitte an**Berechnung** Methoden.

{{% /alert %}}

##  **Direkte Berechnung der Formel**

Aspose.Cells verfügt über eine eingebettete Formelberechnungs-Engine. Aspose.Cells kann nicht nur Formeln berechnen, die aus einer Designer-Datei importiert wurden, sondern auch Formelergebnisse direkt berechnen.

Manchmal müssen Sie Formelergebnisse direkt berechnen, ohne sie in ein Arbeitsblatt einzufügen. Die Werte der in der Formel verwendeten Zellen sind bereits in einem Arbeitsblatt vorhanden und Sie müssen lediglich das Ergebnis dieser Werte basierend auf einer Excel-Formel Microsoft ermitteln, ohne die Formel in ein Arbeitsblatt einzufügen.

 Sie können die Formelberechnungs-Engine-APIs von Aspose.Cells für verwenden[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Zu[**Berechnung**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) die Ergebnisse solcher Formeln, ohne sie dem Arbeitsblatt hinzuzufügen:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

Der obige Code erzeugt die folgende Ausgabe:
{{< highlight "net" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

##  **So berechnen Sie Formeln wiederholt**

Wenn die Arbeitsmappe viele Formeln enthält und der Benutzer sie wiederholt berechnen muss, wobei nur ein kleiner Teil davon geändert werden muss, kann es für die Leistung hilfreich sein, die Formelberechnungskette zu aktivieren:[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

###  **Wichtig zu wissen**

{{% alert color="primary" %}}

Standardmäßig ist die Berechnungskette deaktiviert. Da das Erstellen der Kette auch zusätzliche Zeit erfordert, ist das erste Mal, dass Formeln berechnet werden([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) kann im Vergleich zur Berechnung von Formeln ohne Kette mehr CPU-Verarbeitungszeit und Speicher verbrauchen. Wenn der Benutzer Formeln nicht wiederholt berechnen muss, sollte das Standardverhalten (Formel direkt berechnen, ohne eine Berechnungskette zu erstellen) die bessere Lösung sein.

{{% /alert %}}


##  **Vorabthemen**
- [Fügen Sie Cells zu Microsoft Excel-Formel-Überwachungsfenster hinzu](/cells/de/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Berechnung der IFNA-Funktion mit Aspose.Cells](/cells/de/net/calculating-ifna-function-using-aspose-cells/)
- [Berechnung der Array-Formel von Datentabellen](/cells/de/net/calculation-of-array-formula-of-data-tables/)
- [Berechnung der MINIFS- und MAXIFS-Funktionen von Excel 2016](/cells/de/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Verringern Sie die Berechnungszeit von Cell. Berechnen Sie die Methode](/cells/de/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Erkennen von Zirkelverweisen](/cells/de/net/detecting-circular-reference/)
- [Direkte Berechnung einer benutzerdefinierten Funktion, ohne sie in ein Arbeitsblatt zu schreiben](/cells/de/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementieren Sie eine benutzerdefinierte Berechnungs-Engine, um die Standard-Berechnungs-Engine von Aspose.Cells zu erweitern](/cells/de/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Unterbrechen oder brechen Sie die Formelberechnung der Arbeitsmappe ab](/cells/de/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Zurückgeben eines Wertebereichs mit AbstractCalculationEngine](/cells/de/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [Zurückgeben eines Wertebereichs mithilfe von ICustomFunction](/cells/de/net/returning-a-range-of-values-using-icustomfunction/)
- [Festlegen des Formelberechnungsmodus der Arbeitsmappe](/cells/de/net/setting-formula-calculation-mode-of-workbook/)
- [Verwendung der FormulaText-Funktion in Aspose.Cells](/cells/de/net/using-formulatext-function-in-aspose-cells/)
- [Verwenden der ICustomFunction-Funktion](/cells/de/net/using-icustomfunction-feature/)
