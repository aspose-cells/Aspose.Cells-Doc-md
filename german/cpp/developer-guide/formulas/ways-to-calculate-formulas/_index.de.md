---
title: Möglichkeiten zur Berechnung von Formeln
type: docs
weight: 30
url: /de/cpp/ways-to-calculate-formulas/
---
##  **Einführung**
Aspose.Cells verfügt über eine eingebettete Formelberechnungs-Engine. Es kann nicht nur aus Designer-Vorlagen importierte Formeln neu berechnen, sondern unterstützt auch die Berechnung der Ergebnisse von zur Laufzeit hinzugefügten Formeln.
##  **Formeln hinzufügen und Ergebnisse berechnen**
Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die Teil von Microsoft Excel sind. Sie können über API oder mithilfe von Designer-Tabellen verwendet werden. Aspose.Cells unterstützt eine große Auswahl an mathematischen, Zeichenfolgen-, booleschen, Datums-/Uhrzeit-, statistischen, Nachschlage- und Referenzformeln.

Verwenden Sie die Methode Cell.SetFormula, um einer Zelle eine Formel hinzuzufügen. Wenn Sie eine Formel auf eine Zelle anwenden, beginnen Sie die Zeichenfolge immer mit einem Gleichheitszeichen (=), wie Sie es auch beim Erstellen einer Formel in Microsoft Excel tun. Verwenden Sie ein Komma (,), um Funktionsparameter abzugrenzen.

Um die Ergebnisse von Formeln zu berechnen, rufen Sie die Methode Workbook.CalculateFormula() auf, die alle in einer Excel-Datei eingebetteten Formeln verarbeitet. Bitte sehen Sie sich den folgenden Beispielcode an, der die Formel hinzufügt und ihre Ergebnisse berechnet. Bitte überprüfen Sie die[Excel-Datei ausgeben](38109185.xlsx) mit diesem Code generiert.

**Beispielcode**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults-new.cpp" >}}
<!---## **Direct Calculation of Formula**
Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use Worksheet.CalculateFormula(String formula) method to calculate the results of such formulas without adding them to worksheet.

The code below produces the following output.

{{< highlight java >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Sample Code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}   --->
##  **Formeln nur einmal berechnen**
Wenn Workbook.CalculateFormula() aufgerufen wird, um die Werte von Formeln in einer Arbeitsmappenvorlage zu berechnen, erstellt Aspose.Cells eine Berechnungskette. Es erhöht die Leistung, wenn Formeln zum zweiten oder dritten Mal berechnet werden.

Wenn die Vorlage jedoch viele Formeln enthält, kann die erste Berechnung der Formel viel CPU-Verarbeitungszeit und Speicher verbrauchen.

Mit Aspose.Cells können Sie die Erstellung einer Berechnungskette deaktivieren, was nützlich ist, wenn Sie Formeln nur einmal berechnen möchten.

 Bitte rufen Sie Workbook.GetISettings().SetCreateCalcChain() mit dem Parameter false auf. Du kannst den ... benutzen[bereitgestellte Excel-Datei](38109186.xlsx) um diesen Code zu testen.

**Beispielcode**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly-new.cpp" >}}
