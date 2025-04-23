---
title: 使用 Java 组件 Aspose.Cells for Java 和 Perl
type: docs
weight: 30
url: /zh/java/using-aspose-cells-for-java-with-perl/
---

{{% alert color="primary" %}} 

Aspose.Cells for Java 是一个纯Java组件，可以与Perl一起使用。 使用该组件与在Perl中调用其他常见的Java API相同。 要在Perl中调用任何Java库，首先需要为Perl安装Java-Perl扩展。 这是访问JVM所需的。

{{% /alert %}} 
## **需要的软件和库**
需要以下软件和库。 

- Perl.
- Aspose.Cells for Java.
- Java - Perl 扩展。
- 符合 Aspose.Cells for Java 和 Java-Perl 扩展的Java运行时。
### **指南**
要在 Perl 中调用 Java API，首先需要为 Perl 安装 Java-Perl 扩展。（对于本文，假设 Perl 已被正确安装和设置。）您可以从[Metzzo/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7)获取 Java-Perl 扩展。

在本文档末尾，有一个调用Aspose.Cells for Java的Perl脚本示例。 要运行它，请按照以下步骤进行： 

1. 下载文件 Java-4.7.tar.gz 并将其解压缩到本地驱动器。
1. 为 Perl 安装此软件包。
1. 启动 JavaServer。命令将是： 

{{< highlight java >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

其中...是必须包括应用程序所需的所有库的类路径。 

要使用 Aspose.Cells for Java，至少应包含两个JAR文件： 

1. **Aspose.Cells.jar** 来自 Aspose.Cells for Java
1. 来自 Java-4.7.tar.gz 的 **JavaServer.jar**
1. 运行调用 Aspose.Cells for Java API 的Perl脚本。

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
{{< app/cells/assistant language="java" >}}
