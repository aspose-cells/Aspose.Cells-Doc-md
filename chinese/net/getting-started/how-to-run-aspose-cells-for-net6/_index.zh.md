---
title: 如何运行 Aspose.Cells for .Net6
type: docs
description: "如何在 .Net6 上运行 Aspose.Cells"
weight: 138
url: /zh/net/how-to-run-aspose-cells-for-net6/
---

## 概述

对于 .NET6（或更高版本）平台，与之前的平台（.netcore31或之前）相比，一个重要的区别在于图形库。 
在这份官方[微软文档](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only)中，它说明了对于.NET6或以后的发布版本，图形库"System.Drawing.Common" 仅在Windows上得到支持，并提出了替换图形库的建议。

对于Apose.Cells产品，我们已经进行了评估并完成了图形库的迁移。在非Windows系统中，我们使用SkiaSharp代替System.Drawing.Common，正如Microsoft官方文档建议的那样。请注意，这个关键性的变化将在Aspose.Cells 22.10.1或更高版本中对.NET6生效。

对于 .netcore31 或更早版本，为了保持兼容性和稳定性，目前我们仍然使用 "System.Drawing.Common" 图形库。.netcore31 或更早版本的依赖关系如下：
- System.Drawing.Common, 4.7.0。
- System.Security.Cryptography.Pkcs, 5.0.1。
- System.Text.Encoding.CodePages, 4.7.0。

## 在 Windows 上运行 Aspose.Cells for .Net6

首先，您可以使用 VS2022 创建一个 .net6 应用程序，然后可以选择以下安装选项：

### 通过 Nuget 安装

1. 从 NuGet 搜索 Aspose.Cells：[Aspose.Cells for .NET NuGet Package](https://www.nuget.org/packages/Aspose.Cells/)。 
您还可以在 VS2022 中的 NuGet 包管理器中安装 Aspose.Cells。

2. 自动安装"SkiaSharp"或"System.Drawing.Common"作为 Aspose.Cells 22.10.1 或更高版本在 .Net6 平台上的依赖项，这取决于您项目中的"目标操作系统"配置。
- 为您的项目设置"目标操作系统"为"Windows"，您将在 Windows 系统上为 .Net6 项目使用"System.Drawing.Common"作为依赖项。在此配置中，绘图结果更接近 .netcore31 或之前的版本。
**！[配置目标操作系统](TargetOS.png)**
- 为项目设置"目标操作系统"为"None"或其他选项，您将在 Windows 系统上为 .Net6 项目使用"SkiaSharp"作为依赖项。*请注意使用"SkiaSharp"作为依赖项的版本不支持打印到打印机的功能。*

### 通过 msi 或 DLL 安装

1. [下载 Aspose.Cells.msi 或 DLL](https://releases.aspose.com/cells/net/)。

2. 打开安装目录或 DLL 目录，然后选择以下步骤 3 或 4：

3. 找到"net6.0-windows"子目录，在 .net6 应用程序中添加 Aspose.Cells.dll。手动向您的 .net6 项目中添加以下 NuGet 包：
- System.Drawing.Common, 4.7.0。
- System.Security.Cryptography.Pkcs, 6.0.3。
- System.Text.Encoding.CodePages, 4.7.0。

通过这种方式，在 Windows 系统上为 .Net6 项目使用"System.Drawing.Common"作为依赖项。在此配置中，绘图结果更接近 .netcore31 或之前的版本。

4. 找到"net6.0"子目录，在 .net6 应用程序中添加 Aspose.Cells.dll。手动向您的 .net6 项目中添加以下 NuGet 包：
- SkiaSharp, 2.88.6。
- System.Security.Cryptography.Pkcs, 6.0.3。
- System.Text.Encoding.CodePages, 4.7.0。

通过这种方式，在 Windows 系统上为 .Net6 项目使用"SkiaSharp"作为依赖项。*请注意使用"SkiaSharp"作为依赖项的版本不支持打印到打印机的功能。*
## 在Linux上运行Aspose.Cells for .Net6

参考在Windows上的安装方法，在Linux系统中只能选择SkiaSharp作为图形库依赖。

您需要执行以下附加操作以确保在Linux下正确使用SkiaSharp:

1. 在您的Linux系统中运行以下命令:
```
apt-get update && apt-get install -y libfontconfig1
```
要么
```
apk update && apk add fontconfig 
```

2. 将NuGet包"SkiaSharp.NativeAssets.Linux 2.88.6"添加到您的.net6项目中。

3. 或者您可以选择将NuGet包"SkiaSharp.NativeAssets.Linux.NoDependencies 2.88.6"添加到您的.net6项目中，而不是上述两个步骤。

### Ubuntu示例Dockerfile

1. 将NuGet包"SkiaSharp.NativeAssets.Linux 2.88.6"添加到您的.net6项目中。

2. 使用以下Dockerfile:
{{< highlight plain >}}
# Ubuntu 20.04
FROM mcr.microsoft.com/dotnet/runtime:6.0-focal AS base
WORKDIR /app

# add "libfontconfig1" package if using "SkiaSharp.NativeAssets.Linux" in your project
# Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apt-get update && apt-get install -y libfontconfig1

# Copy fonts from local to docker
# For example, put a "fonts" folder in your project folder, and put the font files in it,
# then, use the following line:
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

### Alpine示例Dockerfile

1. 将NuGet包"SkiaSharp.NativeAssets.Linux 2.88.6"添加到您的.net6项目中。

2. 使用以下Dockerfile:
{{< highlight plain >}}
#Alpine 3.16
FROM mcr.microsoft.com/dotnet/runtime:6.0-alpine3.16 AS base
WORKDIR /app

# add "fontconfig" package if using "SkiaSharp.NativeAssets.Linux" in your project
# Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apk update && apk add fontconfig 

# Copy fonts from local to docker
# For example, put a "fonts" folder in your project folder, and put the font files in it,
# then, use the following line:
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
