---
title: Dynamische Diagramme erstellen
description: Erfahren Sie, wie Sie in Aspose.Cells für Python via .NET dynamische Diagramme erstellen. Unser Leitfaden zeigt, wie Sie Diagrammdaten, Serien und Formatierungen entsprechend Ihren Anforderungen dynamisch aktualisieren, um sich ändernde Daten visuell in Ihren Arbeitsblättern darzustellen.
keywords: Aspose.Cells für Python via .NET, Diagrammerstellung, dynamische Diagramme, Daten, Serien, Formatierungen, Arbeitsblätter, Aktualisierung.
type: docs
weight: 240
url: /de/python-net/create-dynamic-charts/
---

{{% alert color="primary" %}}

Dynamische (oder interaktive) Diagramme haben die Möglichkeit, sich zu ändern, wenn sich der Datenbereich ändert. Mit anderen Worten können sich die dynamischen Diagramme automatisch ändern, wenn sich die Datenquelle ändert. Um die Änderung in der Datenquelle auszulösen, kann die Filteroption von Excel-Tabellen verwendet werden oder ein Steuerelement wie Dropdown-Liste oder Kombinationsfeld.

Dieser Artikel demonstriert die Verwendung der Aspose.Cells für Python via .NET APIs, um dynamische Diagramme mit beiden oben genannten Methoden zu erstellen.

{{% /alert %}}

## **Verwendung von Excel-Tabellen**

{{% alert color="primary" %}}

Excel-Tabellen werden im Aspose.Cells-Kontext als ListObjects bezeichnet, daher verwenden wir den Begriff "ListObject" statt "Tabelle" zur Klarheit. Bitte lesen Sie im Detail, wie Sie [ListObjects erstellen](/cells/de/python-net/create-and-format-table/) mit der API von Aspose.Cells für Python via .NET.

{{% /alert %}}

ListObjects bieten die integrierte Funktionalität, um Daten bei Benutzerinteraktion zu sortieren und zu filtern. Sowohl Sortier- als auch Filteroptionen werden über Dropdown-Listen bereitgestellt, die automatisch in der Kopfzeile des hinzufügten Bereichs eingefügt werden. Aufgrund dieser Funktionen (Sortieren & Filtern) scheint [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) der perfekte Kandidat zu sein, um als Datenquelle für ein dynamisches Diagramm zu dienen, da bei Änderungen in Sortierung oder Filterung die Darstellung der Daten im Diagramm aktualisiert wird.

Um die Demonstration einfach zu verstehen zu halten, werden wir das [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) von Grund auf erstellen und Schritt für Schritt wie unten skizziert fortfahren.

1. Erstellen Sie ein leeres [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Greifen Sie auf den [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) des ersten [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) im [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) zu.
1. Fügen Sie einige Daten in die Zellen ein.
1. Erstellen eines [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) basierend auf den eingefügten Daten.
1. Erstellen eines [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) basierend auf dem Datenbereich von [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject).
1. Speichern Sie das Ergebnis auf der Festplatte.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicCharts.py" >}}

## **Verwendung dynamischer Formeln**

Wenn Sie das [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) nicht als Datenquelle für das dynamische Diagramm verwenden möchten, ist die andere Option, Excel-Funktionen (oder Formeln) zu verwenden, um einen dynamischen Datenbereich zu erstellen und ein Steuerelement (wie z.B. ComboBox) zur Auslösung der Datenä̲nderung zu verwenden. In diesem Szenario verwenden wir die VLOOKUP-Funktion, um die geeigneten Werte basierend auf der Auswahl des ComboBox abzurufen. Wenn die Auswahl geändert wird, wird die VLOOKUP-Funktion den Zellenwert aktualisieren. Wenn ein Zellenbereich die VLOOKUP-Funktion verwendet, kann der gesamte Bereich durch Benutzerinteraktion aktualisiert werden, daher kann er als Datenquelle für das dynamische Diagramm verwendet werden.

Um die Demonstration einfach zu verstehen zu halten, werden wir die Arbeitsmappe von Grund auf erstellen und Schritt für Schritt wie unten skizziert fortfahren.

1. Erstellen Sie ein leeres [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Greifen Sie auf den [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) des ersten [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) im [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) zu.
1. Fügen Sie einige Daten in die Zellen ein, indem Sie einen benannten Bereich erstellen. Diese Daten dienen als Serie für das dynamische Diagramm.
1. Erstellen Sie [**ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) basierend auf dem im vorherigen Schritt erstellten benannten Bereich.
1. Fügen Sie einige weitere Daten in die Zellen ein, die als Quelle für die VLOOKUP-Funktion dienen sollen.
1. Fügen Sie die VLOOKUP-Funktion (mit geeigneten Parametern) in einen Bereich von Zellen ein. Dieser Bereich dient als Quelle für das dynamische Diagramm.
1. Erstellen Sie [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) basierend auf dem im vorherigen Schritt erstellten Bereich.
1. Speichern Sie das Ergebnis auf der Festplatte.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicChartsUsingDynamicFormula.py" >}}
{{< app/cells/assistant language="python-net" >}}
