---
title: Präzedenzfälle und Abhängigkeiten
type: docs
weight: 230
url: /de/java/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Komplexe Finanzarbeitsblätter, insbesondere solche, die gemeinsam entwickelt wurden, können die peinlichsten Fehler verbergen. Das Überprüfen von Formeln auf Genauigkeit und das Auffinden der Fehlerquelle kann schwierig sein, wenn die Formel Vorgängerzellen und abhängige Zellen verwendet.

{{% /alert %}} 
## **Einführung**
- **Vorhergehende Zellen** sind Zellen, auf die durch eine Formel in einem anderen Cell verwiesen wird. Wenn beispielsweise Zelle D10 die Formel =B5 enthält, ist Zelle B5 ein Präzedenzfall für Zelle D10.
- **Abhängige Zellen** Formeln enthalten, die auf andere Zellen verweisen. Wenn beispielsweise Zelle D10 die Formel =B5 enthält, ist Zelle D10 von Zelle B5 abhängig.

Um die Tabellenkalkulation leicht lesbar zu machen, möchten Sie möglicherweise deutlich zeigen, welche Zellen in einer Tabellenkalkulation in einer Formel verwendet werden. Ebenso möchten Sie möglicherweise die abhängigen Zellen anderer Zellen extrahieren.

Aspose.Cells ermöglicht es Ihnen, Zellen zu verfolgen und herauszufinden, welche verknüpft sind.
## **Ablaufverfolgung Präzedenzfall und abhängiger Cells: Microsoft Excel**
Formeln können sich aufgrund von Änderungen ändern, die von einem Kunden vorgenommen wurden. Wenn beispielsweise Zelle C1 von C3 und C4 abhängig ist, die eine Formel enthalten, und C1 geändert wird (so dass die Formel überschrieben wird), müssen C3 und C4 oder andere Zellen geändert werden, um die Tabelle basierend auf Geschäftsregeln auszugleichen.

Angenommen, C1 enthält die Formel "=(B1*22)/(M2*N32)". Ich möchte die Zellen finden, von denen C1 abhängt, also die vorangegangenen Zellen B1, M2 und N32.

Möglicherweise müssen Sie die Abhängigkeit einer bestimmten Zelle von anderen Zellen nachverfolgen. Wenn Geschäftsregeln in Formeln eingebettet sind, möchten wir die Abhängigkeit herausfinden und einige Regeln darauf basierend ausführen. Wenn der Wert einer bestimmten Zelle geändert wird, welche Zellen im Arbeitsblatt sind von dieser Änderung betroffen?

Microsoft Excel ermöglicht es Benutzern, Präzedenzfälle und Abhängige zu verfolgen.

1.  Auf der**Symbolleiste anzeigen** , auswählen**Formel Auditing**. Das Dialogfeld "Formelüberwachung" wird angezeigt.
1. Präzedenzfälle verfolgen:
1. Wählen Sie die Zelle aus, die die Formel enthält, für die Sie vorangegangene Zellen suchen möchten.
 1. Um einen Verfolgungspfeil zu jeder Zelle anzuzeigen, die direkt Daten für die aktive Zelle bereitstellt, klicken Sie auf**Präzedenzfälle verfolgen** auf der**Formel Auditing** Symbolleiste.
1. Verfolgen Sie Formeln, die auf eine bestimmte Zelle verweisen (abhängige Zellen)
 1. Wählen Sie die Zelle aus, für die Sie die abhängigen Zellen identifizieren möchten.
 1. Um einen Verfolgungspfeil zu jeder Zelle anzuzeigen, die von der aktiven Zelle abhängig ist, klicken Sie in der Symbolleiste „Formelprüfung“ auf Abhängigkeiten verfolgen.
## **Verfolgung von Präzedenzfällen und abhängigen Cells: Aspose.Cells**
### **Präzedenzfälle verfolgen**
Aspose.Cells macht es einfach, Präzedenzzellen zu erhalten. Es kann nicht nur Zellen abrufen, die Daten für einfache Formelpräzedenzfälle bereitstellen, sondern auch Zellen finden, die Daten für komplexe Formelpräzedenzfälle mit benannten Bereichen bereitstellen.

