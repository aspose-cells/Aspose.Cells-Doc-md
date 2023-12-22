---
title: Randeinstellungen
description: So verwenden Sie die Bibliothek Aspose.Cells in C#, um den Rahmenstil und die Farbe von Zellen festzulegen. Durch Anpassen der Breite, des Stils und der Farbe des Rahmens haben Sie mehr Kontrolle darüber, wie Zellen aussehen und angezeigt werden.
keywords: Aspose.Cells, Cell Border Settings, C#, Border Width, Border Style, Border Color
type: docs
weight: 40
url: /de/net/cells-border-settings/
---
##  **Hinzufügen von Rändern zu Cells**

Microsoft Excel ermöglicht Benutzern das Formatieren von Zellen durch Hinzufügen von Rändern. Die Art des Rahmens hängt davon ab, wo er hinzugefügt wird. Beispielsweise wird ein oberer Rand an der oberen Position einer Zelle hinzugefügt. Benutzer können auch den Linienstil und die Farbe der Rahmen ändern.

Mit Aspose.Cells können Entwickler Rahmen hinzufügen und deren Aussehen auf die gleiche flexible Weise anpassen wie in Microsoft Excel.

###  **Hinzufügen von Rändern zu Cells**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet die[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung. Jedes Element in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Die Sammlung stellt ein Objekt dar[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse.

 Aspose.Cells bietet die[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)Methode in der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse. Der[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)Die Methode wird verwendet, um den Formatierungsstil einer Zelle festzulegen. Der[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Die Klasse stellt Eigenschaften zum Hinzufügen von Rahmen zu Zellen bereit.

####  **Hinzufügen von Rändern zu einer Cell**

Entwickler können einer Zelle Rahmen hinzufügen, indem sie die verwenden[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Grenzen**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) Sammlung. Der Rahmentyp wird als Index an übergeben[**Grenzen**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) Sammlung. Alle Rahmentypen sind im vordefiniert[**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) Aufzählung.

**Grenzaufzählung**

|**Randtypen**|**Beschreibung**|
| :- | :- |
|Untere Grenze|Eine untere Grenzlinie|
|DiagonalDown|Eine diagonale Linie von links oben nach rechts unten|
|DiagonalUp|Eine diagonale Linie von links unten nach rechts oben|
|Linker Rand|Eine linke Grenzlinie|
|RightBorder|Eine rechte Grenzlinie|
|TopBorder|Eine obere Grenzlinie|

Der[**Grenzen**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)Die Sammlung speichert alle Grenzen. Jede Grenze in der[**Grenzen**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) Die Sammlung wird durch a repräsentiert[**Grenze**](https://reference.aspose.com/cells/net/aspose.cells/border) Objekt, das zwei Eigenschaften bereitstellt,[**Farbe**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) Und[**Linienstil**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)um die Linienfarbe und den Linienstil eines Rahmens festzulegen.

Um die Linienfarbe eines Rahmens festzulegen, wählen Sie mithilfe der Color-Enumeration (Teil des .NET-Frameworks) eine Farbe aus und weisen Sie sie der Color-Eigenschaft des Border-Objekts zu.

 Der Linienstil des Rahmens wird durch Auswahl eines Linienstils aus festgelegt[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)Aufzählung.

**CellBorderType-Aufzählung**

|**Linienstile**|**Beschreibung**|
| :- | :- |
|Strich Punkt|Dünne strichpunktierte Linie|
|DashDotDot|Dünne Strich-Punkt-Punkt-Linie|
|Gestrichelt|Gestrichelte Linie|
|Gepunktet|Gepunktete Linie|
|Doppelt|Doppelte Linie|
|Haar|Haaransatz|
|MediumDashDot|Mittlere strichpunktierte Linie|
|MediumDashDotDot|Mittlere Strich-Punkt-Punkt-Linie|
|MediumDashed|Mittlere gestrichelte Linie|
|Keiner|Keine Linie|
|Mittel|Mittlere Linie|
|SlantedDashDot|Schräge mittlere strichpunktierte Linie|
|Dick|Dicke Linie|
|Dünn|Dünne Linie|
Wählen Sie einen der Linienstile aus und weisen Sie ihn dann dem zu[**Grenze**](https://reference.aspose.com/cells/net/aspose.cells/border) Objekt[**Linienstil**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Sie sollten sowohl den Linienstil als auch die Farbe gleichzeitig festlegen. Die beiden diagonalen Randlinien sollten den gleichen Linienstil und die gleiche Farbe haben.

{{% /alert %}}

####  **Hinzufügen von Grenzen zu einem Bereich von Cells**

 Es ist auch möglich, Rahmen zu einem Bereich von Zellen statt nur zu einer einzelnen Zelle hinzuzufügen. Erstellen Sie dazu zunächst einen Zellbereich, indem Sie den aufrufen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) Methode. Es werden folgende Parameter benötigt:

- Erste Zeile, die erste Zeile des Bereichs.
- Erste Spalte stellt die erste Spalte des Bereichs dar.
- Anzahl der Zeilen, die Anzahl der Zeilen im Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Bereich.

 Der[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) Methode gibt a zurück[**Reichweite**](https://reference.aspose.com/cells/net/aspose.cells/range) Objekt, das den angegebenen Zellbereich enthält. Der[**Reichweite**](https://reference.aspose.com/cells/net/aspose.cells/range) Objekt bietet a[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) Methode, die die folgenden Parameter verwendet, um dem Zellbereich einen Rahmen hinzuzufügen:

-  *Rahmentyp**, der Rahmentyp, ausgewählt aus[**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)Aufzählung.
-  *Linienstil**, der Rahmenlinienstil, ausgewählt aus[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)Aufzählung.
- *Farbe**, die Linienfarbe, ausgewählt aus der Color-Enumeration.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
