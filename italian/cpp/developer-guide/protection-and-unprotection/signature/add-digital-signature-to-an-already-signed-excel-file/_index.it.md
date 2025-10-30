---
title: Aggiungi Firma Digitale a un file Excel già firmato con C++
linktitle: Aggiungere firma digitale a un file Excel già firmato
type: docs
weight: 20
url: /it/cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Impara come aggiungere firme digitali ai file Excel firmati usando Aspose.Cells for C++. Mantieni l integrità del documento con firme multiple.
keywords: Aggiungi Firma Digitale a un file Excel già firmato, firme digitali C++, sicurezza del documento Excel
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells fornisce il metodo [**Workbook::AddDigitalSignature(DigitalSignatureCollectionPtr digitalSignatureCollection)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/) per aggiungere firme digitali a file Excel già firmati.

{{% alert color="primary" %}}

Nota: durante l'aggiunta di una firma digitale a un documento Excel già firmato, se il documento originale è stato generato da Aspose.Cells, funziona correttamente. Tuttavia, se il documento è stato creato da altri motori (ad esempio Microsoft Excel), Aspose.Cells for C++ potrebbe non preservare la struttura esatta del file dopo il caricamento e la risalvataggio, invalidando le firme esistenti.

{{% /alert %}}

## **Come Aggiungere una Firma Digitale a un Documento Excel Già Firmato**

Il seguente esempio di codice dimostra l'uso di [**Workbook::AddDigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/) per aggiungere firme digitali ai file Excel firmati. Il [file Excel di esempio](50528280.xlsx) viene pre-firmato. Il [file di output](50528281.xlsx) mostra il risultato. Usiamo un certificato demo [AsposeDemo.pfx](50528279.pfx) con password **aspose**.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Certificate and workbook paths
    U16String certFilePath = srcDir + u"AsposeDemo.pfx";
    U16String inputFilePath = srcDir + u"sampleDigitallySignedByCells.xlsx";
    U16String outputFilePath = outDir + u"outputDigitallySignedByCells.xlsx";

    // Load digitally signed workbook
    Workbook workbook(inputFilePath);

    // Create digital signature collection
    DigitalSignatureCollection dsCollection;

    // Create digital signature using PFX certificate
    U16String password = u"aspose";
    U16String comments = u"Aspose.Cells added new digital signature in existing digitally signed workbook.";
    DigitalSignature signature(certFilePath, password, comments, Date());

    // Add signature to collection
    dsCollection.Add(signature);

    // Apply digital signatures to workbook
    workbook.AddDigitalSignature(dsCollection);

    // Save modified workbook
    workbook.Save(outputFilePath);

    std::cout << "Digital signature added successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
