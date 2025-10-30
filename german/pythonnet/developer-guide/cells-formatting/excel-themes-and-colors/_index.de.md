---
title: Excel Themen und Farben
type: docs
weight: 100
url: /de/python-net/excel-themes-and-colors/
description: C# Code zur Verwendung des Excel Farbschemas mit der Aspose.Cells für Python via .NET API
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

## **So erstellen und wenden Sie ein Farbschema in Aspose.Cells für Python via .NET an**
Aspose.Cells für Python via .NET bietet Funktionen zur Anpassung von Themen und Farben.

### **So erstellen Sie ein benutzerdefiniertes Farbthema in Aspose.Cells für Python via .NET**
Wenn Designs verwendet werden, müssen wir nicht jede Zelle einzeln ändern, sondern nur die Farben im Design anpassen.

Das folgende Beispiel zeigt, wie benutzerdefinierte Designs mit den gewünschten Farben angewendet werden. Es wird eine Beispieldatei verwendet, die manuell in Microsoft Excel 2007 erstellt wurde.

Im folgenden Beispiel wird eine Vorlagendatei im XLSX-Format geladen, Farben für verschiedene Designtypen definiert und die benutzerdefinierten Farben angewendet, bevor die Excel-Datei gespeichert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CustomizeThemes-1.py" >}}

### **So wenden Sie Themenfarben in Aspose.Cells für Python via .NET an**

Im folgenden Beispiel werden die Vordergrund- und Schriftfarben einer Zelle basierend auf den Standarddesignfarben (des Arbeitsmappen) angewendet. Die Excel-Datei wird ebenfalls auf der Festplatte gespeichert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UtilizeThemeColors-1.py" >}}

### **So erhalten und setzen Sie Themenfarben in Aspose.Cells für Python via .NET**
 Nachfolgend finden Sie einige Methoden und Eigenschaften, die Designs implementieren.

- [**Style.foreground_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_theme_color): Wird verwendet, um die Vordergrundfarbe festzulegen.
- [**Style.background_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_theme_color): Wird verwendet, um die Hintergrundfarbe festzulegen.
- [**Font.theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/theme_color): Wird verwendet, um die Schriftfarbe festzulegen.
- [**Workbook.get_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_theme_color): Wird verwendet, um eine Desigfarbe zu erhalten.
- [**Workbook.set_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/set_theme_color): Wird verwendet, um eine Desigfarbe festzulegen.

Das folgende Beispiel zeigt, wie Designs erhalten und gesetzt werden.

Das folgende Beispiel verwendet eine Vorlagendatei im XLSX-Format, ruft die Farben für verschiedene Designtypen ab, ändert die Farben und speichert die Microsoft Excel-Datei.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetSetThemeColors-1.py" >}}

## **Erweiterte Themen**
- [Extrahieren von Themen-Daten aus Excel-Datei](/cells/de/python-net/extract-theme-data-from-excel-file/)

{{< app/cells/assistant language="python-net" >}}
