---
title: XLSB revizyonunu XLSM ye dönüştürme ile C++
linktitle: XLSB Revizyonunu XLSM ye Dönüştür
type: docs
weight: 290
url: /tr/cpp/convert-revision-of-xlsb-to-xlsm/
description: Aspose.Cells kullanarak XLSB dosyalarının revizyonlarını XLSM formatına dönüştürmeyi öğrenin.
---

{{% alert color="primary" %}} 

Aspose.Cells, XLSB dosyalarının revizyonlarını tam anlamıyla XLSM dosyalarına dönüştürmeyi desteklemektedir. Revizyonlar \xl\revisions dizisinde bulunur. Dosyanın uzantısını ZIP yaparak görüntüleyebilirsiniz. \xl\revisions dizisi, .bin uzantılı dosyalar içerir.

XLSB dosyanızı Aspose.Cells kullanarak XLSM dosyasına dönüştürdüğünüzde, bu .bin dosyaları başarıyla .xml dosyalarına dönüşür; bu iki ekran görüntüsüyle gösterilmektedir.

{{% /alert %}} 

Aşağıdaki kod örneği, Aspose.Cells kullanarak XLSB dosyasını XLSM biçimine nasıl dönüştüreceğinizi gösterir.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsb";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Save Workbook to XLSM format
    workbook.Save(outDir + u"output_out.xlsm", SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully in XLSM format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
