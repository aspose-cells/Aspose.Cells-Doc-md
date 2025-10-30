---
title: DockerでAspose.Cellsを実行する方法
type: docs
description: 「Linux、Windows Server、および他のOSのDockerコンテナでAspose.Cellsを実行する方法」
weight: 139
url: /ja/net/how-to-run-aspose-cells-in-docker/
---

マイクロサービスとコンテナ化を組み合わせることで、開発スタックにどのような技術があっても、Dockerを使用してAspose.Cellsの機能を簡単に統合することができます。 Dockerを使用すると、.NET、C++、またはJavaなどの技術に関係なく、アプリケーションにAspose.Cellsの機能を簡単に統合できます。

マイクロサービスを対象にしている場合、またはスタック内の主要な技術が.NET、C++、またはJavaではなく、Aspose.Cellsの機能が必要な場合、または既にスタックでDockerを使用している場合、DockerコンテナでAspose.Cellsを利用することに興味があるかもしれません。

## 前提条件

- システムにDockerをインストールしている必要があります。WindowsまたはMacにDockerをインストールする方法については、「関連項目」セクションのリンクを参照してください。

- また、以下に示す例でVisual Studio 2019、.NET Core 3.1 SDKが使用されています。


## Hello Worldアプリケーション

この例では、すべてのサポートされている保存形式にHello Worldコンソールアプリケーションを作成し、「Hello World!」ドキュメントを作成して保存します。 その後、アプリケーションをDockerでビルドして実行できます。

### コンソールアプリケーションの作成

Hello Worldプログラムを作成するには、以下の手順に従います:
1. Dockerがインストールされている場合、Linuxコンテナー（デフォルト）を使用することを確認します。必要に応じて、Docker DesktopのメニューからLinuxコンテナーに切り替えるオプションを選択します。
1. In Visual Studio, create a .NET Core console application.<br>
![todo:image_alt_text](create-a-new-project.png)<br>
1. Install the latest Aspose.Cells version from NuGet. System.Drawing.Common and System.Text.Encoding.CodePages will be installed as a dependency of Aspose.Cells.<br>
![todo:image_alt_text](nuget-aspose-cells.png)<br>
1. アプリケーションはLinuxで実行されるため、適切なネイティブLinuxアセットをインストールする必要があります。dotnet core sdk 3.1ベースイメージから始めて、libgdiplus libc6-devをインストールします。
1. When all required dependencies are added, write a simple program that creates a “Hello World!” workbook and saves it in all supported save formats:<br>
**.NET**<br>
{{< highlight csharp >}}
using System;
namespace Aspose.Cells.Docker
{
    class Program
    {
        static void Main(string[] args)
        {
            Workbook workbook = new Workbook();
            workbook.Worksheets[0].Cells[0, 0].PutValue("Hello from Aspose.Cells!!!");
            foreach (SaveFormat sf in Enum.GetValues(typeof(SaveFormat)))
            {
                if (sf != SaveFormat.Unknown)
                {
                    try
                    {
                        // The folder specified will be mounted as a volume when run the application in Docker image.
                        var fileName = string.Format("out{0}", FileFormatUtil.SaveFormatToExtension(sf));
                        workbook.Save(fileName, sf);
                        Console.WriteLine("Saving {0}\t\t[OK]", sf);
                    }
                    catch
                    {
                        Console.WriteLine("Saving {0}\t\t[FAILED]", sf);
                    }
                }
            }
        }
    }
}

{{< /highlight >}}

「TestOut」フォルダーが出力ドキュメントの出力先フォルダーとして指定されていることに注意してください。 Dockerでアプリケーションを実行すると、ホストマシン上のフォルダーがコンテナー内のこのフォルダーにマウントされます。これにより、Dockerコンテナー内で生成された出力を簡単に表示できます。

### Dockerfileの設定

次に、Dockerfileを作成および構成します。

1. Dockerfileを作成し、アプリケーションのソリューションファイルの隣に配置します。このファイル名は拡張子なしで保持してください（デフォルトのままで）。
1. Dockerfileで次のように指定します:

