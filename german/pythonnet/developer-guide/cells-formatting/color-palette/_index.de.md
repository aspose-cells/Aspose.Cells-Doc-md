---
title: So verwenden Sie die Farbpalette
type: docs
weight: 80
url: /de/python-net/excel-color-palette/
description: Python Code zum Hinzufügen benutzerdefinierter Farben zur Palette und Verwendung der Excel Farbpalette mit Aspose.Cells für Python via .NET API
keywords: Python benutzerdefinierte Farben zur Palette hinzufügen, Python Programm zur Verwendung der Excel Farbpalette, Programmatisch, wie man die Farbpalette im Arbeitsbuch verwendet, Python, Verwendung der Farbpalette in Excel
---

## **Farben und Palette**

Eine Palette ist die Anzahl der verfügbaren Farben zur Erstellung eines Bildes. Die Verwendung einer standardisierten Palette in einer Präsentation ermöglicht es dem Benutzer, ein konsistentes Erscheinungsbild zu erstellen. Jede Microsoft Excel (97-2003)-Datei hat eine Palette von 56 Farben, die auf Zellen, Schriften, Gitterlinien, grafische Objekte, Füllungen und Linien in einem Diagramm angewendet werden können.

Mit Aspose.Cells for Python via .NET ist es möglich, nicht nur die vorhandenen Farben der Palette zu verwenden, sondern auch benutzerdefinierte Farben. Bevor Sie eine benutzerdefinierte Farbe verwenden, fügen Sie diese zuerst zur Palette hinzu.

In diesem Thema wird erläutert, wie benutzerdefinierte Farben zur Palette hinzugefügt werden.

## **Benutzerdefinierte Farben zur Palette hinzufügen**

Aspose.Cells für Python via .NET unterstützt die 56-Farbpalette von Microsoft Excel. Um eine benutzerdefinierte Farbe zu verwenden, die nicht in der Palette definiert ist, fügen Sie die Farbe zur Palette hinzu.

Aspose.Cells für Python via .NET stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), dar, die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse bietet eine [**change_palette**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/change_palette)-Methode, die die folgenden Parameter akzeptiert, um eine benutzerdefinierte Farbe hinzuzufügen und die Palette zu modifizieren:

- Benutzerdefinierte Farbe, die benutzerdefinierte Farbe, die hinzugefügt werden soll.
- Index, der Index der Farbe in der Palette, die die benutzerdefinierte Farbe ersetzen wird. Sollte zwischen 0-55 liegen.

Das folgende Beispiel fügt eine benutzerdefinierte Farbe (Orchid) zur Palette hinzu, bevor sie auf eine Schriftart angewendet wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndPalette-1.py" >}}

{{% alert color="primary" %}}

Die Palette bietet Platz für nur 56 Farben. Wenn Sie eine benutzerdefinierte Farbe zur Palette hinzufügen, wird die Palette geändert und jedes Element in der Datei, das zuvor mit der Farbe formatiert wurde, wird geändert. Wenn Sie also die Palette ändern, seien Sie bitte sehr vorsichtig. Außerdem handelt es sich hierbei ausschließlich um eine Einschränkung im XLS (Excel 97 - 2003) Dateiformat, da es für XLSX oder andere fortgeschrittene MS Excel (2007/2010 oder 2013) Dateiformate keine solche Einschränkung gibt.

{{% /alert %}}

