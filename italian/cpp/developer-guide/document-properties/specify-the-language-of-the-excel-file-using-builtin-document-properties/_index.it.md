---
title: Specifica la lingua del file Excel usando le proprietà di documento built in con C++
linktitle: Specifica la lingua del file Excel
type: docs
weight: 30
url: /it/cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
description: Impara come cambiare la lingua di un file Excel programmaticamente usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Puoi cambiare la lingua di un file Excel facendo clic destro sul file, selezionando Proprietà > Dettagli e modificando il campo Lingua. Usa la proprietà [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/) per cambiarla programmaticamente usando le API di Aspose.Cells.

## **Specificare la lingua del file Excel utilizzando le proprietà di documento incorporate**

Il codice di esempio seguente crea una cartella di lavoro e modifica la proprietà di documento integrata chiamata Lingua. Consulta il file Excel di output [64716891.xlsx](#) generato dal codice e lo screenshot che mostra il campo Lingua modificato tramite la proprietà [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/).

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Properties;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access built-in document property collection
    BuiltInDocumentPropertyCollection bdpc = wb.GetBuiltInDocumentProperties();

    // Set the language of the Excel file
    bdpc.SetLanguage(u"German, French");

    // Save the workbook in xlsx format
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx", SaveFormat::Xlsx);

    std::cout << "Language set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
