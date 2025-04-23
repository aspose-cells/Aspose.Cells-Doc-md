---
title: Vorgänger und Abhängige
type: docs
weight: 230
url: /de/python-net/precedents-and-dependents/
---

{{% alert color="primary" %}} 

Komplexe Finanzarbeitsblätter, insbesondere solche, die in Zusammenarbeit entwickelt wurden, können die peinlichsten Fehler verbergen. Formeln auf ihre Genauigkeit zu überprüfen und die Fehlerquelle zu finden, kann schwierig sein, wenn die Formel Vorgänger- und Abhängigenzellen verwendet.

{{% /alert %}} 
## **Einführung**
- **Vorgängerzellen** sind Zellen, auf die in einer anderen Zelle eine Formel verweist. Wenn beispielsweise Zelle D10 die Formel =B5 enthält, dann ist die Zelle B5 ein Vorgänger von Zelle D10.
- **Abhängige Zellen** enthalten Formeln, die auf andere Zellen verweisen. Wenn beispielsweise die Zelle D10 die Formel =B5 enthält, ist die Zelle D10 von der Zelle B5 abhängig.

Um die Tabelle übersichtlicher zu gestalten, möchten Sie möglicherweise klar zeigen, welche Zellen in einer Tabelle in einer Formel verwendet werden. Ebenso möchten Sie die abhängigen Zellen anderer Zellen extrahieren.

Aspose.Cells für Python via .NET erlaubt es, Zellen nachzuverfolgen und herauszufinden, welche verlinkt sind.
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
## **Nachverfolgung von Voraussetzungs- und Abhängigen Zellen: Aspose.Cells für Python via .NET**
### **Vorgänger verfolgen**
Aspose.Cells für Python via .NET macht es einfach, Voraussetzungszellen zu erhalten. Es kann nicht nur Zellen abrufen, die Daten für einfache Formelveorlagen liefern, sondern auch Zellen finden, die Daten für komplexe Formelvoraussetzungen mit benannten Bereichen liefern.

Im folgenden Beispiel wird eine Vorlagen-Excel-Datei, Book1.xls, verwendet. Das Arbeitsblatt enthält Daten und Formeln.

Aspose.Cells für Python via .NET bietet die [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-Klasse mit der [**get_precedents**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_precedents/#)-Methode, um die Vorgängerzellen einer Zelle nachzuverfolgen. Diese gibt einen [**ReferredAreaCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/referredareacollection) zurück. Wie oben gezeigt, enthält in Book1.xls die Zelle B7 eine Formel "=SUM(A1:A3)". Die Zellen A1:A3 sind also die Vorgängerzellen von Zelle B7. Das folgende Beispiel zeigt die Funktion zum Nachverfolgen von Vorgängern anhand der Vorlage Book1.xls.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingPrecedents-1.py" >}}
### **Abhängige verfolgen**
Aspose.Cells für Python via .NET ermöglicht es, abhängige Zellen in Tabellenkalkulationen zu erhalten. Aspose.Cells für Python via .NET kann nicht nur Zellen abrufen, die Daten zu einer einfachen Formel liefern, sondern auch Zellen finden, die Daten für komplexe Formelabhängige mit benannten Bereichen liefern.

Aspose.Cells für Python via .NET stellt die [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-Klasse bereit mit der [**get_dependents**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_dependents/#bool)-Methode, um die abhängigen Zellen einer Zelle zu verfolgen. Zum Beispiel gibt es in Book1.xlsx die Formeln: "=A1+20" und "=A1+30" in den Zellen B2 und C2. Das folgende Beispiel zeigt, wie man die abhängigen Zellen für die A1-Zelle anhand der Vorlage Book1.xlsx verfolgt.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingDependents-1.py" >}}

### **Nachverfolgung von Vorgänger- und abhängigen Zellen gemäß der Berechnungskette**
Oben angegebene APIs zum Nachverfolgen von Vorgängern und Abhängigkeiten basieren auf dem Formel-Ausdruck selbst. Sie bieten eine bequeme Möglichkeit für den Benutzer, Interabhängigkeiten bei einigen Formeln nachzuverfolgen. Wenn im Arbeitsbuch eine große Anzahl von Formeln vorhanden ist und der Benutzer Vorgänger und Abhängige für jede Zelle nachverfolgen muss, liefern sie eine schlechte Leistung. Für solche Situationen sollten Benutzer die [**get_precedents_in_calculation**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_precedents_in_calculation/#)- und [**get_dependents_in_calculation**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_dependents_in_calculation/#bool)-Methoden in Betracht ziehen. Diese beiden Methoden verfolgen Abhängigkeiten basierend auf der Berechnungskette. Daher müssen Sie sie aktivieren, indem Sie zuerst die [**Workbook.settings.formula_settings.enable_calculation_chain**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/enable_calculation_chain/)-Methode für die Berechnungskette aktivieren. Dann sollten Sie das Arbeitsbuch vollständig berechnen mit [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#). Danach können Sie Vorgänger oder Abhängige für alle Zellen, die Sie benötigen, verfolgen.

Für einige Formeln können die resultierenden Vorgänger bei GetPrecedents und GetPrecedentsInCalculation unterschiedlich sein, und die resultierenden Abhängigen bei GetDependents und GetDependentsInCalculation können unterschiedlich sein. Wenn z.B. die Formel von Zelle A1 "=IF(TRUE,B2,C3)" ist, liefert GetPrecedents B2 und C3 als Vorgänger von A1. Demnach haben sowohl B2 als auch C3 die abhängige Zelle A1 bei der Überprüfung durch GetDependents. Für die Berechnung dieser Formel ist jedoch offensichtlich, dass nur B2 das berechnete Ergebnis beeinflussen kann. Daher gibt GetPrecedentsInCalculation A1 nicht für C3 zurück, und GetDependentsInCalculation gibt C3 nicht für A1 zurück. Manchmal hat der Benutzer möglicherweise nur die Anforderung, die interdependencies zu verfolgen, die tatsächlich das berechnete Ergebnis der Formeln basierend auf den aktuellen Daten der Arbeitsmappe beeinflussen, dann sollten sie auch GetDependentsInCalculation/GetPrecedentsInCalculation anstelle von GetDependents/GetPrecedents verwenden.

Das folgende Beispiel zeigt, wie Sie die Präzedenzfälle und Dependenzen gemäß der Berechnungskette für Zellen verfolgen können:


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingDependenciesInCalculation.py" >}}

