---
title: 如何在Linux上安装TrueType字体
type: docs
weight: 20
url: /zh/java/how-to-install-truetype-fonts-on-linux/
---

{{% alert color="primary" %}}

最有可能的情况是，您正在使用Aspose.Cells将电子表格转换为PDF。如果您在诸如Linux之类的非Windows操作系统上执行此操作，那么本主题将解释如何确保Aspose.Cells以最佳的准确性呈现您的电子表格。

为了确保由Aspose.Cells转换的电子表格尽可能接近原始文件，您可能需要在Linux系统上安装"Windows字体"或"TrueType字体"，因为最常用的TrueType字体在Linux发行版中默认情况下不会预装。

在Linux系统上获取TrueType字体有两种主要方法：

1. 从Windows机器复制字体文件（.TTF和.TTC）到您的Linux机器。
1. 安装TrueType字体包，例如msttcorefonts。

{{% /alert %}}

## **从Windows机器复制字体**

一个简单快速的方法是将.C:\Windows\Fonts目录中的.TTF和.TTC文件从Windows机器复制到Linux机器上的某个目录。您不需要以任何方式在Linux上安装或注册这些字体，只需要在应用中使用FontConfigs.setFontFolder方法指定字体的位置。

{{% alert color="primary" %}}

据我们所知，Microsoft授权所有人免费使用这些字体，但请自行检查字体许可证。

{{% /alert %}}

## **安装TrueType字体包**

下面提供的信息将逐步指导您在像Fedora和Red Hat Enterprise Linux（RHEL）这样的Linux发行版上安装微软最著名的TrueType字体。

{{% alert color="primary" %}}

您可能需要'root'级别的权限，因此请以'root'身份登录或设置sudo。

{{% /alert %}}

以下是使用终端执行此操作的方法。

1. 确保您已安装以下RPM软件包。
   1. **rpm-build**：如果未安装，请使用以下命令安装rpm-build软件包

{{< highlight java >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**：如果未安装，请使用以下命令

{{< highlight java >}}

yum \-y install wget

{{< /highlight >}}

1. 使用以下命令从SourceForge下载最新的msttcorefonts spec文件，

{{< highlight java >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. 使用先前下载的spec文件和以下命令构建一个RPM文件，

{{< highlight java >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. RPM文件将存储在：/root/rpmbuild/RPMS/noarch/中, 安装如下,

{{< highlight java >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. 重新启动计算机以使更改生效。

上述提供的说明将安装包括以下字体系列的Microsoft TTFs软件包：

1. Andale Mono
1. Arial Black/Arial（粗体，斜体，粗斜体）
1. Comic Sans MS（粗体）
1. Courier New（粗体，斜体，粗斜体）
1. Georgia（粗体，斜体，粗斜体）
1. Impact
1. Tahoma
1. Times New Roman（粗体，斜体，粗斜体）
1. Trebuchet（粗体，斜体，粗斜体）
1. Verdana（粗体，斜体，粗斜体）
1. Webdings

{{% alert color="primary" %}}

在Ubuntu上，打开Synaptic软件包管理器。查找并安装**ttf-mscorefonts-installer**软件包。

{{% /alert %}}
