---  
title: Dynamische Array Formeln mit C++ setzen  
description: Wie man die Aspose.Cells Bibliothek nutzt, um dynamische Array Formeln in Microsoft Excel mit C++ zu berechnen.  
keywords: Dynamische Array Formeln, Dynamische Array Formeln in Excel, Dynamische Array Formeln festlegen, Berechnung von dynamischen Array Formeln, Operationen mit dynamischen Array Formeln in Excel.  
type: docs  
weight: 70  
url: /de/cpp/calculation-of-dynamic-array-formulas/  
---  

## **Was ist die Excel-Array-Formel**  
In Excel ist eine Array-Formel ein spezieller Formeltyp, der es Ihnen ermöglicht, Berechnungen an Datenarrays anstelle einzelner Zellen durchzuführen. Array-Formeln können verwendet werden, um komplexe Berechnungen durchzuführen, Daten zu manipulieren und bestimmte Probleme effizient zu lösen. Sie werden anders als reguläre Formeln eingegeben und erfordern oft die Verwendung von Strg + Umschalt + Eingabe.  

Hier sind einige wichtige Punkte zu Array-Formeln in Excel:  
1. **Syntax:**  
Array-Formeln werden wie normale Formeln geschrieben, beinhalten jedoch Operationen an Wertearrays. Sie sind in geschweiften Klammern { } eingeschlossen, um anzuzeigen, dass es sich um Array-Formeln handelt. Sie tippen jedoch nicht selbst diese geschweiften Klammern; Excel fügt sie automatisch hinzu, wenn Sie die Formel korrekt eingeben.  
1. **Eingabe von Arrayformeln:**  
Um eine Array-Formel einzugeben, tippen Sie die Formel in die Formelleiste. Anstatt mit Enter abzuschließen, drücken Sie Ctrl + Shift + Enter. Damit teilt Excel mit, dass es sich um eine Array-Formel handelt. Wenn sie korrekt eingegeben wurde, zeigt Excel die Formel in geschweiften Klammern in der Formelleiste an, um dies anzuzeigen.  
1. **Anwendungsfälle:**  
Array-Formeln sind nützlich, um Berechnungen über mehrere Zellen oder Bereiche gleichzeitig durchzuführen. Sie können für fortgeschrittene mathematische Berechnungen, bedingte Operationen, Datenfilterung und mehr verwendet werden.  
1. **Vorteile:**  
Array-Formeln ermöglichen es Ihnen, komplexe Berechnungen in einer einzigen Formel durchzuführen, was die Effizienz verbessern und Ihre Arbeitsblätter vereinfachen kann. Sie können große Datensätze verarbeiten und Berechnungen durchführen, für die sonst mehrere Zwischenschritte erforderlich wären.  
1. **Einschränkungen:**  
Array-Formeln können schwieriger zu verstehen und zu beheben sein als normale Formeln. Sie können die Arbeitsblattleistung verlangsamen, insbesondere wenn sie umfangreich oder mit großen Datensätzen verwendet werden.  
1. **Beispiele:**  
Die Summe der Werte in einem Bereich: **{=SUMME(A1:A5*B1:B5)}**  
Ermittlung des maximalen Werts in einem Bereich: **{=MAX(A1:A5+B1:B5)}**  
<br><image src="1.png" width="70%" />  
<br>  
Denken Sie daran, dass Array-Formeln sparsam eingesetzt werden sollten, und es ist wichtig, zu verstehen, wie sie funktionieren, bevor Sie sie in Ihren Arbeitsblättern implementieren. Sie können leistungsfähige Werkzeuge für die Datenanalyse und -manipulation in Excel sein.  

## **Was ist die Excel-Dynamische Array-Formel**  
Dynamische Array-Formeln sind eine neue Funktion, die in Excel 365 und Excel 2021 eingeführt wurde. Sie ermöglichen es Ihnen, mit Datenarrays nahtloser und effizienter zu arbeiten im Vergleich zu herkömmlichen Array-Formeln. Dynamische Array-Formeln geben die Ergebnisse automatisch in benachbarte Zellen aus, was das Drücken von Strg + Umschalt + Enter überflüssig macht und die Manipulation von Daten erleichtert.  

