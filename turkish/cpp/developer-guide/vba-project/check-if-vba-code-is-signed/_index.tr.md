---  
title: VBA Kodunun İmzalanıp İmzalanmadığını Kontrol Edin  
linktitle: VBA Kodunun İmzalı Olup Olmadığını Kontrol Et  
type: docs  
weight: 100  
url: /tr/cpp/check-if-vba-code-is-signed/  
description: Aspose.Cells kullanarak Excel dosyasındaki VBA kodunun imzalanıp imzalanmadığını nasıl kontrol edeceğinizi öğrenin.  
---  

{{% alert color="primary" %}}  

Aspose.Cells, kullanıcının VBA kod projesinin imzalanıp imzalanmadığını kontrol etmesine olanak tanır. Bu amaçla, [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/) özelliğini kullanın.  

{{% /alert %}}  

 Aşağıdaki kod, VBA kodunun imzalanıp imzalanmadığını [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/) özelliği kullanarak nasıl kontrol edeceğinizi açıklar. Bu kodu test etmek için herhangi bir Excel dosyasını kullanabilirsiniz. Test amacıyla, bu kodda kullanılan [bu excel dosyasını](5115032.xlsm) kullanabilirsiniz.  

## ** C++ ile VBA Kodunun İmzalanıp İmzalanmadığını Kontrol Edin**  

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleVBAProjectSigned.xlsm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Check if the VBA code project is signed
    std::wcout << U"Is VBA Code Project Signed: " << workbook.GetVbaProject().IsSigned() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  

## Konsol Çıkışı  

Aşağıda sağlanan bağlantıdaki [örnek excel dosyası](5115032.xlsm) kullanılarak yukarıdaki kodun konsol çıktısı bulunmaktadır.  

{{< highlight java >}}  

Is VBA Code Project Signed: True  

{{< /highlight >}}  
