---
title: Рендер листа в графический контекст с C++
linktitle: Отобразить Рабочий лист на графический контекст
type: docs
weight: 300
url: /ru/cpp/render-worksheet-to-graphic-context/
description: Узнайте, как рендерить лист в графический контекст с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells теперь может рендерить лист в графический контекст. Графический контекст может быть любым: изображением, экраном или принтером и т.д. Используйте один из следующих двух методов для рендера листа в графический контекст.

- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)
- [**SheetRender::ToImage(int pageIndex, Graphics* g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)

{{% /alert %}}

Следующий код показывает, как использовать Aspose.Cells для рендеринга листа в графический контекст. После выполнения кода весь лист будет напечатан, а пустое пространство заполняется синим цветом, и изображение сохраняется как файл **OutputImage_out_.png**. Любой исходный файл Excel можно использовать для этого кода. Также ознакомьтесь с комментариями внутри кода для лучшего понимания.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleBook.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(ImageType::Png);

    SheetRender sr(worksheet, opts);
    sr.ToImage(0, outDir + u"OutputImage_out.png");

    Aspose::Cells::Cleanup();
}
```
