---
title: Bedingte Formatierungen von Excel und ODS Dateien mit Golang via C++ festlegen
linktitle: Bedingte Formate
type: docs
weight: 60
url: /de/go-cpp/conditional-formatting/
description: Wie man bedingte Formatierungen in Excel und ODS Dateien in C++ anwendet.
keywords: bedingte Formate anwenden 
---

## **Einführung**

Bedingte Formatierung ist eine erweiterte Funktion von Microsoft Excel, die es ermöglicht, Formate auf eine Zelle oder einen Zellenbereich anzuwenden und diese Formatierung abhängig vom Wert der Zelle oder vom Wert einer Formel zu ändern. Zum Beispiel können Sie eine Zelle fett gedruckt anzeigen lassen, nur wenn der Wert der Zelle größer als 500 ist. Wenn der Wert der Zelle der Bedingung entspricht, wird das angegebene Format auf die Zelle angewendet. Wenn der Wert der Zelle nicht der Formatbedingung entspricht, wird das Standardformat der Zelle verwendet. In Microsoft Excel wählen Sie **Format** und dann **Bedingte Formatierung**, um den Dialog für die bedingte Formatierung zu öffnen.

Aspose.Cells unterstützt die Anwendung von bedingten Formatierungen auf Zellen zur Laufzeit. Dieser Artikel erklärt wie. Er erklärt auch, wie die von Excel für die bedingte Formatierung mit Farbskala verwendete Farbe berechnet wird.

## **Anwendung von bedingten Formaten**

Aspose.Cells unterstützt bedingte Formatierungen auf verschiedene Weise:

- Verwenden der Designer-Tabelle
- Verwenden der Kopiermethode
- Erstellen bedingter Formatierungen zur Laufzeit

### **Verwenden der Designer-Tabelle**

Entwickler können eine Designer-Tabelle erstellen, die bedingte Formatierungen in Microsoft Excel enthält, und dann diese Tabelle mit Aspose.Cells öffnen. Aspose.Cells lädt und speichert die Designer-Tabelle und behält dabei alle bedingten Formatierungseinstellungen bei.

### **Verwenden der Kopiermethode**

Aspose.Cells ermöglicht Entwicklern, bedingte Formatierungseinstellungen von einer Zelle auf eine andere im Arbeitsblatt zu kopieren, indem sie die Methode [**Range.Copy()**](https://reference.aspose.com/cells/go-cpp/range/copy_range_pasteoptions/) aufrufen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConditionalFormatting.go" >}}
## **Bedingte Formatierung zur Laufzeit anwenden**

Mit Aspose.Cells können Sie bedingte Formatierungen zur Laufzeit sowohl hinzufügen als auch entfernen. Die unten stehenden Codebeispiele zeigen, wie bedingte Formatierungen festgelegt werden:

1. Instanziieren Sie ein Arbeitsbuch.
1. Fügen Sie eine leere bedingte Formatierung hinzu.
1. Legen Sie den Bereich fest, auf den die Formatierung angewendet werden soll.
1. Definieren Sie die Formatierungsbedingungen.
1. Speichern Sie die Datei.

Nach diesem Beispiel folgen mehrere kleinere Beispiele, die zeigen, wie Schriftart-Einstellungen, Rand-Einstellungen und Muster angewendet werden.

Microsoft Excel 2007 hat eine erweiterte bedingte Formatierung hinzugefügt, die auch von Aspose.Cells unterstützt wird. Die hier aufgeführten Beispiele zeigen, wie einfache Formatierungen verwendet werden. Die Beispiele für Microsoft Excel 2007 zeigen, wie erweiterte bedingte Formatierungen angewendet werden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConditionalFormatting-1.go" >}}
### **Schriftart festlegen**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConditionalFormatting-2.go" >}}
{{% alert color="primary" %}}

Sie können nur die Schriftart, die Textfarbe, den Unterstrichstil und den Durchstreichstil ändern.

{{% /alert %}}

### **Rahmen festlegen**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConditionalFormatting-3.go" >}}
{{% alert color="primary" %}}

Sie können nur dünnere Linienstile für den äußeren Rahmen verwenden. Diagonale Linien sind nicht erlaubt.

{{% /alert %}}

### **Muster festlegen**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConditionalFormatting-4.go" >}}
## **Erweiterte Themen**
- [Hinzufügen von 2-Farben-Skalen und 3-Farben-Skalen bedingter Formatierungen](/cells/de/cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Erweiterte bedingte Formatierung anwenden](/cells/de/cpp/apply-advanced-conditional-formatting/)
- [Bedingte Formatierung in Arbeitsblättern anwenden](/cells/de/cpp/apply-conditional-formatting-in-worksheets/)
- [Abwechselnde Zeilen und Spalten mit bedingter Formatierung schattieren](/cells/de/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Generieren von Datenleistungsimages für bedingte Formatierungen](/cells/de/cpp/generate-conditional-formatting-databars-images/)
- [Erhalten von Symbolsets, Datenleisten oder Farbskalenobjekten, die bei der bedingten Formatierung verwendet werden](/cells/de/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)
