---
title: C++を使用して日付を日本の西暦に変換する方法を学びましょう。
linktitle: 日本の日付への変換
type: docs
weight: 350
url: /ja/cpp/convert-dates-to-japanese-dates/
description: Aspose.Cells for C++を使用して、西暦日付を日本の和暦日付に変換する方法を学びましょう。
---

{{% alert color="primary" %}}

日本の元号では、新しい天皇の即位により新しい元号が始まります。2019年5月1日、新しい天皇が即位し、平成時代が終了し、令和時代が始まりました。

{{% /alert %}}

Aspose.Cellsは、西暦日付を日本の元号に変換する方法を提供します。この変換では、元号の変化も考慮されます。次のコードスニペットは、西暦日付を含む[源のExcel](90112015.xlsx)ファイルを日本の和暦付きの[出力PDF](90112016.pdf)に変換します。画像の例も示します。

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)

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

    // Create load options for XLSX format
    LoadOptions options(LoadFormat::Xlsx);

    // Set culture info to Japanese
    options.SetLanguageCode(CountryCode::Japan);

    // Load the workbook with Japanese dates
    Workbook workbook(srcDir + u"JapaneseDates.xlsx", options);

    // Save the workbook as PDF
    workbook.Save(outDir + u"JapaneseDates.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF with Japanese dates!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
