---
title: 如何在 Linux 上安装 TrueType 字体
type: docs
weight: 20
url: /zh/java/how-to-install-truetype-fonts-on-linux/
---
{{% alert color="primary" %}}

最可能的情况是您使用 Aspose.Cells 将电子表格转换为 PDF。如果您在基于非 Windows 的操作系统（例如 Linux）上执行此操作，则本主题说明如何确保 Aspose.Cells 以最佳保真度呈现您的电子表格。

为确保由 Aspose.Cells 转换的电子表格尽可能接近原始电子表格，您可能需要在 Linux 系统上安装“Windows 字体”或“TrueType 字体”，因为最常用的 TrueType 字体未预装默认情况下是 Linux 发行版。

在 Linux 系统上获取 TrueType 字体主要有两种方式：

1. 将字体文件（.TTF 和 .TTC）从 Windows 机器复制到您的 Linux 机器。
1. 安装 TrueType 字体包，例如 msttcorefonts。

{{% /alert %}}

## **从 Windows 机器复制字体**

一种简单快捷的方法是将 .TTF 和 .TTC 文件从 Windows 机器上的 C:\Windows\Fonts 目录复制到 Linux 机器上的某个目录。您不需要以任何方式在 Linux 上安装或注册这些字体，您只需要在应用程序中使用 FontConfigs.setFontFolder 方法指定字体的位置。

{{% alert color="primary" %}}

据我们所知，Microsoft 许可任何人自由使用这些字体，但请自行检查字体许可。

{{% /alert %}}

## **安装 TrueType 字体包**

下面提供的信息将指导您逐步在 Fedora 和 Red Hat Enterprise Linux (RHEL) 等 Linux 发行版上安装 Microsoft 最著名的 TrueType 字体。

{{% alert color="primary" %}}

您可能需要“root”级别的权限，因此以“root”身份登录或配置 sudo。

{{% /alert %}}

这是使用终端的方法。

1. 确保安装了以下 RPM 包。
   1. **rpm构建**如果没有安装，使用以下命令安装rpm-build包

{{< highlight "java" >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: 如果没有安装，使用以下命令

{{< highlight "java" >}}

yum \-y install wget

{{< /highlight >}}

1. 使用以下命令从 SourceForge 下载最新的 msttcorefonts 规范文件，

{{< highlight "java" >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. 使用之前下载的规范文件和以下命令构建一个 RPM 文件，

{{< highlight "java" >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. RPM 文件将存储在：/root/rpmbuild/RPMS/noarch/，安装如下，

{{< highlight "java" >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. 重新启动机器以使更改生效。

上面提供的说明将安装 Microsoft TTF 包，其中包括以下字体系列：

1. 安达尔 Mono
1. Arial Black/Arial（粗体、斜体、粗体斜体）
1. Comic Sans MS（粗体）
1. Courier New（粗体、斜体、粗体斜体）
1. 格鲁吉亚（粗体、斜体、粗体斜体）
1. 影响
1. 塔霍马
1. Times New Roman（粗体、斜体、粗体斜体）
1. Trebuchet（粗体、斜体、粗体斜体）
1. Verdana（粗体、斜体、粗体斜体）
1. 织带

{{% alert color="primary" %}}

在 Ubuntu 上，转到新立得包管理器。找到并安装**ttf-mscorefonts-installer**包裹。

{{% /alert %}}
