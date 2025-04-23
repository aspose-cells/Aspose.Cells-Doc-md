---
title: 如何用C++将数字格式化为日期
linktitle: 如何将数字格式化为日期
type: docs
weight: 10
url: /zh/cpp/format-number-to-date/
description: 本文介绍了如何使用Aspose.Cells for C++ API将数字格式化为日期。
keywords: 格式化数字为日期，单元格数字设置，格式化数字为日期，日期设置，日期格式。
---

## **可能的使用场景**
在Excel（或任何电子表格软件）中将数字格式化为日期很重要，原因有多方面，特别是当你处理包含时间或日程信息的数据时。以下是格式化数字为日期的好处：

1. **正确解释日期值**：在Excel中，日期作为序列号存储（例如，1代表1900年1月1日，44210代表2021年9月6日）。如果这些数字不被格式化为日期，用户可能看到无意义的数字而不是可识别的日期。正确格式化后，Excel会显示为实际日期（如09/06/2021而不是44210）。
2. **简化与时间相关的计算**：Excel可以使用日期进行许多计算，例如计算两个日期之间的天数，添加或减去天数，或确定星期几。如果数字未格式化为日期，Excel将无法有效执行这些操作。例如，若想计算2023年9月1日至2023年10月1日之间的天数，只要数字作为日期格式，Excel就能轻松计算。
3. **确保一致性**：当所有与日期相关的值都正确格式化后，所有日期都以统一、易读的样式显示。这在商务报告、项目计划和数据库中尤为重要，不同地区使用不同的日期格式（如美国的月/日/年与许多其他国家的日/月/年），格式化可确保正确理解日期。
4. **提升可读性**：以标准格式（如01/01/2024）显示的日期比原始序列号45000更容易阅读。正确的日期格式让你的电子表格更友好，避免混淆。在调度、时间线、事件规划或历史数据等场景尤为重要。
5. **有助于排序和筛选**：正确格式化的日期被Excel识别为实际日期，更便于按时间顺序排序或筛选。例如，可以按日期排序事件列表或筛选出两日期之间的记录。没有正确格式化，排序可能基于原始数字而非实际日期。
6. **支持日期函数的使用**：Excel提供许多强大的日期函数，例如：TODAY()，DATEDIF()，WORKDAY()，YEAR()，MONTH()，DAY()。这些函数需要正确格式化的日期，才能进行精准计算。
7. **支持可视化（图表/时间线）**：正确格式化的日期可以用来创建时间轴上的图表。例如，在时间线图中，Excel需要识别格式的日期来准确绘制事件。格式错误或未格式化的数字可能导致图表无法准确反映信息。
8. **避免误解**：原始数字易被误解。例如，44210可能被视为普通数字，但格式化为日期后，显示为2021年9月6日。正确格式化的日期有助于避免数据的误解。
9. **简化数据输入**：单元格格式为日期时，提示输入有效日期格式，减少输入错误，确保正确捕获日期值。
10. **对调度和跟踪至关重要**：在任何涉及调度、跟踪或截止时间（如项目管理、财务预测或时间敏感报告）的场景中，将数字格式化为日期对确保准确性和理解都至关重要，有助于更好的规划与执行。

## **如何在Excel中将数字格式化为日期**
按照以下步骤在Excel中将数字格式化为日期：

### **使用功能区（开始选项卡）**
1. 选择包含要格式化为日期的数字的单元格。
2. 转到功能区中的“开始”选项卡。
3. 在“数字”组中，点击“数字格式”框中的下拉箭头（可能显示为“常规”或“数字”）。
4. 从下拉菜单中选择“短日期”或“长日期”。短日期：以简洁格式显示日期，例如MM/DD/YYYY（美国格式）或DD/MM/YYYY（国际格式）。长日期：以更详细的格式显示日期，例如星期一，2024年1月1日。
<br>
<img src="1.png" width=60% />

### **使用“设置单元格格式”对话框**
1. 选择你想要格式化的单元格。
2. 右键点击所选单元格，然后选择“设置单元格格式”，或按下 Ctrl + 1（Windows）或 Cmd + 1（Mac）。
3. 在“设置单元格格式”对话框中，切换到“数字”标签页。
4. 从左侧列表中选择“日期”。
5. 从右侧列表中选择所需的日期格式（例如 MM/DD/YYYY、DD/MM/YYYY 或自定义格式）。
<br>
<img src="2.png" width=60% />
6. 点击“确定”应用日期格式。

## **如何在Aspose.Cells中将数字格式化为日期**

要在使用 Excel 文件处理的 Aspose.Cells for C++ 库中将数字格式化为日期，可以以编程方式将日期格式应用于单元格。以下是使用 C++ 和 Aspose.Cells 的方法：

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the cell where you want to apply the date format
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Set a numeric value that represents a date (e.g., 44210 represents 09/06/2021 in Excel)
    a1.PutValue(44210);

    // Create a style object to apply the date format
    Style a1Style = a1.GetStyle();

    // "14" represents a standard date format in Excel (MM/DD/YYYY)
    a1Style.SetNumber(14);

    // Apply the style to the cell
    a1.SetStyle(a1Style);

    // Access the cell where you want to apply the currency format
    Cell a2 = worksheet.GetCells().Get(u"A2");

    // Set a numeric value to the cell
    a2.PutValue(44210);

    // Create a style object to apply the date format
    Style a2Style = a2.GetStyle();

    // Custom format for YYYY-MM-DD
    a2Style.SetCustom(u"YYYY-MM-DD");

    // Apply the style to the cell
    a2.SetStyle(a2Style);

    // Save the workbook
    workbook.Save(u"DateFormatted.xlsx");

    Aspose::Cells::Cleanup();
}
```
