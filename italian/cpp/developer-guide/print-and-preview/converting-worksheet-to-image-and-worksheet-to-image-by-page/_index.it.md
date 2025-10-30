---
title: Conversione di Foglio di Lavoro in Immagine e Foglio di Lavoro a Pagina con C++
linktitle: Convertire foglio elettronico in immagine e foglio elettronico in immagine per pagina
type: docs
weight: 80
url: /it/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
description: Impara come convertire un foglio di lavoro in un file immagine e un foglio di lavoro con più pagine in un file immagine per pagina utilizzando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Questo documento è progettato per fornire agli sviluppatori una comprensione dettagliata di come convertire un foglio di lavoro in un file immagine e un foglio di lavoro con più pagine in un file immagine per pagina.

A volte potresti dover presentare i fogli elettronici come immagini, ad esempio per utilizzarli in applicazioni o pagine web. Potresti aver bisogno di inserire le immagini in un documento di Word, un file PDF, una presentazione PowerPoint o utilizzarle in qualche altro scenario. In sostanza, desideri rendere il foglio elettronico come un'immagine. Aspose.Cells supporta la conversione dei fogli in file Microsoft Excel in immagini. Inoltre, Aspose.Cells supporta la conversione di un libro di lavoro in più file immagine, uno per pagina.

Potresti usare l'Automazione Office per ottenere questo risultato, ma l'automazione Office presenta alcuni svantaggi. Ci sono diverse ragioni e problematiche coinvolte: ad esempio, sicurezza, stabilità, scalabilità/velocità, prezzo e funzionalità. In breve, ci sono molte ragioni, ma quella principale è che Microsoft stessa raccomanda vivamente di evitare l'automazione Office.

{{% /alert %}}

## **Utilizzare Aspose.Cells per convertire un foglio elettronico in un file immagine**

Questo articolo mostra come creare un'applicazione console in Visual Studio, convertire un foglio elettronico in un'immagine e convertire un foglio elettronico in un'immagine per ogni foglio con poche e semplici righe di codice utilizzando l'API Aspose.Cells.

Devi includere lo spazio dei nomi [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) nel tuo programma/progetto. Ha diverse classi di valore, come [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) e così via. La classe [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) rappresenta un foglio di lavoro per renderizzare immagini del foglio di lavoro e ha un metodo sovraccarico [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) che può convertire un foglio di lavoro in file immagine direttamente con tutte le attributi o opzioni impostate. Può restituire un oggetto `System.Drawing.Bitmap`, e puoi salvare un file immagine sul disco/stream. Sono supportati diversi formati di immagine, ad esempio BMP, PNG, GIF, JPG, JPEG, TIFF, EMF e altri.

Questo articolo spiega come:

- Convertire un foglio di lavoro in un'immagine
- Convertire ogni pagina in un foglio di lavoro in un'immagine

Questo compito mostra come utilizzare Aspose.Cells per convertire un foglio di lavoro da un modello di cartella di lavoro in un file di immagine.

### **Progetto di installazione**

1. Prima, [scarica Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
1. Installa sul tuo computer di sviluppo. Tutti i componenti [Aspose](http://www.aspose.com/), una volta installati, funzionano in modalità valutativa. La modalità valutativa non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti. Ora avvia Visual Studio e crea una nuova applicazione console. Questo esempio utilizza un'applicazione console C++. Aggiungi un riferimento a Aspose.Cells nel progetto creato.

### **Converti Foglio di Lavoro in File Immagine**

Ho creato un nuovo workbook in Microsoft Excel e ho aggiunto alcuni dati al primo foglio di lavoro: **Testbook.xlsx** (1 foglio di lavoro). Successivamente, converti il foglio di lavoro del file modello chiamato Sheet1 in un file immagine chiamato SheetImage.jpg.

Di seguito è riportato il codice utilizzato dal componente per completare il compito. Converte Sheet1 in **Testbook.xlsx** in un file immagine per spiegare quanto sia facile questa conversione.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

std::string convert_u16_to_string(const U16String& u16str);

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheettoImageFile.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetImageType(ImageType::Jpeg);

    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputConvertWorksheettoImageFile.jpg");

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Utilizzare Aspose.Cells per convertire il foglio di lavoro in un file immagine per pagina**

Questo esempio mostra come utilizzare Aspose.Cells per convertire un foglio di lavoro da un modello di cartella di lavoro che ha diverse pagine in un file immagine per pagina.

### **Convertire Foglio di Lavoro in Immagine per Pagina**

Ho creato un nuovo workbook in Microsoft Excel e ho aggiunto alcuni dati al primo foglio di lavoro: **Testbook2.xlsx** (1 foglio di lavoro).

Ora, converti il foglio di lavoro del file modello in file immagine (un file per pagina). Poiché ho già creato l'applicazione console per eseguire il compito di copia, salterò quei passaggi di creazione dell'applicazione console e passerò direttamente ai passaggi di conversione del foglio di lavoro.

Di seguito è riportato il codice utilizzato dalla componente per completare il compito. Converte Sheet1 in Testbook2.xlsx in file immagine per pagina.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

std::u16string intToU16String(int value) {
    std::u16string result;
    if (value == 0) {
        result.push_back(u'0');
        return result;
    }
    while (value > 0) {
        result.insert(result.begin(), static_cast<char16_t>(u'0' + (value % 10)));
        value /= 10;
    }
    return result;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::u16string pageNum = intToU16String(j + 1);
        U16String fileName = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + U16String(pageNum.c_str()) + U16String(u".tif");
        sr.ToImage(j, fileName);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
