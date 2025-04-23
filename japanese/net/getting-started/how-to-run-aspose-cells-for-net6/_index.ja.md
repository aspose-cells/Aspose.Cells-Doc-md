---
title: .Net6 で Aspose.Cells を実行する方法
type: docs
description: 「.Net6 で Aspose.Cells を実行する方法について。」
weight: 138
url: /ja/net/how-to-run-aspose-cells-for-net6/
---

## 概要

.NET6（またはそれ以降）プラットフォームでは、以前のプラットフォーム（.netcore31 より前）と比較して、重要な違いはグラフィックスライブラリに関するものです。 
この公式[Microsoftドキュメント](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only)では、.NET6 以降についてグラフィックスライブラリの「System.Drawing.Common」がWindowsでのみサポートされると説明され、グラフィックスライブラリの置換に関する推奨事項が示されています。

Aspose.Cells製品に関して、非WindowsシステムではMicrosoftの公式ドキュメントで推奨されているように、System.Drawing.Commonの代わりにSkiaSharpを使用し、グラフィックライブラリの移行を完了しました。この重要な変更はAspose.Cells 22.10.1以降の.Net6で有効になります。

.netcore31 より前の場合、互換性と安定性のため、現在も「System.Drawing.Common」グラフィックスライブラリを使用しています。.netcore31 より前の場合の依存関係は以下のとおりです:
- System.Drawing.Common, 5.0.3.
- System.Security.Cryptography.Pkcs、6.0.5。
- System.Text.Encoding.CodePages, 4.7.0.

## Windows で .Net6 の Aspose.Cells を実行する

まず、VS2022 で .net6 アプリケーションを作成し、次に以下のインストールオプションを選択します。

### Nuget を使用してインストール

1. NuGet から Aspose.Cells を検索: [Aspose.Cells for .NET NuGet Package](https://www.nuget.org/packages/Aspose.Cells/) 
また、VS2022 の NuGet パッケージマネージャからも Aspose.Cells をインストールすることができます。

2. "SkiaSharp" または "System.Drawing.Common" は、Aspose.Cells 22.10.1 以降の .Net6 プラットフォームに自動的に依存関係としてインストールされます。これは、プロジェクトの「Target OS」構成に依存します。
- プロジェクトの「Target OS」を「Windows」に設定すると、.Net6 プロジェクトでWindowsシステムに「System.Drawing.Common」が依存するようになります。この構成では、描画の結果が.netcore31 より前に近づきます。
**![Config target OS](TargetOS.png)**
- プロジェクトの「Target OS」を「None」またはその他のオプションに設定すると、.Net6 プロジェクトでWindowsシステムに「SkiaSharp」が依存するようになります。*「SkiaSharp」を依存とするバージョンでは、プリンターへの印刷機能はサポートされないことに注意してください。

### msi または DLL を使用してインストール

1. [Aspose.Cells.msi または DLL をダウンロード](https://releases.aspose.com/cells/net/)

2. インストールディレクトリまたは DLL ディレクトリを開き、次に以下のステップ 3 または 4 を選択します:

3. "net6.0-windows" サブディレクトリを見つけ、それに含まれる Aspose.Cells.dll を .net6 アプリケーションに追加します。次に、以下の NuGet パッケージを .net6 プロジェクトに手動で追加します:
- System.Drawing.Common, 6.0.0.
- System.Security.Cryptography.Pkcs、6.0.5。
- System.Text.Encoding.CodePages, 4.7.0.

この方法で、.Net6 プロジェクトでWindowsシステムに「System.Drawing.Common」が依存するようになります。この構成では、描画の結果が.netcore31 より前に近づきます。

4. "net6.0" サブディレクトリを見つけ、それに含まれる Aspose.Cells.dll を .net6 アプリケーションに追加します。次に、以下の NuGet パッケージを .net6 プロジェクトに手動で追加します:
- SkiaSharp、3.116.1。
- System.Security.Cryptography.Pkcs、6.0.5。
- System.Text.Encoding.CodePages, 4.7.0.

この方法で、.Net6 プロジェクトでWindowsシステムに「SkiaSharp」が依存するようになります。*「SkiaSharp」を依存とするバージョンでは、プリンターへの印刷機能はサポートされないことに注意してください。
## Linux で .Net6 の Aspose.Cells を実行する

Windowsでのインストール方法については、Linuxシステム上でのグラフィックライブラリ依存関係としてSkiaSharpを選択することしかできません。

LinuxでSkiaSharpを正しく使用するためには、以下の追加操作を行う必要があります。

1. Linuxシステムで以下のコマンドを実行します:
```
apt-get update && apt-get install -y libfontconfig1
```
または
```
apk update && apk add fontconfig 
```

2. NuGetパッケージ「SkiaSharp.NativeAssets.Linux 3.116.1」をあなたの.NET6プロジェクトに追加します。
3. もしくは、NuGetパッケージ「SkiaSharp.NativeAssets.Linux.NoDependencies 3.116.1」を追加し、上記の二つのステップの代わりに使用できます。

*追加パッケージ "SkiaSharp.NativeAssets.Linux" または "SkiaSharp.NativeAssets.Linux.NoDependencies" のバージョンは、Aspose.Cells for .NETによって参照されている "SkiaSharp" のバージョンに対応している必要があります。Aspose.Cells for .NET のバージョンと対応する参照 "SKiaSharp" のバージョンは以下の通りです:*

| Aspose.Cells for .NET  |                SkiaSharp                |
| :--------------------: | :-------------------------------------: |
| >= 22.10.1 && <= 22.11 |                 2.88.0                  |
|  >= 22.12 && <= 23.9   |                 2.88.3                  |
|  >= 23.10 && <= 24.12  |                 2.88.6                  |
|        = 25.1.1        |                 3.116.1                 |
|        >=25.1.2        | 2.88.9（net6.0、net8.0）、3.116.1（net9.0） |



### Ubuntu向けのDockerfileの例

1. NuGetパッケージ「SkiaSharp.NativeAssets.Linux 3.116.1」をあなたの.NET6プロジェクトに追加します。

2. 次のDockerfileを使用します:
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

### Alpine向けのDockerfileの例

1. NuGetパッケージ「SkiaSharp.NativeAssets.Linux 3.116.1」をあなたの.NET6プロジェクトに追加します。

2. 次のDockerfileを使用します:
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
