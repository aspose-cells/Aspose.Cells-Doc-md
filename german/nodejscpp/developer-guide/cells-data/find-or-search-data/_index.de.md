---  
title: Daten finden oder suchen
type: docs  
weight: 50  
url: /de/nodejs-cpp/find-or-search-data/  
description: Lernen Sie, wie Sie in einem Arbeitsblatt enthaltene Zellen mit bestimmten Daten über die Aspose.Cells for Node.js via C++ API finden oder suchen.  
keywords: Daten finden in Node.js via C++, Daten suchen in Node.js via C++, Zellen mit Formel finden in Node.js via C++, Zellen mit Formel suchen in Node.js via C++, Daten oder Formeln finden mit FindOptions in Node.js via C++, Daten oder Formeln suchen mit FindOptions in Node.js via C++, Zellen mit bestimmten Stringwerten oder Zahlen finden oder suchen in Node.js via C++, Zellen mit bestimmten Daten finden oder suchen  
---  

{{% alert color="primary" %}}  
Microsoft Excel ermöglicht es Benutzern, Zellen in einem Arbeitsblatt zu finden, die bestimmte Daten enthalten.  
{{% /alert %}}  

## **Suchen von Zellen, die bestimmte Daten enthalten**  

### **Verwendung von Microsoft Excel**  

Microsoft Excel ermöglicht es Benutzern, Zellen in einem Arbeitsblatt zu finden, die bestimmte Daten enthalten. Wenn Sie **Bearbeiten** im **Suchen**-Menü in Microsoft Excel auswählen, sehen Sie einen Dialog, in dem Sie den Suchwert festlegen können.  

Hier suchen wir nach dem Wert "Orangen". Aspose.Cells ermöglicht es Entwicklern auch, in einem Arbeitsblatt Zellen mit bestimmten Werten zu finden.  

### **Mit Aspose.Cells for Node.js via C++**  

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), bereit, die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) bietet eine [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert. Die [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung stellt verschiedene Methoden zum Finden von Zellen in einem Arbeitsblatt bereit, die vom Benutzer angegebene Daten enthalten. Einige dieser Methoden werden im Folgenden detaillierter erläutert.  

{{% alert color="primary" %}}  
Alle Find-Methoden geben die Verweise auf die Zellen zurück, die die angegebenen Daten enthalten.  
{{% /alert %}}  

## **Suchen von Zellen, die eine Formel enthalten**  

Entwickler können eine bestimmte Formel im Arbeitsblatt finden, indem sie die [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlungs-Methode [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) aufrufen. Typischerweise akzeptiert die [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-)-Methode drei Parameter:  

- **Objekt:** Das zu suchende Objekt. Der Typ sollte int, double, DateTime, string, bool sein.  
- **Vorherige Zelle:** Vorherige Zelle mit demselben Objekt. Dieser Parameter kann auf null gesetzt werden, wenn von Anfang an gesucht wird.  
- **FindOptions:** Optionen zum Finden des benötigten Objekts.  

Die folgenden Beispiele verwenden Arbeitsblattdaten, um die Find-Methoden zu üben:  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainFormula.js" >}}


## **Suchen von Daten oder Formeln mithilfe von FindOptions**  

Es ist möglich, bestimmte Werte mit der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlungs-[**Cells.find(object, Cell)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-)-Methode und verschiedenen [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions) zu finden. Typischerweise akzeptiert die [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-)-Methode die folgenden Parameter:  

- **Suchwert**, die Daten oder der Wert, nach dem gesucht werden soll.  
- **Vorherige Zelle**, die letzte Zelle, die den gleichen Wert enthielt. Dieser Parameter kann auf null gesetzt werden, wenn von Anfang an gesucht wird.  
- **Suchoptionen**, die Suchoptionen.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindDataUsingFindOptions.js" >}}


## **Zellen finden, die den angegebenen Zeichenfolgenwert oder die angegebene Zahl enthalten**  

Es ist möglich, bestimmte Zeichenkettenwerte durch Aufrufen derselben [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-)-Methode zu finden, die in der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung mit verschiedenen [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions) vorhanden ist.  

Geben Sie die Eigenschaften [**FindOptions.setLookInType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookInType-lookintype-) und [**FindOptions.setLookAtType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookAtType-lookattype-) an. Das folgende Beispiel zeigt, wie diese Eigenschaften verwendet werden, um Zellen mit unterschiedlicher Anzahl von Zeichenketten am **Anfang**, in der **Mitte** oder am **Ende** der Zelle zu finden.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainSpecifyString.js" >}}



## **Erweiterte Themen**  
- [Zellen mit bestimmtem Stil finden](/cells/de/nodejs-cpp/find-cells-with-specific-style/)  
- [Finden, ob der Zellenwert mit einem einzelnen Anführungszeichen beginnt](/cells/de/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Daten mithilfe der Originalwerte suchen](/cells/de/nodejs-cpp/search-data-using-original-values/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
