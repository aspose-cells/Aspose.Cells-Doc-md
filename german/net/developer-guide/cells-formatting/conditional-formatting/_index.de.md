---
title: Legen Sie bedingte Formate von Excel- und ODS-Dateien fest.
linktitle: Bedingte Formate
type: docs
weight: 60
url: /de/net/conditional-formatting/
description: So wenden Sie bedingte Formate auf Excel- und ODS-Dateien in CSharp an.
keywords: apply conditional formats 
---
## **Einführung**

 Die bedingte Formatierung ist eine erweiterte Microsoft Excel-Funktion, mit der Sie Formate auf eine Zelle oder einen Zellbereich anwenden und diese Formatierung abhängig vom Wert der Zelle oder dem Wert einer Formel ändern können. Beispielsweise können Sie eine Zelle nur dann fett darstellen lassen, wenn der Wert der Zelle größer als 500 ist. Wenn der Wert der Zelle die Bedingung erfüllt, wird das angegebene Format auf die Zelle angewendet. Wenn der Wert der Zelle die Formatbedingung nicht erfüllt, wird die Standardformatierung der Zelle verwendet. Wählen Sie in Microsoft Excel aus**Format** , dann**Bedingte Formatierung** , um das Dialogfeld „Bedingte Formatierung“ zu öffnen.

Aspose.Cells unterstützt die Anwendung von bedingter Formatierung auf Zellen zur Laufzeit. Dieser Artikel erklärt, wie. Außerdem wird erläutert, wie die von Excel für die bedingte Formatierung der Farbskala verwendete Farbe berechnet wird.

## **Bedingte Formatierung anwenden**

Aspose.Cells unterstützt die bedingte Formatierung auf verschiedene Weise:

- Verwenden von Designer-Tabellenkalkulationen
- Verwenden der Kopiermethode.
- Bedingte Formatierung zur Laufzeit erstellen.

### **Verwenden von Designer-Tabellenkalkulation**

Entwickler können ein Designer-Arbeitsblatt mit bedingter Formatierung in Microsoft Excel erstellen und dieses Arbeitsblatt dann mit Aspose.Cells öffnen. Aspose.Cells lädt und speichert das Designer-Arbeitsblatt, wobei alle Einstellungen für die bedingte Formatierung beibehalten werden.

### **Verwenden der Kopiermethode**

 Aspose.Cells ermöglicht es Entwicklern, bedingte Formateinstellungen von einer Zelle in eine andere im Arbeitsblatt zu kopieren, indem sie die[**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) Methode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **Anwenden der bedingten Formatierung zur Laufzeit**

Aspose.Cells können Sie bedingte Formatierung zur Laufzeit hinzufügen und entfernen. Die folgenden Codebeispiele zeigen, wie Sie die bedingte Formatierung festlegen:

1. Instanziieren Sie eine Arbeitsmappe.
1. Fügen Sie ein leeres bedingtes Format hinzu.
1. Legen Sie den Bereich fest, für den die Formatierung gelten soll.
1. Definieren Sie die Formatierungsbedingungen.
1. Speicher die Datei.

Nach diesem Beispiel folgen einige weitere kleinere Beispiele, die zeigen, wie Schrifteinstellungen, Rahmeneinstellungen und Muster angewendet werden.

Microsoft Excel 2007 hat erweiterte bedingte Formatierung hinzugefügt, die Aspose.Cells ebenfalls unterstützt. Die Beispiele hier veranschaulichen, wie einfache Formatierung verwendet wird, die Microsoft Excel 2007-Beispiele zeigen, wie fortgeschrittenere bedingte Formatierung angewendet wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **Schriftart festlegen**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

Sie können nur den Schriftstil, die Textfarbe, den Unterstreichungsstil und den Durchstreichungsstil ändern.

{{% /alert %}}

### **Grenze setzen**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

Sie können nur dünne Linienstile für den Umrissrand verwenden. Diagonale Linien sind nicht erlaubt.

{{% /alert %}}

### **Muster setzen**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **Themen vorantreiben**
- [Bedingte Formatierungen für 2-Farben-Skala und 3-Farben-Skala hinzufügen](/cells/de/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Wenden Sie die erweiterte bedingte Formatierung an](/cells/de/net/apply-advanced-conditional-formatting/)
- [Wenden Sie bedingte Formatierung in Arbeitsblättern an](/cells/de/net/apply-conditional-formatting-in-worksheets/)
- [Wenden Sie Schattierung auf abwechselnde Zeilen und Spalten mit bedingter Formatierung an](/cells/de/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Generieren Sie DataBars-Bilder mit bedingter Formatierung](/cells/de/net/generate-conditional-formatting-databars-images/)
- [Holen Sie sich Symbolsätze, Datenbalken oder Farbskalenobjekte, die in der bedingten Formatierung verwendet werden](/cells/de/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

