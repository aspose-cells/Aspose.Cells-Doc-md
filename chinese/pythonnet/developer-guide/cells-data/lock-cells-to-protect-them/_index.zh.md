---
title: 使用Python.NET锁定单元格保护它们
linktitle: 锁定单元格以保护内容
type: docs
weight: 130
url: /zh/python-net/how-to-lock-cells-to-protect-them/
description: 了解如何使用Aspose.Cells for Python via .NET锁定特定单元格和保护工作表。
keywords: 使用Python锁定单元格、保护工作表、单元格保护在Excel中，Aspose.Cells Python教程
---

## **可能的使用场景**
锁定单元格以保护它们是在电子表格应用程序中常见的做法，原因包括：

1. 防止意外更改：锁定单元格可以防止用户意外修改重要数据或公式。
2. 维护数据完整性：确保关键数据保持一致和准确。
3. 控制访问：在协作环境中管理编辑权限。
4. 保护公式：防止关键计算被篡改。
5. 执行业务规则：遵守数据保护要求。
6. 指导用户：在复杂的电子表格中提供清晰的可编辑区域。

## **如何在Excel中锁定单元格以保护它们**
下面介绍在Microsoft Excel中锁定单元格的方法：

1. 选择要锁定的单元格：选择单元格或跳过以锁定整个工作表。
1. 打开格式单元格对话框：右键 > “格式单元格”或Ctrl+1。
<br>
<img src="1.png" width=60% />
1. 锁定单元格：转到“保护”标签 > 勾选“已锁定” > 点击“确定”。
1. 保护工作表：“审阅”标签 > “保护工作表” > 设置密码/权限 > 点击“确定”。
<br>
<img src="2.png" width=60% />

## **如何使用Python锁定单元格以保护它们**

Aspose.Cells for Python via .NET 支持通过编程实现单元格保护。请按照以下步骤操作：
1. 加载[示例文件](sample.xlsx)
2. 解锁所有单元格（默认锁定状态在保护之前不会生效）
3. 锁定特定单元格
4. 保护工作表以强制执行锁定

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]

# Unlock all cells first
style = ac.Style()
style.is_locked = False
style_flag = ac.StyleFlag()
style_flag.locked = True
worksheet.cells.apply_style(style, style_flag)

# Lock specific cells
worksheet.cells["A1"].get_style().is_locked = True
worksheet.cells["B2"].get_style().is_locked = True

# Enable worksheet protection
worksheet.protect(ac.ProtectionType.ALL)

# Save protected workbook
workbook.save("output.xlsx")
```

## **输出结果**
此实现锁定了指定的单元格（A1和B2），同时保持其他单元格可编辑。工作表保护会强制执行这些设置。

<br>
<img src="3.png" width=60% />

```python
from aspose.cells import Workbook, ProtectionType, StyleFlag

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Unlock all cells first
unlock_style = workbook.create_style()
unlock_style.is_locked = False

style_flag = StyleFlag()
style_flag.locked = True
sheet.cells.apply_style(unlock_style, style_flag)

# Lock specific cells (A1 and B2)
lock_style = workbook.create_style()
lock_style.is_locked = True

sheet.cells.get("A1").set_style(lock_style)
sheet.cells.get("B2").set_style(lock_style)

# Protect the worksheet to enforce locking
sheet.protect(ProtectionType.ALL)

# Save the modified workbook
workbook.save("output_locked.xlsx")
```
