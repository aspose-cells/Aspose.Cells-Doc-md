---
title: Präzedenzfälle und Abhängige
type: docs
weight: 100
url: /de/cpp/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Komplexe Finanzarbeitsblätter, insbesondere solche, die gemeinsam entwickelt wurden, können die peinlichsten Fehler verbergen. Es kann schwierig sein, Formeln auf ihre Richtigkeit zu überprüfen und die Fehlerquelle zu finden, wenn die Formel Vorgängerzellen und abhängige Zellen verwendet.

{{% /alert %}} 
##  **Einführung**
- **Präzedenzfälle** sind Zellen, auf die eine Formel in einer anderen Zelle verweist. Wenn beispielsweise Zelle D10 die Formel =B5 enthält, ist Zelle B5 ein Präzedenzfall für Zelle D10.
- **Abhängige Zellen** enthalten Formeln, die auf andere Zellen verweisen. Wenn Zelle D10 beispielsweise die Formel =B5 enthält, ist Zelle D10 von Zelle B5 abhängig.

Damit die Tabelle leichter lesbar ist, möchten Sie möglicherweise deutlich zeigen, welche Zellen in einer Tabelle in einer Formel verwendet werden. Ebenso möchten Sie möglicherweise die abhängigen Zellen anderer Zellen extrahieren.

Mit Aspose.Cells können Sie Zellen verfolgen und herausfinden, welche verknüpft sind.
##  **Verfolgung von Präzedenzfällen und Abhängigkeiten Cells: Microsoft Excel**
Formeln können sich aufgrund von Änderungen eines Kunden ändern. Wenn beispielsweise Zelle C1 von C3 und C4 abhängig ist, die eine Formel enthalten, und C1 geändert wird (so dass die Formel überschrieben wird), müssen C3 und C4 oder andere Zellen geändert werden, um die Tabelle basierend auf Geschäftsregeln auszugleichen.

Angenommen, C1 enthält die Formel „=(B1*22)/(M2*N32)“. Ich möchte die Zellen finden, von denen C1 abhängt, also die Vorgängerzellen B1, M2 und N32.

Möglicherweise müssen Sie die Abhängigkeit einer bestimmten Zelle von anderen Zellen nachverfolgen. Wenn Geschäftsregeln in Formeln eingebettet sind, möchten wir die Abhängigkeit herausfinden und darauf basierend einige Regeln ausführen. Wenn der Wert einer bestimmten Zelle geändert wird, welche Zellen im Arbeitsblatt sind dann von dieser Änderung betroffen?

Microsoft Mit Excel können Benutzer Präzedenzfälle und Verwandte nachverfolgen.

1.  Auf der**Symbolleiste anzeigen**, wählen Sie **Formelprüfung**
1. Präzedenzfälle verfolgen:
 1. Wählen Sie die Zelle aus, die die Formel enthält, für die Sie Vorgängerzellen suchen möchten.
 1. Um einen Markierungspfeil zu jeder Zelle anzuzeigen, der Daten direkt an die aktive Zelle liefert, klicken Sie auf**Präzedenzfälle verfolgen** auf der**Formelprüfung** Symbolleiste.
1. Verfolgungsformeln, die auf eine bestimmte Zelle verweisen (abhängige Zellen)
 1. Wählen Sie die Zelle aus, für die Sie die abhängigen Zellen identifizieren möchten.
1. Um einen Markierungspfeil zu jeder von der aktiven Zelle abhängigen Zelle anzuzeigen, klicken Sie in der Symbolleiste „Formelprüfung“ auf „Abhängige Elemente verfolgen“.
##  **Suche nach Präzedenzfall und abhängigem Cells: Aspose.Cells**
###  **Präzedenzfälle aufspüren**
Aspose.Cells erleichtert den Zugriff auf Vorgängerzellen. Es kann nicht nur Zellen abrufen, die Daten für Präzedenzfälle einfacher Formeln bereitstellen, sondern auch Zellen finden, die Daten für Präzedenzfälle komplexer Formeln mit benannten Bereichen bereitstellen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingPrecedents-new.cpp" >}}
###  **Aufspüren von Angehörigen**
Mit Aspose.Cells können Sie abhängige Zellen in Tabellenkalkulationen abrufen. Aspose.Cells kann nicht nur Zellen abrufen, die Daten zu einer einfachen Formel bereitstellen, sondern auch Zellen finden, die Daten zu komplexen Formelabhängigen mit benannten Bereichen bereitstellen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingDependents-new.cpp" >}}
