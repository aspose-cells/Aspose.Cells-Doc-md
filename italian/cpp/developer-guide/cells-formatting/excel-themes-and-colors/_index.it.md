---
title: Temi e colori di Excel con C++
linktitle: Temi e Colori di Excel
type: docs
weight: 100
url: /it/cpp/excel-themes-and-colors/
description: Codice C++ per utilizzare lo schema dei colori di Excel con API Aspose.Cells for C++
keywords: C++ per creare e applicare schemi di colori, creare programmaticamente uno schema di colori personalizzato, come applicare programmaticamente uno schema di colori personalizzato, come usare lo schema di colori in excel con C++
---

## **Come Applicare e Creare uno Schema Colori in Excel**
I temi del documento facilitano il coordinamento dei colori, dei caratteri e degli effetti di formattazione grafica dei documenti di Excel e consentono di aggiornarli rapidamente. 
I temi forniscono un aspetto unificato con stili denominati, effetti grafici e altri oggetti utilizzati in un documento di lavoro. Ad esempio, lo stile Accent1, ad esempio, appare diverso nei temi Office e Apex. Spesso si applica un tema del documento e quindi lo si modifica a proprio piacimento.

### **Come Applicare uno Schema Colori in Excel**
1. Apri Excel e vai alla scheda "Layout di pagina" nel nastro di Excel.
1. Fai clic sul pulsante "Colori" nella sezione "Temi".
<br>
<img src="color.png" width=70% />
1. Scegli una combinazione di colori che corrisponda alle tue esigenze o passa il mouse su uno schema per vedere un'anteprima in tempo reale.

### **Come creare un set di colori personalizzato in Excel**
Puoi creare il tuo set di colori per dare al tuo documento un aspetto fresco e unico o per conformarti agli standard del marchio della tua organizzazione.

1. Apri Excel e vai alla scheda "Layout di pagina" nel nastro di Excel.
1. Fai clic sul pulsante "Colori" nella sezione "Temi".
1. Fai clic sul pulsante "Personalizza colori...".
<br>
<img src="color2.png" width=70% />

1. Nella finestra di dialogo "Crea nuovi colori tema", puoi selezionare i colori per ciascun elemento facendo clic sul menù a discesa accanto ad essi. Puoi scegliere i colori dalla palette o definire colori personalizzati utilizzando l'opzione "Altri colori".
<br>
<img src="color3.png" width=70% />
1. Dopo aver selezionato tutti i colori desiderati, fornisci un nome per il tuo set di colori personalizzato nel campo "Nome".

1. Fai clic sul pulsante "Salva" per salvare il tuo set di colori personalizzato. Il tuo set di colori personalizzato sarà ora disponibile nel menù a discesa "Colori" per un uso futuro.

## **Come creare e applicare un set di colori in Aspose.Cells**
Aspose.Cells offre funzionalità per personalizzare temi e colori.

### **Come creare un tema di colori personalizzato in Aspose.Cells**
Se vengono utilizzati colori del tema nel file, non è necessario modificare ogni cella singolarmente, è sufficiente modificare i colori nel tema.

Nell'esempio seguente viene mostrato come applicare temi personalizzati con i colori desiderati. Utilizziamo un file modello creato manualmente in Microsoft Excel 2007.

Nell'esempio seguente viene caricato un file XLSX modello, vengono definiti colori per diversi tipi di colori tema, vengono applicati i colori personalizzati e viene salvato il file excel.

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

### **Come applicare colori tema in Aspose.Cells**

Nell'esempio seguente vengono applicati i colori di primo piano e del testo di una cella in base ai tipi di colore tema predefiniti (del foglio di lavoro). Viene inoltre salvato il file excel su disco.

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

### **Come ottenere e impostare colori tema in Aspose.Cells**
 Di seguito sono riportati alcuni metodi e proprietà che implementano i colori tema.

- [**Style.GetForegroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundthemecolor/): Utilizzato per impostare il colore del primo piano.
- [**Style.GetBackgroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundthemecolor/): Utilizzato per impostare il colore di sfondo.
- [**Font.GetThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getthemecolor/): Utilizzato per impostare il colore del testo.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getthemecolor/): Utilizzato per ottenere un colore del tema.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setthemecolor/): Utilizzato per impostare un colore del tema.

L'esempio seguente mostra come ottenere e impostare i colori del tema.

L'esempio seguente utilizza un file XLSX di modello, ottiene i colori per diversi tipi di colori del tema, cambia i colori e salva il file Microsoft Excel.

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

## **Argomenti avanzati**
- [Estrai dati tema dal file Excel](/cells/it/cpp/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="cpp" >}}
