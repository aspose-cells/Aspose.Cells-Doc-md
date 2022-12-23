---
title: 演示设置
type: docs
weight: 40
url: /zh/jasperreports/demos-setup/
---
{{% alert color="primary" %}}

Aspose.Cells for JasperReports 包括许多演示项目，可帮助您开始将报告从您的应用程序导出为 Microsoft Excel 文档格式。

Aspose.Cells for JasperReports 提供的演示是标准的 JasperReports 演示，经过修改以演示新导出器的使用。

{{% /alert %}}

要运行 Aspose.Cells for JasperReports 演示，请执行以下步骤：

1. 下载 JasperReports（例如<https://sourceforge.net/projects/jasperreports/files/archive/>).确保下载包含源代码和演示的整个存档项目，而不仅仅是一个 JAR。
1. 将归档项目解压到硬盘上的某个位置，例如 C:\。
1. 从 \demo 文件夹中复制所有演示文件夹**Aspose.Cells.JasperReports.zip**到**\<安装目录>\demo\samples**， 在哪里 ”\<InstallDir>" 是您将 JasperReports 解压到的位置。此步骤是必需的，因为演示构建脚本依赖于 JasperReports 的文件夹结构，否则您将需要修改构建脚本。
1. 复制**aspose.cells.jasperreports.jar**从 Aspose.Cells.JasperReports.zip 的 \lib 文件夹到**\<安装目录>\lib**.
1. 准备Ant Build Tool和Ivy Dependency Manager，参见**\<安装目录>\readme.txt**.
1. 修改**构建.xml**在**\<安装目录>\demo\samples**，将 aspose.cells.jasperreports.jar 添加到类路径中：
   **\<path id="project-classpath"> ... \<pathelement location="../../lib/aspose.cells.jasperreports.jar"/> </path>**.
1. 将当前目录更改为**\<安装目录>\demo\hsqldb**并运行以下命令行：
   **蚂蚁运行服务器**
1. 将当前目录更改为 Aspose.Cells for JasperReports 演示之一，例如**\<安装目录>\demo\samples\ac.charts**并在命令行中运行以下命令：
   **蚂蚁测试** 使用 Aspose XLS 导出器生成报告文件。
1. 打开生成的文档之一进行查看，例如**\<InstallDir>\demo\samples\ac.charts\build\reports\AreaChartReport.xls**在 Microsoft Excel 或其他应用程序中。
