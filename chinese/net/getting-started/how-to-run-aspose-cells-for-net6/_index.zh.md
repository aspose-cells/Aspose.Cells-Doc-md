---
title: 在 .Net6 中运行 Aspose.Cells
type: docs
description: “如何在 .Net6 中运行 Aspose.Cells。”
weight: 138
url: /zh/net/how-to-run-aspose-cells-for-net6/
---

## 概述

对于 .NET6（或更高版本）平台，与之前的平台（.netcore31 或更早版本）相比，一个重要的区别是关于图形库。 
在这份官方[微软文档](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only)中，它解释了对于 .NET6 或更高版本，图形库“System.Drawing.Common”将仅在 Windows 上受支持，并就替换图形库提出建议。

对于Apose.Cells产品，我们已经进行了评估并已完成了图形库的迁移。在非Windows系统中，我们使用SkiaSharp代替System.Drawing.Common，这是在微软官方文档中建议的。请注意，这个重要的更改将在Aspose.Cells 22.10.1或更高版本的.Net6中生效。

对于.netcore31或之前版本，为了兼容性和稳定性，我们目前仍然使用"System.Drawing.Common"图形库。.netcore31或之前版本的依赖项如下:
- System.Drawing.Common, 5.0.3.
- System.Security.Cryptography.Pkcs, 6.0.5。
- System.Text.Encoding.CodePages, 4.7.0.

## 在 Windows 上运行 Aspose.Cells for .Net6（或更高版本）

首先，您可以使用 VS2022 创建一个 .net6（或更高版本）应用程序，然后可以选择以下安装选项：

### 通过NuGet安装

1. 从 NuGet 搜索 Aspose.Cells: [Aspose.Cells for .NET NuGet软件包](https://www.nuget.org/packages/Aspose.Cells/). 
您还可以通过VS2022的NuGet包管理器安装Aspose.Cells。

2. "SkiaSharp" 或 "System.Drawing.Common" 将作为 Aspose.Cells 22.10.1 或更高版本的依赖自动安装，这取决于您的项目中的 "Target OS" 配置。
- 将您的项目的 "Target OS" 设置为 "Windows"，您将在 Windows 系统中使用 "System.Drawing.Common" 作为依赖。在此配置中，绘图效果更接近 .netcore31 及之前版本。
**![配置目标OS](TargetOS.png)**
- 将您的项目的 "Target OS" 设置为 "None" 或其他选项，在 Windows 系统中将使用 "SkiaSharp" 作为依赖。*请注意，使用 "SkiaSharp" 作为依赖的版本不支持打印功能。*

### 通过msi或DLL安装

1. [下载Aspose.Cells.msi或DLL](https://releases.aspose.com/cells/net/)。

2. 打开安装目录或DLL目录，然后选择以下步骤3或4:

3. 找到"net6.0-windows"子目录，在其中添加Aspose.Cells.dll到您的.net6应用程序。手动将以下NuGet包添加到您的.net6项目:
- System.Drawing.Common, 6.0.0.
- System.Security.Cryptography.Pkcs, 6.0.5。
- System.Text.Encoding.CodePages, 4.7.0.

这样，您将在 Windows 系统中使用 "System.Drawing.Common" 作为依赖。在此配置中，绘图效果更接近 .netcore31 及之前版本。

4. 找到"net6.0"子目录，在其中添加Aspose.Cells.dll到您的.net6应用程序。手动将以下NuGet包添加到您的.net6项目:
- SkiaSharp, 3.116.1。
- System.Security.Cryptography.Pkcs, 6.0.5。
- System.Text.Encoding.CodePages, 4.7.0.

这样，您将在 Windows 系统中使用 "SkiaSharp" 作为依赖。*请注意，使用 "SkiaSharp" 作为依赖的版本不支持打印功能。*

## 在 Linux 上运行 Aspose.Cells for .Net6（或更高版本）

参考在Windows上的安装方法，您只能在Linux系统上选择SkiaSharp作为图形库依赖项。

您需要执行以下附加操作以确保在Linux下正确使用SkiaSharp:

1. 在您的Linux系统中运行以下命令:
```
apt-get update && apt-get install -y libfontconfig1
```
或者
```
apk update && apk add fontconfig 
```

2. 将 nuget 包 "SkiaSharp.NativeAssets.Linux 3.116.1" 添加到您的 .net6（或更高版本）项目中。
3. 或者，您可以选择添加 nuget 包 "SkiaSharp.NativeAssets.Linux.NoDependencies 3.116.1"，替代上述两个步骤。

*请注意，所添加包 "SkiaSharp.NativeAssets.Linux" 或 "SkiaSharp.NativeAssets.Linux.NoDependencies" 的版本应与 Aspose.Cells for .NET 引用的 "SkiaSharp" 版本相对应。Aspose.Cells for .NET 和相应引用的 "SkiaSharp" 版本的描述如下：*

| Aspose.Cells for .NET |                SkiaSharp                |
| :--------------------: | :-------------------------------------: |
| >= 22.10.1 && <= 22.11 |                 2.88.0                  |
|  >= 22.12 && <= 23.9   |                 2.88.3                  |
|  >= 23.10 && <= 24.12  |                 2.88.6                  |
|        = 25.1.1        |                 3.116.1                 |
|        >=25.1.2        | 2.88.9（net6.0，net8.0），3.116.1（net9.0） |



### Ubuntu的Dockerfile示例

1. 将 nuget 包 "SkiaSharp.NativeAssets.Linux 3.116.1" 添加到您的 .net6（或更高版本）项目中。

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

### Alpine的Dockerfile示例

1. 将 nuget 包 "SkiaSharp.NativeAssets.Linux 3.116.1" 添加到您的 .net6（或更高版本）项目中。

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
{{< app/cells/assistant language="csharp" >}}
