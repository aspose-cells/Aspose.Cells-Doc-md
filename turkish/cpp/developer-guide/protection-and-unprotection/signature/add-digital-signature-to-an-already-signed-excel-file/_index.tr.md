---
title: Zaten imzalanmış Excel dosyasına dijital imza ekleme (C++)
linktitle: Zaten İmzalanmış Bir Excel Dosyasına Dijital İmza Eklemek
type: docs
weight: 20
url: /tr/cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Aspose.Cells for C++ kullanarak imzalı Excel dosyalarına dijital imza eklemeyi öğrenin. Çoklu imzalarla belge bütünlüğünü koruyun.
keywords: İmzalısına dijital imza eklemek, C++ dijital imzalar, Excel belge güvenliği
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, zaten imzalanmış Excel dosyalarına dijital imza eklemek için [**Workbook::AddDigitalSignature(DigitalSignatureCollectionPtr digitalSignatureCollection)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/) yöntemini sağlar.

{{% alert color="primary" %}}

Lütfen, zaten imzalanmış bir Excel belgesine dijital imza eklerken: orijinal belge Aspose.Cells ile oluşturulduysa düzgün çalışır. Ancak, belge başka motorlar (örneğin Microsoft Excel) tarafından oluşturulduysa, Aspose.Cells for C++ yükleme ve yeniden kaydetme işleminden sonra tam dosya yapısını koruyamaz, bu da mevcut imzaları geçersiz kılabilir.

{{% /alert %}}

## **Zaten İmzalanmış Bir Excel Dosyasına Dijital İmza Eklemek**

Aşağıdaki kod örneği, imzalanmış Excel dosyalarına dijital imza eklemek için [**Workbook::AddDigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/)'ın kullanımını gösterir. [Örnek Excel dosyası](50528280.xlsx) önceden imzalanmıştır. [Çıktı dosyası](50528281.xlsx) sonucu gösterir. Demo sertifikası [AsposeDemo.pfx](50528279.pfx) şifresi ile **aspose** kullanıyoruz.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Örnek Kod**

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
