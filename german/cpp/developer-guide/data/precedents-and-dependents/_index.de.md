---
title: Vorgänger und Abhängige
type: docs
weight: 100
url: /de/cpp/precedents-and-dependents/
---

{{% alert color="primary" %}} 

Komplexe Finanzarbeitsblätter, insbesondere solche, die in Zusammenarbeit entwickelt wurden, können die peinlichsten Fehler verbergen. Formeln auf ihre Genauigkeit zu überprüfen und die Fehlerquelle zu finden, kann schwierig sein, wenn die Formel Vorgänger- und Abhängigenzellen verwendet.

{{% /alert %}} 
## **Einführung**
- **Vorgängerzellen** sind Zellen, auf die in einer Formel in einer anderen Zelle verwiesen wird. Wenn z. B. Zelle D10 die Formel =B5 enthält, ist Zelle B5 ein Vorgänger von Zelle D10.
- **Abhängige Zellen** enthalten Formeln, die auf andere Zellen verweisen. Wenn beispielsweise die Zelle D10 die Formel =B5 enthält, ist die Zelle D10 von der Zelle B5 abhängig.

Um die Tabelle übersichtlicher zu gestalten, möchten Sie möglicherweise klar zeigen, welche Zellen in einer Tabelle in einer Formel verwendet werden. Ebenso möchten Sie die abhängigen Zellen anderer Zellen extrahieren.

Aspose.Cells ermöglicht es Ihnen, die Zellen zu verfolgen und herauszufinden, welche verknüpft sind.
## **Vorgänger- und Abhängige Zellen verfolgen: Microsoft Excel**
Formeln können sich ändern, basierend auf Änderungen, die von einem Kunden vorgenommen wurden. Wenn beispielsweise die Zelle C1 von C3 und C4 abhängt, die eine Formel enthalten, und C1 geändert wird (d. h. die Formel überschrieben wird), müssen C3 und C4 oder andere Zellen entsprechend den Geschäftsregeln angepasst werden, um die Tabelle auszugleichen.

Ebenso angenommen, C1 enthält die Formel "=(B1*22)/(M2*N32)". Ich möchte die Zellen finden, von denen C1 abhängt, d. h. die vorhergehenden Zellen B1, M2 und N32.

Sie müssen möglicherweise die Abhängigkeit einer bestimmten Zelle zu anderen Zellen verfolgen. Wenn Geschäftsregeln in Formeln eingebettet sind, möchten wir die Abhängigkeit herausfinden und einige Regeln entsprechend ausführen. Ebenso, wenn der Wert einer bestimmten Zelle geändert wird, welche Zellen im Arbeitsblatt sind von dieser Änderung betroffen?

Microsoft Excel ermöglicht es Benutzern, Vorgänger und Abhängige zu verfolgen.

1. Wählen Sie auf der **Ansichtsleiste** **Formelüberwachung** aus
1. Vorgänger verfolgen:
   1. Wählen Sie die Zelle aus, die die Formel enthält, für die Sie Vorgängerzellen finden möchten.
   1. Um an jede Zelle einen Tracer-Pfeil anzuzeigen, die direkt Daten an die aktive Zelle bereitstellt, klicken Sie auf **Vorgänger verfolgen** auf der **Formelüberwachungs**-Symbolleiste.
1. Formeln verfolgen, die auf eine bestimmte Zelle verweisen (Abhängige)
   1. Wählen Sie die Zelle aus, für die Sie die abhängigen Zellen identifizieren möchten.
   1. Um an jede Zelle, die von der aktiven Zelle abhängig ist, einen Tracer-Pfeil anzuzeigen, klicken Sie auf **Abhängige verfolgen** auf der **Formelüberwachungs**-Symbolleiste.
## **Vorgänger- und Abhängige Zellen verfolgen: Aspose.Cells**
### **Vorgänger verfolgen**
Aspose.Cells erleichtert das Abrufen von Vorgängerzellen. Es kann nicht nur Zellen abrufen, die Daten zu einfachen Formelvorgängern bereitstellen, sondern auch Zellen finden, die Daten zu komplexen Formelvorgängern mit benannten Bereichen bereitstellen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingPrecedents-new.cpp" >}}
### **Abhängige verfolgen**
Aspose.Cells ermöglicht es Ihnen, abhängige Zellen in Tabellenkalkulationen zu erhalten. Aspose.Cells kann nicht nur Zellen abrufen, die Daten zu einer einfachen Formelabhängigkeit bereitstellen, sondern auch Zellen finden, die Daten zu komplexen Formelabhängigen mit benannten Bereichen bereitstellen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingDependents-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
