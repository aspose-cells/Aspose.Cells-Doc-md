---
title: Çalışma Kitabının Yönetilmeyen Kaynaklarını C++ ile Serbest Bırakın
linktitle: Çalışma Kitabının Yönetilmeyen Kaynaklarını Serbest Bırak
type: docs
weight: 310
url: /tr/cpp/release-unmanaged-resources-of-the-workbook/
description: Aspose.Cells kullanarak C++ ile Çalışma Kitabının yönetilmeyen kaynaklarını nasıl serbest bırakacağınızı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) nesnesinin yönetilmeyen kaynaklarını serbest bırakmak için [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) yöntemi sağlar. Temizleme deseni, yalnızca dosya ve boru tanıtıcıları, kayıt defteri tanıtıcıları, bekleme tanıtıcıları veya yönetilmeyen bellek bloklarına erişen nesneler için kullanılır. Bu, çöp toplayıcısının kullanılmayan yönetilen nesneleri geri kazanmadaki çok etkili olmasından dolayıdır, ancak yönetilmeyen nesneleri geri kazanamaz.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) nesnesi artık *IDisposable* arayüzünü uygular ve bu arayüz tek bir yöntem [**Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) içerir. [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) yöntemini doğrudan çağırabilir veya bu yöntemi otomatik çağırmak için *Using* ifadesini kullanabilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb1;

    // Call Dispose method
    wb1.Dispose();

    // Call Dispose method via RAII (Resource Acquisition Is Initialization)
    {
        Workbook wb2;
        // Any other code goes here
    } // wb2 is automatically disposed when it goes out of scope

    Aspose::Cells::Cleanup();
}
```
