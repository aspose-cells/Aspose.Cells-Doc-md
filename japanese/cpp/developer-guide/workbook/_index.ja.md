---
title: C++でブックを管理する
linktitle: ワークブック
type: docs
weight: 60
url: /ja/cpp/managing-workbooks-and-worksheets/
description: Aspose.Cells for C++ APIを使ったブックの管理方法を学習しましょう。
keywords: C++でブックを管理する方法、ブックとワークシートの管理、C++での操作について。
---

{{% alert color="primary" %}}

Aspose.Cells for C++は、ブックとワークシートの作成、開く、操作のための強力で柔軟なAPIを提供します。ここでは、その方法を説明します。

{{% /alert %}}

## **新しいワークブックの作成**
新しいブックを作成するには：

1. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスのインスタンスを作成します。
2. [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)クラスを使用してワークシートを追加します。
3. [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドを使ってブックを保存します。

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

## **既存のブックを開く**
既存のブックを開くには：

1. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスのインスタンスを作成し、ファイルパスをコンストラクタに渡します。
2. [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)クラスを使用してワークシートにアクセスします。
3. 必要に応じてブックを編集します。
4. [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドを使ってブックを保存します。

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).SetValue("Hello, World!");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **ワークシートの管理**
Aspose.Cells for C++は、ワークシートの追加、削除、名前変更など、多くの管理方法を提供します。

### **ワークシートの追加**
新しいワークシートを追加するには：

1. ワークブックから [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) クラスにアクセスします。
2. [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) メソッドを使用して新しいワークシートを追加します。

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a new worksheet
    workbook.GetWorksheets().Add("NewSheet");

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **ワークシートの削除**
ワークシートを削除するには：

1. ワークブックから [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) クラスにアクセスします。
2. [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat/) メソッドを使用してインデックスでワークシートを削除します。

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Open an existing workbook
    Aspose::Cells::Workbook workbook("input.xlsx");

    // Remove the first worksheet
    workbook.GetWorksheets().RemoveAt(0);

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **ワークシートの名前を変更する**
ワークシートの名前を変更するには：

1. ワークブックから [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスにアクセスします。
2. [SetName](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setname/) メソッドを使用してワークシートの名前を変更します。

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName("RenamedSheet");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **結論**
Aspose.Cells for C++ は、ワークブックとワークシートの管理に役立つ包括的なツールセットを提供します。新しいワークブックの作成、既存のものを開く、またはワークシートを操作する必要がある場合、Aspose.Cellsを使用してExcelファイルをプログラムで操作するのは簡単です。
