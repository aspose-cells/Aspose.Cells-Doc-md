---  
title: VBA Projesinin Korunup Korunmadığını Kontrol Edin  
linktitle: VBA Projesinin Korunup Korunmadığını Bul  
type: docs  
weight: 20  
url: /tr/cpp/find-out-if-vba-project-is-protected/  
description: Aspose.Cells ile C++ kullanarak bir Excel dosyasının VBA projesinin korunduğunu kontrol edin.  
---  

## **C++ kullanarak VBA Projesinin Korunduğunu Kontrol Edin**

Excel dosyanızdaki VBA (Visual Basic Applications) Projesinin korunan olup olmadığını Aspose.Cells kullanarak [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/) özelliği ile öğrenebilirsiniz.

## **Örnek Kod**

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve ardından VBA projesinin korunup korunmadığını kontrol eder. Ardından VBA projesini korur ve tekrar kontrol eder. Lütfen referans olarak konsol çıkışını inceleyin. Koruma öncesinde, [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/) **false** döner, ancak korumadan sonra **true** döner.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook wb;

    // Access the VBA project of the workbook.
    VbaProject vbaProj = wb.GetVbaProject();

    // Check if VBA Project is Protected using IsProtected method.
    std::wcout << L"IsProtected - Before Protecting VBA Project: " << (vbaProj.IsProtected() ? L"True" : L"False") << std::endl;

    // Protect the VBA project.
    vbaProj.Protect(true, u"11");

    // Check if VBA Project is Protected using IsProtected method.
    std::wcout << L"IsProtected - After Protecting VBA Project: " << (vbaProj.IsProtected() ? L"True" : L"False") << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı referans için görüntülenmiştir.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
