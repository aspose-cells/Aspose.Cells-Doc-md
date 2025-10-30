---
title: C++を使用して埋め込みOLEオブジェクトのクラス識別子を取得または設定する方法
linktitle: 埋め込みOLEオブジェクトのクラス識別子を取得または設定する
type: docs
weight: 200
url: /ja/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Aspose.Cellsを使用して埋め込みOLEオブジェクトのクラス識別子を取得または設定する方法について学びます。
---

## **可能な使用シナリオ**
Aspose.Cellsは、[OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getclassidentifier/) プロパティを提供しており、これを使用して埋め込みOLEオブジェクトのクラス識別子を取得または設定できます。OLEオブジェクトのクラス識別子は実際にはGUID（Globally Unique Identifier）です。GUIDは常に16バイト長で、クラス識別子も16バイト長です。これらはWindowsレジストリ内に見つかることが多く、ホストアプリケーションに埋め込まれたリソースを含むOLEオブジェクトの開き方を指示します。

## **埋め込まれたOLEオブジェクトのクラス識別子を取得または設定する**
以下のスクリーンショットは、[サンプルエクセルファイル](5115190.xls)から読み取られたOLEオブジェクトのクラス識別子（GUID）を示しています。これは埋め込みPowerPoint OLEオブジェクトを含んでいます。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **サンプルコード**
次のサンプルコードは、[サンプルエクセルファイル](5115190.xls)とともに実行され、OLEオブジェクトのクラス識別子（GUID）をコンソールに出力します。出力されるGUIDはスクリーンショットに表示されているものと全く同じです。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include <guiddef.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"sample.xls");
    Worksheet ws = wb.GetWorksheets().Get(0);
    OleObject oleObj = ws.GetOleObjects().Get(0);

    Vector<uint8_t> classIdentifier = oleObj.GetClassIdentifier();
    GUID guid;
    memcpy(&guid, classIdentifier.GetData(), sizeof(GUID));

    char guidStr[39];
    snprintf(guidStr, sizeof(guidStr), "{%08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X}",
             guid.Data1, guid.Data2, guid.Data3,
             guid.Data4[0], guid.Data4[1], guid.Data4[2], guid.Data4[3],
             guid.Data4[4], guid.Data4[5], guid.Data4[6], guid.Data4[7]);

    std::cout << guidStr << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **コンソール出力**
上記のサンプルコードを[サンプルExcelファイル](5115190.xls)で実行した場合のコンソール出力です。

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
