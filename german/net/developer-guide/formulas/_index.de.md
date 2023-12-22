---
title: Verwalten Sie Formeln von Excel-Dateien
linktitle: Formeln
type: docs
weight: 122
url: /de/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells kann einfach Formeln von Excel-Dateien abrufen, festlegen und berechnen.
description: Erfahren Sie, wie Sie Formeln von Excel-Dateien über die APIs Aspose.Cells für NET verwalten.
keywords: How to calculate formulas in C#, Formulas and Functions using C#, C# Manage Built-in Functions, How to Use Add-in Functions with C#, How to Use Array Formula via C#, How to Use R1C1 Formula in C#.
---
##  **Einführung**

Eine der überzeugenden Funktionen von Microsoft Excel ist seine Fähigkeit, Daten mit Formeln und Funktionen zu verarbeiten. Microsoft Excel bietet eine Reihe integrierter Funktionen und Formeln, die Benutzern helfen, komplexe Berechnungen schnell durchzuführen. Aspose.Cells bietet außerdem eine Vielzahl integrierter Funktionen und Formeln, die Entwicklern die einfache Berechnung von Werten erleichtern. Aspose.Cells unterstützt auch Add-In-Funktionen. Darüber hinaus unterstützt Aspose.Cells Array- und R1C1-Formeln in Aspose.Cells.

##  **So verwenden Sie Formeln und Funktionen**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , das eine Microsoft Excel-Datei darstellt. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Jeder Artikel in der Sammlung Cells stellt ein Objekt der dar[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse.

 Es ist möglich, Formeln mithilfe der von angebotenen Eigenschaften und Methoden auf Zellen anzuwenden[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse, die weiter unten ausführlicher besprochen wird.

- Verwendung integrierter Funktionen.
- Verwendung von Add-In-Funktionen.
- Arbeiten mit Arrayformeln.
- Erstellen einer R1C1-Formel.

##  **So verwenden Sie integrierte Funktionen**

Integrierte Funktionen oder Formeln werden als vorgefertigte Funktionen bereitgestellt, um den Aufwand und die Zeit der Entwickler zu reduzieren. Sehen[eine Liste der integrierten Funktionen](/cells/de/net/supported-formula-functions/) unterstützt durch Aspose.Cells. Die Funktionen sind in alphabetischer Reihenfolge aufgelistet. Weitere Funktionen werden in Zukunft unterstützt.

 Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die Microsoft Excel bietet. Entwickler können diese Formeln über API oder verwenden[Designer-Tabelle](/cells/de/net/what-is-a-designer-spreadsheet/). Aspose.Cells unterstützt eine große Auswahl an mathematischen, Zeichenfolgen-, booleschen, Datums-/Uhrzeit-, Statistik-, Datenbank-, Such- und Referenzformeln.

 Benutzen Sie die[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse'[**Formel**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) Eigenschaft, um einer Zelle eine Formel hinzuzufügen. *Komplexe Formeln** zum Beispiel

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, werden auch in Aspose.Cells unterstützt. Wenn Sie eine Formel auf eine Zelle anwenden, beginnen Sie die Zeichenfolge immer mit einem Gleichheitszeichen (=), wie Sie es auch beim Erstellen einer Formel in Microsoft Excel tun, und verwenden Sie ein Komma (,), um Funktionsparameter zu trennen.

 Im folgenden Beispiel wird eine komplexe Formel auf die erste Zelle eines Arbeitsblatts angewendet[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung. Die Formel verwendet eine integrierte**IF** Funktion bereitgestellt von Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

##  **So verwenden Sie Add-In-Funktionen**

Wir können einige benutzerdefinierte Formeln haben, die wir als Excel-Add-In einbinden möchten. Beim Festlegen der Funktion „cell.Formula“ funktionieren die integrierten Funktionen einwandfrei, es ist jedoch erforderlich, die benutzerdefinierten Funktionen oder Formeln mithilfe der Add-in-Funktionen festzulegen.

 Aspose.Cells bietet Funktionen zum Registrieren von Add-In-Funktionen[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Wenn wir anschließend cell.Formula = anyFunctionFromAddIn festlegen, enthält die ausgegebene Excel-Datei den berechneten Wert aus der AddIn-Funktion.

Die folgende Datei XLAM muss heruntergeladen werden, um die Add-in-Funktion im folgenden Beispielcode zu registrieren. Ebenso kann die Ausgabedatei „test_udf.xlsx“ heruntergeladen werden, um die Ausgabe zu überprüfen.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

##  **So verwenden Sie die Array-Formel**

Array-Formeln sind Formeln, die Arrays anstelle einzelner Zahlen als Argumente für die Funktionen verwenden, aus denen die Formel besteht. Wenn eine Array-Formel angezeigt wird, ist sie von geschweiften Klammern ({}) umgeben.

Einige Microsoft Excel-Funktionen geben Arrays mit Werten zurück. Um mehrere Ergebnisse mit einer Array-Formel zu berechnen, geben Sie das Array in einen Zellbereich mit der gleichen Anzahl an Zeilen und Spalten wie die Array-Argumente ein.

 Es ist möglich, eine Array-Formel auf eine Zelle anzuwenden, indem Sie aufrufen[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse'[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) Methode. Der[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) Die Methode benötigt die folgenden Parameter:

- *Array-Formel**, die Array-Formel.
- *Anzahl der Zeilen**, die Anzahl der Zeilen, die als Ergebnis der Array-Formel gefüllt werden sollen.
- *Anzahl der Spalten**, die Anzahl der Spalten, die als Ergebnis der Array-Formel gefüllt werden sollen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

##  **So verwenden Sie die R1C1-Formel**

 Fügen Sie eine hinzu**R1C1** Referenzstilformel auf eine Zelle mit dem[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse'[**R1C1Formel**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

##  **Vorabthemen**
- [Präzedenzfälle und Abhängige](/cells/de/net/precedents-and-dependents/)
- [Legen Sie externe Links in Formeln fest](/cells/de/net/set-external-links-in-formulas/)
- [Geben Sie die Formel automatisch in der Tabelle oder im Listenobjekt weiter, während Sie Daten in neue Zeilen eingeben](/cells/de/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Festlegen der Formel für den benannten Bereich](/cells/de/net/setting-formula-for-named-range/)
- [Formeln festlegen – Hinweis für nicht englische Benutzer](/cells/de/net/setting-formulas-notice-for-non-english-users/)
- [Gemeinsame Formel festlegen](/cells/de/net/setting-shared-formula/)
- [Geben Sie die maximale Anzahl gemeinsam genutzter Formelzeilen an](/cells/de/net/specify-maximum-rows-of-shared-formula/)
- [Unterstützte Excel-Funktionen](/cells/de/net/supported-formula-functions/)

