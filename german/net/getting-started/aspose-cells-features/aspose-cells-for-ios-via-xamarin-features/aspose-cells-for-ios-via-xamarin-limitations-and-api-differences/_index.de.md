---
title: Aspose.Cells für iOS über Xamarin Einschränkungen und API Unterschiede
type: docs
weight: 10
url: /de/net/aspose-cells-for-ios-via-xamarin-limitations-and-api-differences/
---
## Die neueste Version von Aspose.Cells für iOS über Xamarin funktioniert möglicherweise nicht mit der alten Xamarin.iOS-Version
Bitte beachten Sie, dass Aspose.Cells für iOS über Xamarin immer unter Verwendung der neuesten stabilen Versionen von Xamarin- und Xamarin.iOS-Plattformen erstellt wird. Wenn bei der Verwendung von Aspose.Cells für iOS über Xamarin in Ihrer Xamarin.Android-Anwendung Probleme auftreten, stellen Sie bitte sicher, dass Sie die neuesten Xamarin- und Xamarin.iOS-Versionen installiert haben. Manchmal wird Aspose.Cells für iOS über Xamarin mithilfe der neuesten Version von Xamarin (Xamarin.iOS) erstellt, die nicht mit älteren Versionen von Xamarin funktioniert.
## Aspose.Cells für iOS über Xamarin-Einschränkungen
- Einfügen von Bildern - Nicht unterstützt.
- Erstellen von Diagrammen – Nicht unterstützt.
- Hintergrund mit Farbverlauf einstellen - Nicht unterstützt.
- Hinzufügen von Kommentaren zu Zellen – Nicht unterstützt.
- Implementieren von Datenvalidierungen – Nicht unterstützt.
- Erstellen von benutzerdefinierten Seitenumbrüchen – Nicht unterstützt.
- Implementieren von intelligenten Markierungen – nicht unterstützt.
- Arbeitsblätter schützen/entschützen – Nicht unterstützt.
- Festlegen erweiterter Schutzoptionen, die in Excel XP und späteren Versionen eingeführt wurden – nicht unterstützt.
- Einfügen von Formularsteuerelementen und anderen Zeichnungsformen/-objekten – Nicht unterstützt.
- Erstellen von Pivot-Tabellen und Pivot-Diagrammen – Nicht unterstützt.
- Beibehalten oder Entfernen eines Add-Ins, VBA, Makros – Nicht unterstützt.
- Implementieren von Transpositionsoptionen – Nicht unterstützt.
- Erstellen benutzerdefinierter Diagramme – Nicht unterstützt.
- Hinzufügen, Beibehalten oder Extrahieren von OLE-Objekten aus den Tabellenkalkulationen – Nicht unterstützt.
- Implementieren von Microsoft Excel 2010-Sparklines – nicht unterstützt.
- Dateien verschlüsseln – Nicht unterstützt.
## Öffentliche API (Namespace) Unterschiede
In Aspose.Cells für iOS über Xamarin wird der Namespace Aspose.Cells.Drawing anstelle von System.Drawing in .NET API verwendet. Die Liste der betroffenen Objekte lautet wie folgt:

- Aspose.Cells.Drawing.Color
- Aspose.Cells.Drawing.ColorConverter
- Aspose.Cells.Drawing.ColorTranslator
- Aspose.Cells.Drawing.FontStyle
- Aspose.Cells.Drawing.GraphicsUnit
- Aspose.Cells.Drawing.ImageFormatConverter
- Aspose.Cells.Drawing.KnownColor
- Aspose.Cells.Drawing.KnownColors
- Aspose.Cells.Drawing.Locale
- Aspose.Cells.Drawing.SystemColors
- Aspose.Cells.Drawing.Imaging.PixelFormat
- Aspose.Cells.Drawing.Imaging.ImageFormat
- Aspose.Cells.Drawing.Imaging.ImageFlags
- Aspose.Cells.Drawing.Drawing2D.SmoothingMode
- Aspose.Cells.Drawing.Drawing2D.PathPointType
- Aspose.Cells.Drawing.Drawing2D.PathData
- Aspose.Cells.Drawing.Drawing2D


