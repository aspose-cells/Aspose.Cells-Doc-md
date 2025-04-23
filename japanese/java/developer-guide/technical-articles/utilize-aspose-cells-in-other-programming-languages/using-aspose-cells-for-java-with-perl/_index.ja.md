---
title: PerlでAspose.Cells for Javaを使用する
type: docs
weight: 30
url: /ja/java/using-aspose-cells-for-java-with-perl/
---

{{% alert color="primary" %}} 

Aspose.Cells for Java はPerlで使用できる純粋なJavaコンポーネントです。このコンポーネントを使用する際は、Perlで一般的な他のJava APIを呼び出すのと同じです。PerlでJavaライブラリを呼び出すには、まずPerl用のJava-Perl拡張機能をインストールする必要があります。これはJVMへのアクセスに必要です。

{{% /alert %}} 
## **必要なソフトウェアとライブラリ**
次のソフトウェアとライブラリが必要です。 

- Perl.
- Aspose.Cells for Java.
- Java - Perl拡張機能。
- Aspose.Cells for JavaおよびJava-Perl拡張機能の要件を満たすJavaランタイム。
### **ガイド**
PerlでJava APIを呼び出すには、まずPerl向けのJava-Perl拡張機能をインストールする必要があります。（本記事では、Perlがインストールされ適切に設定されているものとします。）Java-Perl拡張機能は[Metzzo/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7)から入手できます。

このドキュメントの最後には、Aspose.Cells for Javaを呼び出すPerlスクリプトの例があります。実行するには、次の手順に従います。 

1. ファイルJava-4.7.tar.gzをダウンロードし、ローカルドライブに解凍します。
1. このパッケージをPerlにインストールします。
1. JavaServerを起動します。コマンドは次のとおりです。 

{{< highlight java >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

ここで...は、アプリケーションに必要なすべてのライブラリが含まれている必要があるクラスパスです。 

Aspose.Cells for Javaを使用するには、少なくとも2つのJARファイルを含める必要があります。 

1. Aspose.Cells for Javaから**Aspose.Cells.jar**
1. Java-4.7.tar.gzから**JavaServer.jar**
1. Aspose.Cells for Java APIを呼び出すPerlスクリプトを実行します。

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
