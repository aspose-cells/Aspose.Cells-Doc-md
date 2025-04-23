---
title: Importa XML in una cartella di lavoro Excel con C++
linktitle: Mappe XML
type: docs
weight: 210
url: /it/cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Importa dati da un file di dati XML in Microsoft Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells permette di importare la mappa XML all’interno della cartella di lavoro usando il metodo [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/). Puoi importare la mappa XML con Microsoft Excel seguendo questi passaggi:

- Seleziona la scheda **Sviluppatore**.
- Fai clic su **Importa** nella sezione XML e segui i passaggi richiesti.

Dovrai fornire i tuoi dati XML per completare l'importazione. Ecco un [esempio di dati XML](5115037.txt) che puoi utilizzare per i test.

{{% /alert %}}

## **Importa la mappa XML utilizzando Microsoft Excel**

La seguente schermata mostra come importare la mappa XML utilizzando Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Importa la mappa XML utilizzando Aspose.Cells**

Il seguente esempio di codice mostra come utilizzare il metodo [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/). Genera il [file Excel di output](5115036.xlsx) come mostrato in questo screenshot.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```c++
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

    // Create a workbook
    Workbook workbook;

    // URL that contains your XML data for mapping
    U16String XML(u"http://www.aspose.com/docs/download/attachments/434475650/sampleXML.txt");

    // Import your XML Map data starting from cell A1
    workbook.ImportXml(XML, u"Sheet1", 0, 0);

    // Save workbook
    U16String outputPath = outDir + u"output_out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully with imported XML data!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Aggiungi mappa XML all'interno del foglio di lavoro utilizzando il metodo XmlMapCollection.Add](/cells/it/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Esporta dati XML collegati alla mappa XML all'interno del Workbook](/cells/it/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Trova il nome dell'elemento radice della mappa XML](/cells/it/cpp/find-the-root-element-name-of-xml-map/)
- [Collega le celle agli elementi della mappa XML](/cells/it/cpp/link-cells-to-xml-map-elements/)
