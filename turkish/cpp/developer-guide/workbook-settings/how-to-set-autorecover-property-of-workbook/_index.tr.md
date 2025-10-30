---
title: WorkBook un Otomatik Kurtarma Özelliğini C++ ile nasıl ayarlayacağınızı öğrenin
linktitle: Çalışma Kitabının Otomatik Kurtarma Özelliğini Ayarlamak
type: docs
weight: 220
url: /tr/cpp/how-to-set-autorecover-property-of-workbook/
description: Bir çalışma kitabının Otomatik Kurtarma özelliğini etkinleştirmek veya devre dışı bırakmak için Aspose.Cells for C++ kullanmayı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak, bir çalışma kitabının Otomatik Kurtarma özelliğini ayarlayabilirsiniz. Bu özelliğin varsayılan değeri **true**'dur. Bunu bir çalışma kitabında **false** olarak ayarladığınızda, Microsoft Excel, AutoRecover (Otomatik Kaydetme) fonksiyonunu devre dışı bırakır.

Aspose.Cells, bu seçeneği etkinleştirmek veya devre dışı bırakmak için [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) özelliğini sağlar.

{{% /alert %}}

Aşağıdaki kod, çalışma kitabının [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) özelliğinin nasıl kullanılacağını açıklar. Öncelikle bu özelliğin varsayılan değeri olan **true** okunur, ardından **false** olarak ayarlanır ve çalışma kitabı kaydedilir. Ardından, tekrar okunur ve bu özelliğin değeri, şu anda **false** olarak okunur.

## C++ ile WorkBook'un Otomatik Kurtarma Özelliğini Ayarlama Kodu

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

    // Create workbook object
    Workbook workbook;

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook.GetSettings().GetAutoRecover() << std::endl;

    // Set AutoRecover property to false
    workbook.GetSettings().SetAutoRecover(false);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    // Read the saved workbook again
    Workbook workbook2(outDir + u"output_out.xlsx");

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook2.GetSettings().GetAutoRecover() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Çıktı**

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
