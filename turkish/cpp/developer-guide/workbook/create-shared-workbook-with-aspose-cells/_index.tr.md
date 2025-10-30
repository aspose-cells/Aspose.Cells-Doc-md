---  
title: Aspose.Cells kullanarak C++ ile Paylaşılan Çalışma Kitabı Oluşturun  
linktitle: Aspose.Cells ile Paylaşılan Çalışma Kitabı Oluşturma  
type: docs  
weight: 40  
url: /tr/cpp/create-shared-workbook-with-aspose-cells/  
description: Aspose.Cells kullanarak paylaşılan bir çalışma kitabı nasıl oluşturulur öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Microsoft Excel, aşağıdaki ekran görüntüsünde gösterildiği gibi çalışma kitabını paylaşmanıza izin verir. Çalışma kitabını paylaştığınızda, birden fazla kullanıcı ağ üzerinde çalışma kitabını düzenleyebilir. Aspose.Cells, [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/) özelliği ile paylaşılmış bir çalışma kitabı oluşturmanıza olanak tanır.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Aspose.Cells ile Paylaşılan Çalışma Kitabı Oluşturma**  

Aşağıdaki örnek kod, [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/) özelliğini **true** olarak ayarlayarak paylaşılan bir çalışma kitabı oluşturur. [Çıktı Excel dosyasını](55541786.xlsx) Microsoft Excel'de açtığınızda, bu ekran görüntüsüyle gösterildiği gibi **Paylaşılan** olarak göreceksiniz.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Örnek Kod**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create Workbook object
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>();

    // Share the Workbook
    wb->GetSettings().SetShared(true);

    // Save the Shared Workbook
    wb->Save(u"outputSharedWorkbook.xlsx");

    std::cout << "Shared workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
