---
title: 如何在Linux上安装TrueType字体
type: docs
weight: 20
url: /zh/java/how-to-install-truetype-fonts-on-linux/
---

{{% alert color="primary" %}}

最可能的情况是您正在使用Aspose.Cells将电子表格转换为PDF。如果您正在使用Linux等非Windows操作系统，请阅读本主题以确保Aspose.Cells尽可能准确地呈现您的电子表格。

为确保Aspose.Cells转换的电子表格尽可能接近原始电子表格，您可能需要在Linux系统上安装“Windows字体”或“TrueType字体”，因为最常用的TrueType字体通常不会在Linux发行版中默认预装。

在Linux系统上获得TrueType字体的两种主要方法：

1. 从Windows计算机复制字体文件（.TTF和.TTC）到您的Linux计算机。
1. 安装TrueType字体包，如msttcorefonts。

{{% /alert %}}

## **从Windows计算机复制字体**

一个简单快速的方法是从Windows计算机的C:\Windows\Fonts目录中复制.TTF和.TTC文件到Linux计算机的某个目录。您无需在Linux上安装或注册这些字体，只需在应用程序中使用FontConfigs.setFontFolder方法指定字体的位置。

{{% alert color="primary" %}}

据我们了解，微软许可任何人免费使用这些字体，但请自行检查字体许可。

{{% /alert %}}

## **安装TrueType字体包**

以下提供的信息将逐步指导您在Fedora和Red Hat Enterprise Linux（RHEL）等Linux发行版上安装微软最著名的TrueType字体。

{{% alert color="primary" %}}

可能需要'root'级别权限，因此以'root'登录或配置sudo。

{{% /alert %}}

以下是使用终端执行此操作的步骤。

1. 确保您已安装以下RPM软件包。
   - **rpm-build**：如果未安装，请使用以下命令安装rpm-build软件包

{{< highlight java >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**：如果未安装，请使用以下命令

{{< highlight java >}}

yum \-y install wget

{{< /highlight >}}

1. 使用以下命令从SourceForge下载最新的msttcorefonts规范文件

{{< highlight java >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. 使用之前下载的规范文件和以下命令构建RPM文件

{{< highlight java >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. RPM文件将存储在：/root/rpmbuild/RPMS/noarch/，按以下方式进行安装

{{< highlight java >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. 重新启动机器以使更改生效。

上述提供的说明将安装包括以下字体系列的Microsoft TTFs包：

1. Andale Mono
1. Arial Black/Arial (粗体, 斜体, 粗斜体)
1. Comic Sans MS (粗体)
1. Courier New (粗体, 斜体, 粗斜体)
1. Georgia (粗体, 斜体, 粗斜体)
1. Impact
1. Tahoma
1. Times New Roman (粗体, 斜体, 粗斜体)
1. Trebuchet (粗体, 斜体, 粗斜体)
1. Verdana (粗体, 斜体, 粗斜体)
1. Webdings

{{% alert color="primary" %}}

在Ubuntu上，打开Synaptic软件包管理器。找到并安装**ttf-mscorefonts-installer**软件包。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
