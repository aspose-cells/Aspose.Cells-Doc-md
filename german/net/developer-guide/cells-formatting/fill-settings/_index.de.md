---
title: Fülleinstellungen
description: Aspose.Cells ist eine .NET-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien. Es unterstützt das Festlegen der Fülleinstellungen von Zellen, sodass Benutzer den Hintergrund und den Stil der Zellen anpassen können. In diesem Artikel wird erläutert, wie Sie mit der Bibliothek Aspose.Cells die Einstellungen für die Zellenfüllung festlegen.
keywords: Aspose.Cells, Cells, Fill Settings, Background, Style
type: docs
weight: 50
url: /de/net/cells-fill-settings/
---
##  **Farben und Hintergrundmuster**

Microsoft Excel kann die Vordergrund- (Umriss) und Hintergrundfarbe (Füllung) von Zellen und Hintergrundmustern festlegen.

Aspose.Cells unterstützt diese Funktionen auch auf flexible Weise. In diesem Thema lernen wir, diese Funktionen mit Aspose.Cells zu nutzen.

###  **Festlegen von Farben und Hintergrundmustern**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung. Jedes Element in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Die Sammlung stellt ein Objekt dar[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse.

 Der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) hat die[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) Und[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) Methoden, die zum Abrufen und Festlegen der Formatierung einer Zelle verwendet werden. Der[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Die Klasse stellt Eigenschaften zum Festlegen der Vordergrund- und Hintergrundfarben der Zellen bereit. Aspose.Cells bietet a[**Hintergrundtyp**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)Aufzählung, die eine Reihe vordefinierter Arten von Hintergrundmustern enthält, die unten aufgeführt sind.

|**Hintergrundmuster**|**Beschreibung**|
| :- | :- |
|DiagonaleKreuzschraffur|Stellt ein diagonales Kreuzschraffurmuster dar|
|DiagonalStripe|Stellt ein diagonales Streifenmuster dar|
|Gray6|Stellt 6,25 % Graumuster dar|
|Gray12|Stellt ein Graumuster von 12,5 % dar|
|Gray25|Stellt 25 % Graumuster dar|
|Gray50|Stellt 50 % graues Muster dar|
|Gray75|Stellt 75 % graues Muster dar|
|HorizontalStripe|Stellt ein horizontales Streifenmuster dar|
|Keiner|Stellt keinen Hintergrund dar|
|ReverseDiagonalStripe|Stellt ein umgekehrtes diagonales Streifenmuster dar|
|Solide|Stellt ein durchgehendes Muster dar|
|DickDiagonalKreuzschraffur|Stellt ein dickes diagonales Kreuzschraffurmuster dar|
|ThinDiagonalCrosshatch|Stellt ein dünnes diagonales Kreuzschraffurmuster dar|
|ThinDiagonalStripe|Stellt ein dünnes diagonales Streifenmuster dar|
|DünnHorizontalKreuzschraffur|Stellt ein dünnes horizontales Kreuzschraffurmuster dar|
|ThinHorizontalStripe|Stellt ein dünnes horizontales Streifenmuster dar|
|ThinReverseDiagonalStripe|Stellt ein dünnes umgekehrtes diagonales Streifenmuster dar|
|Dünner vertikaler Streifen|Stellt ein dünnes vertikales Streifenmuster dar|
|VerticalStripe|Stellt ein vertikales Streifenmuster dar|

Im folgenden Beispiel ist die Vordergrundfarbe der Zelle A1 festgelegt, A2 ist jedoch so konfiguriert, dass sie sowohl Vordergrund- als auch Hintergrundfarben mit einem vertikalen Streifenhintergrundmuster hat.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

###  **Wichtig zu wissen**

{{% alert color="primary" %}}

-  Um die Vordergrund- oder Hintergrundfarbe einer Zelle festzulegen, verwenden Sie die[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Vordergrundfarbe**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) oder[**Hintergrundfarbe**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) Eigenschaften. Beide Eigenschaften werden nur wirksam, wenn die[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Muster**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)Eigenschaft ist konfiguriert.
-  Der[**Vordergrundfarbe**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)Die Eigenschaft legt die Schattenfarbe der Zelle fest.
 Der[**Muster**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)Die Eigenschaft gibt den Typ des Hintergrundmusters an, das für die Vordergrund- oder Hintergrundfarbe verwendet wird. Aspose.Cells bietet eine Aufzählung,[**Hintergrundtyp**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype). das eine Reihe vordefinierter Arten von Hintergrundmustern enthält.
-  Wenn Sie auswählen*BackgroundType.None* Wert aus dem[**Hintergrundtyp**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)Bei der Aufzählung wird die Vordergrundfarbe nicht angewendet.
 Ebenso wird die Hintergrundfarbe nicht angewendet, wenn Sie auswählen*BackgroundType.None* oder*BackgroundType.Solid* Werte.
-  Beim Abrufen der Schattierungs-/Füllfarbe der Zelle, wenn[**Stil.Muster**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) ist *BackgroundType.None*,[**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) gibt *Color.Empty* zurück.

{{% /alert %}}

###  **Anwenden von Verlaufsfülleffekten**

 Um die gewünschten Verlaufsfülleffekte auf die Zelle anzuwenden, verwenden Sie die[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)Methode entsprechend anpassen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

##  **Farben und Palette**

Eine Palette ist die Anzahl der Farben, die zum Erstellen eines Bildes zur Verfügung stehen. Die Verwendung einer standardisierten Palette in einer Präsentation ermöglicht es dem Benutzer, ein einheitliches Erscheinungsbild zu schaffen. Jede Microsoft Excel (97-2003)-Datei verfügt über eine Palette von 56 Farben, die auf Zellen, Schriftarten, Gitterlinien, Grafikobjekte, Füllungen und Linien in einem Diagramm angewendet werden können.

Mit Aspose.Cells ist es möglich, nicht nur die vorhandenen Farben der Palette zu verwenden, sondern auch benutzerdefinierte Farben. Bevor Sie eine benutzerdefinierte Farbe verwenden, fügen Sie diese zunächst der Palette hinzu.

In diesem Thema wird erläutert, wie Sie der Palette benutzerdefinierte Farben hinzufügen.

###  **Benutzerdefinierte Farben zur Palette hinzufügen**

Aspose.Cells unterstützt die 56-Farben-Palette von Excel Microsoft. Um eine benutzerdefinierte Farbe zu verwenden, die nicht in der Palette definiert ist, fügen Sie die Farbe der Palette hinzu.

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , das eine Microsoft Excel-Datei darstellt. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse bietet a[**Palette ändern**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) Methode, die die folgenden Parameter verwendet, um eine benutzerdefinierte Farbe hinzuzufügen, um die Palette zu ändern:

- Benutzerdefinierte Farbe: die benutzerdefinierte Farbe, die hinzugefügt werden soll.
- Index, der Index der Farbe in der Palette, die durch die benutzerdefinierte Farbe ersetzt wird. Sollte zwischen 0 und 55 liegen.

Im folgenden Beispiel wird der Palette eine benutzerdefinierte Farbe (Orchidee) hinzugefügt, bevor sie auf eine Schriftart angewendet wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

Die Palette enthält nur 56 Farben. Wenn Sie der Palette eine benutzerdefinierte Farbe hinzufügen, wird die Palette geändert und jedes Element in der Datei, das mit der vorherigen Farbe formatiert ist, wird geändert. Seien Sie daher bitte sehr vorsichtig, wenn Sie die Palette wechseln. Darüber hinaus gilt diese Einschränkung nur für das Dateiformat XLS (Excel 97 – 2003), da es keine solche Einschränkung für XLSX oder andere erweiterte MS Excel-Dateiformate (2007/2010 oder 2013) gibt.

{{% /alert %}}
