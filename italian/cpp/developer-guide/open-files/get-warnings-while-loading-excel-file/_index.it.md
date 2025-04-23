---
title: Ottieni avvisi durante il caricamento del file Excel con C++
linktitle: Ottieni Avvertimenti durante il Caricamento del File Excel
type: docs
weight: 110
url: /it/cpp/get-warnings-while-loading-excel-file/
description: Impara come catturare e gestire avvisi durante il caricamento di file Excel usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

 A volte l'utente cerca di caricare un workbook che è in qualche modo corrotto ma ancora caricabile. In tali casi, Aspose.Cells genera avvisi durante il caricamento del workbook. Puoi catturare questi avvisi implementando l'interfaccia [**IWarningCallback**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/) e impostando la proprietà [**LoadOptions.GetWarningCallback()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getwarningcallback/).

## **Ottieni avvisi durante il caricamento del file Excel**

 Il codice di esempio seguente spiega come ottenere avvisi durante il caricamento di un file Excel. Il codice carica il [file Excel di esempio](sampleDuplicateDefinedName.xlsx), che genera un avviso [**DuplicateDefinedName**](https://reference.aspose.com/cells/cpp/aspose.cells/warningtype/) durante il caricamento. Questo avviso viene quindi catturato dal metodo [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/warning/), che stampa i messaggi di avviso sulla console. Il codice quindi salva il workbook come [file Excel di output](outputDuplicateDefinedName.xlsx). Se si apre il file Excel di esempio in Microsoft Excel, verrà visualizzato anche questo avviso, come mostrato nello screenshot qui sotto. Si prega di verificare anche l'output della console del codice sottostante per una migliore comprensione.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class WarningCallback : public IWarningCallback {
public:
    void Warning(WarningInfo& warningInfo) override {
        if (warningInfo.GetType() == ExceptionType::DefinedName) {
            std::cout << "Defined Name Warning: " << warningInfo.GetDescription().ToUtf8() << std::endl;
        }
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    LoadOptions options;
    WarningCallback callback;
    options.SetWarningCallback(&callback);

    U16String inputFilePath = srcDir + u"sampleDuplicateDefinedName.xlsx";
    Workbook book(inputFilePath, options);

    U16String outputFilePath = outDir + u"outputDuplicateDefinedName.xlsx";
    book.Save(outputFilePath);

    std::cout << "Workbook saved successfully with warning handling!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Output della console**

Questo è l'output della console del codice sopra quando eseguito con il [file excel di esempio fornito](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
