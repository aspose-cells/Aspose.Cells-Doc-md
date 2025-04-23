---
title: C++ ile HTML yi Excel çalışma kitabına yüklerken DIV etiketlerinin düzenini destekle
linktitle: DIV Etiketleri Düzenini Destekle
type: docs
weight: 50
url: /tr/cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
description: Aspose.Cells for C++ kullanarak HTML yi Excel çalışma kitabına yüklerken DIV etiketlerinin düzenini nasıl destekleyeceğinizi öğrenin.
---

{{% alert color="primary" %}} 

 Normalde, HTML'yi bir Excel çalışma kitabı nesnesine yüklerken DIV etiketlerinin düzeni dikkate alınmaz. Ancak, DIV etiketlerinin düzeninin korunmasını istiyorsanız, [GetSupportDivTag()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getsupportdivtag/) özelliğini **true** olarak ayarlayın. Bu özelliğin varsayılan değeri **false**'dır.

{{% /alert %}} 

Aşağıdaki örnek kod, [GetSupportDivTag()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getsupportdivtag/) özelliğinin kullanımını göstermektedir. Lütfen girdi HTML'sinde kullanılan Aspose Logo'yu (5115218.png) ve kod tarafından oluşturulan [çıktı Excel dosyasını](5115220.xlsx) indirin.

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
