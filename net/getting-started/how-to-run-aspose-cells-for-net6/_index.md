---
title: How to Run Aspose.Cells for .Net6
type: docs
description: "How to Run Aspose.Cells for .Net6."
weight: 138
url: /net/how-to-run-aspose-cells-for-net6/
---

## Overview

For the .NET6 (or later) platforms, compare to previous platforms (.netcore31 or before), an important difference is about the graphics library. 
In this official [Microsoft Document](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), it explains for .NET6 or later releases the graphics library "System.Drawing.Common" will not be supported for detailed reasons, and gives recommendations to replace the graphics library.

For Apose.Cells product, we have conducted the evaluation and have completed the migration of the graphics library. We use SkiaSharp instead of System.Drawing.common, as suggested in Microsoft's official documentation. Please note that this critical change will take effect in Aspose.Cells 22.10 or later for .Net6.

For .netcore31 or before, 

## Run Aspose.Cells for .Net6 on Windows

First you can create a .net6 application with VS2022, then you can then choose the following installation options:

### Install through nuget

Search for Aspose.Cells version from NuGet. SkiaSharp will be installed as a dependency of Aspose.Cells 22.10 or later for .Net6 platforms.

[Aspose.Cells for .NET NuGet Package](https://www.nuget.org/packages/Aspose.Cells/)

### Install through msi or DLL

1. [Download Aspose.Cells.msi or DLL](https://releases.aspose.com/cells/net/)

2. Open the installation directory or the DLL directory and locate the "net6.0" subdirectory, add the Aspose.Cells.dll in it to your .net6 application.

3. Manually add the following nuget packages to your .net6 project:
- SkiaSharp, 2.88.0.
- System.Security.Cryptography.Pkcs, 6.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

## Run Aspose.Cells for .Net6 on Linux

Refer to the installation method on Windows, you need to do the following additional operations to ensure proper use of SkiaSharp under Linux:

1. Run the following command in your Linux System:
{{< highlight plain >}}
RUN apt-get update && apt-get install -y libfontconfig1
{{< /highlight >}}

2. Add the nuget packages "SkiaSharp.NativeAssets.Linux" to your .net6 project.

3. Or you can choose to add nuget packages "SkiaSharp.NativeAssets.Linux.NoDependencies 2.88.0" to your .net6 project, instead of the two steps above.
