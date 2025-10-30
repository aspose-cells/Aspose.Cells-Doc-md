---
title: C++でHTMLリンクターゲットの種類を変更する方法
linktitle: HTMLリンクのターゲットタイプを変更する
type: docs
weight: 320
url: /ja/cpp/change-the-html-link-target-type/
description: Aspose.Cells for C++を使用してHTMLリンクのターゲット属性をプログラムで制御し、ターゲットタイプを変更する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、HTMLリンクのターゲットタイプを変更できます。HTMLリンクは以下のようになります。

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

上記のHTMLリンクで、target属性が**_self**になっています。このtarget属性を[**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/)プロパティを使用して制御できます。このプロパティは以下の値を持つ[**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/)列挙型を受け入れます。

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

次のコードは、[**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/)プロパティの使用方法を示しています。リンクのターゲットタイプを**blank**に変更します。デフォルトでは**parent**が設定されます。

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

    // Path of input Excel file
    U16String inputPath = srcDir + u"Sample1.xlsx";

    // Path of output HTML file
    U16String outputPath = outDir + u"Output.out.html";

    // Create workbook
    Workbook workbook(inputPath);

    // Create HTML save options
    HtmlSaveOptions opts;
    opts.SetLinkTargetType(HtmlLinkTargetType::Self);

    // Save the workbook to HTML format
    workbook.Save(outputPath, opts);

    std::cout << "File saved: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
