---
title: C++を使用してHTMLをExcelワークブックに読み込む際にDIVタグのレイアウトをサポート
linktitle: DIVタグのレイアウトをサポート
type: docs
weight: 50
url: /ja/cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
description: Aspose.Cells for C++を使用してHTMLをExcelワークブックに読み込む際のDIVタグのレイアウトサポート方法を学びます。
---

{{% alert color="primary" %}} 

通常、HTMLをExcelワークブックに読み込む際、DIVタグのレイアウトは無視されます。ただし、DIVタグのレイアウトを保持したい場合は、[GetSupportDivTag()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getsupportdivtag/) プロパティを **true** に設定します。このプロパティのデフォルト値は **false** です。

{{% /alert %}} 

以下のサンプルコードは、[GetSupportDivTag()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getsupportdivtag/) プロパティの使用例を示しています。入力HTML内に使用されているAsposeロゴ（5115218.png）と、コードによって生成された[出力Excelファイル](5115220.xlsx)をダウンロードしてください。

```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <string>
#include <fstream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::string convert_u16_to_string(const char16_t* data) {
    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    return converter.to_bytes(data);
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    U16String export_html = uR"(
        <html>
        <head>
            <meta charset="UTF-8">
        </head>
        <body>
            <table>
                <tr>
                    <td>
                        <div>This is some Text.</div>
                        <div>
                            <div>
                                <span>This is some more Text</span>
                            </div>
                            <div>
                                <span>abc@abc.com</span>
                            </div>
                            <div>
                                <span>1234567890</span>
                            </div>
                            <div>
                                <span>ABC DEF</span>
                            </div>
                        </div>
                        <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>
                    </td>
                    <td>
                        <img src=')" + srcDir + u"ASpose_logo_100x100.png" + uR"(' />
                    </td>
                </tr>
            </table>
        </body>
        </html>)";

    std::string html_utf8 = convert_u16_to_string(export_html.GetData());
    U16String tempHtmlPath = srcDir + u"temp.html";
    std::ofstream tempFile(convert_u16_to_string(tempHtmlPath.GetData()).c_str(), std::ios::binary);
    tempFile.write(html_utf8.data(), html_utf8.size());
    tempFile.close();

    HtmlLoadOptions loadOptions;
    loadOptions.SetSupportDivTag(true);

    Workbook wb(tempHtmlPath, loadOptions);

    Worksheet ws = wb.GetWorksheets().Get(0);
    ws.AutoFitRows();
    ws.AutoFitColumns();

    U16String outputPath = srcDir + u"DivTagsLayout_out.xlsx";
    wb.Save(outputPath, SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
