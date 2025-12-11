---
title: Add Icons to Worksheet with C++
linktitle: Managing Icons
type: docs
weight: 100
url: /cpp/insert-svg-to-excel/
description: Learn how to add icons to Excel worksheets using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Add Icons to a Worksheet in Aspose.Cells

If you need to use [Aspose.Cells](https://products.aspose.com/cells/) to add icons to an Excel file, this document can help you.

The Excel interface corresponding to the insert‑icon operation is as follows:

![](1.png)

- Select the position of the icon to be inserted in the worksheet.  
- Click *Insert* → *Icons*.  
- In the window that opens, select the icon inside the red rectangle shown in the figure above.  
- Click *Insert*; the icon will be inserted into the Excel file.

The effect is as follows:

![](2.png)

Here we have prepared **sample code** to help you insert icons using [Aspose.Cells](https://products.aspose.com/cells/). There is also a required sample file ([sample.xlsx]) and an icon resource file ([icon.zip]). We used the Excel interface to insert an icon that has the same display effect as the resource file in the sample file.

### C++

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName = u"icon.svg";
    std::ifstream fsSource(fileName.ToUtf8(), std::ios::binary);
    if (!fsSource) {
        std::cerr << "Failed to open file: " << fileName.ToUtf8() << std::endl;
        return -1;
    }

    fsSource.seekg(0, std::ios::end);
    size_t fileSize = fsSource.tellg();
    fsSource.seekg(0, std::ios::beg);

    std::vector<uint8_t> bytes(fileSize);
    fsSource.read(reinterpret_cast<char*>(bytes.data()), fileSize);
    fsSource.close();

    Aspose::Cells::Vector<uint8_t> asposeBytes(bytes.size());
    if (!bytes.empty()) {
        memcpy(asposeBytes.GetData(), bytes.data(), bytes.size());
    }

    Workbook workbook(u"sample.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    sheet.GetShapes().AddIcons(3, 0, 7, 0, 100, 100, asposeBytes, Aspose::Cells::Vector<uint8_t>());

    Cell c = sheet.GetCells().Get(8, 7);
    c.PutValue(u"Insert via Aspose.Cells");
    Style s = c.GetStyle();
    s.GetFont().SetColor(Color::Blue());
    c.SetStyle(s);

    workbook.Save(u"sample2.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

When you execute the above code in your project, you will get the following result:

![](3.png)
{{< app/cells/assistant language="cpp" >}}
