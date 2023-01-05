---
title: Erstellen Sie dynamische Diagramme
type: docs
weight: 200
url: /de/java/create-dynamic-charts/
---
{{% alert color="primary" %}}

Dynamische (oder interaktive) Diagramme können sich ändern, wenn Sie den Datenumfang ändern. Mit anderen Worten, die dynamischen Diagramme können Änderungen automatisch widerspiegeln, wenn die Datenquelle geändert wird. Um die Änderung der Datenquelle auszulösen, kann man die Filteroption von Excel-Tabellen verwenden oder ein Steuerelement wie ComboBox oder Dropdown-Liste verwenden.

Dieser Artikel demonstriert die Verwendung von Aspose.Cells for Java-APIs zum Erstellen dynamischer Diagramme mit beiden oben genannten Ansätzen.

{{% /alert %}}

## **Verwenden von Excel-Tabellen**

{{% alert color="primary" %}}

 Excel-Tabellen werden in der Aspose.Cells-Perspektive als ListObjects bezeichnet, daher verwenden wir zur Verdeutlichung den Begriff "ListObject" anstelle von "Table". Bitte lesen Sie im Detail, wie es geht[Listenobjekte erstellen](/cells/de/java/creating-a-list-object/) mit Aspose.Cells for .NET API.

{{% /alert %}}

ListObjects bietet die eingebaute Funktionalität zum Sortieren und Filtern der Daten bei Benutzerinteraktion. Sowohl Sortier- als auch Filteroptionen werden über die Dropdown-Listen bereitgestellt, die automatisch zur Kopfzeile des Listenobjekts hinzugefügt werden. Aufgrund dieser Funktionen (Sortieren und Filtern) scheint das ListObject der perfekte Kandidat zu sein, um als Datenquelle für ein dynamisches Diagramm zu dienen, da beim Ändern des Sortierens oder Filterns die Darstellung der Daten im Diagramm geändert wird, um die aktuelle wiederzugeben Zustand des Listenobjekts.

Um die Demonstration einfach verständlich zu halten, erstellen wir die Arbeitsmappe von Grund auf neu und gehen Schritt für Schritt vor, wie unten beschrieben.

1. Erstellen Sie eine leere Arbeitsmappe.
1. Greifen Sie auf Cells des ersten Arbeitsblatts in der Arbeitsmappe zu.
1. Fügen Sie einige Daten in die Zellen ein.
1. ListObject basierend auf den eingefügten Daten erstellen.
1. Erstellen Sie ein Diagramm basierend auf dem Datenbereich von ListObject.
1. Ergebnis auf Diskette speichern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **Dynamische Formeln verwenden**

Falls Sie die ListObjects nicht als Datenquelle für das dynamische Diagramm verwenden möchten, besteht die andere Möglichkeit darin, Excel-Funktionen (oder Formeln) zu verwenden, um einen dynamischen Datenbereich zu erstellen, und ein Steuerelement (z. B. ComboBox), um die Änderung auszulösen bei Daten. In diesem Szenario verwenden wir die VLOOKUP-Funktion, um die entsprechenden Werte basierend auf der Auswahl von ComboBox abzurufen. Wenn die Auswahl geändert wird, aktualisiert die VLOOKUP-Funktion den Zellenwert. Wenn ein Zellbereich die VLOOKUP-Funktion verwendet, kann der gesamte Bereich bei Benutzerinteraktion aktualisiert werden und kann daher als Quelle für das dynamische Diagramm verwendet werden.

Um die Demonstration einfach verständlich zu halten, erstellen wir die Arbeitsmappe von Grund auf neu und gehen Schritt für Schritt vor, wie unten beschrieben.

1. Erstellen Sie eine leere Arbeitsmappe.
1. Greifen Sie auf Cells des ersten Arbeitsblatts in der Arbeitsmappe zu.
1. Fügen Sie einige Daten in die Zellen ein, indem Sie einen benannten Bereich erstellen. Diese Daten dienen als Reihen für das dynamische Diagramm.
1. Erstellen Sie ComboBox basierend auf dem im vorherigen Schritt erstellten benannten Bereich.
1. Fügen Sie weitere Daten in die Zellen ein, die als Quelle für die SVERWEIS-Funktion dienen.
1. Fügen Sie die VLOOKUP-Funktion (mit entsprechenden Parametern) in einen Bereich von Zellen ein. Dieser Bereich dient als Quelle für das dynamische Diagramm.
1. Erstellen Sie ein Diagramm basierend auf dem im vorherigen Schritt erstellten Bereich.
1. Ergebnis auf Diskette speichern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
