---
title: Loading GridWeb Data in Async Mode
type: docs
weight: 40
url: /net/aspose-cells-gridweb/loading-data-in-async-mode/
description: This article describes how to use async mode to get better performance in GridWeb.
keywords: GridWeb,performance,async,async mode
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

When creating a Workbook with large data sets, or reading a big Microsoft Excel file, it will surely take more time and resources to do that. The total memory the process will consume is always a concern. There are measures which can be adopted to cope with the challenge. Aspose.Cells.GridWeb provides relevant options and APIs to reduce and optimize memory usage. It can also help the process work more efficiently and run faster. For a worksheet that contains large cell data, you may load the dataset asynchronously, which can improve the overall performance of the user’s experience.

{{% /alert %}} 

Use the GridWeb.EnableAsync option to optimize memory and performance for cell data when building a large data set. When you set the option to **true**, the data loading will be based only on the currently visible window area. In short, when you scroll the worksheet’s cell data in GridWeb, it will load new data based on the current scroll position only.

The following example shows how to enable GridWeb's async mode.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
