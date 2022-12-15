---
title: Möglichkeiten zur Berechnung von Formeln
type: docs
weight: 30
url: /de/cpp/ways-to-calculate-formulas/
---
## **Einführung**
Aspose.Cells hat eine eingebettete Formelberechnungsmaschine. Es kann nicht nur aus Designervorlagen importierte Formeln neu berechnen, sondern unterstützt auch die Berechnung der Ergebnisse von Formeln, die zur Laufzeit hinzugefügt wurden.
## **Formeln hinzufügen und Ergebnisse berechnen**
Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die Teil von Microsoft Excel sind. Sie können über die API oder mithilfe von Designer-Tabellen verwendet werden. Aspose.Cells unterstützt eine große Auswahl an mathematischen, Zeichenfolgen-, booleschen, Datums-/Uhrzeit-, Statistik-, Nachschlage- und Referenzformeln.

Verwenden Sie die Methode Cell.Formula, um einer Zelle eine Formel hinzuzufügen. Wenn Sie eine Formel auf eine Zelle anwenden, beginnen Sie die Zeichenfolge immer mit einem Gleichheitszeichen (=), wie Sie es auch beim Erstellen einer Formel in Microsoft Excel tun. Verwenden Sie ein Komma (,), um Funktionsparameter zu begrenzen.

Um die Ergebnisse von Formeln zu berechnen, rufen Sie die Methode Workbook.CalculateFormula() auf, die alle in einer Excel-Datei eingebetteten Formeln verarbeitet. Bitte sehen Sie sich den folgenden Beispielcode an, der die Formel hinzufügt und ihre Ergebnisse berechnet. Bitte überprüfen Sie die[Excel-Datei ausgeben](38109185.xlsx) mit diesem Code generiert.

**Beispielcode**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults.cpp" >}}
## **Direkte Berechnung der Formel**
Manchmal müssen Sie Formelergebnisse direkt berechnen, ohne sie in ein Arbeitsblatt einzufügen. Die Werte der in der Formel verwendeten Zellen sind bereits in einem Arbeitsblatt vorhanden, und alles, was Sie brauchen, ist, das Ergebnis dieser Werte basierend auf einer Microsoft-Excel-Formel zu finden, ohne die Formel in einem Arbeitsblatt hinzuzufügen.

Sie können die Methode Worksheet.CalculateFormula(String formula) verwenden, um die Ergebnisse solcher Formeln zu berechnen, ohne sie dem Arbeitsblatt hinzuzufügen.

Der folgende Code erzeugt die folgende Ausgabe.

{{< highlight "java" >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Beispielcode**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}
## **Formeln nur einmal berechnen**
Wenn Workbook.CalculateFormula() aufgerufen wird, um die Werte von Formeln in einer Arbeitsmappenvorlage zu berechnen, erstellt Aspose.Cells eine Berechnungskette. Es erhöht die Performance, wenn Formeln zum zweiten oder dritten Mal berechnet werden.

Wenn die Vorlage jedoch viele Formeln enthält, kann das erste Mal, wenn die Formel berechnet wird, viel CPU-Verarbeitungszeit und Arbeitsspeicher beanspruchen.

Mit Aspose.Cells können Sie das Erstellen einer Berechnungskette deaktivieren, was nützlich ist, wenn Sie Formeln nur einmal berechnen möchten.

 Bitte rufen Sie Workbook.GetISettings().SetCreateCalcChain() mit falschem Parameter auf. Du kannst den ... benutzen[bereitgestellte Excel-Datei](38109186.xlsx) um diesen Code zu testen.

**Beispielcode**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly.cpp" >}}
