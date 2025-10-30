---
title: Convertire file XLSX in formato PDF con C++
linktitle: Converti il file XLSX nel Formato PDF
type: docs
weight: 30
url: /it/cpp/convert-xlsx-file-to-pdf-format/
description: Impara come convertire i file Excel in formato PDF utilizzando Aspose.Cells for C++ con alta precisione e accuratezza.
---

{{% alert color="primary" %}}

PDF (Portable Document Format) rappresenta documenti indipendentemente dal software, hardware e sistema operativo utilizzati per creare quei documenti. Un file PDF può contenere qualsiasi combinazione di testo, grafica e immagini in modo indipendente dal dispositivo e dalla risoluzione. I file PDF sono spesso compressi, quindi occupano meno spazio rispetto al file originale.

A volte, è necessario convertire un file Microsoft Excel in PDF. Per questo, è necessario un metodo rapido, sicuro, preciso e affidabile che consenta di distribuire i documenti PDF in tutto il mondo. Ci sono numerosi strumenti di conversione che possono eseguire questa operazione. Ma è importante assicurarsi che il layout del documento Excel originale sia mantenuto nel file PDF di output. Immagini, grafici, forme, formattazione dei dati, font, attributi, colori, impostazioni della pagina, orientamento del testo, bordi, grafici, ecc., devono essere resi con precisione e accuratezza. [Aspose.Cells](https://products.aspose.com/cells/cpp/) garantisce una conversione ad alta fedeltà.

Questo documento è progettato per fornire una comprensione completa di come un documento Microsoft Excel (contenente immagini, grafici, formattazione, ecc.) possa essere convertito in PDF. A tal fine, mostra come creare una semplice applicazione console in C++ che converte un file Excel in PDF utilizzando l'API di Aspose.Cells. La conversione viene eseguita con un alto grado di precisione e accuratezza.

{{% /alert %}}

## **Conversione di Excel in PDF**

Questo esempio utilizza un file Excel (SampleInput.xlsx) come modello. Il libro contiene fogli di lavoro con grafici e immagini. Ogni foglio contiene diversi tipi di formattazione utilizzando font, attributi, colori, effetti di ombreggiatura e bordi. Nel primo foglio c’è un grafico a colonne e nell’ultimo un’immagine.

### **Il file Excel di modello**

Il file modello ha tre fogli di lavoro, inclusi grafici e immagini come Media. Il primo foglio di lavoro contiene grafici, e l’ultimo foglio di lavoro ha un’immagine, come mostrato nelle schermate di seguito.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Il primo foglio di lavoro **(Previsioni di vendita)**|Il secondo foglio di lavoro **(Rapporto di vendita)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Il terzo foglio di lavoro **(Inserimento dati)**|L'ultimo foglio di lavoro **(Immagine)**|

### **Processo di conversione**

```c++
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

    try
    {
        // Get the template excel file path
        U16String designerFile = srcDir + u"SampleInput.xlsx";

        // Specify the pdf file path
        U16String pdfFile = outDir + u"Output.out.pdf";

        // Open the template excel file
        Workbook wb(designerFile);

        // Save the pdf file
        wb.Save(pdfFile, SaveFormat::Pdf);

        std::cout << "PDF file saved successfully!" << std::endl;
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare il metodo [Workbook.CalculateFormula](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) proprio prima di esportare il foglio di calcolo in PDF. In questo modo si garantisce che i valori dipendenti dalla formula siano ricalcolati e corretti siano visualizzati nel PDF.

{{% /alert %}}

### **Risultato**

Quando il codice sopra è stato eseguito, viene creato un file PDF nella cartella Files della directory dell'applicazione.
Gli screenshot seguenti mostrano le pagine PDF. Nota che gli header e i footer sono mantenuti anche nel file PDF di output.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Il primo foglio di lavoro **(Previsioni di vendita)**|Il secondo foglio di lavoro **(Rapporto di vendita)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Il terzo foglio di lavoro **(Inserimento dati)**|L'ultimo foglio di lavoro **(Immagine)**|
{{< app/cells/assistant language="cpp" >}}
