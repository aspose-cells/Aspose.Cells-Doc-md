---
title: Ausrichtungseinstellungen
description: In der Aspose.Cells für Python via .NET Bibliothek können Sie Zellenausrichtungseinstellungen verwenden, um das Layout und die Anzeige von Text anzupassen. Durch Anpassen von Einstellungen wie horizontaler Ausrichtung, vertikaler Ausrichtung und Textumbruch haben Sie mehr Kontrolle darüber, wie Text in Zellen fließt. Dieses Dokument gibt Ihnen detaillierte Schritte und Beispielcode, um Ihnen zu helfen, Aspose.Cells für Python via .NET schnell für Zellenausrichtungseinstellungen zu verstehen.
keywords: Aspose.Cells für Python via .NET, Zellenausrichtung, horizontale Ausrichtung, vertikale Ausrichtung, Textumbruch
type: docs
weight: 20
url: /de/python-net/cells-alignment-settings/
---

## **Konfigurieren von Ausrichtungseinstellungen**

### **Ausrichtungseinstellungen in Microsoft Excel**

Jeder, der Microsoft Excel verwendet hat, um Zellen zu formatieren, wird mit den Ausrichtungseinstellungen in Microsoft Excel vertraut sein.

Wie Sie aus der obigen Abbildung sehen können, gibt es verschiedene Arten von Ausrichtungsoptionen:

- Textausrichtung (horizontal & vertikal)
- Einrückung
- Orientierung
- Textkontrolle
- Textrichtung

Alle diese Ausrichtungseinstellungen werden vollständig von Aspose.Cells für Python via .NET unterstützt und im Folgenden ausführlich erläutert.

### **Ausrichtungseinstellungen in Aspose.Cells für Python via .NET**

Aspose.Cells für Python via .NET bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) Sammlung. Jedes Element in der Sammlung [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) stellt ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) dar.

Aspose.Cells für Python via .NET stellt [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) und [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) Methoden für die [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) Klasse bereit, mit denen das Format einer Zelle abgerufen und festgelegt werden kann. Die [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) Klasse bietet nützliche Eigenschaften für die Konfiguration von Ausrichtungseinstellungen.

Wählen Sie einen beliebigen Textausrichtungstyp mithilfe der Aufzählung [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype) aus. Die vordefinierten Textausrichtungstypen in der Aufzählung [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype) lauten:

|**Textausrichtungstypen**|**Beschreibung**|
| :- | :- |
|ALLGEMEIN|Repräsentiert allgemeine Textausrichtung|
|UNTEN|Repräsentiert untere Textausrichtung|
|MITTE|Repräsentiert mittlere Textausrichtung|
|MITTE_QUER|Repräsentiert mittige Textausrichtung über die Zelle hinweg|
|VERTEILT|Repräsentiert verteilte Textausrichtung|
|FÜLLEN|Repräsentiert Fülltextausrichtung|
|JUSTIEREN|Repräsentiert blockierende Textausrichtung|
|LINKS|Repräsentiert linke Textausrichtung|
|RECHTS|Repräsentiert rechte Textausrichtung|
|OBEN|Repräsentiert obere Textausrichtung|
|NEUJUSTIERT_LOW|Richtet den Text mit einer angepassten Kashida-Länge für Arabisch aus|
|THAI_VERTEILT|Verteilt thailändischen Text speziell, da jedes Zeichen als Wort behandelt wird|

{{% alert color="primary" %}}

Sie können auch die Blocksatzverteilung mit der Eigenschaft [**Style.is_justify_distributed**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_justify_distributed) anwenden.

{{% /alert %}}

#### **Horizontale Ausrichtung**

Verwenden Sie die Eigenschaft [**horizontal_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/horizontal_alignment) des Objekts [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style), um den Text horizontal auszurichten.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.py" >}}

#### **Vertikale Ausrichtung**

Ähnlich wie bei der horizontalen Ausrichtung verwenden Sie die Eigenschaft [**vertical_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/vertical_alignment) des Objekts [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style), um den Text vertikal auszurichten.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.py" >}}

#### **Einrückung**

