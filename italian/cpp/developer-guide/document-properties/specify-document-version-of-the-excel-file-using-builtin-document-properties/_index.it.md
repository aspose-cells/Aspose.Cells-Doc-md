---
title: Specifica la versione del documento del file Excel usando le proprietà di documento built in con C++
linktitle: Specifica la versione del documento
type: docs
weight: 20
url: /it/cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Impara come specificare la versione di un file Excel usando le proprietà di documento integrate con Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Puoi modificare **Numero di versione** di un file Excel facendo clic destro sul file, selezionando Proprietà > Dettagli e modificando il campo **Numero di versione**. Usa la proprietà [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/) per cambiarlo programmaticamente usando le API di Aspose.Cells.

## **Specifica la versione del documento del file Excel utilizzando le proprietà del documento integrato**

Il codice di esempio seguente crea una cartella di lavoro e modifica le proprietà di documento integrate che includono Titolo, Autori e Numero di versione. Consulta il file Excel di output [64716811.xlsx](#) generato dal codice e lo screenshot che mostra la modifica del numero di versione tramite la proprietà [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Codice di Esempio**

```cpp
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

    // Set the title
    bdpc.SetTitle(u"Aspose File Format APIs");

    // Set the author
    bdpc.SetAuthor(u"Aspose APIs Developers");

    // Set the document version
    bdpc.SetDocumentVersion(u"Aspose.Cells Version - 18.3");

    // Save the workbook in xlsx format
    wb.Save(u"outputSpecifyDocumentVersionOfExcelFile.xlsx", SaveFormat::Xlsx);

    std::cout << "Document properties set and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
