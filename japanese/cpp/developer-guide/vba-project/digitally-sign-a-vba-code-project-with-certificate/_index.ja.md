---
title: C++で証明書を使用してVBAコードプロジェクトに電子署名を付与します
linktitle: 証明書でVBAコードプロジェクトにデジタル署名する
type: docs
weight: 110
url: /ja/cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Aspose.Cells for C++を使用してVBAコードプロジェクトにデジタル署名を付与する方法について学びます。
---

{{% alert color="primary" %}} 

Aspose.Cellsの[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/)メソッドを使用して、VBAコードプロジェクトにデジタル署名を付与できます。Excelファイルが証明書でデジタル署名されているかどうかを確認する手順に従ってください。

- **開発者**タブから**Visual Basic**をクリックして、**Visual Basic for Applications IDE**を開きます。
- **Visual Basic for Applications IDE**の**ツール** > **デジタル署名...**をクリックします。

これにより、ドキュメントが証明書でデジタル署名されているかどうかを示す**デジタル署名フォーム**が表示されます。

{{% /alert %}} 

## **C++で証明書を使用してVBAコードプロジェクトに電子署名を付与します**

次のサンプルコードは、[**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/)メソッドの使用方法を示しています。サンプルコードの入力および出力ファイルはこちらです。このコードは、任意のExcelファイルと証明書を使ってテストできます。

- サンプルのExcelファイル（5115028.xlsm）
- [サンプルpfxファイル（5115039.pfx）](5115039.pfx)でデジタル署名を作成します。このコードを実行するためにこのファイルをコンピューターにインストールしてください。パスワードは1234です。
- サンプルコードによって生成された出力Excelファイル（5115029.xlsm）

```cpp
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String password(u"1234");
    U16String pfxPath = srcDir + u"sampleDigitallySignVbaProjectWithCertificate.pfx";
    U16String comment(u"Signing Digital Signature using Aspose.Cells");

    Vector<uint8_t> certData;

    std::time_t now = std::time(nullptr);
    std::tm* now_tm = std::localtime(&now);
    int year = now_tm->tm_year + 1900;
    int month = now_tm->tm_mon + 1;
    int day = now_tm->tm_mday;
    int hour = now_tm->tm_hour;
    int minute = now_tm->tm_min;
    int second = now_tm->tm_sec;

    DigitalSignature digitalSignature(certData, password, comment, Date{year, month, day, hour, minute, second, 0});

    U16String inputFilePath = srcDir + u"sampleDigitallySignVbaProjectWithCertificate.xlsm";
    Workbook workbook(inputFilePath);

    workbook.GetVbaProject().Sign(digitalSignature);

    U16String outputFilePath = outDir + u"outputDigitallySignVbaProjectWithCertificate.xlsm";
    workbook.Save(outputFilePath);

    std::cout << "VBA project digitally signed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
