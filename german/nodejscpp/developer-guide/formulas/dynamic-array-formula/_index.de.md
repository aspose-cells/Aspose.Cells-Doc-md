---  
title: Dynamische Arrayformeln mit Node.js via C++ festlegen  
linktitle: Festlegen von dynamischen Array Formeln  
description: So verwenden Sie die Aspose.Cells Bibliothek, um dynamische Arrayformeln in Excel mit Node.js via C++ zu berechnen. Excel Dateien einfach laden, berechnen und speichern.  
keywords: Dynamische Arrayformeln, dynamische Arrayformeln in Excel, dynamische Arrayformeln in Node.js via C++, Berechnung dynamischer Arrayformeln in Node.js via C++, operieren mit dynamischen Arrayformeln in Excel.  
type: docs  
weight: 70  
url: /de/nodejs-cpp/calculation-of-dynamic-array-formulas/  
---  
## **Was ist die Excel-Array-Formel**  
In Excel ist eine Array-Formel ein spezieller Formeltyp, der es Ihnen ermöglicht, Berechnungen an Datenarrays anstelle einzelner Zellen durchzuführen. Array-Formeln können verwendet werden, um komplexe Berechnungen durchzuführen, Daten zu manipulieren und bestimmte Probleme effizient zu lösen. Sie werden anders als reguläre Formeln eingegeben und erfordern oft die Verwendung von Strg + Umschalt + Eingabe.

Hier sind einige wichtige Punkte zu Array-Formeln in Excel:  
1. Syntax:  
<br>  
Array-Formeln werden wie normale Formeln geschrieben, beinhalten jedoch Operationen an Wertearrays. Sie sind in geschweiften Klammern { } eingeschlossen, um anzuzeigen, dass es sich um Array-Formeln handelt. Sie tippen jedoch nicht selbst diese geschweiften Klammern; Excel fügt sie automatisch hinzu, wenn Sie die Formel korrekt eingeben.  
2. Eingabe von Array-Formeln:  
<br>  
Um eine Array-Formel einzugeben, tippen Sie die Formel in die Formelleiste. Anstatt mit Enter abzuschließen, drücken Sie Ctrl + Shift + Enter. Damit teilt Excel mit, dass es sich um eine Array-Formel handelt. Wenn sie korrekt eingegeben wurde, zeigt Excel die Formel in geschweiften Klammern in der Formelleiste an, um dies anzuzeigen.  
3. Anwendungsfälle:  
<br>  
Array-Formeln sind nützlich, um Berechnungen über mehrere Zellen oder Bereiche gleichzeitig durchzuführen. Sie können für fortgeschrittene mathematische Berechnungen, bedingte Operationen, Datenfilterung und mehr verwendet werden.  
4. Vorteile:  
<br>  
Array-Formeln ermöglichen es Ihnen, komplexe Berechnungen in einer einzigen Formel durchzuführen, was die Effizienz verbessern und Ihre Arbeitsblätter vereinfachen kann. Sie können große Datensätze verarbeiten und Berechnungen durchführen, für die sonst mehrere Zwischenschritte erforderlich wären.  
5. Einschränkungen:  
<br>  
Array-Formeln können schwieriger zu verstehen und zu beheben sein als normale Formeln. Sie können die Arbeitsblattleistung verlangsamen, insbesondere wenn sie umfangreich oder mit großen Datensätzen verwendet werden.  
6. Beispiele:  
<br>  
Die Summe der Werte in einem Bereich: **{=SUMME(A1:A5*B1:B5)}**  
<br>  
Ermittlung des maximalen Werts in einem Bereich: **{=MAX(A1:A5+B1:B5)}**  
<br>  
<image src="1.png" width="70%" />  
<br>  

Denken Sie daran, dass Array-Formeln sparsam eingesetzt werden sollten, und es ist wichtig, zu verstehen, wie sie funktionieren, bevor Sie sie in Ihren Arbeitsblättern implementieren. Sie können leistungsfähige Werkzeuge für die Datenanalyse und -manipulation in Excel sein.

## **Was ist die Excel-Dynamische Array-Formel**  
Dynamische Array-Formeln sind eine neue Funktion, die in Excel 365 und Excel 2021 eingeführt wurde. Sie ermöglichen es Ihnen, mit Datenarrays nahtloser und effizienter zu arbeiten im Vergleich zu herkömmlichen Array-Formeln. Dynamische Array-Formeln geben die Ergebnisse automatisch in benachbarte Zellen aus, was das Drücken von Strg + Umschalt + Enter überflüssig macht und die Manipulation von Daten erleichtert.

