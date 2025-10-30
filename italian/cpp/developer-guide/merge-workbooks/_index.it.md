---
title: Combinare più workbook in un singolo workbook con C++
linktitle: Unione Cartelle di Lavoro
type: docs
weight: 66
url: /it/cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Impara come combinare più workbook in un singolo workbook utilizzando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A volte, è necessario combinare workbook con contenuti vari come immagini, grafici e dati in un singolo workbook. Aspose.Cells supporta questa funzionalità. Questo esempio mostra come creare un'applicazione console in Visual Studio e combinare i workbook con alcune righe di codice semplici utilizzando Aspose.Cells.

{{% /alert %}}

## **Unione Cartelle di Lavoro con Immagini e Grafici**

Il codice di esempio unisce due cartelle di lavoro in una singola cartella di lavoro utilizzando Aspose.Cells. Il codice carica le cartelle di lavoro di origine, utilizza il metodo [**Workbook::Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/) per combinarle e salva la cartella di lavoro di output.

### **Cartelle di Lavoro di Origine**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Cartelle di Lavoro di Output**

- [combined.xlsx](5473095.xlsx)

### **Screenshot**

Di seguito sono riportati gli screenshot delle cartelle di lavoro di origine e di output.

{{% alert color="primary" %}}

Puoi utilizzare qualsiasi cartella di lavoro di origine. Queste immagini sono solo a scopo illustrativo.

{{% /alert %}}

**Il primo foglio di lavoro della cartella di lavoro dei grafici - sovrapposto** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Secondo foglio di lavoro della cartella di lavoro dei grafici - linea** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Primo foglio di lavoro della cartella di immagini - immagine** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Tutti e tre i fogli di lavoro nel libro combinato - sovrapposti, linea, immagine** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

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

    // Path of the first source excel file
    U16String sourceFile1 = srcDir + u"SampleChart.xlsx";

    // Path of the second source excel file
    U16String sourceFile2 = srcDir + u"SampleImage.xlsx";

    // Open the first excel file.
    Workbook sourceBook1(sourceFile1);

    // Open the second excel file.
    Workbook sourceBook2(sourceFile2);

    // Combining the two workbooks
    sourceBook1.Combine(sourceBook2);

    // Define the output file path
    U16String outputFilePath = srcDir + u"Combined.out.xlsx";

    // Save the target book file.
    sourceBook1.Save(outputFilePath);

    std::cout << "Workbooks combined and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Unisci più fogli di lavoro in un'unica scheda](/cells/it/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Unire file](/cells/it/cpp/merge-files/)
{{< app/cells/assistant language="cpp" >}}
