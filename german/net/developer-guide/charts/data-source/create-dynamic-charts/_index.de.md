---
title: Dynamische Diagramme erstellen
description: Erfahren Sie, wie Sie dynamische Diagramme in Aspose.Cells for .NET erstellen können. Unser Leitfaden zeigt Ihnen, wie Sie Diagrammdaten, Serien und Formatierungen basierend auf Ihren Anforderungen dynamisch aktualisieren können, um sich ändernde Daten visuell in Ihren Arbeitsblättern darzustellen.
keywords: Aspose.Cells for .NET, Diagrammerstellung, dynamische Diagramme, Daten, Serien, Formatierung, Arbeitsblätter, Aktualisierung.
type: docs
weight: 240
url: /de/net/create-dynamic-charts/
---

{{% alert color="primary" %}}

Dynamische (oder interaktive) Diagramme haben die Möglichkeit, sich zu ändern, wenn sich der Datenbereich ändert. Mit anderen Worten können sich die dynamischen Diagramme automatisch ändern, wenn sich die Datenquelle ändert. Um die Änderung in der Datenquelle auszulösen, kann die Filteroption von Excel-Tabellen verwendet werden oder ein Steuerelement wie Dropdown-Liste oder Kombinationsfeld.

Dieser Artikel zeigt die Verwendung von Aspose.Cells for .NET-APIs zur Erstellung dynamischer Diagramme unter Verwendung beider oben genannter Ansätze.

{{% /alert %}}

## **Verwendung von Excel-Tabellen**

{{% alert color="primary" %}}

Excel-Tabellen werden in der Perspektive von Aspose.Cells als ListObjects bezeichnet. Daher verwenden wir den Begriff "ListObject" anstelle von "Tabelle" für mehr Klarheit. Bitte lesen Sie ausführlich, wie Sie mit der Aspose.Cells for .NET-API [ListObjects erstellen](/cells/de/net/create-and-format-table/).

{{% /alert %}}

ListObjects bieten die eingebaute Funktionalität zum Sortieren und Filtern der Daten durch Benutzerinteraktion. Sowohl Sortierungs- als auch Filteroptionen werden über die Dropdown-Listen bereitgestellt, die automatisch zur Kopfzeile des [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) hinzugefügt werden. Aufgrund dieser Funktionen (Sortierung und Filterung) scheint das [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) der perfekte Kandidat zu sein, um als Datenquelle für ein dynamisches Diagramm zu dienen, da sich bei Änderung der Sortierung oder Filterung die Darstellung der Daten im Diagramm ändert, um den aktuellen Zustand des [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) widerzuspiegeln.

Um die Demonstration einfach zu verstehen zu halten, werden wir das [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) von Grund auf erstellen und Schritt für Schritt wie unten skizziert fortfahren.

1. Erstellen Sie ein leeres [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Greifen Sie auf den [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) des ersten [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) im [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) zu.
1. Fügen Sie einige Daten in die Zellen ein.
1. Erstellen eines [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) basierend auf den eingefügten Daten.
1. Erstellen eines [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) basierend auf dem Datenbereich von [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Speichern Sie das Ergebnis auf der Festplatte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **Verwendung dynamischer Formeln**

Wenn Sie das [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) nicht als Datenquelle für das dynamische Diagramm verwenden möchten, ist die andere Option, Excel-Funktionen (oder Formeln) zu verwenden, um einen dynamischen Datenbereich zu erstellen und ein Steuerelement (wie z.B. ComboBox) zur Auslösung der Datenä̲nderung zu verwenden. In diesem Szenario verwenden wir die VLOOKUP-Funktion, um die geeigneten Werte basierend auf der Auswahl des ComboBox abzurufen. Wenn die Auswahl geändert wird, wird die VLOOKUP-Funktion den Zellenwert aktualisieren. Wenn ein Zellenbereich die VLOOKUP-Funktion verwendet, kann der gesamte Bereich durch Benutzerinteraktion aktualisiert werden, daher kann er als Datenquelle für das dynamische Diagramm verwendet werden.

Um die Demonstration einfach zu verstehen zu halten, werden wir die Arbeitsmappe von Grund auf erstellen und Schritt für Schritt wie unten skizziert fortfahren.

1. Erstellen Sie ein leeres [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Greifen Sie auf den [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) des ersten [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) im [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) zu.
1. Fügen Sie einige Daten in die Zellen ein, indem Sie einen benannten Bereich erstellen. Diese Daten dienen als Serie für das dynamische Diagramm.
1. Erstellen Sie [**ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) basierend auf dem im vorherigen Schritt erstellten benannten Bereich.
1. Fügen Sie einige weitere Daten in die Zellen ein, die als Quelle für die VLOOKUP-Funktion dienen sollen.
1. Fügen Sie die VLOOKUP-Funktion (mit geeigneten Parametern) in einen Bereich von Zellen ein. Dieser Bereich dient als Quelle für das dynamische Diagramm.
1. Erstellen Sie [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) basierend auf dem im vorherigen Schritt erstellten Bereich.
1. Speichern Sie das Ergebnis auf der Festplatte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
