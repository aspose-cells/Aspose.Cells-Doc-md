---
title: 如何为 .Net6 运行 Aspose.Cells
type: docs
description: 如何为 .Net6 运行 Aspose.Cells
weight: 138
url: /zh/net/how-to-run-aspose-cells-for-net6/
---
## 概述

对于 .NET6（或更高版本）平台，与以前的平台（.netcore31 或之前）相比，一个重要的区别在于图形库。
在这个官方[Microsoft 文档](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only)，它解释了 .NET6 或更高版本的图形库“System.Drawing.Common”将仅在 Windows 上受支持，并给出了替换图形库的建议。

对于Apose.Cells产品，我们进行了评估，并完成了图库的迁移。我们在非 Windows 系统中使用 SkiaSharp 而不是 System.Drawing.Common，如 Microsoft 的官方文档中所建议的那样。请注意，此重要更改将在 Aspose.Cells 22.10.1 或更高版本的 .Net6 中生效。

对于.netcore31或之前的版本，为了兼容性和稳定性，目前我们仍然使用“System.Drawing.Common”图形库。 .netcore31 或之前版本的依赖如下：
- System.Drawing.Common，4.7.0。
- System.Security.Cryptography.Pkcs，5.0.1。
- System.Text.Encoding.CodePages，4.7.0。

## 在 Windows 上为 .Net6 运行 Aspose.Cells

首先你可以用VS2022创建一个.net6的应用程序，然后你可以选择以下安装选项：

### 通过nuget安装

1. 从 NuGet 搜索 Aspose.Cells：[Aspose.Cells for .NET NuGet 包](https://www.nuget.org/packages/Aspose.Cells/). 
您也可以从 VS2022 中的 Nuget 包管理器安装 Aspose.Cells。

2.“SkiaSharp”或“System.Drawing.Common”将自动安装为 Aspose.Cells 22.10.1 或更高版本的 .Net6 平台的依赖项，这取决于项目中的“目标操作系统”配置。
- 将项目的“目标操作系统”设置为“Windows”，您将使用“System.Drawing.Common”作为 .Net6 项目对 Windows 系统的依赖。在这个配置中，绘图的结果更接近.netcore31 或之前。
**![配置目标操作系统](TargetOS.png)**
- 将“目标操作系统”设置为“无”或项目的其他选项，您将使用“SkiaSharp”作为 .Net6 项目对 Windows 系统的依赖项。*请注意，使用“SkiaSharp”作为依赖项的版本不支持打印到打印机功能。*

### 通过 msi 或 DLL 安装

1. [下载 Aspose.Cells.msi 或 DLL](https://releases.aspose.com/cells/net/)

2、打开安装目录或DLL目录，然后选择下面的步骤3或4：

3. 找到“net6.0-windows”子目录，将其中的Aspose.Cells.dll 添加到您的.net6 应用程序中。手动将以下 nuget 包添加到您的 .net6 项目中：
- System.Drawing.Common，4.7.0。
- System.Security.Cryptography.Pkcs，6.0.1。
- System.Text.Encoding.CodePages，4.7.0。

这样，您将使用“System.Drawing.Common”作为 .Net6 项目对 Windows 系统的依赖。在这个配置中，绘图的结果更接近.netcore31 或之前。

4. 找到“net6.0”子目录，将其中的Aspose.Cells.dll 添加到您的.net6 应用程序中。手动将以下 nuget 包添加到您的 .net6 项目中：
- SkiaSharp，2.88.3。
- System.Security.Cryptography.Pkcs，6.0.1。
- System.Text.Encoding.CodePages，4.7.0。

这样，您将使用“SkiaSharp”作为 .Net6 项目对 Windows 系统的依赖。*请注意，使用“SkiaSharp”作为依赖项的版本不支持打印到打印机功能。*
## 在 Linux 上为 .Net6 运行 Aspose.Cells

参考Windows的安装方法，Linux系统只能选择SkiaSharp作为图形库依赖。

您需要进行以下额外操作以确保在 Linux 下正确使用 SkiaSharp：

1. 在您的 Linux 系统中运行以下命令：
```
apt-get update && apt-get install -y libfontconfig1
```
OR
```
apk update && apk add fontconfig 
```

2. 将 nuget 包“SkiaSharp.NativeAssets.Linux 2.88.3”添加到您的 .net6 项目中。

3. 或者您可以选择将 nuget 包“SkiaSharp.NativeAssets.Linux.NoDependencies 2.88.3”添加到您的 .net6 项目，而不是上面的两个步骤。

###  Ubuntu 的示例 Dockerfile

1. 将 nuget 包“SkiaSharp.NativeAssets.Linux 2.88.3”添加到您的 .net6 项目。

2. 使用以下 Dockerfile：
{{< highlight "plain" >}}
#  Ubuntu 20.04
FROM mcr.microsoft.com/dotnet/runtime:6.0-focal AS base
WORKDIR /app

#  add "libfontconfig1" package if using "SkiaSharp.NativeAssets.Linux" in your project
#  Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apt-get update && apt-get install -y libfontconfig1

#  Copy fonts from local to docker
#  For example, put a "fonts" folder in your project folder, and put the font files in it,
#  then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build
WORKDIR /src
COPY ["Ubuntu_Docker.csproj", "."]
RUN dotnet restore "./Ubuntu_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Ubuntu_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ubuntu_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ubuntu_Docker.dll"]
{{< /highlight >}}

###  Alpine 的示例 Dockerfile

1. 将 nuget 包“SkiaSharp.NativeAssets.Linux 2.88.3”添加到您的 .net6 项目。

2. 使用以下 Dockerfile：
{{< highlight "plain" >}}
# Alpine 3.16
FROM mcr.microsoft.com/dotnet/runtime:6.0-alpine3.16 AS base
WORKDIR /app

#  add "fontconfig" package if using "SkiaSharp.NativeAssets.Linux" in your project
#  Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apk update && apk add fontconfig 

#  Copy fonts from local to docker
#  For example, put a "fonts" folder in your project folder, and put the font files in it,
#  then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-alpine3.16 AS build
WORKDIR /src
COPY ["Alpine_Docker.csproj", "."]
RUN dotnet restore "./Alpine_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Alpine_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Alpine_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Alpine_Docker.dll"]
{{< /highlight >}}
