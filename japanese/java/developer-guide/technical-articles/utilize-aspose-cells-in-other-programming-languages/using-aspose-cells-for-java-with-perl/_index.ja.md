---
title: Perl で Aspose.Cells for Java を使用する
type: docs
weight: 30
url: /ja/java/using-aspose-cells-for-java-with-perl/
---
{{% alert color="primary" %}} 

Aspose.Cells for Java は、Perl で使用できる純粋な Java コンポーネントです。コンポーネントを使用することは、Perl で他の一般的な Java API を呼び出すことと同じです。 Perl で任意の Java ライブラリを呼び出すには、最初に Perl 用の Java-Perl 拡張機能をインストールする必要があります。これは、JVM にアクセスするために必要です。

{{% /alert %}} 
## **必要なソフトウェアとライブラリ**
以下のソフトウェアとライブラリが必要です。

- パール。
- Aspose.Cells for Java.
- Java - Perl 拡張。
- Aspose.Cells for Java および Java-Perl 拡張の要件を満たす Java ランタイム。
### **ガイド**
Perl で Java API を呼び出すには、最初に Perl 用の Java-Perl 拡張機能をインストールする必要があります。 (この記事では、Perl がインストールされ、適切に設定されていることを前提としています。) Java-Perl 拡張機能は、[メッツォ/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7)

このドキュメントの最後に、Aspose.Cells for Java を呼び出す Perl スクリプトの例があります。実行するには、次の手順に従います。

1. ファイル Java-4.7.tar.gz をダウンロードし、ローカル ドライブに解凍します。
1. Perl 用のこのパッケージをインストールします。
1.  Java サーバーを起動します。コマンドは次のようになります。

{{< highlight "java" >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

ここで ... は、アプリケーションに必要なすべてのライブラリを含める必要があるクラスパスです。

 Aspose.Cells for Java を使用するには、少なくとも 2 つの JAR ファイルが含まれている必要があります。

1. **Aspose.Cells.jar** Aspose.Cells から for Java
1. **JavaServer.jar** Java-4.7.tar.gz から
1. Aspose.Cells for Java API を呼び出す Perl スクリプトを実行します。

 Perl で Java を使用する方法の詳細については、Java - Perl 拡張機能のドキュメントを参照してください。<https://metacpan.org/release/METZZO/Java-4.7>

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
