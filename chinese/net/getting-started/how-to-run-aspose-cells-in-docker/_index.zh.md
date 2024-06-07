---
title: 如何在 Docker 中运行 Aspose.Cells
type: docs
description: 在 Linux、Windows Server 和任何操作系统中运行 Aspose.Cells 的 Docker 容器。
weight: 139
url: /zh/net/how-to-run-aspose-cells-in-docker/
---

微服务与容器化结合，使得轻松组合各种技术成为可能。Docker 允许您轻松集成 Aspose.Cells 功能到您的应用程序中，无论开发栈中使用的是哪种技术。

如果您的目标是微服务，或者栈中的主要技术不是 .NET、C++ 或 Java，但您需要 Aspose.Cells 的功能，或者您已经在栈中使用 Docker，则您可能有兴趣在 Docker 容器中使用 Aspose.Cells。

## 先决条件

- 您的系统上必须安装 Docker。有关在 Windows 或 Mac 上安装 Docker 的信息，请参考“参见”部分中的链接。

- 还要注意，示例中使用的是 Visual Studio 2019、.NET Core 3.1 SDK。


## Hello World 应用程序

在此示例中，您将创建一个简单的 Hello World 控制台应用程序，生成并保存一个“Hello World！”文档，支持所有的保存格式。该应用程序可以在 Docker 中构建和运行。

### 创建控制台应用程序

要创建 Hello World 程序，请按照以下步骤操作：
1. 安装 Docker 后，请确保它使用的是 Linux 容器（默认设置）。如果需要，请从 Docker Desktop 菜单中选择“切换到 Linux 容器”选项。
1. In Visual Studio, create a .NET Core console application.<br>
![todo:image_alt_text](create-a-new-project.png)<br>
1. Install the latest Aspose.Cells version from NuGet. System.Drawing.Common and System.Text.Encoding.CodePages will be installed as a dependency of Aspose.Cells.<br>
![todo:image_alt_text](nuget-aspose-cells.png)<br>
1. 由于应用程序将在 Linux 上运行，因此需要安装适当的本地 Linux 资源。使用 dotnet core sdk 3.1 基础镜像并安装 libgdiplus libc6-dev。
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

请注意，“TestOut”文件夹被指定为保存输出文档的输出文件夹。当在 Docker 中运行应用程序时，会将主机机器上的文件夹挂载到容器中的此文件夹。这样您就可以轻松查看 Aspose.Cells 在 Docker 容器中生成的输出。

### 配置 Dockerfile

下一步是创建和配置 Dockerfile。

1. 创建 Dockerfile，并将其放置在应用程序的解决方案文件旁边。保持文件名不变，不要添加扩展名（使用默认值）。
1. 在 Dockerfile 中指定：

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

上述是一个简单的 Dockerfile，其中包含以下指令：

- 要使用的 SDK 镜像。这里使用的是 .Net Core SDK 3.1 镜像。Docker 将在构建运行时下载它。 SDK 的版本指定为标签。
- 安装字体，因为 SDK 镜像中包含的字体很少。该命令将字体文件从本地复制到 Docker 镜像中。确保您有一个名为“fonts”的本地目录，其中包含您需要安装的所有字体。在本示例中，将本地的“fonts”目录放置在与 Dockerfile 相同的目录中。
- 工作目录，在下一行中指定。
- 复制所有内容到容器中，发布应用程序，并指定入口点。
- 在容器中运行安装 libgdiplus 的命令。这是 System.Drawing.Common 所需的。

### 在 Docker 中构建和运行应用程序

现在可以在 Docker 中构建和运行应用程序了。打开您喜欢的命令提示符，将目录更改为应用程序所在的文件夹（解决方案文件和 Dockerfile 所在的文件夹），然后运行以下命令：

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

第一次执行此命令时可能需要更长时间，因为 Docker 需要下载所需的镜像。完成上一个命令后，请运行以下命令：

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

要注意 mount 参数，因为如前所述，将主机机器上的文件夹挂载到容器的文件夹中，以便轻松查看应用程序执行的结果。Linux 中的路径区分大小写。

{{% /alert %}}

## 支持 Aspose.Cells 的镜像

- Aspose.Cells for .NET Standard 在 Linux 上不支持 EMF 和 TIFF。


## 更多示例

***1. 在Windows Server 2019上运行应用程序***

- Dockerfile

{{< highlight plain >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]
{{< /highlight >}}

- 构建Docker镜像

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- 运行Docker镜像

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. 在Linux上运行应用程序***

- 编写一个简单的程序，设置字体文件夹，创建一个“Hello World！”工作簿并保存它。

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

- 构建Docker镜像

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- 运行Docker镜像

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## 请参阅

- [在Windows上安装Docker桌面版](https://docs.docker.com/docker-for-windows/install/)
- [在Mac上安装Docker桌面版](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019，.NET Core 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- 切换到[Linux容器](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers)选项
- 关于[.NET Core SDK](https://hub.docker.com/_/microsoft-dotnet-sdk)的其他信息
