---
title: Excel Themen und Farben
type: docs
weight: 100
url: /de/net/excel-themes-and-colors/
description: C# Code zur Verwendung des Excel Farbschemas mit der Aspose.Cells for .NET API
keywords: C# zum Erstellen und Anwenden von Farbschemata, c# programmgesteuert Erstellen eines benutzerdefinierten Farbschemas, programmgesteuertes Anwenden eines benutzerdefinierten Farbschemas, c# Verwendung eines Farbschemas in Excel
---

## **Wie man ein Farbschema in Excel erstellt und anwendet**
Dokumentthemen erleichtern die Koordination von Farben, Schriftarten und grafischen Formatierungseffekten von Excel-Dokumenten und ermöglichen eine schnelle Aktualisierung. 
Themen bieten ein einheitliches Erscheinungsbild mit benannten Stilen, grafischen Effekten und anderen Objekten, die in einer Arbeitsmappe verwendet werden. Zum Beispiel sieht der Accent1-Stil in den Office- und Apex-Themen unterschiedlich aus. Oft wenden Sie ein Dokumentthema an und passen es dann Ihren Wünschen an.

### **Wie man ein Farbschema in Excel anwendet**
1. Öffnen Sie Excel und wechseln Sie zum Register „Seitenlayout“ im Excel-Band.
1. Klicken Sie auf die Schaltfläche „Farben“ im Abschnitt „Themen“.
<br>
<img src="color.png" width=70% />
1. Wählen Sie eine Farbpalette aus, die Ihren Anforderungen entspricht, oder fahren Sie mit der Maus über ein Schema, um eine Live-Vorschau anzuzeigen.

### **Wie man ein benutzerdefiniertes Farbschema in Excel erstellt**
Sie können Ihre eigene Farbgebung erstellen, um Ihrem Dokument ein frisches, einzigartiges Aussehen zu verleihen oder den Markenstandards Ihrer Organisation zu entsprechen.

1. Öffnen Sie Excel und wechseln Sie zum Register „Seitenlayout“ im Excel-Band.
1. Klicken Sie auf die Schaltfläche „Farben“ im Abschnitt „Themen“.
1. Klicken Sie auf die Schaltfläche „Farben anpassen...“.
<br>
<img src="color2.png" width=70% />

1. In dem Dialogfeld „Neue Designfarben erstellen“ können Sie für jedes Element Farben auswählen, indem Sie auf die Farbauswahlfelder neben ihnen klicken. Sie können Farben aus der Palette auswählen oder benutzerdefinierte Farben über die Option „Mehr Farben“ definieren.
<br>
<img src="color3.png" width=70% />
1. Nach Auswahl aller gewünschten Farben geben Sie einen Namen für Ihr benutzerdefiniertes Farbschema im Feld „Name“ an.

1. Klicken Sie auf die Schaltfläche „Speichern“, um Ihr benutzerdefiniertes Farbschema zu speichern. Ihr benutzerdefiniertes Farbschema steht jetzt im Drop-Down-Menü „Farben“ für zukünftige Verwendungen zur Verfügung.

## **Wie man ein Farbschema in Aspose.Cells erstellt und anwendet**
Aspose.Cells bietet Funktionen zur Anpassung von Themen und Farben.

### **Wie man ein benutzerdefiniertes Farbdesign in Aspose.Cells erstellt**
Wenn Designs verwendet werden, müssen wir nicht jede Zelle einzeln ändern, sondern nur die Farben im Design anpassen.

Das folgende Beispiel zeigt, wie benutzerdefinierte Designs mit den gewünschten Farben angewendet werden. Es wird eine Beispieldatei verwendet, die manuell in Microsoft Excel 2007 erstellt wurde.

Im folgenden Beispiel wird eine Vorlagendatei im XLSX-Format geladen, Farben für verschiedene Designtypen definiert und die benutzerdefinierten Farben angewendet, bevor die Excel-Datei gespeichert wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

### **So wenden Sie Designs in Aspose.Cells an**

Im folgenden Beispiel werden die Vordergrund- und Schriftfarben einer Zelle basierend auf den Standarddesignfarben (des Arbeitsmappen) angewendet. Die Excel-Datei wird ebenfalls auf der Festplatte gespeichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

### **So erhalten und setzen Sie Designs in Aspose.Cells**
 Nachfolgend finden Sie einige Methoden und Eigenschaften, die Designs implementieren.

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Wird verwendet, um die Vordergrundfarbe festzulegen.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Wird verwendet, um die Hintergrundfarbe festzulegen.
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Wird verwendet, um die Schriftfarbe festzulegen.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Wird verwendet, um eine Desigfarbe zu erhalten.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Wird verwendet, um eine Desigfarbe festzulegen.

Das folgende Beispiel zeigt, wie Designs erhalten und gesetzt werden.

Das folgende Beispiel verwendet eine Vorlagendatei im XLSX-Format, ruft die Farben für verschiedene Designtypen ab, ändert die Farben und speichert die Microsoft Excel-Datei.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

## **Erweiterte Themen**
- [Extrahieren von Themen-Daten aus Excel-Datei](/cells/de/net/extract-theme-data-from-excel-file/)
