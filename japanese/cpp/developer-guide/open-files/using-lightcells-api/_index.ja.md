---
title: LightCells APIをC++で使用する方法
linktitle: LightCells APIの使用
type: docs
weight: 160
url: /ja/cpp/using-lightcells-api/
description: C++でLightCells APIを使用して、大きなExcelファイルを効率的に読み書きし、メモリ使用量を最小限に抑える方法の学習
---

{{% alert color="primary" %}} 

大量のデータやコンテンツを含む大規模なMicrosoft Excelファイルの読み書きが必要な場合があります。LightCells APIは、メモリを少なく使用し、性能と効率を向上させるために役立ちます。

{{% /alert %}} 

# イベント駆動アーキテクチャ
Aspose.Cellsは、セルのコレクションなどの完全なデータモデルブロックをメモリに構築せずに、イベント駆動モードでセルデータを1つずつ操作するために、LightCells APIを提供しています。

ワークブックを保存するには、セルの内容を1つずつ提供し、コンポーネントがそれを直接出力ファイルに保存します。

テンプレートファイルを読み込む際に、コンポーネントはすべてのセルを解析し、その値を1つずつ提供します。

両手順ともに、1つのCellオブジェクトが処理され、その後破棄され、Workbookオブジェクトはコレクションを保持しません。そのため、このモードでは、大規模なデータセットを持つMicrosoft Excelファイルのインポートおよびエクスポート時にメモリを節約することができます。

LightCells APIは、XLSXファイルとXLSファイルでセルを同じように処理します（実際にはすべてのセルをメモリに読み込むのではなく、1つのセルを処理してから破棄します）が、XLSXファイルではXLSファイルよりもメモリを効果的に節約します。これは2つのフォーマットの異なるデータモデルと構造のためです。

ただし、**XLSファイル**の場合、より多くのメモリを節約するには、開発者が保存プロセス中に生成される一時データの保存に一時的な場所を指定することができます。通常、**LightCells APIを使用してXLSXファイルを保存する場合、約50%以上のメモリを節約**できますが、**XLSを保存する場合は20-40%のメモリを節約**できます。

## 大規模なExcelファイルの書き込み
Aspose.Cellsは、`LightCellsDataProvider`インターフェースを提供しており、これはプログラムに実装が必要です。このインターフェースは、大規模なスプレッドシートファイルを軽量モードで保存するためのデータプロバイダを表します。

このモードでブックを保存する際、`StartSheet(int)`は各ワークシートの保存時にチェックされます。シートごとに`StartSheet(int)`がtrueを返す場合、そのシートの行とセルのすべてのデータやプロパティがこの実装によって提供されます。まず`NextRow()`を呼び出して保存対象の次の行番号を取得します。有効な行番号（昇順）を返すと、その行を表す`Row`オブジェクトが提供され、`StartRow(Row)`によってプロパティの設定が可能です。

1行ごとに`NextCell()`を最初に呼び出します。有効な列番号（昇順）が返されると、そのセルを表す`Cell`オブジェクトが提供され、`StartCell(Cell)`を使ってデータやプロパティを設定します。セルのデータを設定後、そのセルは直接スプレッドシートに保存され、次のセルの処理に進みます。

### 大きなExcelファイルを書く例
LightCells APIの動作を確認するために、以下のサンプルコードを参照してください。必要に応じてコードセグメントを追加、削除、または更新してください。

プログラムは、**10,000（10000x30のマトリックス）レコード**を持つ大きなファイルをワークシートに作成し、ダミーデータで埋めます。`Main()`メソッドの`rowsCount`と`colsCount`変数を変更して、自分のマトリックスを指定できます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class TestDataProvider : public LightCellsDataProvider {
private:
    int _row = -1;
    int _column = -1;
    int maxRows;
    int maxColumns;
    Workbook _workbook;

public:
    TestDataProvider(Workbook workbook, int maxRows, int maxColumns)
        : _workbook(workbook), maxRows(maxRows), maxColumns(maxColumns) {}

    bool IsGatherString() override {
        return false;
    }

    int NextCell() override {
        ++_column;
        if (_column < this->maxColumns)
            return _column;
        else {
            _column = -1;
            return -1;
        }
    }

    int NextRow() override {
        ++_row;
        if (_row < this->maxRows) {
            _column = -1;
            return _row;
        }
        else
            return -1;
    }

    void StartCell(Cell& cell) override {
        cell.PutValue(_row + _column);
        if (_row != 1) {
            cell.SetFormula(u"=Rand() + A2");
        }
    }

    void StartRow(Row& row) override {}

    bool StartSheet(int sheetIndex) override {
        return sheetIndex == 0;
    }
};

