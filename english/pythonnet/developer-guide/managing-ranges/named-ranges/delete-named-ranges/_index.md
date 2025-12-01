---
title: Delete Named Ranges
type: docs
weight: 90
url: /python-net/delete-named-ranges/
description: You can learn how to remove defined names or named ranges from Excel or OpenOffice files with Aspose.Cells for Python via .Net.
keywords: Python Excel Library, Python Remove Duplicate Defined Names, Python Delete Duplicate Defined Names.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**
If there are too many defined names or named ranges in the Excel files, we have to clear some for they are not referred again.

## **Remove Named Range in MS Excel**

To remove a named range from Excel, you can follow these steps:
1. Open Microsoft Excel and open the workbook that contains the named range.
2. Go to the "Formulas" tab in the Excel ribbon.
3. Click on the "Name Manager" button in the "Defined Names" group. This will open the Name Manager dialog box.
4. In the Name Manager dialog box, select the named range you want to remove.
5. Click on the "Delete" button. Confirm the deletion when prompted.
6. Click on the "Close" button to close the Name Manager dialog box.
7. Save the workbook to retain the changes.

## **Deletes Named Range using Aspose.Cells for Python via .NET**
With Aspose.Cells for Python via .NET, you can remove named ranges or defined names by [text](https://reference.aspose.com/cells/python-net/aspose.cells/namecollection/remove_a_name/#str) in the list.

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

Note: if the defined name is referred by formulas, it could not be removed . We only can remove formula of the defined name.

## **Removes Some Named Ranges**
When we remove a defined name, we have to check whether it is referred by all formulas in the file.
In order to improve peformance of removing named ranges,we can remove some together.

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


## **Remove Duplicate Defined Names**
Some Excel fiels corrupt because some defined names are duplicate. So we can remove these duplicate names to repair the file.

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
