---
title: Erstellen Sie dynamische Diagramme
description: Erfahren Sie unter Aspose.Cells for .NET, wie Sie dynamische Diagramme erstellen. Unser Leitfaden zeigt Ihnen, wie Sie Diagrammdaten, -reihen und -formatierungen basierend auf Ihren Anforderungen dynamisch aktualisieren, sodass Sie sich ändernde Daten visuell in Ihren Arbeitsblättern darstellen können.
keywords: Aspose.Cells for .NET, charting, dynamic charts, data, series, formatting, worksheets, updating.
type: docs
weight: 240
url: /de/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

Dynamische (oder interaktive) Diagramme können sich ändern, wenn Sie den Datenumfang ändern. Mit anderen Worten: Die dynamischen Diagramme können Änderungen automatisch widerspiegeln, wenn die Datenquelle geändert wird. Um die Änderung in der Datenquelle auszulösen, kann man die Filteroption von Excel-Tabellen nutzen oder ein Steuerelement wie ComboBox oder Dropdown-Liste verwenden.

In diesem Artikel wird die Verwendung der APIs Aspose.Cells for .NET zum Erstellen dynamischer Diagramme mit beiden oben genannten Ansätzen veranschaulicht.

{{% /alert %}}

##  **Verwendung von Excel-Tabellen**

{{% alert color="primary" %}}

 Excel-Tabellen werden in der Perspektive von Aspose.Cells als ListObjects bezeichnet. Aus Gründen der Klarheit verwenden wir daher den Begriff „ListObject“ anstelle von „Table“. Bitte lesen Sie im Detail, wie das geht[Erstellen Sie ListObjects](/cells/de/net/create-and-format-table/)mit Aspose.Cells for .NET API.

{{% /alert %}}

 ListObjects bietet die integrierte Funktionalität zum Sortieren und Filtern der Daten bei Benutzerinteraktion. Sowohl Sortier- als auch Filteroptionen werden über die Dropdown-Listen bereitgestellt, die automatisch zur Kopfzeile des hinzugefügt werden[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) . Aufgrund dieser Funktionen (Sortierung & Filterung) ist die[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) scheint der perfekte Kandidat zu sein, um als Datenquelle für ein dynamisches Diagramm zu dienen, denn wenn die Sortierung oder Filterung geändert wird, wird die Darstellung der Daten im Diagramm geändert, um den aktuellen Status des Diagramms widerzuspiegeln[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

 Um die Demonstration einfach verständlich zu halten, erstellen wir die[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Beginnen Sie von Grund auf und gehen Sie Schritt für Schritt vor, wie unten beschrieben.

1.  Erstellen Sie ein Leerzeichen[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Greife auf ... zu[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) des ersten[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) im[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Fügen Sie einige Daten in die Zellen ein.
1.  Erstellen[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)basierend auf den eingegebenen Daten.
1.  Erstellen[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) basierend auf dem Datenbereich von[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Speichern Sie das Ergebnis auf der Disc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

##  **Verwendung dynamischer Formeln**

Falls Sie das nicht verwenden möchten[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)Als Datenquelle für das dynamische Diagramm besteht die andere Möglichkeit darin, Excel-Funktionen (oder Formeln) zu verwenden, um einen dynamischen Datenbereich zu erstellen, und ein Steuerelement (z. B. ComboBox), um die Datenänderung auszulösen. In diesem Szenario verwenden wir die VLOOKUP-Funktion, um die entsprechenden Werte basierend auf der Auswahl der ComboBox abzurufen. Wenn die Auswahl geändert wird, aktualisiert die SVERWEIS-Funktion den Zellenwert. Wenn ein Zellbereich die VLOOKUP-Funktion verwendet, kann der gesamte Bereich bei Benutzerinteraktion aktualisiert werden und daher als Quelle für das dynamische Diagramm verwendet werden.

Um die Demonstration einfach zu verstehen, erstellen wir das Arbeitsbuch von Grund auf und gehen Schritt für Schritt vor, wie unten beschrieben.

1.  Erstellen Sie ein Leerzeichen[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Greife auf ... zu[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) des ersten[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) im[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Fügen Sie einige Daten in die Zellen ein, indem Sie einen benannten Bereich erstellen. Diese Daten dienen als Reihe zum dynamischen Diagramm.
1.  Erstellen[**Kombinationsfeld**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)basierend auf dem im vorherigen Schritt erstellten benannten Bereich.
1. Fügen Sie weitere Daten in die Zellen ein, die als Quelle für die SVERWEIS-Funktion dienen.
1. Fügen Sie die SVERWEIS-Funktion (mit entsprechenden Parametern) in einen Zellbereich ein. Dieser Bereich dient als Quelle für das dynamische Diagramm.
1.  Erstellen[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)basierend auf dem im vorherigen Schritt erstellten Bereich.
1. Speichern Sie das Ergebnis auf der Disc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
