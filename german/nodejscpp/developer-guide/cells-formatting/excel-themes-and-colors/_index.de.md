---  
title: Excel Themen und Farben
linktitle: Excel Themen und Farben  
type: docs  
weight: 100  
url: /de/nodejs-cpp/excel-themes-and-colors/  
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ benutzerdefinierte Farbschemata verwenden.  
keywords: Node.js Erstellen und Anwenden von Farbschemas, Node.js programmatisch ein benutzerdefiniertes Farb schema erstellen, programmatisch wie man ein benutzerdefiniertes Farb schema in Node.js anwendet, Node.js wie man das Farb Schema in Excel verwendet  
---  

## **Wie man ein Farbschema in Excel erstellt und anwendet**  
Dokumentthemen erleichtern die Koordination von Farben, Schriftarten und grafischen Formatierungseffekten von Excel-Dokumenten und ermöglichen eine schnelle Aktualisierung.  
Themen bieten ein einheitliches Erscheinungsbild mit benannten Stilen, grafischen Effekten und anderen Objekten, die in einer Arbeitsmappe verwendet werden. Zum Beispiel sieht der Accent1-Stil in den Office- und den Apex-Themen unterschiedlich aus. Oft wenden Sie ein Dokumententhema an und ändern es dann nach Wunsch.  

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
Wenn im Dokument Themenfarben verwendet werden, müssen wir nicht jede Zelle einzeln ändern; wir müssen nur die Farben im Thema ändern.  

Das folgende Beispiel zeigt, wie benutzerdefinierte Designs mit den gewünschten Farben angewendet werden. Es wird eine Beispieldatei verwendet, die manuell in Microsoft Excel 2007 erstellt wurde.  

Das folgende Beispiel lädt eine Vorlage XLSX-Datei, definiert Farben für verschiedene Theme-Farbtypen, wendet die benutzerdefinierten Farben an und speichert die Excel-Datei.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-CreateCustomColorTheme.js" >}}



### **So wenden Sie Designs in Aspose.Cells an**  
Das folgende Beispiel wendet die Vordergrund- und Schriftfarben einer Zelle basierend auf den Standard-Theme-Farbtypen an. Es speichert auch die Excel-Datei auf der Festplatte.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-ApplyThemeColors.js" >}}


### **So erhalten und setzen Sie Designs in Aspose.Cells**  
Nachfolgend finden Sie einige Methoden und Eigenschaften, die Designs implementieren.  

- [**Style.setForegroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundThemeColor-themecolor-): Wird verwendet, um die Vordergrundfarbe festzulegen.  
- [**Style.setBackgroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundThemeColor-themecolor-): Wird verwendet, um die Hintergrundfarbe festzulegen.  
- [**Font.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setThemeColor-themecolor-): Wird verwendet, um die Schriftfarbe festzulegen.  
- [**Workbook.getThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getThemeColor-themecolortype-): Wird verwendet, um eine Thema-Farbe zu erhalten.  
- [**Workbook.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#setThemeColor-themecolortype-color-): Wird verwendet, um eine Thema-Farbe festzulegen.  

Das folgende Beispiel zeigt, wie Designs erhalten und gesetzt werden.  

Das folgende Beispiel verwendet eine Vorlage XLSX-Datei, erhält die Farben für verschiedene Theme-Farbtypen, ändert die Farben und speichert die Microsoft Excel-Datei.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetAndSetThemeColors.js" >}}


## **Erweiterte Themen**  
- [Extrahieren von Themen-Daten aus Excel-Datei](/cells/de/nodejs-cpp/extract-theme-data-from-excel-file/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
