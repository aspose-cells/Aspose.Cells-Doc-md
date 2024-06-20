---
title: Rahmeneinstellungen
description: So verwenden Sie die Aspose.Cells Bibliothek in C#, um den Rahmenstil und die Farbe von Zellen festzulegen. Durch Anpassung der Breite, des Stils und der Farbe des Rahmens haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Zellrahmeneinstellungen, C#, Rahmenbreite, Rahmenstil, Rahmenfarbe
type: docs
weight: 40
url: /de/net/cells-border-settings/
---

## **Rahmen zu Zellen hinzufügen**

Microsoft Excel ermöglicht es Benutzern, Zellen durch Hinzufügen von Rahmen zu formatieren. Die Art des Rahmens hängt davon ab, wo er hinzugefügt wird. Zum Beispiel ist ein oberer Rahmen einer, der an der oberen Position einer Zelle hinzugefügt wird. Benutzer können auch den Linienstil und die Farbe der Rahmen ändern.

Mit Aspose.Cells können Entwickler Rahmen hinzufügen und anpassen, wie sie in der gleichen flexiblen Weise wie in Microsoft Excel aussehen.

### **Rahmen zu Zellen hinzufügen**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine Sammlung von [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet die Sammlung [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Jedes Element in der Sammlung [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) repräsentiert ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells bietet die Methode [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) in der Klasse [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Die Methode [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) wird verwendet, um den Formatierungsstil einer Zelle festzulegen. Die Klasse [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) bietet Eigenschaften zum Hinzufügen von Rahmen zu Zellen.

#### **Rahmen zu einer Zelle hinzufügen**

Entwickler können Rahmen zu einer Zelle hinzufügen, indem sie die [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-Objektsammlung [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) verwenden. Der Rahmentyp wird als Index an die Sammlung [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) übergeben. Alle Rahmentypen sind in der Aufzählung [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) vordefiniert.

**Rahmen-Aufzählung**

|**Rahmentypen**|**Beschreibung**|
| :- | :- |
|BottomBorder|Eine untere Rahmenlinie
|DiagonalDown|Eine diagonale Linie von oben links nach rechts unten
|DiagonalUp|Eine diagonale Linie von unten links nach oben rechts|
|LeftBorder|Eine Linie am linken Rand|
|RightBorder|Eine Linie am rechten Rand|
|TopBorder|Eine Linie am oberen Rand|

The [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border) object which provides two properties, [**Color**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) and [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) to set a border's line color and style respectively.

Um die Linienfarbe eines Rahmens festzulegen, wählen Sie eine Farbe aus der Color-Enumeration (Teil des .NET Frameworks) aus und weisen Sie sie der Eigenschaft Color des Rahmenobjekts zu.

Der Linienstil des Rahmens wird festgelegt, indem ein Linienstil aus der [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)-Enumeration ausgewählt wird.

**Zellrahmentyp-Enumeration**

|**Linienstile**|**Beschreibung**|
| :- | :- |
|DashDot|Dünne gestrichelt-punktierte Linie|
|DashDotDot|Dünne gestrichelt-punkt-punktierte Linie|
|Dashed|Gestrichelte Linie|
|Dotted|Gepunktete Linie|
|Double|Doppelte Linie|
|Hair|Haarlinie|
|MediumDashDot|Mittlere gestrichelt-punktierte Linie|
|MediumDashDotDot|Mittlere gestrichelt-punkt-punktierte Linie|
|MediumDashed|Mittlere gestrichelte Linie|
|None|Keine Linie|
|Medium|Mittlere Linie|
|SlantedDashDot|Geneigte mittlere Strichpunktlinie|
|Thick|Dicke Linie|
|Thin|Dünne Linie|
Wählen Sie einen der Linienstile aus undweisen Sie ihn dann der [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border) Eigenschaft des [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) Objekts zu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Sie sollten sowohl den Linienstil als auch die Farbe gleichzeitig festlegen. Die beiden diagonalen Rahmenlinien sollten denselben Linienstil und dieselbe Farbe haben.

{{% /alert %}}

#### **Hinzufügen von Rahmen zu einem Zellenbereich**

Sie können auch einem Zellenbereich Rahmen hinzufügen, anstatt nur einer einzelnen Zelle. Dazu erstellen Sie zunächst einen Zellenbereich, indem Sie die [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Methode der [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) Sammlung aufrufen. Sie nimmt die folgenden Parameter an:

- Erste Zeile, die erste Zeile des Bereichs.
- Erste Spalte, stellt die erste Spalte des Bereichs dar.
- Anzahl der Zeilen, die Anzahl der Zeilen im Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Bereich.

Die [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) Methode gibt ein [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) Objekt zurück, das den angegebenen Zellenbereich enthält. Das [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) Objekt bietet eine [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) Methode an, die die folgenden Parameter annimmt, um einem Zellenbereich einen Rahmen hinzuzufügen:

- **Rahmentyp**, der aus der [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) Aufzählung ausgewählte Rahmentyp.
- **Linienstil**, der aus der [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype) Aufzählung ausgewählte Linienstil.
- **Farbe**, die aus der Farb-Aufzählung ausgewählte Linienfarbe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
