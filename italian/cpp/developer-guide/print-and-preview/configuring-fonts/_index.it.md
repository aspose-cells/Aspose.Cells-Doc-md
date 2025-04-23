---
title: Configurare i caratteri per il rendering dei fogli di calcolo con C++
linktitle: Configurazione dei Font per la Visualizzazione dei Fogli di Lavoro
type: docs
weight: 10
url: /it/cpp/configuring-fonts-for-rendering-spreadsheets/
description: Impara come configurare i caratteri per il rendering di fogli di calcolo in immagini, PDF e formati XPS usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Le API di Aspose.Cells consentono di rendere i fogli di calcolo in formati immagine e di convertirli in PDF e XPS. Per massimizzare la fedeltà della conversione, è necessario che i caratteri usati nel foglio di calcolo siano disponibili nella directory dei font predefiniti del sistema operativo. Se i font richiesti non sono presenti, le API di Aspose.Cells tenteranno di sostituire i font richiesti con quelli disponibili.

## **Selezione dei font**

Di seguito il processo seguito dalle API di Aspose.Cells:

1. L'API cerca di trovare i font nel file system corrispondenti al nome esatto del font utilizzato nel foglio di calcolo.
1. Se l'API non trova i font con lo stesso nome, tenta di usare il font di default specificato sotto la proprietà [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) del Workbook.
1. Se l'API non può trovare il font definito sotto la proprietà [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) del workbook, tenta di usare il font specificato sotto [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) o la proprietà [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/).
1. Se l'API non può localizzare il font definito sotto la proprietà [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) o [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/), tenta di utilizzare il font specificato sotto la proprietà [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/).
1. Se l'API non può localizzare il font definito sotto la proprietà [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/), tenta di selezionare i font più adatti tra tutti quelli disponibili.
1. Infine, se l'API non trova font sul sistema, renderizza il foglio di calcolo usando Arial.

## **Impostazione delle cartelle dei font personalizzate**

Le API di Aspose.Cells cercano i font necessari nella directory dei font di default del sistema operativo. Se i font richiesti non sono disponibili nella directory di sistema, le API cercano tramite directory personalizzate (definite dall'utente). La classe [**FontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/) offre vari modi per impostare directory di font personalizzate, come dettagliato di seguito:

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/): Questo metodo è utile se c'è solo una cartella da impostare.
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/): Questo metodo è utile quando i font risiedono in più cartelle, e l'utente desidera impostare tutte le cartelle separatamente invece di combinarle in una sola.
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsources/): Questo meccanismo è utile quando l'utente desidera caricare font da più cartelle, un singolo file font o dati di font da un array di byte.

{{% alert color="primary" %}}

Sia i metodi [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/) che [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/) accettano un secondo parametro di tipo Boolean. Passare **true** come secondo parametro indicherà alle API di Aspose.Cells di cercare i file font nelle sottocartelle.

{{% /alert %}}

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

Vector<uint8_t> GetDataFromFile(const U16String& file)
{
    std::string f = file.ToUtf8();
    // open a file 
    std::ifstream fileStream(f, std::ios::binary);

    if (!fileStream.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    // Get file size
    fileStream.seekg(0, std::ios::end);
    std::streampos fileSize = fileStream.tellg();
    fileStream.seekg(0, std::ios::beg);

    // Read file contents into uint8_t array
    uint8_t* buffer = new uint8_t[fileSize];
    fileStream.read(reinterpret_cast<char*>(buffer), fileSize);
    fileStream.close();

    Vector<uint8_t>data(buffer, fileSize);
    delete[] buffer;

    return data;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String fontFolder1 = srcDir + u"Arial";
    U16String fontFolder2 = srcDir + u"Calibri";
    U16String fontFile = srcDir + u"arial.ttf";

    FontConfigs::SetFontFolder(fontFolder1, true);

    Vector<U16String> fontFolders{ fontFolder1 , fontFolder2 };

    FontConfigs::SetFontFolders(fontFolders, false);

    FolderFontSource sourceFolder(fontFolder1, false);
    FileFontSource sourceFile(fontFile);
    Vector<uint8_t> fontData = GetDataFromFile(fontFile);
    MemoryFontSource sourceMemory(fontData);

    Vector<FontSourceBase> fontSources{ sourceFolder ,sourceFile ,sourceMemory };

    FontConfigs::SetFontSources(fontSources);

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Si prega di utilizzare uno dei metodi sopra menzionati all'inizio dell'applicazione, cioè prima di invocare qualsiasi altro oggetto delle API di Aspose.Cells.

{{% /alert %}}

{{% alert color="primary" %}}

Se tutti i metodi sopra menzionati vengono utilizzati per impostare le origini dei font, solo le ultime impostazioni avranno effetto.

{{% /alert %}}

## **Meccanismo di sostituzione del font**

Le API di Aspose.Cells offrono anche la possibilità di specificare font sostitutivi per scopi di rendering. Questo meccanismo è utile quando un font richiesto non è disponibile sulla macchina su cui deve avvenire la conversione. Gli utenti possono fornire un elenco di nomi di font come alternativa al font originariamente richiesto. Per farlo, le API di Aspose.Cells hanno esposto il metodo [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsubstitutes/), che accetta due parametri. Il primo parametro è di tipo **string**, che dovrebbe essere il nome del font da sostituire. Il secondo parametro è un array di tipo **string**. Gli utenti possono fornire una lista di nomi di font come sostituzione per il nome del font originale (specificato nel primo parametro).

Ecco uno scenario di utilizzo semplice:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Substituting the Arial font with Times New Roman & Calibri
    Vector<U16String> substituteFonts{ u"Times New Roman", u"Calibri" };
    FontConfigs::SetFontSubstitutes(u"Arial", substituteFonts);

    Aspose::Cells::Cleanup();
}
```

## **Raccolta informazioni**

Oltre ai metodi sopra menzionati, le API di Aspose.Cells forniscono anche mezzi per raccogliere informazioni sulle fonti e sostituzioni impostate:

1. Il metodo [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) restituisce un array di tipo [**FontSourceBase**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsourcebase/) contenente l'elenco delle fonti di font specificate. Se nessuna fonte è stata impostata, il metodo [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) restituirà un array vuoto.
1. Il metodo [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) accetta un parametro di tipo **string**, consentendoti di specificare il nome del font per cui è stata impostata una sostituzione. Se non è stata impostata nessuna sostituzione per il nome del font specificato, il metodo [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) restituirà null.

## **Argomenti Avanzati**
- [Imposta il carattere predefinito durante il rendering del foglio elettronico in immagini](/cells/it/cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Imposta la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions per dare priorità](/cells/it/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formati di carattere supportati](/cells/it/cpp/supported-font-formats/)
