---
title: C++を使用してOData接続情報を取得する方法
linktitle: OData接続情報を取得する方法
type: docs
weight: 60
url: /ja/cpp/how-to-get-odata-connection-information/
description: Aspose.Cells for C++を使ってExcelファイルからOData接続情報を抽出する方法を学びます。
---

## **OData接続情報を取得**

開発者がExcelファイルからOData情報を抽出する必要がある場合があります。 Aspose.Cellsは、Excelファイルに存在するDataMashup情報を返す [**Workbook.GetDataMashup()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getdatamashup/) プロパティを提供します。この情報は [**DataMashup**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/) クラスによって表されます。 [**DataMashup**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/) クラスは [**GetPowerQueryFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/getpowerqueryformulas/) プロパティを提供し、これは [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulacollection/) コレクションを返します。 [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulacollection/) から [**PowerQueryFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformula/) と [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/) にアクセスできます。

次のコードスニペットは、これらのクラスを使用してOData情報を取得する方法を示しています。

以下のコードスニペットで使用されるソースファイルは参照用に添付されています。

[ソースファイル](96928098.xlsx)

### **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook
    Workbook workbook(srcDir + u"ODataSample.xlsx");

    // Get PowerQueryFormulaCollection from DataMashup
    PowerQueryFormulaCollection PQFcoll = workbook.GetDataMashup().GetPowerQueryFormulas();

    // Iterate through each PowerQueryFormula in the collection
    for (int i = 0; i < PQFcoll.GetCount(); ++i)
    {
        PowerQueryFormula PQF = PQFcoll.Get(i);
        std::cout << "Connection Name: " << PQF.GetName().ToUtf8() << std::endl;

        // Get PowerQueryFormulaItemCollection from PowerQueryFormula
        PowerQueryFormulaItemCollection PQFIcoll = PQF.GetPowerQueryFormulaItems();

        // Iterate through each PowerQueryFormulaItem in the collection
        for (int j = 0; j < PQFIcoll.GetCount(); ++j)
        {
            PowerQueryFormulaItem PQFI = PQFIcoll.Get(j);
            std::cout << "Name: " << PQFI.GetName().ToUtf8() << std::endl;
            std::cout << "Value: " << PQFI.GetValue().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **コンソール出力**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
