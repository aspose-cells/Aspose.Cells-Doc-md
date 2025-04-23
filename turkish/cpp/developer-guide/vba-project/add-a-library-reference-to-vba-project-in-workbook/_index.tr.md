---
title: C++ ile çalışma kitabında VBA proje referansı ekleyin
linktitle: VBA projesine kitap başvurusu ekleyin
type: docs
weight: 80
url: /tr/cpp/add-a-library-reference-to-vba-project-in-workbook/
description: Aspose.Cells for C++ kullanarak çalışma kitabında VBA projesine kütüphane referansları nasıl eklenir veya kaydedilir öğrenin.
---

{{% alert color="primary" %}}

Bazen, kitabın VBA projesine kütüphane başvurusu eklemeniz veya kaydetmeniz gerekebilir. Aspose.Cells [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/) yöntemini kullanarak bunu yapabilirsiniz.

{{% /alert %}}

## **Microsoft Excel'de VBA projelerine kütüphane başvurusu ekleyin**

Microsoft Excel'de, **Araçlar > Başvurular...** seçeneklerine tıklayarak VBA projelerine kütüphane başvurusu ekleyebilirsiniz.

## **Aspose.Cells kullanarak bir çalışma kitabında VBA projesine kütüphane başvurusu ekleyin**

Aşağıdaki örnek kod, [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/) yöntemini kullanarak çalışma kitabının VBA projesine iki kütüphane başvurusu ekler veya kaydeder.

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

    // Path of output excel file
    U16String outputPath = outDir + u"Output_out.xlsm";

    // Create a new workbook
    Workbook workbook;

    // Get the VBA project from the workbook
    VbaProject vbaProj = workbook.GetVbaProject();

    // Add registered references to the VBA project
    vbaProj.GetReferences().AddRegisteredReference(u"stdole", u"*\\G{00020430-0000-0000-C000-000000000046}#2.0#0#C:\\Windows\\system32\\stdole2.tlb#OLE Automation");
    vbaProj.GetReferences().AddRegisteredReference(u"Office", u"*\\G{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}#2.0#0#C:\\Program Files\\Common Files\\Microsoft Shared\\OFFICE14\\MSO.DLL#Microsoft Office 14.0 Object Library");

    // Save the workbook
    workbook.Save(outputPath);

    std::cout << "VBA project references added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
