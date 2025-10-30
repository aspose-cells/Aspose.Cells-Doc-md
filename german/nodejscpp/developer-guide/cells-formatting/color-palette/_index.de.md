---  
title: So verwenden Sie die Farbpalette
linktitle: So verwenden Sie die Farbpalette  
type: docs  
weight: 80  
url: /de/nodejs-cpp/excel-color-palette/  
description: Node.js Code zum Hinzufügen benutzerdefinierter Farben zur Palette und Verwendung der Excel Farbpalette mit Aspose.Cells for Node.js via C++.  
keywords: node.js benutzerdefinierte Farben zur Palette hinzufügen, node.js Programmatische Verwendung der Excel Farbpalette, wie man programmatisch die Farbpalette im Arbeitsbuch verwendet, node.js Verwendung der Farbpalette in Excel  
---  

## **Farben und Palette**  

Eine Palette ist die Anzahl der verfügbaren Farben zur Erstellung eines Bildes. Die Verwendung einer standardisierten Palette in einer Präsentation ermöglicht es dem Benutzer, ein konsistentes Erscheinungsbild zu erstellen. Jede Microsoft Excel (97-2003)-Datei hat eine Palette von 56 Farben, die auf Zellen, Schriften, Gitterlinien, grafische Objekte, Füllungen und Linien in einem Diagramm angewendet werden können.  

Mit Aspose.Cells for Node.js via C++ ist es möglich, nicht nur die vorhandenen Farben der Palette, sondern auch benutzerdefinierte Farben zu verwenden. Bevor Sie eine benutzerdefinierte Farbe verwenden, fügen Sie diese zuerst der Palette hinzu.  

In diesem Thema wird erläutert, wie benutzerdefinierte Farben zur Palette hinzugefügt werden.  

## **Benutzerdefinierte Farben zur Palette hinzufügen**  

Aspose.Cells unterstützt Microsoft Excels 56-Farben-Palette. Um eine benutzerdefinierte Farbe zu verwenden, die in der Palette nicht definiert ist, fügen Sie die Farbe der Palette hinzu.  

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/)-Klasse bietet eine [**changePalette(Color, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-)-Methode, die die folgenden Parameter übernimmt, um eine benutzerdefinierte Farbe hinzuzufügen und die Palette zu ändern:  

- Benutzerdefinierte Farbe, die benutzerdefinierte Farbe, die hinzugefügt werden soll.  
- Index, der Index der Farbe in der Palette, die die benutzerdefinierte Farbe ersetzen wird. Sollte zwischen 0-55 liegen.  

Das folgende Beispiel fügt eine benutzerdefinierte Farbe (Orchid) zur Palette hinzu, bevor sie auf eine Schriftart angewendet wird.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ColorPalette.js" >}}


{{% alert color="primary" %}}  

Die Palette bietet Platz für nur 56 Farben. Wenn Sie eine benutzerdefinierte Farbe zur Palette hinzufügen, wird die Palette geändert und jedes Element in der Datei, das zuvor mit der Farbe formatiert wurde, wird geändert. Wenn Sie also die Palette ändern, seien Sie bitte sehr vorsichtig. Außerdem handelt es sich hierbei ausschließlich um eine Einschränkung im XLS (Excel 97 - 2003) Dateiformat, da es für XLSX oder andere fortgeschrittene MS Excel (2007/2010 oder 2013) Dateiformate keine solche Einschränkung gibt.  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