Wichtige Punkte zu dynamischen Array-Formeln in Excel:  
1. **Automatisches Spillen:**  
Dynamische Array-Formeln geben die Ergebnisse automatisch in benachbarte Zellen aus, basierend auf der Größe der Ausgabedaten. Dies bedeutet, dass Sie keinen Zellbereich auswählen müssen, bevor Sie die Formel eingeben, oder Strg + Umschalt + Enter verwenden müssen, um die Formel zu bestätigen.  
1. **Einzellzell-Eingabe:**  
Dynamische Array-Formeln werden in eine einzelne Zelle eingegeben, und Excel füllt automatisch die benachbarten Zellen mit den Ergebnissen aus. Dies erleichtert das Verwalten und Verstehen von Formeln, da Sie die Formel nur einmal eingeben müssen.  
1. **Neue Funktionen:**  
Dynamische Array-Formeln führen neue Funktionen ein, die Arrays nativ verarbeiten können, wie z. B. **FILTER**, **SORT**, **UNIQUE**, **SEQUENCE**, **SORTBY** und **RANDARRAY**. Diese Funktionen können mehrere Werte zurückgeben oder Arrays direkt bearbeiten und somit komplexe Berechnungen vereinfachen.  
1. **Flexible Bereichsverwaltung:**  
Dynamische Array-Formeln passen die Größe des ausgegebenen Bereichs dynamisch an die Größe der Eingangsdaten oder an die durchgeführte Berechnung an. Diese Flexibilität ermöglicht eine effizientere Nutzung des Arbeitsblattbereichs und vereinfacht die Formelerstellung.  
1. **Verbesserte Leistung:**  
Dynamische Array-Formeln können die Leistung im Vergleich zu herkömmlichen Array-Formeln verbessern, insbesondere bei der Arbeit mit großen Datensätzen oder komplexen Berechnungen.  
1. **Kompatibilität:**  
Dynamische Array-Formeln sind in Excel 365 und Excel 2021 verfügbar. Sie werden möglicherweise nicht von älteren Excel-Versionen unterstützt.  
1. **Beispiele für dynamische Arrayformeln:**  
**FILTER**: Gibt ein Array von Werten zurück, die bestimmte Kriterien erfüllen.  
**SORT**: Sortiert die Werte in einem Bereich oder Array.  
**UNIQUE**: Gibt eindeutige Werte aus einer Liste oder einem Bereich zurück.  
**SEQUENCE**: Generiert eine Folge von Zahlen oder Datumswerten.  
**RANDARRAY**: Generiert ein Array von Zufallszahlen.  
<br><image src="2.png" width="70%" />  
<br>  
Dynamische Array-Formeln bieten leistungsstarke Funktionen zur Datenmanipulation und -analyse in Excel und vereinfachen die Arbeit mit Datenarrays sowie die Durchführung komplexer Berechnungen.  

## **Was ist der Unterschied zwischen Array-Formeln und dynamischen Array-Formeln in Excel**  
In Excel werden sowohl Array-Formeln als auch dynamische Array-Formeln verwendet, um Berechnungen gleichzeitig für mehrere Werte durchzuführen, jedoch unterscheiden sie sich in Bezug auf Funktionalität und Implementierung.  

### **Array-Formeln Funktionen**  
1. Array-Formeln sind herkömmliche Formeln in Excel, die Berechnungen an Datenarrays durchführen können.  
1. Sie werden eingetragen, indem nach Eingabe der Formel Strg + Umschalt + Eingabe gedrückt wird, was Excel darüber informiert, dass es sich um eine Array-Formel handelt.  
1. Arrayformeln haben Begrenzungen hinsichtlich ihrer Fähigkeit, Ergebnisse in benachbarte Zellen zu spillen. Sie liefern in der Regel ein einzelnes Ergebnis zurück, obwohl dieses Ergebnis eine Zellarray sein könnte.  
1. Sie existieren schon lange und werden in allen Versionen von Excel unterstützt.  

### **Features dynamischer Array-Formeln**  
1. Dynamische Array-Formeln sind eine neue Funktion, die in Excel 365 (Office 365-Abonnement) und Excel 2021 eingeführt wurde.  
1. Sie geben Ergebnisse automatisch in benachbarte Zellen aus, abhängig von der Größe der Eingabedaten oder der Berechnung der Formel.  
1. Dynamische Array-Formeln erfordern nicht das Drücken von Strg + Umschalt + Eingabe; Sie geben einfach die Formel in eine Zelle ein, und Excel füllt automatisch die benachbarten Zellen mit den Ergebnissen aus.  
1. Diese Formeln können mehrere Ergebnisse (eine Zellenbereich) direkt ohne das Erfordernis einer Array-Formel oder Strg + Umschalt + Eingabe zurückgeben.  
1. Sie verfügen über neue Funktionen wie **FILTER**, **SORT**, **UNIQUE** usw., die Arrays nativ verarbeiten und Ergebnisse im Format eines dynamischen Arrays zurückgeben können.  
Zusammenfassend sind dynamische Array-Formeln eine modernere und bequemere Methode zur Arbeit mit Arrays in Excel, die automatisches Ausschütten von Ergebnissen bietet und den Prozess der Arbeit mit Arrays im Vergleich zu traditionellen Array-Formeln vereinfacht. Sie sind jedoch nur in neueren Versionen von Excel verfügbar, die dynamische Arrays unterstützen.  

## **So legen Sie dynamische Array-Formeln in Excel fest und berechnen sie**  
Das Einrichten dynamischer Array-Formeln in Excel erfordert die Verwendung spezifischer Funktionen, die für die Arbeit mit Datenarrays entwickelt wurden und die Ergebnisse automatisch in benachbarte Zellen ausschütten.  

