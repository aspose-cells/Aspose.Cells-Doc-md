---
title: C++でシートの保護解除
linktitle: ワークシートの保護解除
type: docs
weight: 20
url: /ja/cpp/unprotect-a-worksheet/
description: Aspose.Cells for C++を使ったシートの保護解除方法を学びます。
---

{{% alert color="primary" %}}

保護されたシートから保護解除するには、開発者はRuntimeでの保護解除が必要な場合、Aspose.Cellsを使用して簡単に行うことができます。

{{% /alert %}}

## **ワークシートの保護を解除する**

### **Microsoft Excel の使用**

ワークシートから保護を解除するには：

**ツール**メニューから**保護**を選び、次に**シートの保護解除**を選択します。シートがパスワード保護されている場合はダイアログが表示され、パスワードの入力を求められます。パスワードを入力すると、シートの保護が解除されます。

### **Aspose.Cells を使用して単純に保護されたワークシートの保護解除**

シートは、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/)メソッドを呼び出すことで保護解除できます。パスワードが設定されていないシンプルな保護シートは、パラメータを指定せずに[**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/)メソッドを呼び出すだけで解除可能です。

```c++
#include <iostream>
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

    // Create a Workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unprotect the worksheet without a password
    worksheet.Unprotect();

    // Save the Workbook in Excel97-2003 format
    workbook.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet unprotected and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Aspose.Cells を使用してパスワードで保護されたワークシートの保護解除**

パスワード保護されたシートは、パスワードを設定した後に保護されたシートです。こうしたシートは、パスワードを引数として取るオーバーロードされた[**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/)メソッドを呼び出すことで解除できます。

```c++
#include <iostream>
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
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unprotecting the worksheet with a password
    worksheet.Unprotect(u"");

    // Save Workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet unprotected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
