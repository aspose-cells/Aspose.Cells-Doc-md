---
title: Docker で Aspose.Cells を実行する方法
type: docs
description: Linux、Windows サーバー、および任意の OS の Docker コンテナーで Aspose.Cells を実行します。
weight: 139
url: /ja/net/how-to-run-aspose-cells-in-docker/
---
マイクロサービスとコンテナ化を組み合わせることで、テクノロジーを簡単に組み合わせることができます。 Docker を使用すると、開発スタックに含まれるテクノロジに関係なく、Aspose.Cells の機能をアプリケーションに簡単に統合できます。

マイクロサービスをターゲットにしている場合、またはスタックの主要なテクノロジが .NET、C++、または Java ではなく、Aspose.Cells の機能が必要な場合、またはスタックで既に Docker を使用している場合は、Docker で Aspose.Cells を利用することに興味があるかもしれません。容器。

## 前提条件

- Docker がシステムにインストールされている必要があります。 Windows または Mac に Docker をインストールする方法については、「関連項目」セクションのリンクを参照してください。

- また、以下に示す例では、Visual Studio 2019、.NET Core 3.1 SDK が使用されていることに注意してください。


## Hello World お申し込み

この例では、「Hello World!」を生成する単純な Hello World コンソール アプリケーションを作成します。サポートされているすべての保存形式で保存します。その後、アプリケーションをビルドして Docker で実行できます。

### コンソール アプリケーションの作成

Hello World プログラムを作成するには、次の手順に従います。
1. Docker がインストールされたら、Linux コンテナー (デフォルト) が使用されていることを確認します。必要に応じて、Docker デスクトップ メニューから [Linux コンテナーに切り替える] オプションを選択します。
1. Visual Studio で、.NET Core コンソール アプリケーションを作成します。<br>
![todo:画像_代替_文章](create-a-new-project.png)<br>
1. NuGet から最新の Aspose.Cells バージョンをインストールします。System.Drawing.Common および System.Text.Encoding.CodePages は、Aspose.Cells の依存関係としてインストールされます。<br>
![todo:画像_代替_文章](nuget-aspose-cells.png)<br>
1. アプリケーションは Linux で実行されるため、適切なネイティブ Linux アセットをインストールする必要があります。 dotnet core sdk 3.1 ベース イメージから始めて、libgdiplus libc6-dev をインストールします。
1. 必要なすべての依存関係が追加されたら、「Hello World!」を作成する簡単なプログラムを作成します。サポートされているすべての保存形式で保存します。<br>
**.NET**<br>
{{< highlight "csharp" >}}
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

なお、出力文書を保存する出力フォルダとして「TestOut」フォルダを指定します。 Docker でアプリケーションを実行すると、ホスト マシン上のフォルダーがコンテナー内のこのフォルダーにマウントされます。これにより、Docker コンテナーで Aspose.Cells によって生成された出力を簡単に表示できます。

### Dockerfile の構成

次のステップは、Dockerfile を作成して構成することです。

1. Dockerfile を作成し、アプリケーションのソリューション ファイルの横に配置します。このファイル名には拡張子を付けずに保持します (デフォルト)。
1. Dockerfile で、次を指定します。

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
COPY fonts/* /usr/share/fonts/
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

上記は単純な Dockerfile で、次の手順が含まれています。

- 使用する SDK イメージ。これが .Net Core SDK 3.1 イメージです。 Docker は、ビルドの実行時にそれをダウンロードします。タグには SDK のバージョンを指定します。
- SDK イメージにはフォントがほとんど含まれていないため、フォントをインストールします。このコマンドは、フォント ファイルをローカルから Docker イメージにコピーします。インストールする必要があるすべてのフォントを含むローカルの「fonts」ディレクトリがあることを確認してください。この例では、ローカルの "fonts" ディレクトリが Dockerfile と同じディレクトリに置かれています。
- 次の行で指定されている作業ディレクトリ。
- すべてをコンテナにコピーし、アプリケーションを公開し、エントリ ポイントを指定するコマンド。
- libgdiplus をインストールするコマンドはコンテナーで実行されます。これは System.Drawing.Common で必要です。

### Docker でのアプリケーションのビルドと実行

これで、アプリケーションをビルドして Docker で実行できるようになりました。任意のコマンド プロンプトを開き、ディレクトリをアプリケーションのあるフォルダー (ソリューション ファイルと Dockerfile が配置されているフォルダー) に変更し、次のコマンドを実行します。

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

このコマンドを初めて実行するときは、Docker が必要なイメージをダウンロードする必要があるため、時間がかかる場合があります。前のコマンドが完了したら、次のコマンドを実行します。

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

前述のように、アプリケーションの実行結果を簡単に確認できるように、ホスト マシン上のフォルダーがコンテナーのフォルダーにマウントされるため、mount 引数に注意してください。 Linux のパスは大文字と小文字が区別されます。

{{% /alert %}}

## Aspose.Cellsをサポートする画像

- Aspose.Cells for .NET 標準は Linux で EMF と TIFF をサポートしていません。


## その他の例

***1. Windows Server 2019 でアプリケーションを実行するには***

- Dockerfile

{{< highlight "plain" >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

- Docker イメージのビルド

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Docker イメージの実行

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. Linux でアプリケーションを実行するには***

- フォントフォルダーを設定し、「Hello World!」を作成する簡単なプログラムを作成します。ワークブックを作成して保存します。

{{< highlight "csharp" >}}
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

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.Fonts.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.Fonts.dll"]{{< /highlight >}}

- Docker イメージのビルド

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Docker イメージの実行

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## 関連項目

- [Windows に Docker デスクトップをインストールします。](https://docs.docker.com/docker-for-windows/install/)
- [Mac に Docker デスクトップをインストールする](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019、.NET コア 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- [Linux コンテナーに切り替える](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers)オプション
- に関する追加情報[.NET コア SDK](https://hub.docker.com/_/microsoft-dotnet-sdk)
