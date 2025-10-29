---
title: 删除命名范围
type: docs
weight: 90
url: /zh/python-net/delete-named-ranges/
description: 您可以学习如何使用 Aspose.Cells for Python 通过 .Net 从 Excel 或 OpenOffice 文件中删除定义名称或命名范围。
keywords: Python Excel 库、Python 删除重复的定义名称、Python 删除重复的命名范围。
---

## **介绍**
如果 Excel 文件中有太多的定义名称或命名范围，我们必须清除一些，因为它们再也不会被引用。

## **在MS Excel中删除命名区域**

要从Excel中删除命名区域，可以按照以下步骤进行：
1. 打开Microsoft Excel并打开包含命名区域的工作簿。
2. 转到Excel功能区中的“公式”选项卡。
3. 单击“已定义名称”组中的“名称管理器”按钮。这将打开名称管理器对话框。
4. 在名称管理器对话框中，选择要删除的命名区域。
5. 单击“删除”按钮。在提示时确认删除。
6. 单击“关闭”按钮关闭名称管理器对话框。
7. 保存工作簿以保留更改。

## **使用 Aspose.Cells for Python via .NET 删除命名范围**
使用 Aspose.Cells for Python via .NET，您可以通过列表中的[文本](https://reference.aspose.com/cells/python-net/aspose.cells/namecollection/remove_a_name/#str)删除命名范围或定义的名称。

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# The path to the documents directory
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a new Workbook
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete a named range by text
worksheets.names.remove_a_name("NamedRange")


# Save the workbook to retain the changes
workbook.save(os.path.join(data_dir, "Book2.xlsx"))
```

注意：如果已定义的名称由公式引用，则不能删除。我们只能删除已定义名称的公式。

## **删除一些已命名范围**
当我们删除已定义名称时，必须检查它是否被文件中的所有公式引用。
为了提高删除命名范围的性能，我们可以一起删除一些。

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete some defined names
worksheets.names.remove_names_by_array(["NamedRange1", "NamedRange2"])

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```


## **删除重复的已定义名称**
一些Excel文件损坏是因为某些已定义名称是重复的。因此，我们可以删除这些重复名称以修复文件。

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete duplicate defined names
worksheets.names.remove_duplicate_names()

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```
{{< app/cells/assistant language="python-net" >}}
