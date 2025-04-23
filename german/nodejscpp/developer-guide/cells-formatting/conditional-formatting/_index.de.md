---  
title: Setzen von bedingten Formatierungen für Excel und ODS Dateien
linktitle: Bedingte Formate  
type: docs  
weight: 60  
url: /de/nodejs-cpp/conditional-formatting/  
description: So wenden Sie bedingte Formatierungen in Excel und ODS Dateien in Node.js via C++ an.  
keywords: Anwenden bedingter Formatierungen Node.js via C++  
---  

## **Einführung**

Bedingte Formatierung ist eine erweiterte Funktion, die es ermöglicht, Formate auf eine Zelle oder einen Zellbereich anzuwenden und diese Formatierung je nach Wert der Zelle oder einer Formel zu ändern. Zum Beispiel kann eine Zelle nur fett erscheinen, wenn der Wert der Zelle größer als 500 ist. Wenn der Wert der Zelle die Bedingung erfüllt, wird das angegebene Format auf die Zelle angewendet. Wenn die Bedingung nicht erfüllt ist, nutzt die Zelle die Standardformatierung. In Microsoft Excel wählen Sie **Format**, dann **Bedingte Formatierung**, um den Dialog für bedingte Formatierungen zu öffnen.

Aspose.Cells unterstützt die Anwendung von bedingten Formatierungen auf Zellen zur Laufzeit. Dieser Artikel erklärt wie. Er erklärt auch, wie die von Excel für die bedingte Formatierung mit Farbskala verwendete Farbe berechnet wird.

## **Anwendung von bedingten Formaten**

Aspose.Cells unterstützt bedingte Formatierungen auf verschiedene Weise:

- Verwenden der Designer-Tabelle
- Verwenden der Kopiermethode
- Erstellen bedingter Formatierungen zur Laufzeit

### **Verwenden der Designer-Tabelle**

Entwickler können eine Designer-Tabelle erstellen, die bedingte Formatierungen in Microsoft Excel enthält, und dann diese Tabelle mit Aspose.Cells öffnen. Aspose.Cells lädt und speichert die Designer-Tabelle und behält dabei alle bedingten Formatierungseinstellungen bei.

### **Verwenden der Kopiermethode**

Aspose.Cells ermöglicht Entwicklern, bedingte Formatierungseinstellungen von einer Zelle auf eine andere im Arbeitsblatt zu kopieren, indem sie die Methode [**Range.copy()**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-) aufrufen.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-CopyConditionalFormattsByCopyRange.js" >}}


## **Bedingte Formatierung zur Laufzeit anwenden**

Mit Aspose.Cells können Sie bedingte Formatierungen zur Laufzeit sowohl hinzufügen als auch entfernen. Die unten stehenden Codebeispiele zeigen, wie bedingte Formatierungen festgelegt werden:

1. Instanziieren Sie ein Arbeitsbuch.
1. Fügen Sie eine leere bedingte Formatierung hinzu.
1. Legen Sie den Bereich fest, auf den die Formatierung angewendet werden soll.
1. Definieren Sie die Formatierungsbedingungen.
1. Speichern Sie die Datei.

Nach diesem Beispiel folgen mehrere kleinere Beispiele, die zeigen, wie Schriftart-Einstellungen, Rand-Einstellungen und Muster angewendet werden.

Microsoft Excel 2007 hat erweiterte bedingte Formatierung eingeführt, die auch von Aspose.Cells unterstützt wird. Die Beispiele hier veranschaulichen die Verwendung einfacher Formatierung, während die Microsoft Excel 2007-Beispiele zeigen, wie man erweiterte bedingte Formatierungen anwendet.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyingConditionalFormattingAtRuntime.js" >}}


### **Schriftart festlegen**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetFont.js" >}}



{{% alert color="primary" %}}

Sie können nur die Schriftart, die Textfarbe, den Unterstrichstil und den Durchstreichstil ändern.

{{% /alert %}}

### **Rahmen festlegen**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetBorder.js" >}}


{{% alert color="primary" %}}

Sie können nur dünne Linienstile für die Outline-Grenze verwenden. Diagonale Linien sind nicht erlaubt.

{{% /alert %}}

### **Muster festlegen**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetPattern.js" >}}



## **Erweiterte Themen**  
- [Hinzufügen von 2-Farben-Skalen und 3-Farben-Skalen bedingter Formatierungen](/cells/de/nodejs-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)  
- [Bedingte Formatierung in Arbeitsblättern anwenden](/cells/de/nodejs-cpp/apply-conditional-formatting-in-worksheets/)  
- [Abwechselnde Zeilen und Spalten mit bedingter Formatierung schattieren](/cells/de/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)  
- [Generieren von Datenleistungsimages für bedingte Formatierungen](/cells/de/nodejs-cpp/generate-conditional-formatting-databars-images/)  
- [Erhalten von Symbolsets, Datenleisten oder Farbskalenobjekten, die bei der bedingten Formatierung verwendet werden](/cells/de/nodejs-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)  


