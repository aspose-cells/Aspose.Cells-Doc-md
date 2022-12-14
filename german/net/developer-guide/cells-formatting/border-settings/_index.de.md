---
title: Rahmeneinstellungen
type: docs
weight: 40
url: /de/net/cells-border-settings/
---
## **Grenzen zu Cells hinzufügen**

Microsoft Excel ermöglicht Benutzern das Formatieren von Zellen durch Hinzufügen von Rahmen. Die Art der Umrandung hängt davon ab, wo sie hinzugefügt wird. Ein oberer Rand wird beispielsweise an der obersten Position einer Zelle hinzugefügt. Benutzer können auch den Linienstil und die Farbe der Rahmen ändern.

Mit Aspose.Cells können Entwickler Rahmen hinzufügen und deren Aussehen auf die gleiche flexible Weise wie in Microsoft Excel anpassen.

### **Grenzen zu Cells hinzufügen**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse bietet die[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung. Jeder Artikel in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung stellt ein Objekt der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse.

 Aspose.Cells bietet die[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)Methode in der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse. Das[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)-Methode wird verwendet, um den Formatierungsstil einer Zelle festzulegen. Das[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)-Klasse bietet Eigenschaften zum Hinzufügen von Rahmen zu Zellen.

#### **Rahmen zu Cell hinzufügen**

Entwickler können Rahmen zu einer Zelle hinzufügen, indem sie die verwenden[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Grenzen**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) Sammlung. Der Rahmentyp wird als Index an die übergeben[**Grenzen**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) Sammlung. Alle Randtypen sind in der vordefiniert[**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) Aufzählung.

**Grenzaufzählung**

|**Grenztypen**|**Beschreibung**|
|:- |:- |
|Untere Grenze|Eine untere Grenzlinie|
|DiagonalUnten|Eine diagonale Linie von links oben nach rechts unten|
|Diagonal nach oben|Eine diagonale Linie von links unten nach rechts oben|
|Linker Rand|Eine linke Grenzlinie|
|Rechter Rand|Eine rechte Grenzlinie|
|Oberer Rand|Eine obere Grenzlinie|

