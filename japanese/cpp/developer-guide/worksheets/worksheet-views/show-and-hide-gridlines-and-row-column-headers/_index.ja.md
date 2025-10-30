---
title: C++でグリッド線と行・列のヘッダーの表示・非表示を行う
linktitle: グリッド線と行列ヘッダーの表示および非表示
type: docs
weight: 30
url: /ja/cpp/show-and-hide-gridlines-and-row-column-headers/
description: この記事は、C++のAPIまたはライブラリを使用してExcelのワークシートのグリッドラインや行・列のヘッダーをプログラム的に隠したり表示したりするサンプルコードを提供します。
---

{{% alert color="primary" %}}

Aspose.Cellsは、デフォルトで表示されているワークシートのグリッド線の非表示および表示をサポートしています。また、ワークシートの行列ヘッダーの表示を制御する機能も提供しています。

{{% /alert %}}

## **グリッド線の表示と非表示**

すべてのExcelワークシートはデフォルトでグリッド線を持っています。これにより、特定のセルにデータを入力することが簡単になります。グリッド線により、ワークシートをセルのコレクションとして表示し、各セルを簡単に識別することができます。

### **グリッド線の表示の制御**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスは、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシートの管理に役立つさまざまなプロパティとメソッドを提供します。グリッドラインの表示/非表示を制御するには、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/)プロパティを使用します。[**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/)はBooleanプロパティであり、**true**または**false**の値のみを格納できます。

#### **グリッド線を表示する**

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/)プロパティを**true**に設定して、グリッドラインを表示します。

#### **グリッド線を非表示にする**

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/)プロパティを**false**に設定して、グリッドラインを非表示にします。

以下に、[**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/)プロパティの使用例を示します。Excelファイル（book1.xls）を開き、最初のワークシートのグリッドラインを非表示にして、結果をoutput.xlsとして保存します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the grid lines of the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Grid lines hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **行列ヘッダーの表示および非表示**

Excelファイルのすべてのワークシートは、行と列で配置されたセルから構成されています。すべての行と列には、それぞれユニークな値があり、行と列、また個々のセルを識別するために使用されます。たとえば、行には数字が付いています- 1、2、3、4など- そして列はアルファベット順に並んでいます- A、B、C、Dなど- 行と列の値はヘッダーに表示されます。Aspose.Cellsを使用すると、これらの行列ヘッダーの表示を制御することができます。

### **ワークシートの表示を制御する**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスは、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシートを管理するための多くのプロパティとメソッドを提供します。行と列のヘッダーの表示を制御するには、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/)プロパティを使用します。[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/)はBooleanプロパティで、**true**または**false**の値だけを格納します。

#### **行/列ヘッダーを表示する**

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/)プロパティを**true**に設定して、行と列のヘッダーを表示します。

#### **行/列ヘッダーを非表示にする**

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/)プロパティを**false**に設定して、行と列のヘッダーを非表示にします。

以下に、[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/)プロパティの使用例を示します。Excelファイル（book1.xls）を開き、最初のワークシートの行と列のヘッダーを非表示にして、結果をoutput.xlsとして保存します。

```cpp
#include <iostream>
#include <memory>
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the headers of rows and columns
    worksheet.SetIsRowColumnHeadersVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Headers hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

[**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/)と[**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/)のメソッドを使用して複数の行と列を表示させることも可能です。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
