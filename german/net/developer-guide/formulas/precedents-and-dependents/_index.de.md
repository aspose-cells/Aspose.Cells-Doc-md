---
title: Vorgänger und Abhängige
type: docs
weight: 230
url: /de/net/precedents-and-dependents/
---

{{% alert color="primary" %}} 

Komplexe Finanzarbeitsblätter, insbesondere solche, die in Zusammenarbeit entwickelt wurden, können die peinlichsten Fehler verbergen. Formeln auf ihre Genauigkeit zu überprüfen und die Fehlerquelle zu finden, kann schwierig sein, wenn die Formel Vorgänger- und Abhängigenzellen verwendet.

{{% /alert %}} 
## **Einführung**
- **Vorgängerzellen** sind Zellen, auf die in einer anderen Zelle eine Formel verweist. Wenn beispielsweise Zelle D10 die Formel =B5 enthält, dann ist die Zelle B5 ein Vorgänger von Zelle D10.
- **Abhängige Zellen** enthalten Formeln, die auf andere Zellen verweisen. Wenn beispielsweise die Zelle D10 die Formel =B5 enthält, ist die Zelle D10 von der Zelle B5 abhängig.

Um die Tabelle übersichtlicher zu gestalten, möchten Sie möglicherweise klar zeigen, welche Zellen in einer Tabelle in einer Formel verwendet werden. Ebenso möchten Sie die abhängigen Zellen anderer Zellen extrahieren.

Aspose.Cells ermöglicht es Ihnen, die Zellen zu verfolgen und herauszufinden, welche verknüpft sind.
## **Vorgänger- und Abhängige Zellen verfolgen: Microsoft Excel**
Formeln können sich ändern, basierend auf Änderungen, die von einem Kunden vorgenommen wurden. Wenn beispielsweise die Zelle C1 von C3 und C4 abhängt, die eine Formel enthalten, und C1 geändert wird (d. h. die Formel überschrieben wird), müssen C3 und C4 oder andere Zellen entsprechend den Geschäftsregeln angepasst werden, um die Tabelle auszugleichen.

Ebenso angenommen, C1 enthält die Formel "=(B1*22)/(M2*N32)". Ich möchte die Zellen finden, von denen C1 abhängt, d. h. die vorhergehenden Zellen B1, M2 und N32.

Sie müssen möglicherweise die Abhängigkeit einer bestimmten Zelle zu anderen Zellen verfolgen. Wenn Geschäftsregeln in Formeln eingebettet sind, möchten wir die Abhängigkeit herausfinden und einige Regeln entsprechend ausführen. Ebenso, wenn der Wert einer bestimmten Zelle geändert wird, welche Zellen im Arbeitsblatt sind von dieser Änderung betroffen?

Microsoft Excel ermöglicht es Benutzern, Vorgänger und Abhängige zu verfolgen.

1. Auf der **Ansichts-Symbolleiste** wählen Sie **Formelüberwachung** aus. Der Dialog zur Formelüberwachung wird angezeigt.
1. Vorgänger verfolgen:
   1. Wählen Sie die Zelle aus, die die Formel enthält, für die Sie Vorgängerzellen finden möchten.
   1. Um an jede Zelle einen Tracer-Pfeil anzuzeigen, die direkt Daten an die aktive Zelle bereitstellt, klicken Sie auf **Vorgänger verfolgen** auf der **Formelüberwachungs**-Symbolleiste.
1. Formeln verfolgen, die auf eine bestimmte Zelle verweisen (Abhängige)
   1. Wählen Sie die Zelle aus, für die Sie die abhängigen Zellen identifizieren möchten.
   1. Um an jede Zelle, die von der aktiven Zelle abhängig ist, einen Tracer-Pfeil anzuzeigen, klicken Sie auf **Abhängige verfolgen** auf der **Formelüberwachungs**-Symbolleiste.
## **Vorgänger- und Abhängige Zellen verfolgen: Aspose.Cells**
### **Vorgänger verfolgen**
Aspose.Cells erleichtert das Abrufen von Vorgängerzellen. Es kann nicht nur Zellen abrufen, die Daten zu einfachen Formelvorgängern bereitstellen, sondern auch Zellen finden, die Daten zu komplexen Formelvorgängern mit benannten Bereichen bereitstellen.

