---
title: 使用 Aspose.Cells for Java 与 Perl
type: docs
weight: 30
url: /zh/java/using-aspose-cells-for-java-with-perl/
---

{{% alert color="primary" %}} 

Aspose.Cells for Java 是一个纯 Java 组件，可以与 Perl 一起使用。使用该组件与在 Perl 中调用其他常见的 Java API 相同。要在 Perl 中调用任何 Java 库，首先需要为 Perl 安装 Java-Perl 扩展。这是访问 JVM 所必需的。

{{% /alert %}} 
## **所需软件和库**
需要以下软件和库。 

- Perl。
- Aspose.Cells for Java。
- Java - Perl 扩展。
- 满足 Aspose.Cells for Java 和 Java-Perl 扩展要求的 Java 运行时。
### **指南**
要在 Perl 中调用 Java API，您需要先为 Perl 安装 Java-Perl 扩展。(在本文中，我们假设 Perl 已安装并设置正确。) 您可以从 [Metzzo/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7) 获取 Java-Perl 扩展。

本文档末尾附有一个调用 Aspose.Cells for Java 的示例 Perl 脚本。要运行它，请按以下步骤操作： 

1. 下载文件 Java-4.7.tar.gz 并解压到本地驱动器。
1. 为 Perl 安装该软件包。
1. 启动 JavaServer。命令为： 

{{< highlight java >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

其中...是类路径，必须包含应用程序所需的所有库。 

要使用 Aspose.Cells for Java，应至少包含两个 JAR 文件： 

1. 来自 Aspose.Cells for Java 的 **Aspose.Cells.jar**
1. 来自 Java-4.7.tar.gz 的 **JavaServer.jar**
1. 运行调用 Aspose.Cells for Java API 的 Perl 脚本。

For more information on how to work with Java in Perl, see documentation of Java - Perl extension at <https://metacpan.org/release/METZZO/Java-4.7>

**Java**

{{< highlight csharp >}}

 my $ok = 0;

BEGIN { $| = 1; print "1..33\n"; }

END {print "not ok $ok - is JavaServer on localhost running?\nJavaServer must be running for these tests to function.\n" unless $loaded;}

BEGIN {

print "WARNING: You cannot run these tests unless JavaServer is running!\n";

print "Do you want to continue? (Y/n) ";

my $in = <STDIN>;

exit 1 if ($in =~ /^n/i);

}

use lib '.';

use Java;

my $java = new Java();

$loaded = 1;

$ok++;

print "ok $ok\n";

my $workbook = $java->create_object("com.aspose.cells.Workbook");

$ok++;

print "workbook $ok\n";

#$workbook->open("t.xls");

$ok++;

print "open $ok\n";

my $worksheets = $workbook->getWorksheets();

$ok++;

print "worksheets $ok\n";

my $worksheet = $worksheets->get(0);

$ok++;

print "worksheet $ok\n";

my $cells = $worksheet->getCells();

$ok++;

print "cells $ok\n";

my $cell = $cells->getCell(0,1);

$ok++;

print "cell $ok\n";

$cell->setValue(123);

$cell = $cells->getCell(1,1);

$cell->setValue(456);

$cell = $cells->getCell(2,1);

$cell->setFormula("=SUM(B1:B2)");

$cell = $cells->getCell(3,1);

$cell->setValue("abc");

$workbook->save("t1.xls");

$ok++;

print "save $ok\n";



{{< /highlight >}}
