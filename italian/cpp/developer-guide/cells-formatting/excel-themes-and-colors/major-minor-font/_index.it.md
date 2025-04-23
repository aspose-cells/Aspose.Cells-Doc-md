---
title: Font del tema di intestazioni e corpo con C++
linktitle: Tema dei Titoli e del Testo
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo. Supporta l impostazione dei font del tema di intestazioni e corpo nei documenti Excel, consentendo agli utenti di personalizzare l aspetto e lo stile del documento. Questo articolo introdurrà come usare la libreria Aspose.Cells per lavorare con i font del tema di intestazioni e corpo nei documenti Excel.
keywords: Aspose.Cells, Documento Excel, Titolo, Corpo, Tema del Testo, Aspetto, Stile
type: docs
weight: 120
url: /it/cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Il font predefinito cambierà automaticamente quando viene modificata l'impostazione della regione.

Se viene modificato il font predefinito, verrà modificata anche l'altezza della riga e la larghezza della colonna, e potrebbe persino disordinare la disposizione della pagina.

Cos'ha causato il cambiamento del font predefinito?

Se il font del tema di Excel è impostato, Excel passerà automaticamente tra diversi font in base all'ambiente linguistico corrente.

{{% /alert %}}

## **Titoli e Corpo del Tema del Testo in Excel**

In Excel, seleziona la scheda Home, clicca sulla casella a discesa dei font, vedrai "Font del tema" con due font del tema: Calibri Light (Intestazioni) e Calibri (Corpo) in alto con impostazione regione inglese.

**![Font del Tema](Theme-Fonts.png)**

Se si seleziona Font del tema, il nome del font verrà visualizzato in modo diverso in regioni diverse.
Se non vuoi che il font venga modificato automaticamente in regioni diverse, non selezionare i due font del tema.

## **Modifica dei font di intestazioni e corpo tramite codice**
Con Aspose.Cells for C++, possiamo verificare se il font predefinito è un font del tema o impostare il font del tema con la proprietà [**Font.GetSchemeType()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getschemetype/).

Il seguente codice di esempio mostra come manipolare il font del tema.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook(u"Book1.xlsx");

    // Get the default style
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the font scheme type
    FontSchemeType schemeType = defaultStyle.GetFont().GetSchemeType();

    // Check if the font is a theme font
    if (schemeType == FontSchemeType::Major || schemeType == FontSchemeType::Minor)
    {
        std::cout << "It's theme font" << std::endl;
    }

    // Change theme font to normal font
    defaultStyle.GetFont().SetSchemeType(FontSchemeType::None);

    // Set the modified default style back to the workbook
    workbook.SetDefaultStyle(defaultStyle);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Ottieni dinamicamente il font del tema locale tramite codice**
A volte, i nostri server e i computer degli utenti non si trovano nella stessa regione. Come possiamo ottenere lo stesso font desiderato dagli utenti per l'elaborazione dei file?

È necessario impostare le impostazioni regionali del sistema prima di caricare il file con la proprietà [**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getregion/).

Il seguente esempio di codice mostra come ottenere il font del tema locale.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new LoadOptions
    LoadOptions options;

    // Set the customer's region to Japan
    options.SetRegion(CountryCode::Japan);

    // Instantiate a new Workbook with the specified options
    Workbook workbook(u"Book1.xlsx", options);

    // Get the default style of the workbook
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the customer's local font name
    U16String localFontName = defaultStyle.GetFont().GetName();

    std::cout << "Local Font Name: " << localFontName.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
