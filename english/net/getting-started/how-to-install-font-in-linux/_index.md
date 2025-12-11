---
title: How to Install Fonts in Linux
type: docs
description: "How to Install Fonts in Linux"
weight: 139
url: /net/how-to-install-font-in-linux/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Overview

When using Aspose.Cells on Linux, because Linux has fewer default fonts, the font referenced in your Excel file may not exist by default on your Linux system.  
When this happens, Aspose.Cells will use a similar font instead to display the characters. However, this could cause the following effects:

1. Different fonts can result in images that are rendered in layouts that differ from Excel.  
2. Since the font has changed, the output characters may not meet your expectations.

In order for your program to produce more accurate results, install the fonts you need on Linux. It is important to ensure that the fonts you use in Excel files exist in your environment.

## How to Install Fonts in Linux

There are two ways to install fonts on Linux, as described below:

### Copy the font files to the Linux system path

1. Put a folder named **fonts** into your program directory, and copy the font files you need into this folder.  
2. Add the following command to your Linux Dockerfile:
   ```dockerfile
   COPY fonts/ /usr/share/fonts
   ```
3. After the above operation, the font files will be copied to the Linux system path. Aspose.Cells will go to the system path to find and use them. This is our recommended scenario.

### Set Font Folder with Aspose.Cells API

In some cases, you may not be able to control or modify the Linux system directory—for example, on cloud servers. In this case, you can use the second scenario.

1. Put a folder named **fonts** into your program directory, and copy the font files you need into this folder.  
2. In your program code, call the Aspose.Cells API:
   ```csharp
   Aspose.Cells.FontConfigs.SetFontFolder("fonts", true);
   ```
3. The above operation will ensure the program can find the fonts from the project path.

## See Also

- [How to Run Aspose.Cells for .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
