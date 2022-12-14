---
title: Verwalten Sie Formeln von Excel-Dateien
linktitle: Formeln
type: docs
weight: 122
url: /de/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells kann Formeln aus Excel-Dateien einfach abrufen, einstellen und berechnen.
---
## **Einführung**

Eines der überzeugenden Merkmale von Microsoft Excel ist die Fähigkeit, Daten mit Formeln und Funktionen zu verarbeiten. Microsoft Excel bietet eine Reihe integrierter Funktionen und Formeln, mit denen Benutzer komplexe Berechnungen schnell durchführen können. Aspose.Cells bietet auch eine große Auswahl an integrierten Funktionen und Formeln, die Entwicklern helfen, Werte einfach zu berechnen. Aspose.Cells unterstützt auch Add-in-Funktionen. Darüber hinaus unterstützt Aspose.Cells Array- und R1C1-Formeln in Aspose.Cells.

## **Verwenden von Formeln und Funktionen**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Jeder Artikel in der Sammlung Cells repräsentiert ein Objekt der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse.

 Es ist möglich, Formeln auf Zellen anzuwenden, indem Sie Eigenschaften und Methoden verwenden, die von angeboten werden[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse, die weiter unten ausführlicher besprochen wird.

- Verwendung integrierter Funktionen.
- Verwenden von Add-In-Funktionen.
- Arbeiten mit Matrixformeln.
- Erstellen einer R1C1-Formel.

## **Verwenden von integrierten Funktionen**

 Integrierte Funktionen oder Formeln werden als vorgefertigte Funktionen bereitgestellt, um den Aufwand und die Zeit der Entwickler zu reduzieren. Sehen[eine Liste der integrierten Funktionen](/cells/de/net/supported-formula-functions/) unterstützt von Aspose.Cells. Die Funktionen sind in alphabetischer Reihenfolge aufgelistet. In Zukunft werden weitere Funktionen unterstützt.

 Aspose.Cells unterstützt die meisten Formeln oder Funktionen von Microsoft Excel. Entwickler können diese Formeln über die API oder verwenden[Designer-Tabelle](/cells/de/net/what-is-a-designer-spreadsheet/). Aspose.Cells unterstützt eine große Menge mathematischer, Zeichenfolgen-, Boolean-, Datums-/Uhrzeit-, Statistik-, Datenbank-, Such- und Referenzformeln.

 Verwenden Sie die[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse'[**Formel**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)-Eigenschaft, um einer Zelle eine Formel hinzuzufügen.**Komplexe Formeln**, zum Beispiel

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, werden auch in Aspose.Cells unterstützt. Wenn Sie eine Formel auf eine Zelle anwenden, beginnen Sie die Zeichenfolge immer mit einem Gleichheitszeichen (=), wie Sie es beim Erstellen einer Formel in Microsoft Excel tun, und verwenden Sie ein Komma (,), um Funktionsparameter zu begrenzen.

 Im folgenden Beispiel wird eine komplexe Formel auf die erste Zelle eines Arbeitsblatts angewendet[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung. Die Formel verwendet eine eingebaute**WENN** Funktion bereitgestellt von Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **Verwenden von Add-In-Funktionen**

Wir können einige benutzerdefinierte Formeln haben, die wir als Excel-Add-In einfügen möchten. Beim Festlegen der cell.Formula-Funktion funktionieren die integrierten Funktionen einwandfrei, es ist jedoch erforderlich, die benutzerdefinierten Funktionen oder Formeln mithilfe der Add-In-Funktionen festzulegen.

 Aspose.Cells bietet Funktionen zum Registrieren von Zusatzfunktionen[**Arbeitsblätter.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Wenn wir danach cell.Formula = anyFunctionFromAddIn setzen, enthält die Excel-Ausgabedatei den berechneten Wert aus der AddIn-Funktion.

Die folgende XLAM-Datei muss heruntergeladen werden, um die Add-In-Funktion im folgenden Beispielcode zu registrieren. Ebenso kann die Ausgabedatei "test_udf.xlsx" heruntergeladen werden, um die Ausgabe zu überprüfen.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **Array-Formel verwenden**

Array-Formeln sind Formeln, die Arrays anstelle einzelner Zahlen als Argumente für die Funktionen verwenden, aus denen die Formel besteht. Wenn eine Matrixformel angezeigt wird, ist sie von geschweiften Klammern ({}) umgeben.

Einige Microsoft Excel-Funktionen geben Arrays von Werten zurück. Um mehrere Ergebnisse mit einer Array-Formel zu berechnen, geben Sie das Array in einen Zellbereich mit der gleichen Anzahl von Zeilen und Spalten wie die Array-Argumente ein.

 Es ist möglich, eine Matrixformel auf eine Zelle anzuwenden, indem Sie die aufrufen[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse'[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) Methode. Das[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) Die Methode nimmt die folgenden Parameter an:

- **Array-Formel**, die Matrixformel.
- **Reihenanzahl**die Anzahl der Zeilen, die das Ergebnis der Matrixformel füllen sollen.
- **Anzahl der Spalten**die Anzahl der Spalten, die das Ergebnis der Matrixformel füllen sollen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **Verwenden der R1C1-Formel**

 Fügen Sie ein hinzu**R1C1** Referenzstilformel auf eine Zelle mit dem[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse'[**R1C1Formel**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **Themen vorantreiben**
- [Präzedenzfälle und Abhängigkeiten](/cells/de/net/precedents-and-dependents/)
- [Setzen Sie externe Links in Formeln](/cells/de/net/set-external-links-in-formulas/)
- [Geben Sie die Formel automatisch in Tabellen- oder Listenobjekten weiter, während Sie Daten in neue Zeilen eingeben](/cells/de/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Einstellungsformel für den benannten Bereich](/cells/de/net/setting-formula-for-named-range/)
- [Festlegen von Formeln – Hinweis für nicht englische Benutzer](/cells/de/net/setting-formulas-notice-for-non-english-users/)
- [Freigegebene Formel einstellen](/cells/de/net/setting-shared-formula/)
- [Geben Sie die maximalen Zeilen der freigegebenen Formel an](/cells/de/net/specify-maximum-rows-of-shared-formula/)
- [Unterstützte Excel-Funktionen](/cells/de/net/supported-formula-functions/)

