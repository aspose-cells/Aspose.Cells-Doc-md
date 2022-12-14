---
title: 在 Perl 中使用 Aspose.Cells for Java
type: docs
weight: 30
url: /zh/java/using-aspose-cells-for-java-with-perl/
---
{{% alert color="primary" %}} 

Aspose.Cells for Java 是可以与 Perl 一起使用的纯 Java 组件。使用该组件与在 Perl 中调用其他常用 Java API 相同。要在 Perl 中调用任何 Java 库，您需要先为 Perl 安装 Java-Perl 扩展。这是访问 JVM 所必需的。

{{% /alert %}} 
## **所需的软件和库**
需要以下软件和库。

- 佩尔。
- Aspose.Cells for Java.
- Java - Perl 扩展。
- Java 运行时满足 Aspose.Cells for Java 和 Java-Perl 扩展的要求。
### **指导**
要在 Perl 中调用 Java API，您需要先为 Perl 安装 Java-Perl 扩展。 （出于本文的目的，我们假设已正确安装和设置 Perl。）您可以从以下位置获得 Java-Perl 扩展名[梅佐/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7)

在本文档的最后，有一个调用 Aspose.Cells for Java 的 Perl 脚本示例。要运行它，请按照以下步骤操作：

1. 下载文件 Java-4.7.tar.gz 并将其解压缩到本地驱动器。
1. 为 Perl 安装这个包。
1. 启动Java服务器。该命令将是：

{{< highlight "java" >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

其中 ... 是必须包含应用程序所需的所有库的类路径。

要使用Aspose.Cells for Java，至少要包含两个JAR文件：

1. **Aspose.Cells.jar**从 Aspose.Cells for Java
1. **JavaServer.jar**来自 Java-4.7.tar.gz
1. 运行调用 Aspose.Cells for Java API 的 Perl 脚本。

有关如何在 Perl 中使用 Java 的更多信息，请参阅 Java 的文档 - Perl 扩展，网址为<https://metacpan.org/release/METZZO/Java-4.7>

**Java**

{{< highlight "csharp" >}}

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

# $workbook->open("t.xls");

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