Hier ist eine schrittweise Anleitung zum Einrichten dynamischer Array-Formeln:  
1. **Zelle auswählen:**  
Wählen Sie die Zelle aus, in der die Ergebnisse der dynamischen Array-Formel erscheinen sollen. Dynamische Array-Formeln schütten die Ergebnisse in benachbarte Zellen aus, also stellen Sie sicher, dass genügend Platz für die ausgegossenen Ausgaben vorhanden ist.  
1. **Formel eingeben:**  
Geben Sie die dynamische Array-Formel in die Formelleiste der ausgewählten Zelle ein. Verwenden Sie eine der dynamischen Array-Funktionen, die in Excel 365 und Excel 2021 verfügbar sind, wie z. B. **FILTER**, **SORT**, **UNIQUE**, **SEQUENCE**, **SORTBY** oder **RANDARRAY**.  
Sie können beispielsweise die FILTER-Funktion verwenden, um eine Liste von Daten basierend auf bestimmten Kriterien zu filtern: **=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.  
<br><image src="3.png" width="70%" />  
<br>  
1. **Enter drücken:**  
Nachdem Sie die Formel eingegeben haben, drücken Sie einfach die Eingabetaste auf Ihrer Tastatur. Im Gegensatz zu traditionellen Array-Formeln müssen Sie nicht Strg + Umschalt + Eingabe drücken.  
1. **Spillbereich beobachten:**  
Excel schüttet die Ergebnisse der Formel automatisch in benachbarte Zellen aus. Der ausgeschüttete Bereich passt sich dynamisch an die Größe der Ausgabedaten oder die Berechnung an, die von der Formel durchgeführt wird. Excel hebt den ausgeschütteten Bereich mit einem Rahmen und einem diagonalen Pfeilsymbol hervor, um anzuzeigen, dass er ausgegossene Daten enthält.  
1. **Mit dem Spillbereich interagieren:**  
Sie können mit dem verschütteten Bereich genauso interagieren wie mit jedem anderen Zellenbereich in Excel. Verwenden Sie den verschütteten Bereich in anderen Formeln, führen Sie Berechnungen durch, formatieren Sie ihn oder beziehen Sie ihn in Diagrammen oder Tabellen ein.  
1. **Formel aktualisieren:**  
Wenn Sie die dynamische Arrayformel ändern müssen, bearbeiten Sie einfach die Formel in der ursprünglichen Zelle, in der sie eingegeben wurde.  
Nach der Bearbeitung drücken Sie erneut Enter, um die Änderungen zu bestätigen. Excel aktualisiert den verschütteten Bereich automatisch, wenn dies erforderlich ist.  
1. **Das Spill Bereich löschen:**  
Wenn Sie die verschütteten Daten löschen möchten, können Sie die Formel aus der ursprünglichen Zelle löschen. Excel löscht dann auch den verschütteten Bereich. Alternativ können Sie den verschütteten Bereich direkt löschen, indem Sie ihn auswählen und die Löschtaste drücken.  
<br>  
Indem Sie diesen Schritten folgen, können Sie in Excel dynamische Arrayformeln einrichten, um Arrays von Daten effizient zu analysieren und zu manipulieren und somit Datenanalyseaufgaben und -berichterstellung zu erleichtern.  

## **So richten Sie dynamische Arrayformeln ein und aktualisieren sie mithilfe von Aspose.Cells**  
Siehe folgenden Beispielcode, der die [Beispiel-Excel-Datei](dynamicArrayFormula.xlsx) lädt, die einige Dummy-Daten enthält. Nach dem Laden der Datei rufen Sie die [Cell.SetDynamicArrayFormula](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setdynamicarrayformula/#setdynamicarrayformula) Funktion auf, um eine dynamische Arrayformel zu setzen, und die [Workbook.RefreshDynamicArrayFormulas](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/refreshdynamicarrayformulas/#refreshdynamicarrayformulas) Funktion, um die dynamischen Arrayformeln zu aktualisieren, bevor Sie die Formelauswertung aufrufen, und speichern schließlich die Arbeitsmappe als [Ausgabe-Excel-Datei](out.xlsx).  

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook(u"dynamicArrayFormula.xlsx");

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Getting the F16 
    Cell f16 = ws.GetCells().Get(u"F16");

    // Set dynamic array formula
    FormulaParseOptions formulaParseOptions;
    f16.SetDynamicArrayFormula(u"=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=25),\"\")", formulaParseOptions, false);

    // Refresh the dynamic array formulas
    workbook.RefreshDynamicArrayFormulas(true);

    workbook.CalculateFormula();
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```  

Die Ausgabesnapshot:  
<br><image src="4.png" width="70%" />  
{{< app/cells/assistant language="cpp" >}}
