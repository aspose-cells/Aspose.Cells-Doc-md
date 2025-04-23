---
title: Füllungseinstellungen
description: Aspose.Cells ist eine Python Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Es unterstützt das Festlegen der Füll Optionen von Zellen, sodass Benutzer den Hintergrund und Stil der Zellen anpassen können. Dieser Artikel zeigt, wie man die Aspose.Cells für Python via .NET Bibliothek verwendet, um Füll Optionen für Zellen zu setzen.
keywords: Aspose.Cells für Python via .NET, Zellen, Füll Optionen, Hintergrund, Stil
type: docs
weight: 50
url: /de/python-net/cells-fill-settings/
---

## **Farben und Hintergrundmuster**

Microsoft Excel kann die Vordergrund- (Rahmen) und Hintergrundfarben (Fülle) von Zellen sowie Hintergrundmuster festlegen.

Aspose.Cells für Python via .NET unterstützt diese Funktionen ebenfalls flexibel. In diesem Thema lernen wir, diese Funktionen mit Aspose.Cells zu verwenden.

### **Einstellen von Farben und Hintergrundmustern**

Aspose.Cells für Python via .NET stellt eine Klasse bereit, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung stellt ein Objekt der [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-Klasse dar.

Die [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) besitzt die Methoden [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) und [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style), die zum Abrufen und Setzen der Zellformatierung verwendet werden. Die [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-Klasse stellt Eigenschaften zum Festlegen der Vordergrund- und Hintergrundfarben der Zellen bereit. Aspose.Cells für Python via .NET bietet eine [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype)-Aufzählung, die eine Reihe vordefinierter Hintergrundmuster enthält, die unten aufgeführt sind.

|**Hintergrundmuster**|**Beschreibung**|
| :- | :- |
|DIAGONAL_CROSSHATCH|Repräsentiert diagonales Kreuzschraffurmuster|
|DIAGONAL_STRIPE|Repräsentiert diagonales Streifenmuster|
|GRAY6|Repräsentiert Grau-Muster mit 6,25%|
|GRAY12|Repräsentiert Grau-Muster mit 12,5%|
|GRAY25|Repräsentiert Grau-Muster mit 25%|
|GRAY50|Repräsentiert Grau-Muster mit 50%|
|GRAY75|Repräsentiert Grau-Muster mit 75%|
|HORIZONTAL_STRIPE|Repräsentiert horizontales Streifenmuster|
|NONE|Repräsentiert keinen Hintergrund|
|REVERSE_DIAGONAL_STRIPE|Repräsentiert umgekehrtes diagonales Streifenmuster|
|SOLID|Repräsentiert ein einfarbiges Muster|
|DICK_DIAGONAL_SCHACHTPATRON|Stellt dicken diagonalen Schachthintergrundmuster dar|
|DÜNN_DIAGONAL_SCHACHTPATRON|Stellt dünnes diagonales Schachthintergrundmuster dar|
|DÜNN_DIAGONAL_STREIFEN|Stellt dünnes diagonales Streifenmuster dar|
|DÜNN_HORISONTALES_SCHACHTPATRON|Stellt dünnes horizontales Schachthintergrundmuster dar|
|DÜNN_HORISONTALE_STREIFEN|Stellt dünnes horizontales Streifenmuster dar|
|DÜNN_REVERSE_DIAGONAL_STREIFEN|Stellt dünnes umgekehrtes diagonales Streifenmuster dar|
|DÜNN_VERTIKAle_STREIFEN|Stellt dünnes vertikales Streifenmuster dar|
|VERTIKALER_STREIFEN|Stellt vertikalen Streifenmuster dar|

Im folgenden Beispiel ist die Vordergrundfarbe der Zelle A1 festgelegt, aber A2 ist so konfiguriert, dass sowohl Vordergrund- als auch Hintergrundfarben mit einem vertikalen Streifenmuster hinterlegt sind.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndBackground-1.py" >}}

### **Wichtig zu wissen**

{{% alert color="primary" %}}

- Verwenden Sie zum Festlegen der Vordergrund- oder Hintergrundfarbe einer Zelle die Eigenschaften [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) oder [**background_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_color) des Objekts [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Beide Eigenschaften werden nur wirksam, wenn die Eigenschaft [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) des Objekts [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) konfiguriert ist.
- Die Eigenschaft [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) legt die Schattierungsfarbe der Zelle fest.
  Die [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern)-Eigenschaft gibt den Typ des Hintergrundmusters an, das für die Vordergrund- oder Hintergrundfarbe verwendet wird. Aspose.Cells for Python via .NET bietet eine Enumeration, [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype), die eine Reihe vordefinierter Hintergrundmuster enthält.
- Wenn Sie den Wert *BackgroundType.None* aus der Aufzählung [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype) auswählen, wird die Vordergrundfarbe nicht angewendet.
  - Ebenso wird die Hintergrundfarbe nicht angewendet, wenn Sie die Werte *BackgroundType.None* oder *BackgroundType.Solid* auswählen.
- Beim Abrufen der Schattierungs-/Füllfarbe der Zelle gibt [**Style.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) *Color.Empty* zurück, wenn [**Style.pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) *BackgroundType.None* ist.

{{% /alert %}}

### **Anwendung von Verlaufsfülleffekten**

Verwenden Sie zum Anwenden Ihrer gewünschten Verlaufsfülleffekte auf die Zelle die Methode [**set_two_color_gradient**](https://reference.aspose.com/cells/python-net/aspose.cells/style/set_two_color_gradient) des Objekts [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) entsprechend.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyingGradientFillEffects-1.py" >}}

## **Farben und Palette**

Eine Palette ist die Anzahl der verfügbaren Farben zur Erstellung eines Bildes. Die Verwendung einer standardisierten Palette in einer Präsentation ermöglicht es dem Benutzer, ein konsistentes Erscheinungsbild zu erstellen. Jede Microsoft Excel (97-2003)-Datei hat eine Palette von 56 Farben, die auf Zellen, Schriften, Gitterlinien, grafische Objekte, Füllungen und Linien in einem Diagramm angewendet werden können.

Mit Aspose.Cells for Python via .NET ist es möglich, nicht nur die vorhandenen Farben der Palette zu verwenden, sondern auch benutzerdefinierte Farben. Bevor Sie eine benutzerdefinierte Farbe verwenden, fügen Sie diese zuerst zur Palette hinzu.

In diesem Thema wird erläutert, wie benutzerdefinierte Farben zur Palette hinzugefügt werden.

### **Hinzufügen von benutzerdefinierten Farben zur Palette**

Aspose.Cells für Python via .NET unterstützt die 56-Farbpalette von Microsoft Excel. Um eine benutzerdefinierte Farbe zu verwenden, die nicht in der Palette definiert ist, fügen Sie die Farbe zur Palette hinzu.

Aspose.Cells für Python via .NET stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), dar, die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse bietet eine [**change_palette**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/change_palette)-Methode, die die folgenden Parameter akzeptiert, um eine benutzerdefinierte Farbe hinzuzufügen und die Palette zu modifizieren:

- Benutzerdefinierte Farbe, die benutzerdefinierte Farbe, die hinzugefügt werden soll.
- Index, der Index der Farbe in der Palette, die die benutzerdefinierte Farbe ersetzen wird. Sollte zwischen 0-55 liegen.

Das folgende Beispiel fügt eine benutzerdefinierte Farbe (Orchid) zur Palette hinzu, bevor sie auf eine Schriftart angewendet wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndPalette-1.py" >}}

{{% alert color="primary" %}}

Die Palette bietet Platz für nur 56 Farben. Wenn Sie eine benutzerdefinierte Farbe zur Palette hinzufügen, wird die Palette geändert und jedes Element in der Datei, das zuvor mit der Farbe formatiert wurde, wird geändert. Wenn Sie also die Palette ändern, seien Sie bitte sehr vorsichtig. Außerdem handelt es sich hierbei ausschließlich um eine Einschränkung im XLS (Excel 97 - 2003) Dateiformat, da es für XLSX oder andere fortgeschrittene MS Excel (2007/2010 oder 2013) Dateiformate keine solche Einschränkung gibt.

{{% /alert %}}

