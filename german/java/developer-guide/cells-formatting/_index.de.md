---
title: Cells Formate
type: docs
weight: 100
url: /de/java/cells-formatting/
---
## **Grenzen zu Cells hinzufügen**
Microsoft Excel ermöglicht Benutzern das Formatieren von Zellen durch Hinzufügen von Rahmen.

**Rahmeneinstellungen in Microsoft Excel** 

![todo: Bild_alt_Text](cells-formatting_1.png)

Die Art der Umrandung hängt davon ab, wo sie hinzugefügt wird. Ein oberer Rand wird beispielsweise an der obersten Position einer Zelle hinzugefügt. Benutzer können auch den Linienstil und die Farbe der Rahmen ändern.

Mit Aspose.Cells können Entwickler Grenzen hinzufügen und deren Aussehen auf dieselbe flexible Weise anpassen wie in Microsoft Excel.
### **Grenzen zu Cells hinzufügen**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) das stellt eine Microsoft Excel-Datei dar. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse bietet a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Jeder Artikel in der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung stellt ein Objekt der[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)Klasse.

 Aspose.Cells bietet die[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ) Methode in der[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse zum Festlegen des Formatierungsstils einer Zelle. Auch das Objekt der[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-Klasse wird verwendet und stellt Eigenschaften zum Konfigurieren von Schriftarteinstellungen bereit.
#### **Rahmen zu Cell hinzufügen**
 Fügen Sie Rahmen zu einer Zelle mit hinzu[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) Objekt[setRand](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) Methode. Als Parameter wird der Rahmentyp übergeben. Alle Randtypen sind in der vordefiniert[BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType)Aufzählung.

|**Grenztypen**|**Beschreibung**|
|:- |:- |
|[UNTERE GRENZE](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|Die untere Grenzlinie|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|Eine diagonale Linie von links oben nach rechts unten|
|[DIAGONAL_OBEN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|Eine diagonale Linie von links unten nach rechts oben|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|Die linke Grenzlinie|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|Die rechte Grenzlinie|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|Die obere Grenzlinie|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Nur für dynamische Stile wie bedingte Formatierung.|
|[VERTIKAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Nur für dynamische Stile wie bedingte Formatierung.|
 Um die Linienfarbe einzustellen, wählen Sie eine Farbe mit aus[Farbe](https://reference.aspose.com/cells/java/com.aspose.cells/Color) Aufzählung und übergeben Sie es an die[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) Objekt[setRand](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) Color-Parameter der Methode. Die Linienstile sind in der vordefiniert[CellRandType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)Aufzählung.

|**Linienstile**|**Beschreibung**|
|:- |:- |
|[STRICH PUNKT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|Repräsentiert eine dünne strichpunktierte Linie|
|[BINDESTRICH_PUNKT_PUNKT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|Repräsentiert eine dünne Strich-Punkt-Punkt-Linie|
|[GESTRICHELT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Stellt eine gestrichelte Linie dar|
|[GEPUNKTET](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Stellt eine gepunktete Linie dar|
|[DOPPELT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Stellt eine Doppellinie dar|
|[HAAR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Repräsentiert die Haarlinie|
|[MITTEL_BINDESTRICH_PUNKT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|Repräsentiert eine mittlere strichpunktierte Linie|
|[MITTEL_BINDESTRICH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|Repräsentiert eine mittlere Strich-Punkt-Punkt-Linie|
|[MITTEL_GEstrichelt](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|Repräsentiert eine mittlere gestrichelte Linie|
|[KEINER](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Stellt keine Linie dar|
|[MITTEL](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Repräsentiert mittlere Linie|
|[GENEIGT_BINDESTRICH_PUNKT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|Stellt eine schräge mittlere strichpunktierte Linie dar|
|[DICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Stellt eine dicke Linie dar|
|[DÜNN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Stellt dünne Linie dar|
 Wählen Sie einen der obigen Linienstile aus und weisen Sie ihn dann dem zu[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style)Objekt[setRand](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) Methode.

Die folgende Ausgabe wird generiert, wenn der folgende Code ausgeführt wird.

**Auf allen Seiten einer Zelle angewendete Rahmen** 

![todo: Bild_alt_Text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Hinzufügen von Grenzen zu einem Bereich von Cells**
 Es ist möglich, Grenzen zu einem Bereich von Zellen hinzuzufügen, statt nur zu einer einzelnen Zelle. Erstellen Sie zunächst eine Reihe von Zellen, indem Sie die aufrufen[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\))-Methode, die die folgenden Parameter akzeptiert:

- **Erste Reihe**, die erste Zeile des Bereichs.
- **Erste Spalte**, die erste Spalte des Bereichs.
- **Reihenanzahl**, die Anzahl der Zeilen im Bereich.
- **Anzahl der Spalten**, die Anzahl der Spalten im Bereich.

 Das[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\) )-Methode gibt a zurück[Bereich](https://reference.aspose.com/cells/java/com.aspose.cells/Range) Objekt, das den angegebenen Bereich enthält. Das[Bereich](https://reference.aspose.com/cells/java/com.aspose.cells/Range) Objekt bietet a[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\))-Methode, die die folgenden Parameter akzeptiert:

- **CellRandType**, der Rahmenlinienstil, ausgewählt aus der[CellRandType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)Aufzählung.
- **Farbe**, die Rahmenlinienfarbe, ausgewählt aus der[Farbe](https://reference.aspose.com/cells/java/com.aspose.cells/Color)Aufzählung.

Die folgende Ausgabe wird generiert, wenn der folgende Code ausgeführt wird.

**Auf eine Reihe von Zellen angewendete Rahmen** 

![todo: Bild_alt_Text](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **Farben und Palette**
Eine Palette ist die Anzahl der Farben, die zur Verwendung beim Erstellen eines Bildes zur Verfügung stehen. Die Verwendung einer standardisierten Palette in einer Präsentation ermöglicht es dem Benutzer, ein konsistentes Erscheinungsbild zu erstellen. Jede Microsoft Excel (97-2003)-Datei hat eine Palette von 56 Farben, die auf Zellen, Schriftarten, Gitterlinien, Grafikobjekte, Füllungen und Linien in einem Diagramm angewendet werden können.

**Paletteneinstellungen in Microsoft Excel** 

![todo: Bild_alt_Text](cells-formatting_4.png)

Mit Aspose.Cells können nicht nur vorhandene Farben, sondern auch benutzerdefinierte Farben verwendet werden. Bevor Sie eine benutzerdefinierte Farbe verwenden, fügen Sie sie der Palette hinzu. In diesem Thema wird erläutert, wie Sie der Palette benutzerdefinierte Farben hinzufügen.
### **Hinzufügen benutzerdefinierter Farben zur Palette**
Aspose.Cells unterstützt auch eine Palette von 56 Farben. Oben ist eine Standardfarbpalette abgebildet. Wenn Sie eine benutzerdefinierte Farbe verwenden möchten, die nicht in der Palette definiert ist, müssen Sie diese Farbe vor der Verwendung zur Palette hinzufügen.

{{% alert color="primary" %}} 

Die Palette enthält nur 56 Farben. Wenn Sie der Palette eine benutzerdefinierte Farbe hinzufügen, wird die Palette geändert und alle Elemente in der Datei, die mit der vorherigen Farbe formatiert wurden, werden geändert. Seien Sie also bitte sehr vorsichtig, wenn Sie die Palette ändern. Darüber hinaus ist dies nur die Einschränkung im Dateiformat XLS (Excel 97 - 2003), da es keine solche Einschränkung für XLSX oder andere fortgeschrittene Dateiformate von MS Excel (2007/2010) gibt.

{{% /alert %}} 

Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse bietet die[Palette ändern](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\))-Methode, die die folgenden Parameter verwendet, um eine benutzerdefinierte Farbe hinzuzufügen, um die Palette zu ändern:

- **Freiwählbare Farbe**, die benutzerdefinierte Farbe, die der Palette hinzugefügt werden soll.
- **Index**, der Index der Farbe, die durch die benutzerdefinierte Farbe ersetzt wird. Sollte zwischen 0-55 liegen.

Im folgenden Beispiel wird der Palette eine benutzerdefinierte Farbe hinzugefügt, bevor sie auf eine Schriftart angewendet wird.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **Farben und Hintergrundmuster**
Microsoft Excel kann die Vordergrund- (Umriss-) und Hintergrund- (Füll-) Farben von Zellen und Hintergrundmustern wie unten gezeigt festlegen.

**Festlegen von Farben und Hintergrundmustern in Microsoft Excel** 

![todo: Bild_alt_Text](cells-formatting_5.png)

Aspose.Cells unterstützt diese Features ebenfalls flexibel. In diesem Thema lernen wir, diese Funktionen mit Aspose.Cells zu verwenden.
### **Einstellen von Farben und Hintergrundmustern**
Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), die eine Microsoft Excel-Datei darstellt. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)Klasse bietet a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Sammlung. Jeder Artikel in der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Sammlung stellt ein Objekt der[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)Klasse.

Aspose.Cells bietet die[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) Methode in der[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)Klasse, die verwendet wird, um die Formatierung einer Zelle festzulegen. Auch das Objekt der[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-Klasse kann zum Konfigurieren von Schriftarteinstellungen verwendet werden.

{{% alert color="primary" %}} 

 Um die Vorder- oder Hintergrundfarbe einer Zelle festzulegen, verwenden Sie die[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) Objekt[setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) oder[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) Eigenschaften. Diese Eigenschaften kommen nur zum Tragen, wenn die[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) Objekt[Muster setzen](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) Eigenschaft konfiguriert ist.

{{% /alert %}} 

Das[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)-Eigenschaft legt die Schattierungsfarbe der Zelle fest.

Das[Muster setzen](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) -Eigenschaft gibt das Hintergrundmuster an, das für die Vorder- oder Hintergrundfarbe verwendet wird. Aspose.Cells bietet die[Hintergrundtyp](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)Enumeration, die einen Satz vordefinierter Arten von Hintergrundmustern enthält.

|**Muster-Art**|**Beschreibung**|
|:- |:- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|Stellt ein diagonales Schraffurmuster dar|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|Stellt ein diagonales Streifenmuster dar|
|[GRAU_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|Repräsentiert 6,25 % graues Muster|
|[GRAU_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|Repräsentiert 12,5 % graues Muster|
|[GRAU_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|Repräsentiert 25 % graues Muster|
|[GRAU_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|Repräsentiert 50 % graues Muster|
|[GRAU_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|Repräsentiert 75 % graues Muster|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|Repräsentiert ein horizontales Streifenmuster|
|[KEINER](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|Stellt keinen Hintergrund dar|
|[UMKEHREN_DIAGONALE_STREIFEN](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|Stellt umgekehrtes diagonales Streifenmuster dar|
|[FEST](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Stellt ein durchgehendes Muster dar|
|[DICK_DIAGONALE_Kreuzschlitz](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|Stellt ein dickes diagonales Schraffurmuster dar|
|[DÜNN_DIAGONALE_Kreuzschlitz](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|Stellt ein dünnes diagonales Schraffurmuster dar|
|[DÜNN_DIAGONALE_STREIFEN](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|Stellt ein dünnes diagonales Streifenmuster dar|
|[DÜNN_HORIZONTAL_Kreuzschlitz](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|Stellt ein dünnes horizontales Schraffurmuster dar|
|[DÜNN_HORIZONTAL_STREIFEN](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|Repräsentiert ein dünnes horizontales Streifenmuster|
|[DÜNN_UMKEHREN_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|Repräsentiert ein dünnes umgekehrtes diagonales Streifenmuster|
|[DÜNN_VERTIKAL_STREIFEN](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|Stellt ein dünnes vertikales Streifenmuster dar|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|Stellt ein vertikales Streifenmuster dar|
Im Beispiel unten ist die Vordergrundfarbe der A1-Zelle eingestellt, aber A2 ist so konfiguriert, dass sie sowohl Vorder- als auch Hintergrundfarbe mit einem vertikalen Streifenhintergrundmuster hat.

Beim Ausführen des Codes wird die folgende Ausgabe generiert.

**Vorder- und Hintergrundfarben, die auf Zellen mit Hintergrundmustern angewendet werden** 

![todo: Bild_alt_Text](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **Wichtig zu wissen**
{{% alert color="primary" %}} 

-  Um die Vorder- oder Hintergrundfarbe einer Zelle festzulegen, verwenden Sie die[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) Objekt[Vordergrundfarbe](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) oder[Hintergrundfarbe](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) Eigenschaften. Beide Eigenschaften werden nur wirksam, wenn die[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) Objekt[Muster](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) Eigenschaft konfiguriert ist.
-  Das[Vordergrundfarbe](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) -Eigenschaft legt die Schattierungsfarbe der Zelle fest.
 Das[Muster](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) -Eigenschaft gibt den Typ des Hintergrundmusters an, das für die Vorder- oder Hintergrundfarbe verwendet wird. Aspose.Cells liefert eine Aufzählung,[Hintergrundtyp](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)das eine Reihe vordefinierter Arten von Hintergrundmustern enthält.
-  Wenn Sie auswählen[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) Wert aus dem[Hintergrundtyp](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) Aufzählung wird die Vordergrundfarbe nicht angewendet.
 Ebenso wird die Hintergrundfarbe nicht angewendet, wenn Sie die auswählen[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) oder[BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID) Werte.
-  Beim Abrufen der Schattierungs-/Füllfarbe der Zelle, wenn[Stil.Muster](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) ist[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), [Style.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) wird zurückkehren*Farbe.Leer*.

{{% /alert %}} 
## **Ausgewählte Zeichen in Cell formatieren**
[Umgang mit Schrifteinstellungen](/cells/de/java/dealing-with-font-settings/) erklärt, wie Zellen formatiert werden, aber nur, wie der Inhalt der gesamten Zelle formatiert wird. Was ist, wenn Sie nur ausgewählte Zeichen formatieren möchten?

Aspose.Cells unterstützt diese Funktion. In diesem Thema wird die Verwendung dieser Funktion erläutert.
### **Ausgewählte Zeichen formatieren**
Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), die eine Microsoft Excel-Datei darstellt. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)Klasse bietet a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Sammlung. Jeder Artikel in der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Sammlung stellt ein Objekt der[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)Klasse.

Das[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse bietet[Figuren](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\))-Methode, die die folgenden Parameter verwendet, um einen Bereich von Zeichen in einer Zelle auszuwählen:

- **Startindex**, der Index des Zeichens, ab dem die Auswahl beginnen soll.
- **Anzahl von Charakteren**, die Anzahl der auszuwählenden Zeichen.

In der Ausgabedatei ist in der Zelle „A1“ das Wort „Besuch“ mit der Standardschrift formatiert, aber „Aspose!“ ist fett und blau.

**Ausgewählte Zeichen formatieren** 

![todo: Bild_alt_Text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

 Wenn du interessiert bist[Formatieren eines Teils von Rich Text in einer Zelle](/cells/de/java/access-and-update-the-portions-of-rich-text-of-cell/) , erwägen Sie die Verwendung von[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) & Cell.setCharacters-Methoden. Das[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) Methode verwendet werden, um auf die Teile des Textes zuzugreifen, und dann können Änderungen mit der Methode Cell.setCharacters vorgenommen werden, während die**erhalten**-Methode gibt ein Array von zurück[Schrifteinstellung](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) Objekte, die manipuliert werden können, um verschiedene Eigenschaften wie Schriftartname, Schriftfarbe, Fettschrift usw. festzulegen und**einstellen** -Methode verwendet werden, um die Änderungen anzuwenden.

{{% /alert %}}

## **Themen vorantreiben**
- [Ausrichtungseinstellungen](/cells/de/java/cells-alignment-settings/)
- [Bedingte Formatierung](/cells/de/java/conditional-formatting/)
- [Datenformatierung](/cells/de/java/data-formatting/)
- [Excel-Designs und -Farben](/cells/de/java/excel-2007-themes-and-colors/)
- [Umgang mit Schrifteinstellungen](/cells/de/java/dealing-with-font-settings/)
- [Formatieren Sie das Arbeitsblatt Cells in einer Arbeitsmappe](/cells/de/java/format-worksheet-cells-in-a-workbook/)
- [Implementieren Sie das 1904-Datumssystem](/cells/de/java/implement-1904-date-system/)
- [Zusammenführen und Trennen Cells](/cells/de/java/merging-and-unmerging-cells/)
- [Nummerneinstellungen](/cells/de/java/cells-number-settings/)
- [Präfix für einfache Anführungszeichen von Cell Wert oder Bereich beibehalten](/cells/de/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Styling und Datenformatierung](/cells/de/java/styling-and-data-formatting/)
