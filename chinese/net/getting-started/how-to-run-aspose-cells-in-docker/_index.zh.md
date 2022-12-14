---
title: 如何在 Docker 中运行 Aspose.Cells
type: docs
description: 在 Linux、Windows 服务器和任何操作系统的 Docker 容器中运行 Aspose.Cells。
weight: 139
url: /zh/net/how-to-run-aspose-cells-in-docker/
---
微服务与容器化相结合，使得轻松组合技术成为可能。 Docker 允许您轻松地将 Aspose.Cells 功能集成到您的应用程序中，无论您的开发堆栈中采用何种技术。

如果您的目标是微服务，或者如果您堆栈中的主要技术不是 .NET、C++ 或 Java，但您需要 Aspose.Cells 功能，或者如果您已经在堆栈中使用 Docker，那么您可能有兴趣在 Docker 中使用 Aspose.Cells容器。

## 先决条件

- 必须在您的系统上安装 Docker。有关如何在 Windows 或 Mac 上安装 Docker 的信息，请参阅“另请参阅”部分中的链接。

- 另请注意，示例中使用了 Visual Studio 2019、.NET Core 3.1 SDK，如下所示。


## Hello World 申请

在此示例中，您创建了一个简单的 Hello World 控制台应用程序，它生成一个“Hello World!”文档并将其保存为所有支持的保存格式。然后可以在 Docker 中构建和运行应用程序。

### 创建控制台应用程序

要创建 Hello World 程序，请按照以下步骤操作：
1. 安装 Docker 后，确保它使用 Linux 容器（默认）。如有必要，从 Docker 桌面菜单中选择切换到 Linux 容器选项。
1. 在 Visual Studio 中，创建一个 .NET Core 控制台应用程序。<br>
![待办事项：图片_替代_文本](create-a-new-project.png)<br>
1. 从 NuGet 安装最新的 Aspose.Cells 版本。System.Drawing.Common 和 System.Text.Encoding.CodePages 将作为 Aspose.Cells 的依赖项安装。<br>
![待办事项：图片_替代_文本](nuget-aspose-cells.png)<br>
1. 由于应用程序将在 Linux 上运行，因此必须安装适当的本机 Linux 资产。从 dotnet core sdk 3.1 基础映像开始并安装 libgdiplus libc6-dev。
1. 添加所有必需的依赖项后，编写一个简单的程序来创建一个“Hello World！”工作簿并将其保存为所有支持的保存格式：<br>
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

请注意，“TestOut”文件夹被指定为用于保存输出文档的输出文件夹。当在 Docker 中运行应用程序时，主机上的一个文件夹将被挂载到容器中的这个文件夹中。这将使您能够轻松地在 Docker 容器中查看 Aspose.Cells 生成的输出。

### 配置 Dockerfile

下一步是创建和配置 Dockerfile。

1. 创建 Dockerfile 并将其放在应用程序的解决方案文件旁边。保留此文件名，不带扩展名（默认）。
1. 在 Dockerfile 中，指定：

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
COPY fonts/* /usr/share/fonts/
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

上面是一个简单的 Dockerfile，其中包含以下指令：

- 要使用的 SDK 镜像。这是 .Net Core SDK 3.1 图像。 Docker 将在构建运行时下载它。 SDK 的版本被指定为一个标签。
- 安装字体，因为 SDK 映像包含的字体非常少。该命令将字体文件从本地复制到 docker 镜像。确保您有一个本地“字体”目录，其中包含您需要安装的所有字体。在此示例中，本地“字体”目录与 Dockerfile 放在同一目录中。
- 工作目录，在下一行中指定。
- 将所有内容复制到容器、发布应用程序并指定入口点的命令。
- 安装 libgdiplus 的命令在容器中运行。这是 System.Drawing.Common 所要求的。

### 在 Docker 中构建和运行应用程序

现在可以在 Docker 中构建和运行应用程序。打开您最喜欢的命令提示符，将目录更改为包含应用程序的文件夹（放置解决方案文件和 Dockerfile 的文件夹）并运行以下命令：

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

第一次执行此命令可能需要更长的时间，因为 Docker 需要下载所需的图像。完成上一个命令后，运行以下命令：

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

注意 mount 参数，因为如前所述，宿主机上的一个文件夹被挂载到容器的文件夹中，以便轻松查看应用程序执行的结果。 Linux 中的路径区分大小写。

{{% /alert %}}

## 图片支持 Aspose.Cells

- Aspose.Cells for .NET 标准在 Linux 上不支持 EMF 和 TIFF。


## 更多例子

***1.在Windows Server 2019中运行应用***

- 文件

{{< highlight "plain" >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

- 构建 Docker 镜像

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- 运行 Docker 镜像

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. 在 Linux 中运行应用程序***

- 编写一个设置字体文件夹的简单程序，创建一个“Hello World！”工作簿并保存。

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
- 文件

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

- 构建 Docker 镜像

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- 运行 Docker 镜像

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## 也可以看看

- [在 Windows 上安装 Docker Desktop](https://docs.docker.com/docker-for-windows/install/)
- [在 Mac 上安装 Docker 桌面](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Core 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- [切换到 Linux 容器](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers)选项
- 有关的附加信息[.NET 核心SDK](https://hub.docker.com/_/microsoft-dotnet-sdk)
