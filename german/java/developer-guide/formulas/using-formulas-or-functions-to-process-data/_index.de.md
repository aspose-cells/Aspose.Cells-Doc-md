---
title: Verwenden von Formeln oder Funktionen zum Verarbeiten von Daten
type: docs
weight: 5
url: /de/java/get-and-set-formula/
---
{{% alert color="primary" %}}

Eines der überzeugenden Merkmale von Microsoft Excel ist die Fähigkeit, Daten mit Formeln und Funktionen zu verarbeiten. Microsoft Excel bietet eine Reihe integrierter Funktionen und Formeln, mit denen Benutzer komplexe Berechnungen schnell durchführen können. Aspose.Cells bietet auch eine große Auswahl an integrierten Funktionen und Formeln, die Entwicklern helfen, Werte einfach zu berechnen. Aspose.Cells unterstützt auch Add-in-Funktionen. Darüber hinaus unterstützt Aspose.Cells Array- und R1C1-Formeln in Aspose.Cells.

{{% /alert %}}

## **Verwenden von Formeln und Funktionen**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) Sammlung. Jeder Artikel in der[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) Sammlung stellt ein Objekt der[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)Klasse.

 Es ist möglich, Formeln auf Zellen anzuwenden, indem Sie Eigenschaften und Methoden verwenden, die von angeboten werden[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)Klasse, die weiter unten ausführlicher besprochen wird.

- [Verwendung integrierter Funktionen](/cells/de/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [Verwenden von Add-In-Funktionen](/cells/de/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [Arbeiten mit Matrixformeln](/cells/de/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [Erstellen einer R1C1-Formel](/cells/de/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **Verwenden von integrierten Funktionen**

 Integrierte Funktionen oder Formeln werden als vorgefertigte Funktionen bereitgestellt, um den Aufwand und die Zeit der Entwickler zu reduzieren. Sehen[eine Liste der integrierten Funktionen](/cells/de/java/supported-formula-functions/). Die Funktionen sind in alphabetischer Reihenfolge aufgelistet. In Zukunft werden weitere Funktionen unterstützt.

 Aspose.Cells unterstützt die meisten Formeln oder Funktionen von Microsoft Excel. Entwickler können diese Formeln über die API oder verwenden[Designer-Tabelle](/cells/de/java/what-is-a-designer-spreadsheet/). Aspose.Cells unterstützt eine große Auswahl an mathematischen, Zeichenfolgen-, Booleschen, Datums-/Uhrzeit-, Statistik-, Datenbank-, Such- und Referenzformeln.

 Verwenden Sie die[**Formel**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)Eigentum der[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse, um einer Zelle eine Formel hinzuzufügen.**Komplexe Formeln**, zum Beispiel

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, werden auch in Aspose.Cells unterstützt. Wenn Sie eine Formel auf eine Zelle anwenden, beginnen Sie die Zeichenfolge immer mit einem Gleichheitszeichen (=), wie Sie es beim Erstellen einer Formel in Microsoft Excel tun, und verwenden Sie ein Komma (,), um Funktionsparameter zu begrenzen.

 Im folgenden Beispiel wird eine komplexe Formel auf die erste Zelle eines Arbeitsblatts angewendet[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) Sammlung. Die Formel verwendet eine eingebaute**WENN** Funktion bereitgestellt von Aspose.Cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **Verwenden von Add-In-Funktionen**

 Wir können einige benutzerdefinierte Formeln haben, die wir als Excel-Add-In einfügen möchten. Beim Einstellen der[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) Die integrierten Funktionen der Funktion funktionieren einwandfrei, es ist jedoch erforderlich, die benutzerdefinierten Funktionen oder Formeln mithilfe der Add-In-Funktionen festzulegen.

 Aspose.Cells bietet Funktionen zum Registrieren von Zusatzfunktionen[**Arbeitsblätter.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction(java.lang.String,%20java.lang.String,%20boolean)). Danach, wenn wir uns setzen[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) anyFunctionFromAddIn enthält die Excel-Ausgabedatei den berechneten Wert aus der AddIn-Funktion.

Anschließend wird die XLAM-Datei zur Registrierung der Add-in-Funktion im unten stehenden Beispielcode heruntergeladen. Ebenso kann die Ausgabedatei „test_udf.xlsx“ heruntergeladen werden, um die Ausgabe zu überprüfen.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **Array-Formel verwenden**

Array-Formeln sind Formeln, die mit Arrays anstelle von einzelnen Zahlen als Argumente für die Funktionen arbeiten, aus denen die Formel besteht. Wenn eine Matrixformel angezeigt wird, ist sie wie unten gezeigt von geschweiften Klammern ({}) umgeben.

**Festlegen einer Matrixformel für Zelle G2** 

![todo: Bild_alt_Text](using-formulas-or-functions-to-process-data_1.png)

Einige Microsoft Excel-Funktionen geben Arrays von Werten zurück. Um mehrere Ergebnisse mit einer Array-Formel zu berechnen, geben Sie das Array in einen Zellbereich mit der gleichen Anzahl von Zeilen und Spalten wie die Array-Argumente ein.

 Es ist möglich, eine Matrixformel auf eine Zelle anzuwenden, indem Sie die aufrufen[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse'[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int) ) Methode. Das[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int))-Methode nimmt die folgenden Parameter an:

- **Array-Formel**, die Matrixformel.
- **Reihenanzahl**die Anzahl der Zeilen, die das Ergebnis der Matrixformel füllen sollen.
- **Anzahl der Spalten**, die Anzahl der Spalten, in die das Ergebnis der Matrixformel gefüllt werden soll.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **Verwenden der R1C1-Formel**

 Bewerben Sie sich ein**R1C1** Referenzstilformel auf eine Zelle mit dem[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse'[**setR1C1Formel**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula)Eigentum.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

