---
title: Verwendung von Formeln oder Funktionen zur Verarbeitung von Daten
type: docs
weight: 5
url: /de/java/get-and-set-formula/
---

{{% alert color="primary" %}}

Eine der fesselnden Funktionen von Microsoft Excel ist seine Fähigkeit, Daten mit Formeln und Funktionen zu verarbeiten. Microsoft Excel bietet eine Reihe von integrierten Funktionen und Formeln, die Benutzern helfen, komplexe Berechnungen schnell durchzuführen. Aspose.Cells bietet auch eine Vielzahl von integrierten Funktionen und Formeln, die Entwicklern die Berechnung von Werten erleichtern. Außerdem unterstützt Aspose.Cells Add-In-Funktionen. Darüber hinaus unterstützt Aspose.Cells Array- und R1C1-Formeln in Aspose.Cells.

{{% /alert %}}

## **Verwendung von Formeln und Funktionen**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)-Sammlung, die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-Sammlung repräsentiert ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Es ist möglich, Formeln auf Zellen mithilfe der Eigenschaften und Methoden, die von der Klasse [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) angeboten werden, anzuwenden, die im Folgenden genauer erörtert werden.

- [Verwendung von integrierten Funktionen](/cells/de/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [Verwendung von Add-In-Funktionen](/cells/de/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [Arbeiten mit Array-Formeln](/cells/de/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [Erstellen einer R1C1-Formel](/cells/de/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **Verwendung von integrierten Funktionen**

Integrierte Funktionen oder Formeln werden als fertige Funktionen bereitgestellt, um den Aufwand und die Zeit von Entwicklern zu reduzieren. Siehe [eine Liste der integrierten Funktionen](/cells/de/java/supported-formula-functions/). Die Funktionen sind alphabetisch aufgeführt. Weitere Funktionen werden in Zukunft unterstützt.

Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die von Microsoft Excel angeboten werden. Entwickler können diese Formeln über die API oder das [Designer-Tabellenblatt](/cells/de/java/what-is-a-designer-spreadsheet/) verwenden. Aspose.Cells unterstützt eine Vielzahl von mathematischen, Zeichenfolgen-, Booleschen, Datum/Zeit-, statistischen, Datenbank-, Such-, und Verweisformeln.

Verwenden Sie die [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)-Eigenschaft der Klasse [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell), um einer Zelle eine Formel hinzuzufügen. **Komplexe Formeln**, zum Beispiel

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, werden auch von Aspose.Cells unterstützt. Beim Anwenden einer Formel auf eine Zelle beginnen Sie immer die Zeichenfolge mit einem Gleichheitszeichen (=), wie Sie es bei der Erstellung einer Formel in Microsoft Excel tun, und verwenden ein Komma (,) zur Trennung der Funktionsparameter.

Im folgenden Beispiel wird eine komplexe Formel auf die erste Zelle der [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-Sammlung eines Arbeitsblatts angewendet. Die Formel verwendet eine integrierte **IF**-Funktion, die von Aspose.Cells bereitgestellt wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **Verwenden von Add-in-Funktionen**

Wir können einige benutzerdefinierte Formeln haben, die wir als Excel-Add-In einfügen möchten. Beim Einstellen der [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)-Funktion funktionieren integrierte Funktionen gut, jedoch besteht die Notwendigkeit, benutzerdefinierte Funktionen oder Formeln mit den Add-In-Funktionen einzustellen.

Aspose.Cells bietet Funktionen zur Registrierung von Add-In-Funktionen mit [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction(java.lang.String,%20java.lang.String,%20boolean)). Anschließend, wenn wir [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) = anyFunctionFromAddIn einstellen, enthält die Ausgabedatei von Excel den berechneten Wert aus der Add-In-Funktion.

Die folgende XLAM-Datei soll für die Registrierung der Add-In-Funktion im untenstehenden Beispielcode heruntergeladen werden. Ebenso kann die Ausgabedatei "test_udf.xlsx" heruntergeladen werden, um das Ergebnis zu überprüfen.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **Verwendung von Array-Formel**

Array-Formeln sind Formeln, die mit Arrays anstelle einzelner Zahlen als Argumente für die Funktionen arbeiten, die die Formel bilden. Wenn eine Array-Formel angezeigt wird, ist sie wie unten gezeigt von geschweiften Klammern ({}) umgeben.

**Einrichten einer Array-Formel in Zelle G2** 

![todo:image_alt_text](using-formulas-or-functions-to-process-data_1.png)

Einige Microsoft Excel-Funktionen geben Arrays von Werten zurück. Um mehrere Ergebnisse mit einer Array-Formel zu berechnen, geben Sie das Array in einen Zellenbereich mit derselben Anzahl von Zeilen und Spalten wie die Array-Argumente ein.

Es ist möglich, eine Array-Formel auf eine Zelle anzuwenden, indem die [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-Klasse die [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int))-Methode aufruft. Die [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int))-Methode nimmt die folgenden Parameter an:

- **Array-Formel**, die Array-Formel.
- **Anzahl der Zeilen**, die Anzahl der Zeilen zum Ausfüllen des Ergebnisses der Array-Formel.
- **Anzahl der Spalten**, die Anzahl der Spalten zur Ergebnisausgabe der Array-Formel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **Verwenden von R1C1-Formel**

Wenden Sie eine Referenzformel im *R1C1*-Format auf eine Zelle mit der [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-Klasse [**setR1C1Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula)-Eigenschaft an.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