Wichtige Punkte zu dynamischen Array-Formeln in Excel:  
1. Automatisches Ausdehnen:  
<br>  
Dynamische Array-Formeln geben die Ergebnisse automatisch in benachbarte Zellen aus, basierend auf der Größe der Ausgabedaten. Dies bedeutet, dass Sie keinen Zellbereich auswählen müssen, bevor Sie die Formel eingeben, oder Strg + Umschalt + Enter verwenden müssen, um die Formel zu bestätigen.  
2. Einzelzelleingabe:  
<br>  
Dynamische Array-Formeln werden in eine einzelne Zelle eingegeben, und Excel füllt automatisch die benachbarten Zellen mit den Ergebnissen aus. Dies erleichtert das Verwalten und Verstehen von Formeln, da Sie die Formel nur einmal eingeben müssen.  
3. Neue Funktionen:  
<br>  
Dynamische Array-Formeln führen neue Funktionen ein, die Arrays nativ verarbeiten können, wie z. B. **FILTER**, **SORT**, **UNIQUE**, **SEQUENCE**, **SORTBY** und **RANDARRAY**. Diese Funktionen können mehrere Werte zurückgeben oder Arrays direkt bearbeiten und somit komplexe Berechnungen vereinfachen.  
4. Flexible Bereichsverwaltung:  
<br>  
Dynamische Array-Formeln passen die Größe des ausgegebenen Bereichs dynamisch an die Größe der Eingangsdaten oder an die durchgeführte Berechnung an. Diese Flexibilität ermöglicht eine effizientere Nutzung des Arbeitsblattbereichs und vereinfacht die Formelerstellung.  
5. Verbesserte Leistung:  
<br>  
Dynamische Array-Formeln können die Leistung im Vergleich zu herkömmlichen Array-Formeln verbessern, insbesondere bei der Arbeit mit großen Datensätzen oder komplexen Berechnungen.  
6. Kompatibilität:  
<br>  
Dynamische Array-Formeln sind in Excel 365 und Excel 2021 verfügbar. Sie werden möglicherweise nicht von älteren Excel-Versionen unterstützt.  
7. Beispiele für dynamische Arrayformeln:  
<br>  
**FILTER**: Gibt ein Array von Werten zurück, die bestimmte Kriterien erfüllen.  
<br>  
**SORT**: Sortiert die Werte in einem Bereich oder Array.  
<br>  
**UNIQUE**: Gibt eindeutige Werte aus einer Liste oder einem Bereich zurück.  
<br>  
**SEQUENCE**: Generiert eine Folge von Zahlen oder Datumswerten.  
<br>  
**RANDARRAY**: Generiert ein Array von Zufallszahlen.  
<br>  
<image src="2.png" width="70%" />  
<br>  

Dynamische Array-Formeln bieten leistungsstarke Funktionen zur Datenmanipulation und -analyse in Excel und vereinfachen die Arbeit mit Datenarrays sowie die Durchführung komplexer Berechnungen.

## **Was ist der Unterschied zwischen Array-Formeln und dynamischen Array-Formeln in Excel**  
In Excel werden sowohl Array-Formeln als auch dynamische Array-Formeln verwendet, um Berechnungen gleichzeitig für mehrere Werte durchzuführen, jedoch unterscheiden sie sich in Bezug auf Funktionalität und Implementierung.

### **Array-Formeln Funktionen**  
1. Array-Formeln sind herkömmliche Formeln in Excel, die Berechnungen an Datenarrays durchführen können.  
2. Sie werden durch Drücken von Strg + Umschalt + Eingabetaste nach Eingabe der Formel eingegeben, was Excel mitteilt, dass es sich um eine Array-Formel handelt.  
3. Array-Formeln haben Einschränkungen hinsichtlich ihrer Fähigkeit, Ergebnisse in benachbarte Zellen zu spillen. Sie geben typischerweise ein einzelnes Ergebnis zurück, obwohl dieses Ergebnis ein Zellarray sein kann.  
4. Sie sind schon lange vorhanden und werden in allen Versionen von Excel unterstützt.

### **Features dynamischer Array-Formeln**  
1. Dynamische Array-Formeln sind eine neue Funktion, die in Excel 365 (Office 365-Abonnement) und Excel 2021 eingeführt wurde.  
2. Sie spillen Ergebnisse automatisch in benachbarte Zellen basierend auf der Größe der Eingabedaten oder der Berechnung der Formel.  
3. Dynamische Array-Formeln benötigen kein Drücken von Strg + Umschalt + Eingabetaste; Sie tippen die Formel einfach in eine Zelle ein, und Excel füllt automatisch die benachbarten Zellen mit den Ergebnissen.  
4. Diese Formeln können mehrere Ergebnisse (einen Zellbereich) direkt zurückgeben, ohne dass eine Array-Formel oder Strg + Umschalt + Eingabetaste erforderlich ist.  
5. Sie verfügen über neue Funktionen wie **FILTER**, **SORT**, **UNIQUE** usw., die Arrays nativ verarbeiten und Ergebnisse in einem dynamischen Array-Format zurückgeben können.  
Zusammenfassend sind dynamische Array-Formeln eine modernere und bequemere Methode zur Arbeit mit Arrays in Excel, die automatisches Ausschütten von Ergebnissen bietet und den Prozess der Arbeit mit Arrays im Vergleich zu traditionellen Array-Formeln vereinfacht. Sie sind jedoch nur in neueren Versionen von Excel verfügbar, die dynamische Arrays unterstützen.

