---
title: Erstellen Sie dynamische Diagramme
type: docs
weight: 240
url: /de/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

Dynamische (oder interaktive) Diagramme können sich ändern, wenn Sie den Datenumfang ändern. Mit anderen Worten, die dynamischen Diagramme können Änderungen automatisch widerspiegeln, wenn die Datenquelle geändert wird. Um die Änderung der Datenquelle auszulösen, kann man die Filteroption von Excel-Tabellen verwenden oder ein Steuerelement wie ComboBox oder Dropdown-Liste verwenden.

Dieser Artikel demonstriert die Verwendung von Aspose.Cells for .NET-APIs zum Erstellen dynamischer Diagramme mit beiden oben genannten Ansätzen.

{{% /alert %}}

## **Verwenden von Excel-Tabellen**

{{% alert color="primary" %}}

 Excel-Tabellen werden in der Aspose.Cells-Perspektive als ListObjects bezeichnet, daher verwenden wir zur Verdeutlichung den Begriff „ListObject“ anstelle von „Table“. Bitte lesen Sie im Detail, wie es geht[Listenobjekte erstellen](/cells/de/net/create-and-format-table/) mit Aspose.Cells for .NET API.

{{% /alert %}}

 ListObjects bietet die eingebaute Funktionalität zum Sortieren und Filtern der Daten bei Benutzerinteraktion. Sowohl Sortier- als auch Filteroptionen werden über die Dropdown-Listen bereitgestellt, die automatisch zur Kopfzeile des hinzugefügt werden[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) . Aufgrund dieser Funktionen (Sortieren & Filtern) ist die[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)scheint der perfekte Kandidat zu sein, um als Datenquelle für ein dynamisches Diagramm zu dienen, denn wenn die Sortierung oder Filterung geändert wird, wird die Darstellung der Daten im Diagramm geändert, um den aktuellen Status des Diagramms widerzuspiegeln[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

 Um die Demonstration einfach verständlich zu halten, erstellen wir die[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)von Grund auf neu und gehen Sie Schritt für Schritt vor, wie unten beschrieben.

1.  Erstellen Sie eine leere[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Greife auf ... zu[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) des ersten[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) in dem[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Fügen Sie einige Daten in die Zellen ein.
1.  Schaffen[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)basierend auf den eingegebenen Daten.
1.  Schaffen[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) basierend auf dem Datenbereich von[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Speichern Sie das Ergebnis auf der Disc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **Dynamische Formeln verwenden**

 Falls Sie die nicht verwenden möchten[**Listenobjekt**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)Als Datenquelle für das dynamische Diagramm besteht die andere Möglichkeit darin, Excel-Funktionen (oder Formeln) zu verwenden, um einen dynamischen Datenbereich zu erstellen, und ein Steuerelement (z. B. ComboBox), um die Änderung der Daten auszulösen. In diesem Szenario verwenden wir die VLOOKUP-Funktion, um die entsprechenden Werte basierend auf der Auswahl von ComboBox abzurufen. Wenn die Auswahl geändert wird, aktualisiert die VLOOKUP-Funktion den Zellenwert. Wenn ein Zellbereich die VLOOKUP-Funktion verwendet, kann der gesamte Bereich bei einer Benutzerinteraktion aktualisiert werden, sodass er als Quelle für das dynamische Diagramm verwendet werden kann.

Um die Demonstration einfach verständlich zu halten, erstellen wir die Arbeitsmappe von Grund auf neu und gehen Schritt für Schritt vor, wie unten beschrieben.

1.  Erstellen Sie eine leere[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Greife auf ... zu[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) des ersten[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) in dem[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Fügen Sie einige Daten in die Zellen ein, indem Sie einen benannten Bereich erstellen. Diese Daten dienen als Reihe für das dynamische Diagramm.
1.  Schaffen[**Kombinationsfeld**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)basierend auf dem im vorherigen Schritt erstellten benannten Bereich.
1. Fügen Sie weitere Daten in die Zellen ein, die als Quelle für die SVERWEIS-Funktion dienen.
1. Fügen Sie die VLOOKUP-Funktion (mit entsprechenden Parametern) in einen Bereich von Zellen ein. Dieser Bereich dient als Quelle für das dynamische Diagramm.
1.  Schaffen[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)basierend auf dem im vorherigen Schritt erstellten Bereich.
1. Speichern Sie das Ergebnis auf der Disc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
