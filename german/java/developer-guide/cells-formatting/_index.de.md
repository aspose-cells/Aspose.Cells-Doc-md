---
title: Zellformate
type: docs
weight: 100
url: /de/java/cells-formatting/
---

## **Rahmen zu Zellen hinzufügen**
Microsoft Excel ermöglicht Benutzern, Zellen zu formatieren, indem sie Rahmen hinzufügen.

**Rahmeneinstellungen in Microsoft Excel** 

![todo:image_alt_text](cells-formatting_1.png)

Die Art des Rahmens hängt davon ab, wo er hinzugefügt wird. Zum Beispiel ist ein oberer Rahmen einer, der an die obere Position einer Zelle hinzugefügt wird. Benutzer können auch den Linienstil und die Farbe der Rahmen ändern.

Mit Aspose.Cells können Entwickler Rahmen hinzufügen und anpassen, wie sie in Microsoft Excel in gleicher flexibler Weise aussehen.
### **Rahmen zu Zellen hinzufügen**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)-Klasse enthält eine [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-Klasse dargestellt. Die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-Klasse bietet eine [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung. Jedes Element in der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung stellt ein Objekt der [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)-Klasse dar.

Aspose.Cells bietet die Methode [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) in der Klasse [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell), um das Format einer Zelle festzulegen. Außerdem wird das Objekt der Klasse [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) verwendet und bietet Eigenschaften zur Konfiguration von Schriftarteinstellungen.
#### **Rahmen zu einer Zelle hinzufügen**
Fügen Sie einem Zell mit der Methode [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) des [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-Objekts Rahmenlinien hinzu. Der Border-Typ wird als Parameter übergeben. Alle Border-Typen sind in der Enumeration [BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType) vorgegeben.

|**Rahmentypen**|**Beschreibung**|
| :- | :- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM-BORDER)|Der untere Rand|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL-DOWN)|Eine diagonale Linie von oben links nach rechts unten|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL-UP)|Eine diagonale Linie von unten links nach oben rechts|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT-BORDER)|Der linke Rand|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT-BORDER)|Der rechte Rand|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP-BORDER)|Der obere Rand|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Nur für dynamischen Stil, z. B. bedingte Formatierung.|
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Nur für dynamischen Stil, z. B. bedingte Formatierung.|
Um die Linienfarbe zu setzen, wählen Sie eine Farbe mit der Enumeration [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) und übergeben Sie sie als Parameter an die Methode [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) des [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-Objekts. Die Linienarten sind in der Enumeration [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType) vorgegeben.

|**Linienstile**|**Beschreibung**|
| :- | :- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH-DOT)|Repräsentiert eine dünne gestrichelte Linie|
|[DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH-DOT_DOT)|Repräsentiert eine dünne gestrichelte Linie mit Punkten|
|[DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Stellt gestrichelte Linie dar|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Stellt gepunktete Linie dar|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Stellt doppelte Linie dar|
|[HAIR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Stellt Haarlinie dar|
|[MEDIUM_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASH-DOT)|Repräsentiert eine mittlere gestrichelte Linie|
|[MEDIUM_DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASH-DOT_DOT)|Repräsentiert mittel-dashed-dot-dot Linie|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASHED)|Repräsentiert mittlere gestrichelte Linie|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Stellt keine Linie dar|
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Stellt mittlere Linie dar|
|[SLANTED_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED-DASH-DOT)|Repräsentiert schräg mittlere gestrichelte Linie|
|[THICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Stellt dicke Linie dar|
|[THIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Stellt dünne Linie dar|
Wählen Sie einen der oben genannten Linienstile aus und weisen Sie ihn dann der [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-Objekt [Methode setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) zu.

Der folgende Output wird generiert, wenn der unten stehende Code ausgeführt wird.

**Ränder auf allen Seiten einer Zelle angewendet** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Hinzufügen von Rahmen zu einem Zellenbereich**
Es ist möglich, Grenzen zu einem Zellbereich hinzuzufügen, anstatt nur zu einer einzelnen Zelle. Erstellen Sie zunächst einen Zellbereich, indem Sie die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung aufrufen und die [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) Methode verwenden, welche die folgenden Parameter übernimmt:

- **Erste Zeile**, erste Zeile des Bereichs.
- **Erste Spalte**, erste Spalte des Bereichs.
- **Anzahl der Zeilen**, Anzahl der Zeilen im Bereich.
- **Anzahl der Spalten**, Anzahl der Spalten im Bereich.

Die [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) Methode gibt ein [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range)-Objekt zurück, das den angegebenen Bereich enthält. Das [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range)-Objekt bietet eine [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders-int-com.aspose.cells.Color-) Methode, die die folgenden Parameter übernimmt:

- **CellBorderType**, der Grenzlinienstil, ausgewählt aus der [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)-Aufzählung.
- **Farbe**, die Rahmenfarbe, ausgewählt aus der [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)-Enumeration.

Der folgende Output wird generiert, wenn der unten stehende Code ausgeführt wird.

**Angewendete Rahmen auf einem Zellenbereich** 

![todo:image_alt_text](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **Farben und Palette**
Eine Palette ist die Anzahl der verfügbaren Farben zur Erstellung eines Bildes. Die Verwendung einer standardisierten Palette in einer Präsentation ermöglicht es dem Benutzer, ein konsistentes Erscheinungsbild zu erstellen. Jede Microsoft Excel (97-2003)-Datei hat eine Palette von 56 Farben, die auf Zellen, Schriften, Gitterlinien, grafische Objekte, Füllungen und Linien in einem Diagramm angewendet werden können.

**Paletten-Einstellungen in Microsoft Excel** 

![todo:image_alt_text](cells-formatting_4.png)

Mit Aspose.Cells ist es nicht nur möglich, vorhandene Farben zu verwenden, sondern auch benutzerdefinierte Farben. Bevor Sie eine benutzerdefinierte Farbe verwenden, fügen Sie sie der Palette hinzu. In diesem Thema wird erläutert, wie benutzerdefinierte Farben der Palette hinzugefügt werden.
### **Hinzufügen von benutzerdefinierten Farben zur Palette**
Aspose.Cells unterstützt auch eine Palette von 56 Farben. Eine Standard-Farbpalette wird oben gezeigt. Wenn Sie eine benutzerdefinierte Farbe verwenden möchten, die nicht in der Palette definiert ist, müssen Sie diese Farbe vor der Verwendung zur Palette hinzufügen.

{{% alert color="primary" %}} 

Die Palette enthält nur 56 Farben. Wenn Sie eine benutzerdefinierte Farbe zur Palette hinzufügen, wird die Palette geändert und jedes Element in der Datei, das mit der vorherigen Farbe formatiert ist, wird geändert. Seien Sie also sehr vorsichtig, wenn Sie die Palette ändern. Außerdem ist dies nur eine Einschränkung bei XLS (Excel 97 - 2003)-Dateiformaten, da es keine solche Einschränkung für XLSX oder andere fortgeschrittene MS Excel (2007/2010)-Dateiformate gibt.

{{% /alert %}} 

Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse bietet die [changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette-com.aspose.cells.Color-int-) Methode, die die folgenden Parameter übernimmt, um eine benutzerdefinierte Farbe zur Änderung der Palette hinzuzufügen:

- **Benutzerdefinierte Farbe**, die benutzerdefinierte Farbe, die zur Palette hinzugefügt werden soll.
- **Index**, der Index der Farbe, die durch die benutzerdefinierte Farbe ersetzt werden soll. Sollte zwischen 0-55 liegen.

Das folgende Beispiel fügt eine benutzerdefinierte Farbe zur Palette hinzu, bevor sie auf eine Schriftart angewendet wird.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **Farben und Hintergrundmuster**
Microsoft Excel kann Vordergrund- (Umriss) und Hintergrund- (Füll-)Farben von Zellen und Hintergrundmuster wie unten gezeigt festlegen.

**Festlegen von Farben und Hintergrundmustern in Microsoft Excel** 

![todo:image_alt_text](cells-formatting_5.png)

Aspose.Cells unterstützt diese Funktionen ebenfalls in flexibler Weise. In diesem Thema lernen wir, diese Funktionen mit Aspose.Cells zu verwenden.
### **Setzen von Farben & Hintergrundmustern**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) enthält eine [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) dargestellt. Die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) bietet eine [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung. Jedes Element in der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung stellt ein Objekt der Klasse [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) dar.

Aspose.Cells bietet die [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) Methode in der [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-Klasse, die verwendet wird, um die Formatierung einer Zelle festzulegen. Außerdem kann das Objekt der [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-Klasse verwendet werden, um Schriftarteinstellungen zu konfigurieren.

{{% alert color="primary" %}} 

Um die Vordergrund- oder Hintergrundfarbe einer Zelle festzulegen, verwenden Sie die Eigenschaften [setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) oder [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) des Objekts [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Diese Eigenschaften kommen nur dann zur Geltung, wenn die Eigenschaft [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) des Objekts [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) konfiguriert ist.

{{% /alert %}} 

Die Eigenschaft [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) legt die Farbe des Zellenschattierung fest.

Die Eigenschaft [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) legt das Hintergrundmuster fest, das für die Vordergrund- oder Hintergrundfarbe verwendet wird. Aspose.Cells bietet die Enumeration [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType), die eine Reihe von vordefinierten Arten von Hintergrundmustern enthält.

|**Mustertyp**|**Beschreibung**|
| :- | :- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL-CROSSHATCH)|Repräsentiert diagonales Schraffurmuster|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL-STRIPE)|Repräsentiert diagonales Streifenmuster|
|[GRAY_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-6)|Repräsentiert grau Muster mit 6,25%|
|[GRAY_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-12)|Repräsentiert grau Muster mit 12,5%|
|[GRAY_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-25)|Repräsentiert grau Muster mit 25%|
|[GRAY_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-50)|Repräsentiert grau Muster mit 50%|
|[GRAY_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-75)|Repräsentiert grau Muster mit 75%|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL-STRIPE)|Repräsentiert horizontales Streifenmuster|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|Stellt keinen Hintergrund dar|
|[REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE-DIAGONAL-STRIPE)|Repräsentiert Muster mit umgekehrten diagonalen Streifen|
|[SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Stellt das einfarbige Muster dar|
|[THICK_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK-DIAGONAL-CROSSHATCH)|Repräsentiert dickes diagonales Schraffurmuster|
|[THIN_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-DIAGONAL-CROSSHATCH)|Repräsentiert dünnes diagonales Schraffurmuster|
|[THIN_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-DIAGONAL-STRIPE)|Repräsentiert dünnes diagonales Streifenmuster|
|[THIN_HORIZONTAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-HORIZONTAL-CROSSHATCH)|Repräsentiert dünnes horizontalens Schraffurmuster|
|[THIN_HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-HORIZONTAL-STRIPE)|Repräsentiert dünnes horizontalen Streifenmuster|
|[THIN_REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-REVERSE-DIAGONAL-STRIPE)|Repräsentiert dünnes umgekehrtes diagonales Streifenmuster|
|[THIN_VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-VERTICAL-STRIPE)|Repräsentiert dünnes vertikales Streifenmuster|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL-STRIPE)|Repräsentiert vertikales Streifenmuster|
Im folgenden Beispiel ist die Vordergrundfarbe der Zelle A1 festgelegt, aber A2 ist so konfiguriert, dass sowohl Vordergrund- als auch Hintergrundfarben mit einem vertikalen Streifenmuster hinterlegt sind.

Die folgende Ausgabe wird bei der Ausführung des Codes generiert.

**Vordergrund- und Hintergrundfarben auf Zellen mit Hintergrundmustern angewendet** 

![todo:image_alt_text](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **Wichtig zu wissen**
{{% alert color="primary" %}} 

- Verwenden Sie für die Festlegung der Vordergrund- oder Hintergrundfarbe einer Zelle die Eigenschaften [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) oder [BackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) des [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-Objekts. Beide Eigenschaften wirken sich nur aus, wenn die Eigenschaft [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) des [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-Objekts konfiguriert ist.
- Die Eigenschaft [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) legt die Farbe des Zellenschattens fest.
  Die Eigenschaft [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) gibt den Typ des verwendeten Hintergrundmusters für die Vordergrund- oder Hintergrundfarbe an. Aspose.Cells bietet eine Aufzählung [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType), die eine Reihe vordefinierter Typen von Hintergrundmustern enthält.
- Wenn Sie den Wert [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) aus der Aufzählung [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) auswählen, wird die Vordergrundfarbe nicht angewendet.
  Ebenso wird die Hintergrundfarbe nicht angewendet, wenn Sie die Werte [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) oder [BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID) auswählen.
- Beim Abrufen der Schattierungs-/Füllfarbe der Zelle gibt die Eigenschaft [Style.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) *Color.Empty* zurück, wenn [Style.Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) den Wert [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) hat.

{{% /alert %}} 
## **Formatieren ausgewählter Zeichen in einer Zelle**
[Umgang mit Schrifteinstellungen](/cells/de/java/dealing-with-font-settings/) erklärte, wie Zellen formatiert werden, aber nur, wie der Inhalt der gesamten Zellen formatiert wird. Was ist, wenn Sie nur ausgewählte Zeichen formatieren möchten?

Aspose.Cells unterstützt diese Funktion. Dieser Artikel erläutert, wie Sie diese Funktion verwenden können.
### **Formatieren ausgewählter Zeichen**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) enthält eine [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) dargestellt. Die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) bietet eine [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung. Jedes Element in der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung stellt ein Objekt der Klasse [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) dar.

Die [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse bietet die [characters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters-int-int-) Methode, die die folgenden Parameter übernimmt, um einen Bereich von Zeichen in einer Zelle auszuwählen:

- **Start-Index**, der Index des Zeichens, von dem aus die Auswahl beginnen soll.
- **Anzahl der Zeichen**: Die Anzahl der ausgewählten Zeichen.

In der Ausgabedatei ist in der Zelle A1 das Wort 'Besuchen' mit der Standardschrift formatiert, aber 'Aspose!' ist fett und blau.

**Auswahl von formatierten Zeichen** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

Wenn Sie daran interessiert sind, einen Teil des Rich Texts in einer Zelle zu formatieren, sollten Sie die [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters--) & Cell.setCharacters Methoden verwenden. Die [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters--) Methode wird verwendet, um die Textabschnitte abzurufen, und Änderungen können mit der Cell.setCharacters Methode vorgenommen werden. Das **get**-Verfahren gibt ein Array von [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) Objekten zurück, die manipuliert werden können, um verschiedene Eigenschaften wie Schriftartname, Schriftfarbe, Fettdruck usw. festzulegen, während die **set**-Methode verwendet werden kann, um die Änderungen anzuwenden.

{{% /alert %}}

## **Erweiterte Themen**
- [Ausrichtungseinstellungen](/cells/de/java/cells-alignment-settings/)
- [Bedingte Formatierung](/cells/de/java/conditional-formatting/)
- [Datenaufbereitung](/cells/de/java/data-formatting/)
- [Excel-Themen und Farben](/cells/de/java/excel-2007-themes-and-colors/)
- [Umgang mit Schrifteinstellungen](/cells/de/java/dealing-with-font-settings/)
- [Zellenformat in einer Arbeitsmappe](/cells/de/java/format-worksheet-cells-in-a-workbook/)
- [Implementieren des 1904-Datumsformats](/cells/de/java/implement-1904-date-system/)
- [Zusammenführen und Aufheben der Zellenzusammenführung](/cells/de/java/merging-and-unmerging-cells/)
- [Nummern-Einstellungen](/cells/de/java/cells-number-settings/)
- [Einzelnes Anführungszeichen-Prefix des Zellenwerts oder -bereichs beibehalten](/cells/de/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Styling und Datenformatierung](/cells/de/java/styling-and-data-formatting/)
{{< app/cells/assistant language="java" >}}
