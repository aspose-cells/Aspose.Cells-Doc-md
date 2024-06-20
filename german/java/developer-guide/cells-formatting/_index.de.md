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

Aspose.Cells bietet die Methode [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) in der [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)-Klasse, die verwendet wird, um den Formatierungsstil einer Zelle festzulegen. Außerdem wird das Objekt der [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-Klasse verwendet und bietet Eigenschaften zur Konfiguration der Schrifteinstellungen.
#### **Rahmen zu einer Zelle hinzufügen**
Fügen Sie einer Zelle mit der Methode [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) des Objekts [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) einen Rahmen hinzu. Der Rahmen-Typ wird als Parameter übergeben. Alle Rahmen-Typen sind in der Enumeration [BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType) vordefiniert.

|**Rahmentypen**|**Beschreibung**|
| :- | :- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|Die Untergrenzlinie|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|Eine diagonale Linie von oben links nach rechts unten|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|Eine diagonale Linie von unten links nach rechts oben|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|Die linke Grenzlinie|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|Die rechte Grenzlinie|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|Die obere Grenzlinie|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Nur für dynamischen Stil, z. B. bedingte Formatierung.|
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Nur für dynamischen Stil, z. B. bedingte Formatierung.|
Um die Linienfarbe festzulegen, wählen Sie mit der Enumeration [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) eine Farbe aus und übergeben Sie sie dem Parameter Color der Methode [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) des Objekts [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Die Linienstile sind in der Enumeration [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType) vordefiniert.

|**Linienstile**|**Beschreibung**|
| :- | :- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|Stellt dünn gestrichelte Linie dar|
|[DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|Stellt dünn gestrichelte Punktlinie dar|
|[DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Stellt gestrichelte Linie dar|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Stellt gepunktete Linie dar|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Stellt doppelte Linie dar|
|[HAIR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Stellt Haarlinie dar|
|[MEDIUM_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|Stellt mittlere strichpunktierende Linie dar|
|[MEDIUM_DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|Stellt mittlere strich-punkt-strichpunktierende Linie dar|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|Stellt mittlere gestrichelte Linie dar|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Stellt keine Linie dar|
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Stellt mittlere Linie dar|
|[SLANTED_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|Stellt geneigte mittlere strichpunktierende Linie dar|
|[THICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Stellt dicke Linie dar|
|[THIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Stellt dünne Linie dar|
Wählen Sie einen der obigen Linienstile aus und weisen Sie ihn dann der [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-Objektmethode [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) zu.

Der folgende Output wird generiert, wenn der unten stehende Code ausgeführt wird.

**Ränder auf allen Seiten einer Zelle angewendet** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Hinzufügen von Rahmen zu einem Zellenbereich**
Es ist möglich, Grenzen zu einem Zellenbereich hinzuzufügen, anstatt nur einer einzelnen Zelle. Erstellen Sie zunächst einen Zellenbereich, indem Sie die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlungsmethode [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) aufrufen, die die folgenden Parameter verwendet:

- **Erste Zeile**, erste Zeile des Bereichs.
- **Erste Spalte**, erste Spalte des Bereichs.
- **Anzahl der Zeilen**, Anzahl der Zeilen im Bereich.
- **Anzahl der Spalten**, Anzahl der Spalten im Bereich.

Die Methode [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) gibt ein [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range)-Objekt zurück, das den angegebenen Bereich enthält. Das [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range)-Objekt bietet eine Methode [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)), die die folgenden Parameter verwendet:

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

Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse bietet die Methode [changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)), die die folgenden Parameter annimmt, um eine benutzerdefinierte Farbe zur Änderung der Palette hinzuzufügen:

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

Aspose.Cells bietet die Methode [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) in der Klasse [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell), die verwendet wird, um das Format einer Zelle festzulegen. Außerdem kann das Objekt der Klasse [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) zur Konfiguration von Schriftart-Einstellungen verwendet werden.

{{% alert color="primary" %}} 

Um die Vordergrund- oder Hintergrundfarbe einer Zelle festzulegen, verwenden Sie die Eigenschaften [setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) oder [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) des Objekts [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Diese Eigenschaften kommen nur dann zur Geltung, wenn die Eigenschaft [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) des Objekts [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) konfiguriert ist.

{{% /alert %}} 

Die Eigenschaft [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) legt die Farbe des Zellenschattierung fest.

Die Eigenschaft [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) legt das Hintergrundmuster fest, das für die Vordergrund- oder Hintergrundfarbe verwendet wird. Aspose.Cells bietet die Enumeration [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType), die eine Reihe von vordefinierten Arten von Hintergrundmustern enthält.

|**Mustertyp**|**Beschreibung**|
| :- | :- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|Stellt das diagonale Kreuzschraffur-Muster dar|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|Stellt das diagonale Streifenmuster dar|
|[GRAY_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|Stellt das Muster mit 6,25% Grau dar|
|[GRAY_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|Stellt das Muster mit 12,5% Grau dar|
|[GRAY_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|Stellt das Muster mit 25% Grau dar|
|[GRAY_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|Stellt das Muster mit 50% Grau dar|
|[GRAY_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|Stellt das Muster mit 75% Grau dar|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|Stellt das horizontale Streifenmuster dar|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|Stellt keinen Hintergrund dar|
|[REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|Stellt das Muster mit umgekehrtem diagonalem Streifen dar|
|[SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Stellt das einfarbige Muster dar|
|[THICK_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|Stellt das Muster mit dickem diagonalem Kreuzschraffur dar|
|[THIN_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|Stellt das Muster mit dünnem diagonalem Kreuzschraffur dar|
|[THIN_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|Stellt das Muster mit dünnem diagonalem Streifen dar|
|[THIN_HORIZONTAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|Stellt das Muster mit dünnem horizontalen Kreuzschraffur dar|
|[THIN_HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|Stellt dünnen horizontalen Streifenmuster dar|
|[THIN_REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|Stellt dünnen diagonalen Streifenmuster umgekehrt dar|
|[THIN_VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|Stellt dünnen vertikalen Streifenmuster dar|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|Stellt vertikales Streifenmuster dar|
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

Die Klasse [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) bietet die Methode [characters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)), die die folgenden Parameter enthält, um eine Zeichenbereich in einer Zelle auszuwählen:

- **Start-Index**, der Index des Zeichens, von dem aus die Auswahl beginnen soll.
- **Anzahl der Zeichen**: Die Anzahl der ausgewählten Zeichen.

In der Ausgabedatei ist in der Zelle A1 das Wort 'Besuchen' mit der Standardschrift formatiert, aber 'Aspose!' ist fett und blau.

**Auswahl von formatierten Zeichen** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

Wenn Sie daran interessiert sind, [einen Teil von Rich-Text in einer Zelle zu formatieren](/cells/de/java/access-and-update-the-portions-of-rich-text-of-cell/), sollten Sie die Methoden [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) & Cell.setCharacters verwenden. Die Methode [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) wird verwendet, um auf die Textabschnitte zuzugreifen, und anschließend können Änderungen mit der Methode Cell.setCharacters vorgenommen werden, wobei die **get**-Methode ein Array von [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting)-Objekten zurückgibt, die manipuliert werden können, um verschiedene Eigenschaften wie Schriftartname, Schriftfarbe, Fettdruck usw. zu setzen, und die **set**-Methode zum Anwenden der Änderungen verwendet werden kann.

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
