---
title: リボンXMLのカスタマイズ方法（C++）
linktitle: Excelメニューのカスタマイズ
type: docs
weight: 1500
url: /ja/cpp/customizing-the-ribbon-xml/
description: Aspose.Cellsを使用したExcelファイルのリボンXMLカスタマイズ方法を学習します（C++）。
---

{{% alert color="primary" %}} 

Microsoft Officeは2007以降、メニューやツールバーを廃止し、アプリケーションウィンドウの上部にリボンを配置しています。リボンはカスタマイズ可能です。 
Aspose.Cellsは次のことを可能にします：

- リボンXMLを解析せずに保持できます。
- リボンXMLを解析せずに読み書きできます。
- リボンXMLデータの取得と設定ができます。

リボンXMLを変更する場合は、XMLパーサーまたは他のリボンXMLツールで解析する必要があります。

{{% /alert %}} 

```cpp
#include <iostream>
#include <fstream>
#include <string>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook wb(srcDir + u"aspose-sample.xlsx");

    std::ifstream file((srcDir + u"CustomUI.xml").ToUtf8());
    if (!file.is_open())
    {
        std::cerr << "Failed to open CustomUI.xml" << std::endl;
        return -1;
    }

    std::string ribbonXml((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();

    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    std::u16string utf16Xml = converter.from_bytes(ribbonXml);
    U16String xmlStr(reinterpret_cast<const char16_t*>(utf16Xml.c_str()));

    wb.SetRibbonXml(xmlStr);

    std::cout << "Ribbon XML set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
