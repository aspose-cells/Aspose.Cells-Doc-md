---
title: So verwenden Sie die Farbpalette
type: docs
weight: 80
url: /de/net/excel-color-palette/
description: C# Code zum Hinzufügen benutzerdefinierter Farben zur Palette und zur Verwendung der Excel Farbpalette mit der Aspose.Cells for .NET API
keywords: C# benutzerdefinierte Farben zur Palette hinzufügen, C# programmgesteuert Excel Farbpalette, programmgesteuert Verwendung der Farbpalette in der Arbeitsmappe, C# Verwendung der Farbpalette in Excel
---

## **Farben und Palette**

Eine Palette ist die Anzahl der verfügbaren Farben zur Erstellung eines Bildes. Die Verwendung einer standardisierten Palette in einer Präsentation ermöglicht es dem Benutzer, ein konsistentes Erscheinungsbild zu erstellen. Jede Microsoft Excel (97-2003)-Datei hat eine Palette von 56 Farben, die auf Zellen, Schriften, Gitterlinien, grafische Objekte, Füllungen und Linien in einem Diagramm angewendet werden können.

Mit Aspose.Cells ist es möglich, nicht nur die vorhandenen Farben der Palette zu verwenden, sondern auch benutzerdefinierte Farben. Bevor Sie eine benutzerdefinierte Farbe verwenden, fügen Sie diese zunächst der Palette hinzu.

In diesem Thema wird erläutert, wie benutzerdefinierte Farben zur Palette hinzugefügt werden.

## **Benutzerdefinierte Farben zur Palette hinzufügen**

Aspose.Cells unterstützt Microsoft Excels 56-Farben-Palette. Um eine benutzerdefinierte Farbe zu verwenden, die in der Palette nicht definiert ist, fügen Sie die Farbe der Palette hinzu.

Aspose.Cells stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bietet eine Methode [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette), die die folgenden Parameter verwendet, um eine benutzerdefinierte Farbe zur Modifizierung der Palette hinzuzufügen:

- Benutzerdefinierte Farbe, die benutzerdefinierte Farbe, die hinzugefügt werden soll.
- Index, der Index der Farbe in der Palette, die die benutzerdefinierte Farbe ersetzen wird. Sollte zwischen 0-55 liegen.

Das folgende Beispiel fügt eine benutzerdefinierte Farbe (Orchid) zur Palette hinzu, bevor sie auf eine Schriftart angewendet wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

Die Palette bietet Platz für nur 56 Farben. Wenn Sie eine benutzerdefinierte Farbe zur Palette hinzufügen, wird die Palette geändert und jedes Element in der Datei, das zuvor mit der Farbe formatiert wurde, wird geändert. Wenn Sie also die Palette ändern, seien Sie bitte sehr vorsichtig. Außerdem handelt es sich hierbei ausschließlich um eine Einschränkung im XLS (Excel 97 - 2003) Dateiformat, da es für XLSX oder andere fortgeschrittene MS Excel (2007/2010 oder 2013) Dateiformate keine solche Einschränkung gibt.

{{% /alert %}}
