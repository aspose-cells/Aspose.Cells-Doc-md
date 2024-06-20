---
title: Dynamische Diagramme erstellen
type: docs
weight: 200
url: /de/java/create-dynamic-charts/
---

{{% alert color="primary" %}}

Dynamische (oder interaktive) Diagramme haben die Möglichkeit, sich zu ändern, wenn der Datenbereich geändert wird. Mit anderen Worten können dynamische Diagramme automatisch Änderungen widerspiegeln, wenn die Datenquelle geändert wird. Um die Änderung in der Datenquelle auszulösen, kann man die Filteroptionen von Excel-Tabellen verwenden oder eine Steuerung wie ComboBox oder Dropdown-Liste verwenden.

Dieser Artikel demonstriert die Verwendung von Aspose.Cells for Java APIs, um dynamische Diagramme unter Verwendung beider oben genannter Ansätze zu erstellen.

{{% /alert %}}

## **Verwendung von Excel-Tabellen**

{{% alert color="primary" %}}

Excel-Tabellen werden aus der Perspektive von Aspose.Cells als "ListObjects" bezeichnet, daher werden wir den Begriff "ListObject" anstelle von "Tabelle" verwenden, um die Klarheit zu wahren. Bitte lesen Sie ausführlich, wie Sie [ListObjects erstellen](/cells/de/java/erstellen-eines-List-Objekts/) mit Aspose.Cells for .NET API.

{{% /alert %}}

ListObjects bieten die integrierte Funktionalität, um die Daten bei Benutzerinteraktion zu sortieren und zu filtern. Beide Sortier- und Filteroptionen werden über die Dropdown-Listen in der Kopfzeile des ListObjects bereitgestellt. Aufgrund dieser Funktionen (Sortieren und Filtern) scheint das ListObject der perfekte Kandidat als Datenquelle für ein dynamisches Diagramm zu sein, denn wenn das Sortieren oder Filtern geändert wird, wird die Darstellung der Daten im Diagramm geändert, um den aktuellen Zustand des ListObjects widerzuspiegeln.

Um die Demonstration einfach zu verstehen zu halten, werden wir die Arbeitsmappe von Grund auf erstellen und Schritt für Schritt wie unten skizziert fortfahren.

1. Erstellen Sie eine leere Arbeitsmappe.
1. Zugriff auf die Zellen des ersten Arbeitsblatts in der Arbeitsmappe.
1. Fügen Sie einige Daten in die Zellen ein.
1. Erstellen Sie ein ListObject basierend auf den eingefügten Daten.
1. Erstellen Sie ein Diagramm basierend auf dem Datenbereich des ListObjects.
1. Speichern Sie das Ergebnis auf der Festplatte.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **Verwendung dynamischer Formeln**

Wenn Sie die ListObjects nicht als Datenquelle für das dynamische Diagramm verwenden möchten, besteht die andere Option darin, Excel-Funktionen (oder Formeln) zu verwenden, um einen dynamischen Datenbereich zu erstellen, und eine Steuerung (wie ComboBox) zu verwenden, um die Änderung in den Daten auszulösen. In diesem Szenario werden wir die VLOOKUP-Funktion verwenden, um die entsprechenden Werte basierend auf der Auswahl der ComboBox abzurufen. Wenn die Auswahl geändert wird, wird die VLOOKUP-Funktion den Zellenwert aktualisieren. Wenn ein Zellenbereich die VLOOKUP-Funktion verwendet, kann der gesamte Bereich bei Benutzerinteraktion aktualisiert werden und somit als Quelle für das dynamische Diagramm verwendet werden.

Um die Demonstration einfach zu verstehen zu halten, werden wir die Arbeitsmappe von Grund auf erstellen und Schritt für Schritt wie unten skizziert fortfahren.

1. Erstellen Sie eine leere Arbeitsmappe.
1. Zugriff auf die Zellen des ersten Arbeitsblatts in der Arbeitsmappe.
1. Fügen Sie den Zellen einige Daten ein, indem Sie einen benannten Bereich erstellen. Diese Daten dienen als Serie für das dynamische Diagramm.
1. Erstellen Sie ComboBox basierend auf dem im vorherigen Schritt erstellten benannten Bereich.
1. Fügen Sie den Zellen einige weitere Daten ein, die als Quelle für die VLOOKUP-Funktion dienen.
1. Fügen Sie den Bereich der Zellen die VLOOKUP-Funktion (mit geeigneten Parametern) ein. Dieser Bereich dient als Quelle für das dynamische Diagramm.
1. Erstellen Sie ein Diagramm basierend auf dem im vorherigen Schritt erstellten Bereich.
1. Speichern Sie das Ergebnis auf der Festplatte.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
