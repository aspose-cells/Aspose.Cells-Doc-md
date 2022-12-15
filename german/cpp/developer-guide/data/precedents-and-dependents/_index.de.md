---
title: Präzedenzfälle und Abhängigkeiten
type: docs
weight: 100
url: /de/cpp/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Komplexe Finanzarbeitsblätter, insbesondere solche, die gemeinsam entwickelt wurden, können die peinlichsten Fehler verbergen. Das Überprüfen von Formeln auf Genauigkeit und das Auffinden der Fehlerquelle kann schwierig sein, wenn die Formel Vorgängerzellen und abhängige Zellen verwendet.

{{% /alert %}} 
## **Einführung**
- **Vorhergehende Zellen** sind Zellen, auf die durch eine Formel in einer anderen Zelle verwiesen wird. Wenn beispielsweise Zelle D10 die Formel =B5 enthält, ist Zelle B5 ein Präzedenzfall für Zelle D10.
- **Abhängige Zellen** Formeln enthalten, die auf andere Zellen verweisen. Wenn beispielsweise Zelle D10 die Formel =B5 enthält, ist Zelle D10 von Zelle B5 abhängig.

Um die Tabellenkalkulation leicht lesbar zu machen, möchten Sie möglicherweise deutlich zeigen, welche Zellen in einer Tabellenkalkulation in einer Formel verwendet werden. Ebenso möchten Sie möglicherweise die abhängigen Zellen anderer Zellen extrahieren.

Aspose.Cells ermöglicht es Ihnen, Zellen zu verfolgen und herauszufinden, welche verknüpft sind.
## **Ablaufverfolgung Präzedenzfall und abhängiger Cells: Microsoft Excel**
Formeln können sich aufgrund von Änderungen ändern, die von einem Kunden vorgenommen wurden. Wenn beispielsweise Zelle C1 von C3 und C4 abhängig ist, die eine Formel enthalten, und C1 geändert wird (so dass die Formel überschrieben wird), müssen C3 und C4 oder andere Zellen geändert werden, um die Tabelle basierend auf Geschäftsregeln auszugleichen.

Angenommen, C1 enthält die Formel "=(B1*22)/(M2*N32)". Ich möchte die Zellen finden, von denen C1 abhängt, also die vorangegangenen Zellen B1, M2 und N32.

Möglicherweise müssen Sie die Abhängigkeit einer bestimmten Zelle von anderen Zellen nachverfolgen. Wenn Geschäftsregeln in Formeln eingebettet sind, möchten wir die Abhängigkeit herausfinden und einige Regeln darauf basierend ausführen. Wenn der Wert einer bestimmten Zelle geändert wird, welche Zellen im Arbeitsblatt sind von dieser Änderung betroffen?

Microsoft Excel ermöglicht es Benutzern, Präzedenzfälle und Abhängige zu verfolgen.

1.  Auf der**Symbolleiste anzeigen** , auswählen**Formel Auditing**
1. Präzedenzfälle verfolgen:
1. Wählen Sie die Zelle aus, die die Formel enthält, für die Sie vorangegangene Zellen suchen möchten.
 1. Um einen Verfolgungspfeil zu jeder Zelle anzuzeigen, die direkt Daten für die aktive Zelle bereitstellt, klicken Sie auf**Präzedenzfälle verfolgen** auf der**Formel Auditing** Symbolleiste.
1. Verfolgen Sie Formeln, die auf eine bestimmte Zelle verweisen (abhängige Zellen)
 1. Wählen Sie die Zelle aus, für die Sie die abhängigen Zellen identifizieren möchten.
 1. Um einen Verfolgungspfeil zu jeder Zelle anzuzeigen, die von der aktiven Zelle abhängig ist, klicken Sie in der Symbolleiste „Formelprüfung“ auf Abhängigkeiten verfolgen.
## **Verfolgung von Präzedenzfällen und abhängigen Cells: Aspose.Cells**
### **Präzedenzfälle verfolgen**
Aspose.Cells macht es einfach, Präzedenzzellen zu erhalten. Es kann nicht nur Zellen abrufen, die Daten für einfache Formelpräzedenzfälle bereitstellen, sondern auch Zellen finden, die Daten für komplexe Formelpräzedenzfälle mit benannten Bereichen bereitstellen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingPrecedents.cpp" >}}
### **Abhängigkeiten verfolgen**
Mit Aspose.Cells können Sie abhängige Zellen in Tabellenkalkulationen abrufen. Aspose.Cells kann nicht nur Zellen abrufen, die Daten zu einer einfachen Formel bereitstellen, sondern auch Zellen finden, die Daten zu komplexen Formelabhängigen mit benannten Bereichen bereitstellen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingDependents.cpp" >}}
