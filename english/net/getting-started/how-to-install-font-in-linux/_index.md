---
title: How to Install Font in Linux
type: docs
description: "How to Install Font in Linux"
weight: 139
url: /net/how-to-install-font-in-linux/
---

## Overview

When using Aspose.Cells in Linux, as Linux has fewer default fonts, the font referenced in your Excel file may not exist by default on your Linux system.
When this happens, Aspose.Cells will use a similar font instead to show the characters. However, this could cause the following effects:

1. Different fonts can result in images that are rendered in different layouts than Excel.
2. Since the font has changed, the output characters may not be to your satisfaction.

In order for your program to output more accurate results, install the fonts you need under Linux. It is important to make sure that the fonts you use in Excel files exist in your environment.

## How to Install font in Linux

There are two ways to install fonts on Linux, as described below:

### Copy the font files to the Linux system path

1. Put a folder named "fonts" into your program directory, copy the font files you need into this folder.
2. Add the following command to your Linux Dockerfile:
```
COPY fonts/ /usr/share/fonts
```
3. After the above operation, the font files will be copied to the Linux system path. Aspose.Cells will go to the system path and to find and use them. This is our recommended scenario.

### Set Font Folder with Aspose.Cells API
In some cases, you may not be able to control or modify the Linux system directory. For example, on cloud servers. In this case, you can use the second scenario.
1. Put a folder named "fonts" into your program directory copy the font files you need into this folder.
2. In your program code, call Aspose.Cells API:
```
Aspose.Cells.FontConfigs.SetFontFolder("fonts", true);
```
3. The above operation will make sure the program can find the font from the project path.

## See Also

- [How to Run Aspose.Cells for .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