Es ist möglich, den Einrückungsgrad des Textes in einer Zelle mit der [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) -Objekteigenschaft [**indent_level**](https://reference.aspose.com/cells/python-net/aspose.cells/style/indent_level) festzulegen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Indentation-1.py" >}}

#### **Ausrichtung**

Legen Sie die Ausrichtung (Rotation) des Textes in einer Zelle mit der [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) -Objekteigenschaft [**rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) fest.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Orientation-1.py" >}}

#### **Textsteuerung**

Im Folgenden wird erläutert, wie Sie Text steuern können, indem Sie Textrahmen, Anpassung an die Größe und andere Formatierungsoptionen festlegen.

##### **Textumschlag**

Das Umwickeln von Text in einer Zelle erleichtert das Lesen: Die Höhe der Zelle passt sich an, um den gesamten Text aufzunehmen, anstatt ihn abzuschneiden oder über benachbarte Zellen überlaufen zu lassen. Legen Sie das Textumwickeln mit der [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-Objekteigenschaft [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) ein oder aus.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

##### **Anpassen an Größe**

Eine Option zum Umwickeln von Text in einem Feld ist das Verkleinern der Textgröße, um sich an die Abmessungen einer Zelle anzupassen. Dies erfolgt durch Festlegen der [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-Objekteigenschaft [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) auf **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.py" >}}

##### **Zellen zusammenführen**

Wie Microsoft Excel unterstützt Aspose.Cells für Python via .NET das Zusammenführen mehrerer Zellen zu einer. Aspose.Cells für Python via .NET bietet zwei Ansätze für diese Aufgabe. Ein Weg ist, die Methode [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) der [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) Sammlung aufzurufen. Die [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) Methode benötigt die folgenden Parameter zum Zusammenführen der Zellen:

- Erste Zeile: Die erste Zeile, ab der das Zusammenführen beginnt.
- Erste Spalte: Die erste Spalte, ab der das Zusammenführen beginnt.
- Anzahl der Zeilen: Die Anzahl der zu zusammenführenden Zeilen.
- Anzahl der Spalten: Die Anzahl der zu zusammenführenden Spalten.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Merging-MergingCellsInWorksheet.-1.py" >}}

Der andere Weg besteht darin, zuerst die [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/)-Sammlungsmethode [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) aufzurufen, um einen Bereich der zu zusammenführenden Zellen zu erstellen. Die [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range)-Methode akzeptiert denselben Satz von Parametern wie die zuvor diskutierte [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge)-Methode und gibt ein [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)-Objekt zurück. Das [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)-Objekt bietet auch eine [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge)-Methode, die den im [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)-Objekt angegebenen Bereich zusammenführt.

##### **Textausrichtung**

Es ist möglich, die Lesereihenfolge von Text in Zellen festzulegen. Die Lesereihenfolge gibt die visuelle Reihenfolge an, in der Zeichen, Wörter usw. angezeigt werden. Zum Beispiel ist Englisch eine von links nach rechts lesbare Sprache, während Arabisch eine von rechts nach links lesbare Sprache ist.

Die Lesereihenfolge wird mit der Eigenschaft [**text_direction**](https://reference.aspose.com/cells/python-net/aspose.cells/style/text_direction) des [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) Objekts festgelegt. Aspose.Cells für Python via .NET bietet vordefinierte Textausrichtungstypen in der [**TextDirectionType**](https://reference.aspose.com/cells/python-net/aspose.cells/textdirectiontype) Enumeration.

|**Text Direction Types**|**Beschreibung**|
| :- | :- |
|KONTEXT|Die Lesereihenfolge entspricht der Sprache des ersten eingegebenen Zeichens|
|LINKS_NACH_RECHTS|Lesereihenfolge von links nach rechts|
|RECHTS_NACH_LINKS|Lesereihenfolge von rechts nach links|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeTextDirection-1.py" >}}

## **Erweiterte Themen**
- [Zellenausrichtung ändern und vorhandenes Format beibehalten](/cells/de/python-net/change-cells-alignment-and-keep-existing-formatting/)
- [Zeilenumbrüche und Textumbrüche](/cells/de/python-net/line-breaks-and-text-wrapping/)


{{< app/cells/assistant language="python-net" >}}
