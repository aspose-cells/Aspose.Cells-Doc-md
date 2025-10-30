---
title: C++で安全なPDFドキュメントを作成する
linktitle: セキュアなPDFドキュメント
type: docs
weight: 120
url: /ja/cpp/secure-pdf-documents/
description: Aspose.CellsをC++とともに使用して、所有者およびユーザーパスワードでPDFドキュメントのセキュリティを設定する方法を学びます。
---

{{% alert color="primary" %}}

開発者は、暗号化されたPDFファイルと作業する必要がある場合があります。

- ドキュメントをオーナーパスワードとユーザーパスワードでセキュリティ保護して、誰もがそれを開けなくする。
- ドキュメントを開いた後にドキュメントに制限や権限を設定します。例: ドキュメントの内容を印刷または抽出できるかどうかを制限します。

この記事では、スプレッドシートをPDFに保存する際にPDFセキュリティオプションを渡す方法について説明します。

{{% /alert %}}

Aspose.Cellsはセキュリティを扱うための[**PdfSecurityOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)を提供します。PDFに保存する際に所有者パスワードとユーザーパスワードを設定できます。暗号化されたPDFドキュメントを開くには、所有者またはユーザーパスワードが必要です。

- ユーザーパスワードはnullまたは空の文字列にすることができます。この場合、ユーザーがPDFドキュメントを開く際にパスワードが要求されません。
- 正しい所有者パスワードを使ってPDFドキュメントを開くと、アクセス制限なしでドキュメントに完全にアクセスできます。
- 正しいユーザーパスワードでPDFドキュメントを開く（またはユーザーパスワードのないドキュメントを開く）と、指定された権限に応じて限定されたアクセスが可能です。

以下のサンプルコードは、Aspose.CellsでPDFをセキュアにする方法を説明しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;
using namespace Aspose::Cells::Rendering::PdfSecurity;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"securepdf_test.out.pdf";

    // Open an Excel file
    Workbook workbook(inputFilePath);

    // Instantiate PDFSaveOptions to manage security attributes
    PdfSaveOptions saveOption;

    // Create and configure PDF security options
    PdfSecurityOptions securityOptions;
    securityOptions.SetUserPassword(u"user");
    securityOptions.SetOwnerPassword(u"owner");
    securityOptions.SetExtractContentPermission(false);
    securityOptions.SetPrintPermission(false);

    // Assign security options to save options
    saveOption.SetSecurityOptions(securityOptions);

    // Save the PDF document with encrypted settings
    workbook.Save(outputFilePath, saveOption);

    std::cout << "PDF saved with security settings successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、これをPDFにレンダリングする直前に[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)を呼び出すのが最良です。これにより、数式に依存した値が再計算され、正しい値がPDFにレンダリングされます。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
