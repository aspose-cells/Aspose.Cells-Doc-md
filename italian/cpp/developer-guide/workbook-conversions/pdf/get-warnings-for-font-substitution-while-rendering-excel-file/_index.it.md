---
title: Ottieni avvisi per la Sostituzione dei Caratteri durante il Rendering del File Excel con C++
linktitle: Ottieni avvisi per la Sostituzione dei Caratteri
type: docs
weight: 230
url: /it/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Impara come ottenere avvisi per la sostituzione dei caratteri durante il rendering di file Excel in PDF usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A volte, durante la conversione di un file Microsoft Excel in PDF, Aspose.Cells sostituisce i font. Aspose.Cells fornisce una funzione che permette agli sviluppatori di sapere quale particolare font è stato sostituito scatenando un avviso. Si tratta di una funzionalità utile che può aiutarti a capire perché un PDF generato da Aspose.Cells appare diverso dal file di origine di Microsoft Excel, in modo da poter adottare azioni appropriate. Ad esempio, installare i font mancanti in modo che i risultati della conversione siano uguali.

{{% /alert %}}

Per ottenere avvisi per la sostituzione dei caratteri durante il rendering di file Excel in PDF, implementa l'interfaccia `IWarningCallback` e imposta la proprietà `PdfSaveOptions.WarningCallback` con la tua interfaccia implementata.

La schermata sottostante mostra un file Excel di origine che utilizzeremo nel codice seguente. Contiene del testo nelle celle A6 e A7 con caratteri che non vengono visualizzati correttamente in Microsoft Excel.

|**Non tutti i font vengono visualizzati correttamente**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|

Aspose.Cells sostituirà i font nelle celle A6 e A7 con font appropriati come mostrato di seguito.

|**Font sostituiti**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|

## **Scarica file di origine e PDF di output**
Puoi scaricare il file Excel di origine e il PDF di output dai link sottostanti:

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)

## **Codice**
Il seguente codice implementa `IWarningCallback` e imposta la proprietà `PdfSaveOptions.WarningCallback` con l'interfaccia implementata. Ora, ogni volta che un carattere verrà sostituito in una cella qualsiasi, Aspose.Cells genererà un avviso all'interno del metodo `WarningCallback.Warning()`.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GetWarningsForFontSubstitution : public IWarningCallback
{
public:
    void Warning(WarningInfo& info) override
    {
        if (info.GetType() == ExceptionType::FontSubstitution)
        {
            std::cout << "WARNING INFO: " << info.GetDescription().ToUtf8() << std::endl;
        }
    }

    static void Run()
    {
        U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
        U16String outDir(u"..\\Data\\02_OutputDirectory\\");
        Workbook workbook(srcDir + u"source.xlsx");
        PdfSaveOptions options;
        auto callback = std::make_shared<GetWarningsForFontSubstitution>();
        options.SetWarningCallback(callback.get());
        workbook.Save(outDir + u"output_out.pdf", options);
        std::cout << "PDF saved successfully with font substitution warnings!" << std::endl;
    }
};

int main()
{
    Aspose::Cells::Startup();
    GetWarningsForFontSubstitution::Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Output**
Dopo la conversione del file Excel di origine in PDF, gli avvisi vengono visualizzati sulla console di debug come segue:

{{< highlight java >}}
WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].
WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].
{{< /highlight >}}

{{% alert color="primary" %}}

Se il tuo foglio di calcolo contiene formule, è meglio chiamare il metodo `Workbook.CalculateFormula` subito prima di rendere il foglio di calcolo in formato PDF. Questo assicurerà che i valori dipendenti dalle formule vengano ricalcolati e vengano resi correttamente nel PDF.

{{% /alert %}}
