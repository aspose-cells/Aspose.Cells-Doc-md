---
title: Einstellungen füllen
type: docs
weight: 50
url: /de/net/cells-fill-settings/
---
## **Farben und Hintergrundmuster**

Microsoft Excel kann die Vordergrund- (Umriss-) und Hintergrund- (Füll-) Farben von Zellen und Hintergrundmustern festlegen.

Aspose.Cells unterstützt diese Features ebenfalls flexibel. In diesem Thema lernen wir, diese Funktionen mit Aspose.Cells zu verwenden.

### **Einstellen von Farben und Hintergrundmustern**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung. Jeder Artikel in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung stellt ein Objekt der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse.

 Das[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) hat die[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) und[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) Methoden, die zum Abrufen und Festlegen der Formatierung einer Zelle verwendet werden. Das[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)-Klasse bietet Eigenschaften zum Festlegen der Vorder- und Hintergrundfarbe der Zellen. Aspose.Cells bietet eine[**Hintergrundtyp**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)Aufzählung, die einen Satz vordefinierter Arten von Hintergrundmustern enthält, die unten angegeben sind.

|**Hintergrundmuster**|**Beschreibung**|
|:- |:- |
|Diagonale Kreuzschraffur|Stellt ein diagonales Schraffurmuster dar|
|DiagonalStreifen|Stellt ein diagonales Streifenmuster dar|
|Grau6|Repräsentiert 6,25 % graues Muster|
|Grau12|Repräsentiert 12,5 % graues Muster|
|Grau25|Repräsentiert 25 % graues Muster|
|Grau50|Repräsentiert 50 % graues Muster|
|Grau75|Repräsentiert 75 % graues Muster|
|HorizontalStripe|Repräsentiert ein horizontales Streifenmuster|
|Keiner|Stellt keinen Hintergrund dar|
|ReverseDiagonalStripe|Stellt umgekehrtes diagonales Streifenmuster dar|
|Solide|Stellt ein durchgehendes Muster dar|
|Dicke Diagonale Kreuzschraffur|Stellt ein dickes diagonales Schraffurmuster dar|
|ThinDiagonalCrosshatch|Stellt ein dünnes diagonales Schraffurmuster dar|
|ThinDiagonalStripe|Stellt ein dünnes diagonales Streifenmuster dar|
|ThinHorizontalCrosshatch|Stellt ein dünnes horizontales Schraffurmuster dar|
|ThinHorizontalStripe|Repräsentiert ein dünnes horizontales Streifenmuster|
|ThinReverseDiagonalStripe|Repräsentiert ein dünnes umgekehrtes diagonales Streifenmuster|
|ThinVerticalStripe|Stellt ein dünnes vertikales Streifenmuster dar|
|VerticalStripe|Stellt ein vertikales Streifenmuster dar|

Im Beispiel unten ist die Vordergrundfarbe der A1-Zelle eingestellt, aber A2 ist so konfiguriert, dass sie sowohl Vorder- als auch Hintergrundfarbe mit einem vertikalen Streifenhintergrundmuster hat.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **Wichtig zu wissen**

{{% alert color="primary" %}}

-  Um die Vorder- oder Hintergrundfarbe einer Zelle festzulegen, verwenden Sie die[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Vordergrundfarbe**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) oder[**Hintergrundfarbe**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) Eigenschaften. Beide Eigenschaften werden nur wirksam, wenn die[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Muster**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)Eigenschaft konfiguriert ist.
-  Das[**Vordergrundfarbe**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)-Eigenschaft legt die Schattierungsfarbe der Zelle fest.
 Das[**Muster**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)-Eigenschaft gibt den Typ des Hintergrundmusters an, das für die Vorder- oder Hintergrundfarbe verwendet wird. Aspose.Cells liefert eine Aufzählung,[**Hintergrundtyp**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)das eine Reihe vordefinierter Arten von Hintergrundmustern enthält.
-  Wenn Sie auswählen*BackgroundType.None* Wert aus dem[**Hintergrundtyp**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)Aufzählung wird die Vordergrundfarbe nicht angewendet.
 Ebenso wird die Hintergrundfarbe nicht angewendet, wenn Sie die auswählen*BackgroundType.None* oder*BackgroundType.Solid* Werte.
-  Beim Abrufen der Schattierungs-/Füllfarbe der Zelle, wenn[**Stil.Muster**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) ist*BackgroundType.None*, [**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) wird zurückkehren*Farbe.Leer*.

{{% /alert %}}

### **Anwenden von Verlaufsfülleffekten**

 Um die gewünschten Verlaufsfülleffekte auf die Zelle anzuwenden, verwenden Sie die[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)Methode entsprechend.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

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

Die Palette enthält nur 56 Farben. Wenn Sie der Palette eine benutzerdefinierte Farbe hinzufügen, wird die Palette geändert und alle Elemente in der Datei, die mit der vorherigen Farbe formatiert wurden, werden geändert. Seien Sie also bitte sehr vorsichtig, wenn Sie die Palette ändern. Darüber hinaus ist dies nur die Einschränkung im Dateiformat XLS (Excel 97 - 2003), da es keine solche Einschränkung für XLSX oder andere erweiterte MS Excel-Dateiformate (2007/2010 oder 2013) gibt.

{{% /alert %}}