Das[**Grenzen**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)Sammlung speichert alle Grenzen. Jede Grenze in der[**Grenzen**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) Sammlung wird vertreten durch a[**Grenze**](https://reference.aspose.com/cells/net/aspose.cells/border) Objekt, das zwei Eigenschaften bereitstellt,[**Farbe**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) und[**Linienstil**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle), um die Linienfarbe und den Stil eines Rahmens einzustellen.

Um die Linienfarbe eines Rahmens festzulegen, wählen Sie eine Farbe mithilfe der Color-Enumeration (Teil des .NET-Frameworks) aus und weisen Sie sie der Color-Eigenschaft des Border-Objekts zu.

 Der Linienstil des Rahmens wird durch Auswahl eines Linienstils aus festgelegt[**CellRandType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)Aufzählung.

**CellBorderType-Aufzählung**

|**Linienstile**|**Beschreibung**|
|:- |:- |
|Strich Punkt|Dünne strichpunktierte Linie|
|DashDotDot|Dünne Strich-Punkt-Punkt-Linie|
|Gestrichelt|Gestrichelte Linie|
|Gepunktet|Gepunktete Linie|
|Doppelt|Doppelte Linie|
|Haar|Haaransatz|
|MediumDashDot|Mittlere strichpunktierte Linie|
|MediumDashDotDot|Mittlere Strich-Punkt-Punkt-Linie|
|Mittelgestrichelt|Mittlere gestrichelte Linie|
|Keiner|Keine Linie|
|Mittel|Mittlere Linie|
|SlantedDashDot|Schräge mittlere strichpunktierte Linie|
|Dick|Dicke Linie|
|Dünn|Dünne Linie|
Wählen Sie einen der Linienstile aus und weisen Sie ihn dann dem zu[**Grenze**](https://reference.aspose.com/cells/net/aspose.cells/border) Objekt[**Linienstil**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Sie sollten sowohl den Linienstil als auch die Farbe gleichzeitig festlegen. Die beiden diagonalen Grenzlinien sollten denselben Linienstil und dieselbe Farbe haben.

{{% /alert %}}

#### **Hinzufügen von Grenzen zu einem Bereich von Cells**

Es ist auch möglich, Grenzen zu einem Bereich von Zellen hinzuzufügen, statt nur zu einer einzelnen Zelle. Erstellen Sie dazu zunächst einen Zellbereich, indem Sie die aufrufen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung[**Bereich erstellen**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) Methode. Es nimmt die folgenden Parameter:

- Erste Reihe, die erste Reihe des Bereichs.
- Erste Spalte, stellt die erste Spalte des Bereichs dar.
- Anzahl der Zeilen, die Anzahl der Zeilen im Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Bereich.

 Das[**Bereich erstellen**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) Methode gibt a zurück[**Bereich**](https://reference.aspose.com/cells/net/aspose.cells/range) Objekt, das den angegebenen Zellbereich enthält. Das[**Bereich**](https://reference.aspose.com/cells/net/aspose.cells/range) Objekt bietet a[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) Methode, die die folgenden Parameter verwendet, um dem Zellbereich einen Rahmen hinzuzufügen:

- **Grenztyp** , der Rahmentyp, ausgewählt aus der[**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)Aufzählung.
- **Linienstil** , der Rahmenlinienstil, ausgewählt aus der[**CellRandType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)Aufzählung.
- **Farbe**, die Linienfarbe, ausgewählt aus der Color-Enumeration.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}

## **Farben und Palette**

Eine Palette ist die Anzahl der Farben, die zur Verwendung beim Erstellen eines Bildes zur Verfügung stehen. Die Verwendung einer standardisierten Palette in einer Präsentation ermöglicht es dem Benutzer, ein konsistentes Erscheinungsbild zu erstellen. Jede Microsoft Excel (97-2003)-Datei hat eine Palette von 56 Farben, die auf Zellen, Schriftarten, Gitterlinien, Grafikobjekte, Füllungen und Linien in einem Diagramm angewendet werden können.

Mit Aspose.Cells ist es möglich, nicht nur die vorhandenen Farben der Palette, sondern auch benutzerdefinierte Farben zu verwenden. Bevor Sie eine benutzerdefinierte Farbe verwenden, fügen Sie sie zuerst der Palette hinzu.

In diesem Thema wird erläutert, wie Sie der Palette benutzerdefinierte Farben hinzufügen.

### **Hinzufügen benutzerdefinierter Farben zur Palette**

Aspose.Cells unterstützt die 56-Farben-Palette von Microsoft Excel. Um eine benutzerdefinierte Farbe zu verwenden, die nicht in der Palette definiert ist, fügen Sie die Farbe der Palette hinzu.

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse bietet a[**Palette ändern**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) Methode, die die folgenden Parameter benötigt, um eine benutzerdefinierte Farbe hinzuzufügen, um die Palette zu ändern:

- Benutzerdefinierte Farbe, die hinzuzufügende benutzerdefinierte Farbe.
- Index, der Index der Farbe in der Palette, die durch die benutzerdefinierte Farbe ersetzt wird. Sollte zwischen 0-55 liegen.

Im folgenden Beispiel wird der Palette eine benutzerdefinierte Farbe (Orchidee) hinzugefügt, bevor sie auf eine Schriftart angewendet wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

Die Palette enthält nur 56 Farben. Wenn Sie der Palette eine benutzerdefinierte Farbe hinzufügen, wird die Palette geändert und alle Elemente in der Datei, die mit der vorherigen Farbe formatiert wurden, werden geändert. Seien Sie also bitte sehr vorsichtig, wenn Sie die Palette ändern. Darüber hinaus ist dies nur die Einschränkung im XLS-Dateiformat (Excel 97 - 2003), da es keine solche Einschränkung für XLSX- oder andere fortgeschrittene MS Excel-Dateiformate (2007/2010 oder 2013) gibt.

{{% /alert %}}