Im folgenden Beispiel wird eine Excel-Vorlagendatei, Book1.xls, verwendet. Die Tabelle enthält Daten und Formeln auf dem ersten Arbeitsblatt.

 Aspose.Cells bietet die[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) Klasse'[GetPrecedents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedents() ) Methode, die verwendet wird, um die Präzedenzfälle einer Zelle zu verfolgen. Es gibt a zurück[ReferredAreaCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredAreaCollection)Wie Sie oben sehen können, enthält Zelle B7 in Book1.xls eine Formel „=SUMME(A1:A3)“. Die Zellen A1:A3 sind also die Vorgängerzellen von Zelle B7. Das folgende Beispiel demonstriert das Tracing-Precedence-Feature unter Verwendung der Vorlagendatei Book1.xls.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingPrecedents.java" >}}
### **Abhängigkeiten verfolgen**
Mit Aspose.Cells können Sie abhängige Zellen in Tabellenkalkulationen abrufen. Aspose.Cells kann nicht nur Zellen abrufen, die Daten zu einer einfachen Formel liefern, sondern auch Zellen finden, die Daten zu komplexen Formelabhängigen mit benannten Bereichen liefern.

 Aspose.Cells bietet die[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) Klasse'[GetDependents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependents(boolean))-Methode, die verwendet wird, um die abhängigen Zellen einer Zelle zu verfolgen. Beispielsweise gibt es in Book1.xlsx Formeln: „=A1+20“ und „=A1+30“ in den B2- bzw. C2-Zellen. Das folgende Beispiel zeigt, wie die abhängigen Elemente für die A1-Zelle mithilfe der Vorlagendatei Book1.xlsx nachverfolgt werden.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependents.java" >}}
### **Verfolgen von Präzedenzfällen und abhängigen Zellen gemäß der Berechnungskette**
Die obigen APIs zur Verfolgung von Präzedenzfällen und abhängigen Personen entsprechen dem Formelausdruck selbst. Sie bieten dem Benutzer einfach eine bequeme Möglichkeit, Abhängigkeiten für einige Formeln zu verfolgen. Wenn die Arbeitsmappe eine große Anzahl von Formeln enthält und der Benutzer Präzedenzfälle und abhängige Elemente für jede Zelle nachverfolgen muss, führt dies zu einer schlechten Leistung. Für eine solche Situation sollte der Benutzer die Verwendung in Betracht ziehen[GetPrecedentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedentsInCalculation() /) und[GetDependentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependentsInCalculation(boolean) /) Methoden. Diese beiden Methoden verfolgen Abhängigkeiten gemäß der Berechnungskette. Um sie zu verwenden, müssen Sie also zunächst die Berechnungskette aktivieren[Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/java/com.aspose.cells/FormulaSettings#EnableCalculationChain) . Dann sollten Sie die vollständige Berechnung für die Arbeitsmappe durchführen[Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)). Danach können Sie Präzedenzfälle oder abhängige Zellen für alle benötigten Zellen verfolgen.

Bei einigen Formeln können sich die resultierenden Präzedenzfälle für GetPrecedents und GetPrecedentsInCalculation unterscheiden, und die resultierenden abhängigen Elemente können für GetDependents und GetDependentsInCalculation unterschiedlich sein. Wenn die Formel von Zelle A1 beispielsweise „=IF(TRUE,B2,C3)“ lautet, stellt GetPrecedents B2 und C3 als Präzedenzfall von A1 bereit. Dementsprechend haben B2 und C3 bei der Überprüfung durch GetDependents beide das abhängige A1. Für die Berechnung dieser Formel ist jedoch offensichtlich, dass nur B2 das berechnete Ergebnis beeinflussen kann. Daher stellt GetPrecedentsInCalculation C3 nicht für A1 bereit, und GetDependentsInCalculation stellt A1 nicht für C3 bereit. Manchmal müssen Benutzer nur die Abhängigkeiten verfolgen, die sich tatsächlich auf das berechnete Ergebnis von Formeln auf der Grundlage aktueller Daten der Arbeitsmappe auswirken, dann müssen sie auch GetDependentsInCalculation/GetPrecedentsInCalculation anstelle von GetDependents/GetPrecedents verwenden.

Das folgende Beispiel zeigt, wie die Präzedenzfälle und abhängigen Elemente gemäß der Berechnungskette für Zellen verfolgt werden:


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependenciesInCalculation.java" >}}
