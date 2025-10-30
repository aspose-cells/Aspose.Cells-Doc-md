---
title: Kendini Kapanan Etiketleri Tanıma C++ ile
linktitle: Kendiliğinden Kapalı Etiketleri Tanıma
type: docs
weight: 120
url: /tr/cpp/recognise-self-closing-tags/
description: Aspose.Cells ile HTML’de kendini kapatan etiketleri nasıl yönetileceğinizi öğrenin ve C++ kullanın.
---

HTML can have a variety of tag formats for empty tags like `<td></td>` or `<td/>`. Aspose.Cells supports both these formats now, whereas earlier it was supporting only `<td></td>` like tags. This feature can be tested by converting the attached sample HTML file to an Excel file. The sample HTML file and output Excel file can be downloaded from the following links for testing.

[sampleSelfClosingTags.html](sampleSelfClosingTags)

[outsampleSelfClosingTags.xlsx](73990156.xlsx)

## **Örnek Kod**

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

    // Set HTML load options and keep precision true
    HtmlLoadOptions loadOptions(LoadFormat::Html);

    // Load sample source file
    Workbook wb(srcDir + u"sampleSelfClosingTags.html", loadOptions);

    // Save the workbook
    wb.Save(outDir + u"outsampleSelfClosingTags.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
