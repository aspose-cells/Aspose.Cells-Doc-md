+++
title = "Loading GridWeb Data in Async Mode" 
description = "" 
weight = 20340 
+++

Aspose.Cells for .NET : Loading GridWeb Data in Async Mode  

# Aspose.Cells for .NET : Loading GridWeb Data in Async Mode


When creating a Workbook with large data sets, or reading a big Microsoft Excel file, it will surely take more time and resources to do that. The total memory the process will take is always a concern. There are measures which can be adopted to cope with the challenge. Aspose.Cells.GridWeb provides some relevant options and APIs to lower, reduce and optimize memory usage. Also, it can help the process work more efficiently and run faster. For a worksheet that contains large cells data, you may load the dataset asynchronously that can improve the overall performance for user's experience.

Use the `GridWeb.EnableAsync` option to optimize memory and performance for cells data. When building a large data set for cells. When you set the option to true, the data loading will be based on current visible Windows area only. In short, when you scroll in the worksheet's cells data in GridWeb, it will load new Windows data based on the current scroll position only.

The following example shows how to enable GridWeb's async mode.

