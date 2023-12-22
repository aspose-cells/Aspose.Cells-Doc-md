---
title: So verwenden Sie die Farbpalette
type: docs
weight: 80
url: /de/net/excel-color-palette/
description: C#-Code zum Hinzufügen benutzerdefinierter Farben zur Palette und zur Verwendung der Excel-Farbpalette mit Aspose.Cells for .NET API
keywords: c# add custom colors to the palette, c# programmatically excel color palette, programmatically how to use color palette in workbook, c# how to use color palette in excel
---
##  **Farben und Palette**

Eine Palette ist die Anzahl der Farben, die zum Erstellen eines Bildes zur Verfügung stehen. Die Verwendung einer standardisierten Palette in einer Präsentation ermöglicht es dem Benutzer, ein einheitliches Erscheinungsbild zu schaffen. Jede Microsoft Excel (97-2003)-Datei verfügt über eine Palette von 56 Farben, die auf Zellen, Schriftarten, Gitterlinien, Grafikobjekte, Füllungen und Linien in einem Diagramm angewendet werden können.

Mit Aspose.Cells ist es möglich, nicht nur die vorhandenen Farben der Palette zu verwenden, sondern auch benutzerdefinierte Farben. Bevor Sie eine benutzerdefinierte Farbe verwenden, fügen Sie diese zunächst der Palette hinzu.

In diesem Thema wird erläutert, wie Sie der Palette benutzerdefinierte Farben hinzufügen.

##  **Fügen Sie der Palette benutzerdefinierte Farben hinzu**

Aspose.Cells unterstützt die 56-Farben-Palette von Excel Microsoft. Um eine benutzerdefinierte Farbe zu verwenden, die nicht in der Palette definiert ist, fügen Sie die Farbe der Palette hinzu.

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , das eine Microsoft Excel-Datei darstellt. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse bietet a[**Palette ändern**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) Methode, die die folgenden Parameter verwendet, um eine benutzerdefinierte Farbe hinzuzufügen, um die Palette zu ändern:

- Benutzerdefinierte Farbe: die benutzerdefinierte Farbe, die hinzugefügt werden soll.
- Index, der Index der Farbe in der Palette, die durch die benutzerdefinierte Farbe ersetzt wird. Sollte zwischen 0 und 55 liegen.

Im folgenden Beispiel wird der Palette eine benutzerdefinierte Farbe (Orchidee) hinzugefügt, bevor sie auf eine Schriftart angewendet wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

Die Palette enthält nur 56 Farben. Wenn Sie der Palette eine benutzerdefinierte Farbe hinzufügen, wird die Palette geändert und jedes Element in der Datei, das mit der vorherigen Farbe formatiert ist, wird geändert. Seien Sie daher bitte sehr vorsichtig, wenn Sie die Palette wechseln. Darüber hinaus gilt diese Einschränkung nur für das Dateiformat XLS (Excel 97 – 2003), da es keine solche Einschränkung für XLSX oder andere erweiterte MS Excel-Dateiformate (2007/2010 oder 2013) gibt.

{{% /alert %}}