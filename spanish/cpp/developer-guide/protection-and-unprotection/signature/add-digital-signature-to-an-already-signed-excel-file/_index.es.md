---
title: Agregar firma digital a un archivo de Excel ya firmado con C++
linktitle: Agregar Firma Digital a un archivo de Excel que ya está firmado
type: docs
weight: 20
url: /es/cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Aprende cómo agregar firmas digitales a archivos de Excel firmados usando Aspose.Cells for C++. Mantén la integridad del documento con múltiples firmas.
keywords: Agregar firma digital a un archivo de Excel ya firmado, firmas digitales en C++, seguridad del documento de Excel
---

## **Escenarios de uso posibles**

Aspose.Cells proporciona el método [**Workbook::AddDigitalSignature(DigitalSignatureCollectionPtr digitalSignatureCollection)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/) para agregar firmas digitales a archivos de Excel ya firmados.

{{% alert color="primary" %}}

Tenga en cuenta que al agregar una firma digital a un documento de Excel ya firmado: si el documento original fue generado por Aspose.Cells, funciona correctamente. Sin embargo, si el documento fue creado por otros motores (por ejemplo, Microsoft Excel), Aspose.Cells for C++ no puede preservar exactamente la estructura del archivo después de cargar y volver a guardar, lo que puede invalidar las firmas existentes.

{{% /alert %}}

## **Cómo agregar una firma digital a un archivo de Excel ya firmado**

El siguiente ejemplo de código demuestra cómo usar [**Workbook::AddDigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/) para agregar firmas digitales a archivos de Excel firmados. El [archivo de Excel de ejemplo](50528280.xlsx) viene prefirmado. El [archivo de salida](50528281.xlsx) demuestra el resultado. Usamos un certificado de demostración [AsposeDemo.pfx](50528279.pfx) con contraseña **aspose**.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Código de muestra**

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
