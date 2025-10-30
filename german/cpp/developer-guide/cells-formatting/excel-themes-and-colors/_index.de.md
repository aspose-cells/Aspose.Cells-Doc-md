---
title: Excel Themen und Farben mit C++
linktitle: Excel Themen und Farben
type: docs
weight: 100
url: /de/cpp/excel-themes-and-colors/
description: C++ Code zur Verwendung des Excel Farbschemas mit der API Aspose.Cells for C++.
keywords: C++, um Farbschemata zu erstellen und anzuwenden, C++ programmatisch ein benutzerdefiniertes Farbschema erstellen, wie man programmatisch ein benutzerdefiniertes Farbschema anwendet, C++ wie man das Farbschema in Excel verwendet.
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

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Define Color array (of 12 colors) for Theme
    Vector<Aspose::Cells::Color> carr(12);
    carr[0] = Color::AntiqueWhite(); // Background1
    carr[1] = Color::Brown();       // Text1
    carr[2] = Color::AliceBlue();   // Background2
    carr[3] = Color::Yellow();      // Text2
    carr[4] = Color::YellowGreen(); // Accent1
    carr[5] = Color::Red();         // Accent2
    carr[6] = Color::Pink();        // Accent3
    carr[7] = Color::Purple();      // Accent4
    carr[8] = Color::PaleGreen();   // Accent5
    carr[9] = Color::Orange();      // Accent6
    carr[10] = Color::Green();      // Hyperlink
    carr[11] = Color::Gray();       // Followed Hyperlink

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Instantiate a Workbook and open the template file
    Workbook workbook(inputFilePath);

    // Set the custom theme with specified colors
    workbook.CustomTheme(u"CustomeTheme1", carr);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Save as the excel file
    workbook.Save(outputFilePath);

    std::cout << "Custom theme applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **So wenden Sie Designs in Aspose.Cells an**

Im folgenden Beispiel werden die Vordergrund- und Schriftfarben einer Zelle basierend auf den Standarddesignfarben (des Arbeitsmappen) angewendet. Die Excel-Datei wird ebenfalls auf der Festplatte gespeichert.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Get cells collection in the first (default) worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Get the D3 cell
    Cell c = cells.Get(u"D3");

    // Get the style of the cell
    Style s = c.GetStyle();

    // Set foreground color for the cell from the default theme Accent2 color
    s.SetForegroundThemeColor(ThemeColor(ThemeColorType::Accent2, 0.5));

    // Set the pattern type
    s.SetPattern(BackgroundType::Solid);

    // Get the font for the style
    Font f = s.GetFont();

    // Set the theme color
    f.SetThemeColor(ThemeColor(ThemeColorType::Accent4, 0.1));

    // Apply style
    c.SetStyle(s);

    // Put a value
    c.PutValue(u"Testing1");

    // Save the excel file
    workbook.Save(outDir + u"output.out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **So erhalten und setzen Sie Designs in Aspose.Cells**
 Nachfolgend finden Sie einige Methoden und Eigenschaften, die Designs implementieren.

- [**Style.GetForegroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundthemecolor/): Wird verwendet, um die Vordergrundfarbe festzulegen.
- [**Style.GetBackgroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundthemecolor/): Wird verwendet, um die Hintergrundfarbe festzulegen.
- [**Font.GetThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getthemecolor/): Wird verwendet, um die Schriftfarbe festzulegen.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getthemecolor/): Wird verwendet, um eine Desigfarbe zu erhalten.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setthemecolor/): Wird verwendet, um eine Desigfarbe festzulegen.

Das folgende Beispiel zeigt, wie Designs erhalten und gesetzt werden.

Das folgende Beispiel verwendet eine Vorlagendatei im XLSX-Format, ruft die Farben für verschiedene Designtypen ab, ändert die Farben und speichert die Microsoft Excel-Datei.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Background1 theme color
    Color c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the color
    std::cout << "theme color Background1: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Get the Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the color
    std::cout << "theme color Accent2: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Background1 theme color
    workbook.SetThemeColor(ThemeColorType::Background1, Color::Red());

    // Get the updated Background1 theme color
    c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the updated color for confirmation
    std::cout << "theme color Background1 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Accent2 theme color
    workbook.SetThemeColor(ThemeColorType::Accent2, Color::Blue());

    // Get the updated Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the updated color for confirmation
    std::cout << "theme color Accent2 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Save the updated file
    workbook.Save(outputFilePath);

    std::cout << "Theme colors updated and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Extrahieren von Themen-Daten aus Excel-Datei](/cells/de/cpp/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="cpp" >}}
