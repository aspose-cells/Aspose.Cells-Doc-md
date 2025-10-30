---
title: Rahmeneinstellungen
description: So verwenden Sie die Aspose.Cells für Python via .NET Bibliothek in Python, um den Rahmenstil und die Farbe von Zellen festzulegen. Durch Anpassen der Breite, des Stils und der Farbe des Rahmens haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells für Python via .NET, Zellrand Einstellungen, Python Border Breite, Rahmenstil, Rahmenfarbe
type: docs
weight: 40
url: /de/python-net/cells-border-settings/
---

## **Rahmen zu Zellen hinzufügen**

Microsoft Excel ermöglicht es Benutzern, Zellen durch Hinzufügen von Rahmen zu formatieren. Die Art des Rahmens hängt davon ab, wo er hinzugefügt wird. Zum Beispiel ist ein oberer Rahmen einer, der an der oberen Position einer Zelle hinzugefügt wird. Benutzer können auch den Linienstil und die Farbe der Rahmen ändern.

Mit Aspose.Cells für Python via .NET können Entwickler Rahmen hinzufügen und anpassen, wie sie in der gleichen flexiblen Weise wie in Microsoft Excel aussehen.

### **Rahmen zu Zellen hinzufügen**

Aspose.Cells für Python via .NET stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet die [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) Sammlung. Jedes Element in der Sammlung [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) stellt ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) dar.

Aspose.Cells für Python via .NET bietet die [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) Methode in der [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) Klasse. Die [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) Methode wird verwendet, um den Formatierungsstil einer Zelle festzulegen. Die [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) Klasse bietet Eigenschaften zum Hinzufügen von Rahmenlinien zu Zellen.

#### **Rahmen zu einer Zelle hinzufügen**

Entwickler können Rahmen zu einer Zelle hinzufügen, indem sie die [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-Objektsammlung [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) verwenden. Der Rahmentyp wird als Index an die Sammlung [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) übergeben. Alle Rahmentypen sind in der Aufzählung [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype) vordefiniert.

**Rahmen-Aufzählung**

|**Rahmentypen**|**Beschreibung**|
| :- | :- |
|BOTTOM_BORDER|Eine untere Rahmenlinie|
|DIAGONAL_DOWN|Eine diagonale Linie von oben links nach unten rechts|
|DIAGONAL_UP|Eine diagonale Linie von unten links nach oben rechts|
|LEFT_BORDER|Eine linke Rahmenlinie|
|RIGHT_BORDER|Eine rechte Rahmenlinie|
|TOP_BORDER|Eine obere Rahmenlinie|

The [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border) object which provides two properties, [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/border/color) and [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) to set a border's line color and style respectively.

Um die Linienfarbe eines Rahmens festzulegen, wählen Sie eine Farbe aus der Color-Enumeration (Teil des .NET Frameworks) aus und weisen Sie sie der Eigenschaft Color des Rahmenobjekts zu.

Der Linienstil des Rahmens wird festgelegt, indem ein Linienstil aus der [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype)-Enumeration ausgewählt wird.

**Zellrahmentyp-Enumeration**

|**Linienstile**|**Beschreibung**|
| :- | :- |
|DASH_DOT|Dünne gestrichelte Linie|
|DASH_DOT_DOT|Dünne gestrichelte-dotierte Linie|
|DASHED|Gestrichelte Linie|
|DOTTED|Gepunktete Linie|
|DOUBLE|Doppelte Linie|
|HAIR|Haarlinie|
|MEDIUM_DASH_DOT|Mittlere gestrichelte Linie|
|MEDIUM_DASH_DOT_DOT|Mittlere gestrichelte-dotierte Linie|
|MEDIUM_DASHED|Mittlere gestrichelte Linie|
|NONE|Keine Linie|
|MEDIUM|Mittlere Linie|
|SLANTED_DASH_DOT|Schräge mittlere gestrichelte Linie|
|THICK|Dicke Linie|
|THIN|Dünne Linie|
Wählen Sie einen der Linienstile aus undweisen Sie ihn dann der [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border) Eigenschaft des [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) Objekts zu.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBordersToCells-1.py" >}}

{{% alert color="primary" %}}

Sie sollten sowohl den Linienstil als auch die Farbe gleichzeitig festlegen. Die beiden diagonalen Rahmenlinien sollten denselben Linienstil und dieselbe Farbe haben.

{{% /alert %}}

#### **Hinzufügen von Rahmen zu einem Zellenbereich**

Sie können auch einem Zellenbereich Rahmen hinzufügen, anstatt nur einer einzelnen Zelle. Dazu erstellen Sie zunächst einen Zellenbereich, indem Sie die [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) Methode der [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) Sammlung aufrufen. Sie nimmt die folgenden Parameter an:

- Erste Zeile, die erste Zeile des Bereichs.
- Erste Spalte, stellt die erste Spalte des Bereichs dar.
- Anzahl der Zeilen, die Anzahl der Zeilen im Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Bereich.

Die [**create_range**](hhttps://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str) Methode gibt ein [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) Objekt zurück, das den angegebenen Zellenbereich enthält. Das [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) Objekt bietet eine [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border) Methode an, die die folgenden Parameter annimmt, um einem Zellenbereich einen Rahmen hinzuzufügen:

- **Rahmentyp**, der aus der [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype) Aufzählung ausgewählte Rahmentyp.
- **Linienstil**, der aus der [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype) Aufzählung ausgewählte Linienstil.
- **Farbe**, die aus der Farb-Aufzählung ausgewählte Linienfarbe.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBorderstoRange-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
