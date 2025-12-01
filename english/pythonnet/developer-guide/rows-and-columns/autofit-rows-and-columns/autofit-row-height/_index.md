---
title: AutoFit Row Height Automatically When Loading file
type: docs
weight: 120
url: /python-net/autofit-row-height/
description: Learn how to fit the rows which height are not customed through the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python AutoFit Row Height when loading file, Python automatically adjust the row height when opening excel file. 
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
The height of the row automatically matches the font of the content, but when the height of the cached row does not match the height of the content in the file, MS Excel will automatically adjust the row height when loading the file, while Aspose.Cells for Python via .NET will not automatically adjust it to improve performance. If you need to use the Aspose.Cells for Python via .NET program to automatically match line heights when loading files, you can achieve the goal through the parameter [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/).

Please refer to the following image data. We can observe that the cache row height in line 11 is 15, but Excel automatically adjusted the row height when loading the file.
<br>
<img src="1.png" width=70% />

## **Adjust Row Height using Aspose.Cells for Python Excel Library**
If you directly load the file and save it to PDF, the data will not be fully displayed in PDF because its cache line height is only 15.
<br>
<img src="2.png" width=70% />
<br>
If you set the parameter [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/) to true when loading the file, then Aspose.Cells for Python via .NET will automatically adjust the row height. The adjusted line height can effectively meet the text display requirements.
<br>
<img src="3.png" width=70% />

## **Python Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Rows-autofit-row-height.py" >}}
{{< app/cells/assistant language="python-net" >}}
