---  
title: Füllungseinstellungen
linktitle: Füllungseinstellungen  
description: Lernen Sie, wie Sie die Füll Einstellungen, den Hintergrund und den Stil von Zellen mit der Aspose.Cells Bibliothek für Node.js über C++ anpassen.  
keywords: Aspose.Cells, Zellen, Füll Einstellungen, Hintergrund, Stil, Node.js über C++  
type: docs  
weight: 50  
url: /de/nodejs-cpp/cells-fill-settings/  
---  

## **Farben und Hintergrundmuster**  

Microsoft Excel kann die Vordergrund- (Rahmen) und Hintergrundfarben (Fülle) von Zellen sowie Hintergrundmuster festlegen.  

Aspose.Cells unterstützt diese Funktionen ebenfalls in flexibler Weise. In diesem Thema lernen wir, diese Funktionen mit Aspose.Cells zu verwenden.  

### **Einstellen von Farben und Hintergrundmustern**  

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung stellt ein Objekt der [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Klasse dar.  

Die [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) hat die [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) und [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)-Methoden, die zum Abrufen und Festlegen der Formatierung einer Zelle verwendet werden. Die [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Klasse stellt Eigenschaften zum Festlegen der Vordergrund- und Hintergrundfarben der Zellen bereit. Aspose.Cells bietet eine [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype)-Aufzählung, die eine Reihe vordefinierter Hintergrundmuster enthält, wie unten angegeben.  

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

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-SetColorsAndBackgroundPatterns.js" >}}


### **Wichtig zu wissen**  

{{% alert color="primary" %}}  

- Um die Vordergrund- oder Hintergrundfarbe einer Zelle festzulegen, verwenden Sie die Methoden [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) oder [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) des [**setBackgroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundColor-color-)-Objekts. Beide Methoden treten nur in Kraft, wenn die [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Eigenschaft des [**Pattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-)-Objekts konfiguriert ist.  
- Die [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-)-Methode legt die Schattierungsfarbe der Zelle fest.  
  Die [**setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-)-Methode gibt den Typ des Hintergrundmusters an, das für die Vordergrund- oder Hintergrundfarbe verwendet wird. Aspose.Cells bietet eine Aufzählung, [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype), die eine Reihe vordefinierter Hintergrundmustertypen enthält.  
- Wenn Sie den Wert *BackgroundType.None* aus der [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype)-Aufzählung wählen, wird die Vordergrundfarbe nicht angewendet.  
  - Ebenso wird die Hintergrundfarbe nicht angewendet, wenn Sie die Werte *BackgroundType.None* oder *BackgroundType.Solid* auswählen.  
- Beim Abrufen der Schattierungs-/Füllfarbe der Zelle gibt [**Style.getForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#getForegroundColor--) *Color.Empty* zurück, wenn [**Style.setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) *BackgroundType.None* ist.  

{{% /alert %}}  

### **Anwendung von Verlaufsfülleffekten**  

Um Ihre gewünschten Gradientenfüll-Effekte auf die Zelle anzuwenden, verwenden Sie die [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Methode des [**setTwoColorGradient**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTwoColorGradient-color-color-gradientstyletype-number-)-Objekts entsprechend.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-ApplyGradientFillEffects.js" >}}


## **Farben und Palette**  

Eine Palette ist die Anzahl der verfügbaren Farben zur Erstellung eines Bildes. Die Verwendung einer standardisierten Palette in einer Präsentation ermöglicht es dem Benutzer, ein konsistentes Erscheinungsbild zu erstellen. Jede Microsoft Excel (97-2003)-Datei hat eine Palette von 56 Farben, die auf Zellen, Schriften, Gitterlinien, grafische Objekte, Füllungen und Linien in einem Diagramm angewendet werden können.  

Mit Aspose.Cells ist es möglich, nicht nur die vorhandenen Farben der Palette zu verwenden, sondern auch benutzerdefinierte Farben. Bevor Sie eine benutzerdefinierte Farbe verwenden, fügen Sie diese zunächst der Palette hinzu.  

In diesem Thema wird erläutert, wie benutzerdefinierte Farben zur Palette hinzugefügt werden.  

### **Hinzufügen von benutzerdefinierten Farben zur Palette**  

Aspose.Cells unterstützt Microsoft Excels 56-Farben-Palette. Um eine benutzerdefinierte Farbe zu verwenden, die in der Palette nicht definiert ist, fügen Sie die Farbe der Palette hinzu.  

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse bietet eine [**changePalette**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-)-Methode, die die folgenden Parameter übernimmt, um eine benutzerdefinierte Farbe hinzuzufügen und die Palette zu ändern:  

- Benutzerdefinierte Farbe, die benutzerdefinierte Farbe, die hinzugefügt werden soll.  
- Index, der Index der Farbe in der Palette, die die benutzerdefinierte Farbe ersetzen wird. Sollte zwischen 0-55 liegen.  

Das folgende Beispiel fügt eine benutzerdefinierte Farbe (Orchid) zur Palette hinzu, bevor sie auf eine Schriftart angewendet wird.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-AddCustomColorsToPalette.js" >}}


{{% alert color="primary" %}}  

Die Palette bietet Platz für nur 56 Farben. Wenn Sie eine benutzerdefinierte Farbe zur Palette hinzufügen, wird die Palette geändert und jedes Element in der Datei, das zuvor mit der Farbe formatiert wurde, wird geändert. Wenn Sie also die Palette ändern, seien Sie bitte sehr vorsichtig. Außerdem handelt es sich hierbei ausschließlich um eine Einschränkung im XLS (Excel 97 - 2003) Dateiformat, da es für XLSX oder andere fortgeschrittene MS Excel (2007/2010 oder 2013) Dateiformate keine solche Einschränkung gibt.  

{{% /alert %}}  

