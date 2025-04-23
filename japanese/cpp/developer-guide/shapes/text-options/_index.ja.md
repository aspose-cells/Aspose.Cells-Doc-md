---
title: C++で図形のテキストオプションを管理する
linktitle: 形状テキストオプションを管理する
type: docs
weight: 200
url: /ja/cpp/managing-shape-text-options/
description: Aspose.Cells for C++を使用して、プログラム的に図形のテキストオプションを管理する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.CellsはExcelファイル内の図形テキストオプションをプログラム的に管理するための強力な機能を提供します。このガイドでは、Aspose.Cells for C++を使って配置、向き、書式設定などの図形のテキストプロパティを操作する方法を解説します。

{{% /alert %}}

## **図形テキストオプションの管理**

Aspose.CellsはExcelファイル内の図形のテキストをカスタマイズできます。 [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/)クラスは配置、向き、書式設定などのテキストオプションを管理するメソッドとプロパティを提供します。

### **テキストの配置設定**
[**GetTextHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettexthorizontalalignment/)と[**GetTextVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextverticalalignment/)プロパティを使って図形内のテキストの水平および垂直配置を設定できます。

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

void SetTextAlignment() {
    // Load the Excel file
    Workbook workbook("example.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the shape
    Shape shape = worksheet.GetShapes().Get(0);

    // Set text alignment
    shape.SetTextHorizontalAlignment(TextAlignmentType::Center);
    shape.SetTextVerticalAlignment(TextAlignmentType::Center);

    // Save the workbook
    workbook.Save("output.xlsx");
}
```

### **テキストの向き設定**
また、[**TextOrientationType**](https://reference.aspose.com/cells/cpp/aspose.cells/textorientationtype/)プロパティを使って図形内のテキストの向きを設定することも可能です。

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

void SetTextOrientation() {
    Workbook workbook("example.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    TextBox textbox = worksheet.GetTextBoxes().Get(0);
    textbox.SetTextOrientationType(TextOrientationType::ClockWise);

    workbook.Save("output.xlsx");
}
```

### **書式設定**
[**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/)クラスを使って図形のテキスト内の書式を設定できます。フォントサイズ、色、スタイルなどのプロパティを調整できます。

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

void FormatText() {
    // Load the Excel file
    Workbook workbook("example.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the shape
    Shape shape = worksheet.GetShapes().Get(0);

    // Access the font of the shape's text
    Font font = shape.GetTextBody().GetParagraphEnumerator().GetCurrent().GetFont();

    // Set font properties
    font.SetSize(14);
    font.SetColor(Color::Red());
    font.SetIsBold(true);

    // Save the workbook
    workbook.Save("output.xlsx");
}
```

## **結論**
Aspose.Cells for C++は、Excelファイル内の図形のテキストオプションを管理するための包括的なツールセットを提供します。[**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/)クラスを使って、配置、向き、書式設定を簡単にカスタマイズ可能です。
