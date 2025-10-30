---
title: Setzen Sie bedingte Formate in Excel und ODS Dateien.
linktitle: Bedingte Formate
type: docs
weight: 60
url: /de/python-net/conditional-formatting/
description: So wenden Sie bedingte Formatierungen in Excel und ODS Dateien in Python an.
keywords: bedingte Formate anwenden 
---

## **Einführung**

Bedingte Formatierung ist eine erweiterte Funktion von Microsoft Excel, die es ermöglicht, Formate auf eine Zelle oder einen Zellenbereich anzuwenden und diese Formatierung abhängig vom Wert der Zelle oder vom Wert einer Formel zu ändern. Zum Beispiel können Sie eine Zelle fett gedruckt anzeigen lassen, nur wenn der Wert der Zelle größer als 500 ist. Wenn der Wert der Zelle der Bedingung entspricht, wird das angegebene Format auf die Zelle angewendet. Wenn der Wert der Zelle nicht der Formatbedingung entspricht, wird das Standardformat der Zelle verwendet. In Microsoft Excel wählen Sie **Format** und dann **Bedingte Formatierung**, um den Dialog für die bedingte Formatierung zu öffnen.

Aspose.Cells für Python via .NET unterstützt die Anwendung bedingter Formatierungen zur Laufzeit. Dieser Artikel erklärt, wie das funktioniert. Er erklärt auch, wie die von Excel verwendete Farbe für Farbskalen-Bedingungsformatierungen berechnet wird.

## **Anwendung von bedingten Formaten**

Aspose.Cells für Python via .NET unterstützt bedingte Formatierungen auf verschiedene Weisen:

- Verwenden der Designer-Tabelle
- Verwenden der Kopiermethode
- Erstellen bedingter Formatierungen zur Laufzeit

### **Verwenden der Designer-Tabelle**

Entwickler können eine Designer-Tabelle erstellen, die bedingte Formatierungen in Microsoft Excel enthält, und diese Tabelle dann mit Aspose.Cells für Python via .NET öffnen. Aspose.Cells für Python via .NET lädt und speichert die Designer-Tabelle und bewahrt alle Einstellungen der bedingten Formatierung.

### **Verwenden der Kopiermethode**

Aspose.Cells für Python via .NET ermöglicht es Entwicklern, bedingte Formatierungen von einer Zelle auf eine andere in der Arbeitsmappe zu kopieren, indem die [**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy)-Methode aufgerufen wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCopyMethod-1.py" >}}

## **Bedingte Formatierung zur Laufzeit anwenden**

Aspose.Cells für Python via .NET erlaubt das Hinzufügen und Entfernen von bedingten Formatierungen zur Laufzeit. Die nachfolgenden Code-Beispiele zeigen, wie man bedingte Formatierungen festlegt:

1. Instanziieren Sie ein Arbeitsbuch.
1. Fügen Sie eine leere bedingte Formatierung hinzu.
1. Legen Sie den Bereich fest, auf den die Formatierung angewendet werden soll.
1. Definieren Sie die Formatierungsbedingungen.
1. Speichern Sie die Datei.

Nach diesem Beispiel folgen mehrere kleinere Beispiele, die zeigen, wie Schriftart-Einstellungen, Rand-Einstellungen und Muster angewendet werden.

Microsoft Excel 2007 führte fortschrittlichere bedingte Formatierungen ein, die ebenfalls von Aspose.Cells für Python via .NET unterstützt werden. Die Beispiele hier demonstrieren die Verwendung einfacher Formatierungen, während die Microsoft Excel 2007-Beispiele zeigen, wie man komplexere bedingte Formatierungen anwendet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConditionalFormattingatRuntime-1.py" >}}

### **Schriftart festlegen**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontStyle-1.py" >}}

{{% alert color="primary" %}}

Sie können nur die Schriftart, die Textfarbe, den Unterstrichstil und den Durchstreichstil ändern.

{{% /alert %}}

### **Rahmen festlegen**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetBorder-1.py" >}}

{{% alert color="primary" %}}

Sie können nur dünnere Linienstile für den äußeren Rahmen verwenden. Diagonale Linien sind nicht erlaubt.

{{% /alert %}}

### **Muster festlegen**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetPattern-1.py" >}}

## **Erweiterte Themen**
- [Hinzufügen von 2-Farben-Skalen und 3-Farben-Skalen bedingter Formatierungen](/cells/de/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Bedingte Formatierung in Arbeitsblättern anwenden](/cells/de/python-net/apply-conditional-formatting-in-worksheets/)
- [Abwechselnde Zeilen und Spalten mit bedingter Formatierung schattieren](/cells/de/python-net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Generieren von Datenleistungsimages für bedingte Formatierungen](/cells/de/python-net/generate-conditional-formatting-databars-images/)
- [Erhalten von Symbolsets, Datenleisten oder Farbskalenobjekten, die bei der bedingten Formatierung verwendet werden](/cells/de/python-net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

{{< app/cells/assistant language="csharp" >}}
{{< app/cells/assistant language="python-net" >}}
