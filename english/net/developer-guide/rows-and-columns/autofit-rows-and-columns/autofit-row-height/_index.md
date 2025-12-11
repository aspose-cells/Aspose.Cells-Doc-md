---
title: AutoFit Row Height Automatically When Loading File
type: docs
weight: 120
url: /net/autofit-row-height/
description: Learn how to fit rows whose height is not customized.
keywords: AutoFit Row Height when loading file, automatically adjust the row height when opening Excel file.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
The row height automatically matches the font of the content, but when the height of the cached row does not match the height of the content in the file, MS Excel will automatically adjust the row height when loading the file, whereas Aspose.Cells does not adjust it automatically to improve performance. If you need to use Aspose.Cells to automatically match row heights when loading files, you can achieve this through the parameter [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

Please refer to the following image. We can observe that the cached row height in row 11 is 15, but Excel automatically adjusts the row height when loading the file.  
<br>
<img src="1.png" width=70% />

## **Adjust Row Height using Aspose.Cells**
If you directly load the file and save it to PDF, the data will not be fully displayed in the PDF because its cached row height is only 15.  
<br>
<img src="2.png" width=70% />
<br>
If you set the parameter [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) to **true** when loading the file, Aspose.Cells will automatically adjust the row height. The adjusted row height can effectively meet the text‑display requirements.  
<br>
<img src="3.png" width=70% />

## **C# Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}
{{< app/cells/assistant language="csharp" >}}
