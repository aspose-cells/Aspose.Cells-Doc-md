---
title: Perl ile Aspose.Cells for Java Kullanımı
type: docs
weight: 30
url: /tr/java/using-aspose-cells-for-java-with-perl/
---

{{% alert color="primary" %}} 

Aspose.Cells for Java, Perl ile kullanılabilen saf bir Java bileşenidir. Bileşeni kullanmak, Perl'de diğer yaygın Java API'leri çağırmakla aynıdır. Perl'de herhangi bir Java kütüphanesini çağırmak için öncelikle Perl için Java-Perl uzantısını yüklemeniz gerekmektedir. Bu, JVM'e erişmek için gereklidir.

{{% /alert %}} 
## **Gerekli Yazılım ve Kütüphaneler**
Aşağıdaki yazılım ve kütüphaneler gereklidir. 

- Perl.
- Aspose.Cells for Java.
- Java - Perl uzantısı.
- Aspose.Cells for Java'nin gereksinimlerini karşılayan Java çalıştırma zamanı ve Java-Perl uzantısı.
### **Rehber**
Bir Java API'sını Perl'de çağırmak için önce Perl için Java-Perl uzantısını kurmanız gerekir. (Bu makalede, Perl'in kurulduğunu ve doğru bir şekilde ayarlandığını varsayıyoruz.) Java-Perl uzantısını [Metzzo/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7) adresinden alabilirsiniz.

Bu belgenin sonunda, Aspose.Cells for Java'yi çağıran bir Perl betiği örneği bulunmaktadır. Çalıştırmak için aşağıdaki adımları izleyin: 

1. Java-4.7.tar.gz dosyasını indirin ve yerel sürücünüze açın.
1. Bu paketi Perl için yükleyin.
1. JavaServer'ı başlatın. Komut şu şekilde olacaktır: 

{{< highlight java >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

burada ... uygulamanız tarafından gereken tüm kütüphaneleri içermesi gereken classpath'tir. 

Aspose.Cells for Java'yi kullanmak için en az iki JAR dosyası içermelidir: 

1. Aspose.Cells for Java'den **Aspose.Cells.jar**
1. Java-4.7.tar.gz dosyasından **JavaServer.jar**
1. Aspose.Cells for Java API'sini çağıran Perl betiğini çalıştırın.

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
