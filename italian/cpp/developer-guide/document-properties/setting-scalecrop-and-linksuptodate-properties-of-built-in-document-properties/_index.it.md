---
title: Impostare le proprietà ScaleCrop e LinksUpToDate delle proprietà di documento integrate con C++
linktitle: Impostazione delle proprietà ScaleCrop e LinksUpToDate
type: docs
weight: 320
url: /it/cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Impara come impostare le proprietà ScaleCrop e LinksUpToDate delle proprietà di documento integrate usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**
[GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) e [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) sono due proprietà estese delle proprietà di documento integrate definite all’interno del formato OpenXml. Lo scopo di queste proprietà è:

## **1) ScaleCrop**
Questo elemento indica la modalità di visualizzazione dell'anteprima del documento. Imposta questo elemento su **TRUE** per abilitare il ridimensionamento dell'anteprima del documento per la visualizzazione. Imposta questo elemento su **FALSE** per abilitare il ritaglio dell'anteprima del documento per mostrare solo le sezioni che si adattano alla visualizzazione.

I valori possibili per questo elemento sono definiti dal tipo di dato booleano dello schema XML del W3C.

## **2) LinksUpToDate**
Questo elemento indica se i collegamenti ipertestuali in un documento sono aggiornati. Imposta questo elemento su **TRUE** per indicare che i collegamenti ipertestuali sono aggiornati. Imposta questo elemento su **FALSE** per indicare che i collegamenti ipertestuali sono obsoleti.

I valori possibili per questo elemento sono definiti dal tipo di dato booleano dello schema XML del W3C.

## **Screenshot che mostra queste proprietà all'interno del file app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Impostazione delle proprietà ScaleCrop e LinksUpToDate delle proprietà di documento integrate**
Il codice di esempio seguente imposta le proprietà estese di documento integrate [GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) e [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) del foglio di lavoro. Controlla il file excel di output [5115500.xlsx](#), generato con questo codice, cambiane l’estensione in .zip ed estrai il contenuto per visualizzare il file app.xml come mostrato nello screenshot sopra.

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

    // Instantiating a Workbook object.
    Workbook workbook;

    // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
    workbook.GetBuiltInDocumentProperties().SetScaleCrop(true);
    workbook.GetBuiltInDocumentProperties().SetLinksUpToDate(true);

    // Saving the Excel file.
    workbook.Save(outDir + u"output.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
