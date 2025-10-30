---
title: Shape`den Bağlantı Noktalarını Alma ile C++
linktitle: Şekilden Bağlantı Noktalarını Al
type: docs
weight: 3500
url: /tr/cpp/get-connection-points-from-shape/
description: Aspose.Cells for C++ kullanarak şekil bağlantı noktalarını nasıl alacağınızı öğrenin.
---

Aspose.Cells, elektronik tablolardaki şekilleri yönetmek için zengin özellikler sunar. Bazen hizalama veya yerleştirme amaçlarıyla bir şeklin bağlantı noktalarını almak gerekebilir. Aşağıdaki kod, [Shape.GetConnectionPoints()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getconnectionpoints/) yöntemi kullanılarak bir şeklin bağlantı noktalarını listelemek için kullanılabilir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"sampleGetFonts.xlsx");

    Vector<Font> fonts = workbook.GetFonts();

    for (int i = 0; i < fonts.GetLength(); ++i)
    {
        std::cout << fonts[i].ToString().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

.
{{< app/cells/assistant language="cpp" >}}