Im folgenden Beispiel wird eine Vorlagen-Excel-Datei, Book1.xls, verwendet. Das Arbeitsblatt enthält Daten und Formeln.

Aspose.Cells bietet die [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) -Methode [GetPrecedents](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedents) zum Nachverfolgen von Vorgängerzellen. Sie gibt eine [ReferredAreaCollection](https://reference.aspose.com/cells/net/aspose.cells/referredareacollection) zurück. Wie in Book1.xls zu sehen ist, enthält die Zelle B7 die Formel "=SUM(A1:A3)". Daher sind die Zellen A1:A3 die Vorgängerzellen der Zelle B7. Das folgende Beispiel zeigt die Nachverfolgung von Vorgängern unter Verwendung der Vorlagendatei Book1.xls.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingPrecedents-1.cs" >}}
### **Abhängige verfolgen**
Aspose.Cells ermöglicht es Ihnen, abhängige Zellen in Tabellenkalkulationen zu erhalten. Aspose.Cells kann nicht nur Zellen abrufen, die Daten zu einer einfachen Formel bereitstellen, sondern auch Zellen finden, die Daten für komplexe Formeln mit benannten Bereichen bereitstellen.

Aspose.Cells bietet die [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) -Methode [GetDependents](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependents) zum Nachverfolgen von abhängigen Zellen an. Zum Beispiel gibt es in Book1.xlsx die Formeln: "=A1+20" und "=A1+30" in den Zellen B2 und C2. Das folgende Beispiel zeigt, wie die Abhängigkeiten für die Zelle A1 unter Verwendung der Vorlagendatei Book1.xlsx nachverfolgt werden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependents-1.cs" >}}
### **Nachverfolgung von Vorgänger- und abhängigen Zellen gemäß der Berechnungskette**
Die oben genannten APIs zur Nachverfolgung von Vorgängern und Abhängigen richten sich nach dem Formelausdruck selbst. Sie bieten lediglich eine bequeme Möglichkeit für den Benutzer, Abhängigkeiten für einige Formeln zu verfolgen. Wenn es viele Formeln in der Arbeitsmappe gibt und der Benutzer für jede Zelle Vorgänger und Abhängige verfolgen muss, wird die Leistung beeinträchtigt. In solchen Situationen sollten Benutzer in Betracht ziehen, die Methoden [GetPrecedentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedentsincalculation/) und [GetDependentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependentsincalculation/) zu verwenden. Diese beiden Methoden verfolgen Abhängigkeiten gemäß der Berechnungskette. Um sie zu verwenden, müssen Sie zuerst die Berechnungskette mit [Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/enablecalculationchain/) aktivieren. Dann sollten Sie eine vollständige Berechnung für die Arbeitsmappe mit [Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) durchführen. Danach können Sie Vorgänger oder Abhängige für all die Zellen nachverfolgen, die Sie benötigen.

Für einige Formeln können die resultierenden Vorgänger bei GetPrecedents und GetPrecedentsInCalculation unterschiedlich sein, und die resultierenden Abhängigen bei GetDependents und GetDependentsInCalculation können unterschiedlich sein. Wenn z.B. die Formel von Zelle A1 "=IF(TRUE,B2,C3)" ist, liefert GetPrecedents B2 und C3 als Vorgänger von A1. Demnach haben sowohl B2 als auch C3 die abhängige Zelle A1 bei der Überprüfung durch GetDependents. Für die Berechnung dieser Formel ist jedoch offensichtlich, dass nur B2 das berechnete Ergebnis beeinflussen kann. Daher gibt GetPrecedentsInCalculation A1 nicht für C3 zurück, und GetDependentsInCalculation gibt C3 nicht für A1 zurück. Manchmal hat der Benutzer möglicherweise nur die Anforderung, die interdependencies zu verfolgen, die tatsächlich das berechnete Ergebnis der Formeln basierend auf den aktuellen Daten der Arbeitsmappe beeinflussen, dann sollten sie auch GetDependentsInCalculation/GetPrecedentsInCalculation anstelle von GetDependents/GetPrecedents verwenden.

Das folgende Beispiel zeigt, wie Sie die Präzedenzfälle und Dependenzen gemäß der Berechnungskette für Zellen verfolgen können:


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependenciesInCalculation.cs" >}}
{{< app/cells/assistant language="csharp" >}}