{{< highlight plain >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
COPY fonts/* /usr/share/fonts/
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]
{{< /highlight >}}

上記は簡単なDockerfileで、次の命令が含まれています:

- 使用されるSDKイメージ。ここでは、.Net Core SDK 3.1イメージです。ビルド実行時にDockerがダウンロードします。SDKのバージョンはタグで指定されています。
- SDKイメージには非常に少ないフォントしか含まれていないので、フォントをインストールします。コマンドでローカルからフォントファイルをドッカーイメージにコピーします。インストールする必要があるすべてのフォントを含むローカル「fonts」ディレクトリがあることを確認してください。この例では、ローカルの「fonts」ディレクトリがDockerfileと同じディレクトリに配置されています。
- 次の行で指定されている作業ディレクトリ。
- すべてをコンテナーにコピーして、アプリケーションを公開し、エントリーポイントを指定します。
- libgdiplusのインストールコマンドをコンテナーで実行します。これはSystem.Drawing.Commonに必要です。

### Dockerでアプリケーションのビルドと実行

ここで、アプリケーションをDockerでビルドして実行できます。お気に入りのコマンドプロンプトを開き、アプリケーションがあるフォルダーに移動し（解決ファイルとDockerfileが配置されているフォルダー）、次のコマンドを実行します:

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

このコマンドを実行するのは初めての場合は、必要なイメージをダウンロードするために時間がかかる場合があります。前のコマンドが完了したら、次のコマンドを実行します:

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

ホストマシン上のフォルダーがコンテナーのフォルダーにマウントされるため、mount引数に注意してください。Linuxのパスは大文字と小文字を区別しますので、注意してください。

{{% /alert %}}

## Aspose.Cellsをサポートするイメージ

- Aspose.Cells for .NET StandardはLinuxではEMFとTIFFをサポートしていません。


## その他の例

***1. Windows Server 2019でアプリケーションを実行する***

- Dockerfile

{{< highlight plain >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]
{{< /highlight >}}

- Dockerイメージのビルド

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Dockerイメージの実行

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. Linuxでアプリケーションを実行する***

- フォントフォルダを設定し、"Hello World!"ワークブックを作成して保存する単純なプログラムを書きます。

{{< highlight csharp >}}
namespace Aspose.Cells.Docker.Fonts
{
    using System;
    using System.IO;

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Set font folders on linux.
                string[] fonts = { "/Fonts" };
                FontConfigs.SetFontFolders(fonts, true);
                // build workbook
                Workbook workbook = new Workbook();
                MemoryStream memoryStream = new MemoryStream();
                workbook.Worksheets[0].Cells[0, 0].PutValue("Hello from Aspose.Cells!!!");
                Style style = workbook.CreateStyle();
                style.Font.Name = "Arial";
                style.Font.Size = 16;
                workbook.Worksheets[0].Cells[0, 0].SetStyle(style);
                workbook.Save("/TestOut/TestFontsOut.xlsx");
            }
            catch (Exception e)
            {
                Console.WriteLine("Saving outfonts.xlsx\t\t[FAILED],{0}", e.Message);
            }

        }
    }
}

{{< /highlight >}}
- Dockerfile

{{< highlight plain >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.Fonts.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.Fonts.dll"]
{{< /highlight >}}

- Dockerイメージのビルド

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Dockerイメージの実行

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

## 推奨ソリューション

.NET6（またはそれ以降）プラットフォームでは、以前のプラットフォーム（.netcore31 より前）と比較して、重要な違いはグラフィックスライブラリに関するものです。 
この公式[Microsoftドキュメント](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only)では、.NET6 以降についてグラフィックスライブラリの「System.Drawing.Common」がWindowsでのみサポートされると説明され、グラフィックスライブラリの置換に関する推奨事項が示されています。

したがって、Aspose.Cellsは非Windowsプラットフォーム上でSkiaSharpグラフィックスライブラリに依存したソリューションを提供しています。macOSではSkiaSharpをライブラリとして使用することをお勧めします。これにより、libgdiplusのインストールが不要となります。

非Windowsプラットフォーム上でAspose.Cellsをインストールし、SkiaSharpをグラフィックライブラリとして使用する方法については、以下の記事をご参照ください：
[Aspose.Cells for .Net6の実行方法](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

## 関連項目

- [Windows に Docker Desktop をインストールする](https://docs.docker.com/docker-for-windows/install/)
- [Mac に Docker Desktop をインストールする](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Core 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- [Linux コンテナに切り替える](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers) オプション
- [.NET Core SDK](https://hub.docker.com/_/microsoft-dotnet-sdk) の追加情報
{{< app/cells/assistant language="csharp" >}}
