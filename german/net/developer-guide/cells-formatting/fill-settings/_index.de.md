---
title: Füllungseinstellungen
description: Aspose.Cells ist eine .NET Bibliothek zum Arbeiten mit Tabellendateien. Sie unterstützt das Festlegen von Fülleinstellungen für Zellen, wodurch Benutzer den Hintergrund und den Stil von Zellen anpassen können. Dieser Artikel führt ein, wie die Aspose.Cells Bibliothek verwendet werden kann, um Fülleinstellungen für Zellen festzulegen.
keywords: Aspose.Cells, Zellen, Fülleinstellungen, Hintergrund, Stil
type: docs
weight: 50
url: /de/net/cells-fill-settings/
---

## **Farben und Hintergrundmuster**

Microsoft Excel kann die Vordergrund- (Rahmen) und Hintergrundfarben (Fülle) von Zellen sowie Hintergrundmuster festlegen.

Aspose.Cells unterstützt diese Funktionen ebenfalls in flexibler Weise. In diesem Thema lernen wir, diese Funktionen mit Aspose.Cells zu verwenden.

### **Einstellen von Farben und Hintergrundmustern**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung repräsentiert ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Die Klasse [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) verfügt über die Methoden [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) und [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index), die zur Abfrage und Änderung der Formatierung einer Zelle verwendet werden. Die Klasse [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) stellt Eigenschaften zur Festlegung der Vordergrund- und Hintergrundfarben der Zellen bereit. Aspose.Cells bietet eine Enumeration [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype), die eine Reihe von vordefinierten Arten von Hintergrundmustern enthält, die unten aufgeführt sind.

|**Hintergrundmuster**|**Beschreibung**|
| :- | :- |
|DiagonalCrosshatch|: Stellt das diagonale Kreuzmuster dar
|DiagonalStripe|: Stellt das diagonale Streifenmuster dar
|Gray6|: Stellt das 6,25%-graue Muster dar
|Gray12|: Stellt das 12,5%-graue Muster dar
|Gray25|: Stellt das 25%-graue Muster dar
|Gray50|: Stellt das 50%-graue Muster dar
|Gray75|: Stellt das 75%-graue Muster dar
|HorizontalStripe|: Stellt das horizontale Streifenmuster dar
|None|: Stellt keinen Hintergrund dar
|ReverseDiagonalStripe|: Stellt das umgekehrte diagonale Streifenmuster dar
|Solid|: Stellt das einfarbige Muster dar
|ThickDiagonalCrosshatch|: Stellt das dicke diagonale Kreuzmuster dar
|ThinDiagonalCrosshatch|: Stellt das dünnere diagonale Kreuzmuster dar
|ThinDiagonalStripe|: Stellt das dünnere diagonale Streifenmuster dar
|ThinHorizontalCrosshatch|: Stellt das dünnere horizontale Kreuzmuster dar
|ThinHorizontalStripe|: Stellt das dünnere horizontale Streifenmuster dar
|ThinReverseDiagonalStripe|Stellt ein dünn umgekehrtes diagonales Streifenmuster dar|
|ThinVerticalStripe|Stellt ein dünn vertikales Streifenmuster dar|
|VerticalStripe|Stellt ein vertikales Streifenmuster dar|

Im folgenden Beispiel ist die Vordergrundfarbe der Zelle A1 festgelegt, aber A2 ist so konfiguriert, dass sowohl Vordergrund- als auch Hintergrundfarben mit einem vertikalen Streifenmuster hinterlegt sind.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **Wichtig zu wissen**

{{% alert color="primary" %}}

- Verwenden Sie zum Festlegen der Vordergrund- oder Hintergrundfarbe einer Zelle die Eigenschaften [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) oder [**BackgroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) des Objekts [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Beide Eigenschaften werden nur wirksam, wenn die Eigenschaft [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) des Objekts [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) konfiguriert ist.
- Die Eigenschaft [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) legt die Schattierungsfarbe der Zelle fest.
  Die Eigenschaft [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) legt den Typ des Hintergrundmusters fest, das für die Vordergrund- oder Hintergrundfarbe verwendet wird. Aspose.Cells bietet eine Aufzählung, [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype), die eine Reihe von vordefinierten Arten von Hintergrundmustern enthält.
- Wenn Sie den Wert *BackgroundType.None* aus der Aufzählung [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) auswählen, wird die Vordergrundfarbe nicht angewendet.
  - Ebenso wird die Hintergrundfarbe nicht angewendet, wenn Sie die Werte *BackgroundType.None* oder *BackgroundType.Solid* auswählen.
- Beim Abrufen der Schattierungs-/Füllfarbe der Zelle gibt [**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) *Color.Empty* zurück, wenn [**Style.Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) *BackgroundType.None* ist.

{{% /alert %}}

### **Anwendung von Verlaufsfülleffekten**

Verwenden Sie zum Anwenden Ihrer gewünschten Verlaufsfülleffekte auf die Zelle die Methode [**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient) des Objekts [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) entsprechend.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **Farben und Palette**

Eine Palette ist die Anzahl der verfügbaren Farben zur Erstellung eines Bildes. Die Verwendung einer standardisierten Palette in einer Präsentation ermöglicht es dem Benutzer, ein konsistentes Erscheinungsbild zu erstellen. Jede Microsoft Excel (97-2003)-Datei hat eine Palette von 56 Farben, die auf Zellen, Schriften, Gitterlinien, grafische Objekte, Füllungen und Linien in einem Diagramm angewendet werden können.

Mit Aspose.Cells ist es möglich, nicht nur die vorhandenen Farben der Palette zu verwenden, sondern auch benutzerdefinierte Farben. Bevor Sie eine benutzerdefinierte Farbe verwenden, fügen Sie diese zunächst der Palette hinzu.

In diesem Thema wird erläutert, wie benutzerdefinierte Farben zur Palette hinzugefügt werden.

### **Hinzufügen von benutzerdefinierten Farben zur Palette**

Aspose.Cells unterstützt Microsoft Excels 56-Farben-Palette. Um eine benutzerdefinierte Farbe zu verwenden, die in der Palette nicht definiert ist, fügen Sie die Farbe der Palette hinzu.

Aspose.Cells stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bietet eine Methode [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette), die die folgenden Parameter verwendet, um eine benutzerdefinierte Farbe zur Modifizierung der Palette hinzuzufügen:

- Benutzerdefinierte Farbe, die benutzerdefinierte Farbe, die hinzugefügt werden soll.
- Index, der Index der Farbe in der Palette, die die benutzerdefinierte Farbe ersetzen wird. Sollte zwischen 0-55 liegen.

Das folgende Beispiel fügt eine benutzerdefinierte Farbe (Orchid) zur Palette hinzu, bevor sie auf eine Schriftart angewendet wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

Die Palette bietet Platz für nur 56 Farben. Wenn Sie eine benutzerdefinierte Farbe zur Palette hinzufügen, wird die Palette geändert und jedes Element in der Datei, das zuvor mit der Farbe formatiert wurde, wird geändert. Wenn Sie also die Palette ändern, seien Sie bitte sehr vorsichtig. Außerdem handelt es sich hierbei ausschließlich um eine Einschränkung im XLS (Excel 97 - 2003) Dateiformat, da es für XLSX oder andere fortgeschrittene MS Excel (2007/2010 oder 2013) Dateiformate keine solche Einschränkung gibt.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