## **So legen Sie dynamische Array-Formeln in Excel fest und berechnen sie**  
Das Einrichten dynamischer Array-Formeln in Excel erfordert die Verwendung spezifischer Funktionen, die für die Arbeit mit Datenarrays entwickelt wurden und die Ergebnisse automatisch in benachbarte Zellen ausschütten. 

Hier ist eine schrittweise Anleitung zum Einrichten dynamischer Array-Formeln:  
1. Wählen Sie die Zelle aus:  
<br>  
Wählen Sie die Zelle aus, in der die Ergebnisse der dynamischen Array-Formel erscheinen sollen. Dynamische Array-Formeln schütten die Ergebnisse in benachbarte Zellen aus, also stellen Sie sicher, dass genügend Platz für die ausgegossenen Ausgaben vorhanden ist.  
2. Geben Sie die Formel ein:  
<br>  
Geben Sie die dynamische Array-Formel in die Formelleiste der ausgewählten Zelle ein. Verwenden Sie eine der dynamischen Array-Funktionen, die in Excel 365 und Excel 2021 verfügbar sind, wie z. B. **FILTER**, **SORT**, **UNIQUE**, **SEQUENCE**, **SORTBY** oder **RANDARRAY**.  
<br>  
Sie können beispielsweise die FILTER-Funktion verwenden, um eine Liste von Daten basierend auf bestimmten Kriterien zu filtern: **=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.  
<br>  
<image src="3.png" width="70%" />  
<br>  
3. Drücken Sie Enter:  
<br>  
Nachdem Sie die Formel eingegeben haben, drücken Sie einfach die Eingabetaste auf Ihrer Tastatur. Im Gegensatz zu traditionellen Array-Formeln müssen Sie nicht Strg + Umschalt + Eingabe drücken.  
4. Beobachten Sie den Spill-Bereich:  
<br>  
Excel schüttet die Ergebnisse der Formel automatisch in benachbarte Zellen aus. Der ausgeschüttete Bereich passt sich dynamisch an die Größe der Ausgabedaten oder die Berechnung an, die von der Formel durchgeführt wird. Excel hebt den ausgeschütteten Bereich mit einem Rahmen und einem diagonalen Pfeilsymbol hervor, um anzuzeigen, dass er ausgegossene Daten enthält.  
5. Interagieren Sie mit dem Spill-Bereich:  
<br>  
Sie können mit dem verschütteten Bereich genauso interagieren wie mit jedem anderen Zellenbereich in Excel. Verwenden Sie den verschütteten Bereich in anderen Formeln, führen Sie Berechnungen durch, formatieren Sie ihn oder beziehen Sie ihn in Diagrammen oder Tabellen ein.  
6. Aktualisieren Sie die Formel:  
<br>  
Wenn Sie die dynamische Array-Formel ändern müssen, bearbeiten Sie einfach die Formel in der ursprünglichen Zelle, in der sie eingegeben wurde. Nach der Bearbeitung drücken Sie erneut Enter, um die Änderungen zu bestätigen. Excel aktualisiert automatisch den Spill-Bereich, falls erforderlich.  
7. Das Löschen des Spill-Bereichs:  
<br>  
Wenn Sie die verschütteten Daten löschen möchten, können Sie die Formel aus der ursprünglichen Zelle löschen. Excel löscht dann auch den verschütteten Bereich. Alternativ können Sie den verschütteten Bereich direkt löschen, indem Sie ihn auswählen und die Löschtaste drücken.  
<br>  

Indem Sie diesen Schritten folgen, können Sie in Excel dynamische Arrayformeln einrichten, um Arrays von Daten effizient zu analysieren und zu manipulieren und somit Datenanalyseaufgaben und -berichterstellung zu erleichtern.

## **So richten Sie dynamische Arrayformeln ein und aktualisieren sie mithilfe von Aspose.Cells**  
Siehe folgendes Beispiel, das den Ladeprozess der [Beispiel-Excel-Datei](dynamicArrayFormula.xlsx) zeigt, die einige Dummy-Daten enthält. Nach dem Laden der Datei rufen Sie die [Cell.setDynamicArrayFormula(string, FormulaParseOptions, boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setDynamicArrayFormula-string-formulaparseoptions-boolean-) Funktion auf, um die dynamische Array-Formel zu setzen, und die [Workbook.refreshDynamicArrayFormulas(boolean)](https://reference.aspose.com/cells/nodejs-cpp/workbook/#refreshDynamicArrayFormulas-boolean-) Funktion, um die dynamischen Array-Formeln zu aktualisieren, bevor Sie die Formel berechnen, und speichern schließlich die Arbeitsmappe als [Ausgabedatei](out.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "dynamicArrayFormula.xlsx");

// Instantiate an Workbook object
const wb = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const ws = wb.getWorksheets().get(0);

// Getting the F16 
const f16 = ws.getCells().get("F16");

// Set dynamic array formula
f16.setDynamicArrayFormula("=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=25),\"\")", new AsposeCells.FormulaParseOptions(), false);

// Refresh the dynamic array formulas
wb.refreshDynamicArrayFormulas(true);

wb.calculateFormula();
wb.save("out.xlsx");
```

Die Ausgabesnapshot:  
<br>  
<image src="4.png" width="70%" />  

