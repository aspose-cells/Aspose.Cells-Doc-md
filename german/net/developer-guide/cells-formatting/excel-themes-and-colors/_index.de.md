---
title: Excel-Themen und -Farben
type: docs
weight: 100
url: /de/net/excel-themes-and-colors/
description: C#-Code zur Verwendung des Excel-Farbschemas mit Aspose.Cells for .NET API
keywords: C# to Create and Apply Color Schemes, c# programmatically Create a Custom Color Scheme, programmatically how to Apply a Custom Color Scheme, c# how to Use Color Scheme in excel
---
##  **So wenden Sie ein Farbschema in Excel an und erstellen es**
Dokumentthemen erleichtern die Abstimmung von Farben, Schriftarten und grafischen Formatierungseffekten von Excel-Dokumenten und deren schnelle Aktualisierung.
Designs sorgen für ein einheitliches Erscheinungsbild mit benannten Stilen, grafischen Effekten und anderen in einer Arbeitsmappe verwendeten Objekten. Beispielsweise sieht der Accent1-Stil im Office- und im Apex-Design anders aus. Oft wenden Sie ein Dokumentthema an und ändern es dann nach Ihren Wünschen.

###  **So wenden Sie ein Farbschema in Excel an**
1. Öffnen Sie Excel und gehen Sie im Excel-Menüband auf die Registerkarte „Seitenlayout“.
1. Klicken Sie im Abschnitt „Themen“ auf die Schaltfläche „Farben“.
<br>
<img src="color.png" width=70% />
1. Wählen Sie eine Farbpalette, die Ihren Anforderungen entspricht, oder bewegen Sie den Mauszeiger über ein Schema, um eine Live-Vorschau anzuzeigen.

###  **So erstellen Sie ein benutzerdefiniertes Farbschema in Excel**
Sie können Ihren eigenen Farbsatz erstellen, um Ihrem Dokument ein frisches, einzigartiges Aussehen zu verleihen oder den Markenstandards Ihres Unternehmens zu entsprechen.

1. Öffnen Sie Excel und gehen Sie im Excel-Menüband auf die Registerkarte „Seitenlayout“.
1. Klicken Sie im Abschnitt „Themen“ auf die Schaltfläche „Farben“.
1. Klicken Sie auf die Schaltfläche „Farben anpassen…“.
<br>
<img src="color2.png" width=70% />

1. Im Dialogfeld „Neue Designfarben erstellen“ können Sie Farben für jedes Element auswählen, indem Sie auf die Farb-Dropdown-Menüs daneben klicken. Sie können Farben aus der Palette auswählen oder mithilfe der Option „Weitere Farben“ benutzerdefinierte Farben definieren.
<br>
<img src="color3.png" width=70% />
1. Nachdem Sie alle gewünschten Farben ausgewählt haben, geben Sie im Feld „Name“ einen Namen für Ihr benutzerdefiniertes Farbschema ein.

1. Klicken Sie auf die Schaltfläche „Speichern“, um Ihr individuelles Farbschema zu speichern. Ihr benutzerdefiniertes Farbschema ist jetzt im Dropdown-Menü „Farben“ für die zukünftige Verwendung verfügbar.

##  **So erstellen und wenden Sie ein Farbschema in Aspose.Cells an**
Aspose.Cells bietet Funktionen zum Anpassen von Themen und Farben.

###  **So erstellen Sie ein benutzerdefiniertes Farbthema in Aspose.Cells**
Wenn in der Datei Designfarben verwendet werden, müssen wir nicht jede Zelle einzeln ändern, sondern nur die Farben im Design.

Das folgende Beispiel zeigt, wie Sie benutzerdefinierte Designs mit Ihren gewünschten Farben anwenden. Wir verwenden eine Beispielvorlagendatei, die manuell in Microsoft Excel 2007 erstellt wurde.

Das folgende Beispiel lädt eine Vorlagendatei XLSX, definiert Farben für verschiedene Designfarbtypen, wendet die benutzerdefinierten Farben an und speichert die Excel-Datei.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

###  **So wenden Sie Designfarben in Aspose.Cells an**

Im folgenden Beispiel werden die Vordergrund- und Schriftfarben einer Zelle basierend auf den Farbtypen des Standarddesigns (der Arbeitsmappe) angewendet. Außerdem wird die Excel-Datei auf der Festplatte gespeichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

###  **So erhalten und legen Sie Designfarben in Aspose.Cells fest**
 Nachfolgend finden Sie einige Methoden und Eigenschaften, die Designfarben implementieren.

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Wird verwendet, um die Vordergrundfarbe festzulegen.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Wird zum Festlegen der Hintergrundfarbe verwendet.
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Wird zum Festlegen der Schriftfarbe verwendet.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Wird verwendet, um eine Designfarbe zu erhalten.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Wird verwendet, um eine Designfarbe festzulegen.

Das folgende Beispiel zeigt, wie Sie Designfarben abrufen und festlegen.

Das folgende Beispiel verwendet eine Vorlagendatei XLSX, ruft die Farben für verschiedene Designfarbtypen ab, ändert die Farben und speichert die Excel-Datei Microsoft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

##  **Vorabthemen**
- [Extrahieren Sie Theme-Daten aus einer Excel-Datei](/cells/de/net/extract-theme-data-from-excel-file/)