void WriteUsingLightCellsAPI() {
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    int rowsCount = 10000;
    int colsCount = 30;

    Workbook workbook;
    OoxmlSaveOptions ooxmlSaveOptions;

    TestDataProvider dataProvider(workbook, rowsCount, colsCount);
    ooxmlSaveOptions.SetLightCellsDataProvider(&dataProvider);

    workbook.Save(outDir + u"output.out.xlsx", ooxmlSaveOptions);

    std::cout << "File saved successfully using LightCells API!" << std::endl;
}

int main() {
    Aspose::Cells::Startup();
    WriteUsingLightCellsAPI();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 大規模なExcelファイルの読み込み
Aspose.Cellsは、`LightCellsDataHandler`インターフェースの実装が必要です。このインターフェースは、軽量モードで大規模なスプレッドシートファイルを読み取るためのデータプロバイダを表します。

このモードでブックを読み込む時、`StartSheet`が各ワークシートの読み込み時にチェックされます。シートごとに`StartSheet`がtrueを返すと、そのシートの行と列のセルのすべてのデータやプロパティがこのインターフェースの実装によって処理されます。各行については`StartRow`を呼び出し、処理が必要かどうかを判断します。必要な場合、その行のプロパティを先に読み込み、`ProcessRow`でアクセス可能です。行内のセルも処理対象なら`ProcessCell`を呼び出します。

### 大規模Excelファイルの読み取り例
LightCells APIの動作を確認するために、以下のサンプルコードを参照してください。必要に応じてコードセグメントを追加、削除、または更新してください。

プログラムはワークシート内に数百万のレコードが含まれる巨大なファイルを読み込みます。ワークブック内の各シートを読み込むには少し時間がかかります。サンプルコードはファイルを読み込み、各ワークシートにおけるセルの総数、文字列の数、および数式の数を取得します。

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class LightCellsDataHandlerVisitCells : public LightCellsDataHandler
{
private:
    int cellCount;
    int formulaCount;
    int stringCount;

public:
    LightCellsDataHandlerVisitCells() : cellCount(0), formulaCount(0), stringCount(0) {}

    int GetCellCount() const { return cellCount; }
    int GetFormulaCount() const { return formulaCount; }
    int GetStringCount() const { return stringCount; }

    bool StartSheet(Worksheet& sheet) override
    {
        std::cout << "Processing sheet[" << sheet.GetName().ToUtf8() << "]" << std::endl;
        return true;
    }

    bool StartRow(int32_t rowIndex) override
    {
        return true;
    }

    bool ProcessRow(Row& row) override
    {
        return true;
    }

    bool StartCell(int32_t columnIndex) override
    {
        return true;
    }

    bool ProcessCell(Cell& cell) override
    {
        cellCount++;
        if (cell.IsFormula())
        {
            formulaCount++;
        }
        else if (cell.GetType() == CellValueType::IsString)
        {
            stringCount++;
        }
        return false;
    }
};

void Run()
{
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create load options and set the light cells data handler
    LoadOptions opts;
    auto handler = std::make_shared<LightCellsDataHandlerVisitCells>();
    opts.SetLightCellsDataHandler(handler.get());

    // Load the workbook with the specified options
    Workbook wb(srcDir + u"LargeBook1.xlsx", opts);

    // Get the total number of sheets
    int sheetCount = wb.GetWorksheets().GetCount();

    // Output the results
    std::cout << "Total sheets: " << sheetCount << ", cells: " << handler->GetCellCount()
              << ", strings: " << handler->GetStringCount() << ", formulas: " << handler->GetFormulaCount() << std::endl;
}

int main()
{
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
