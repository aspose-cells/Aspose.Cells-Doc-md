---
title: Aspose.Cells for Java'i Perl ile kullanma
type: docs
weight: 30
url: /tr/java/using-aspose-cells-for-java-with-perl/
---
{{% alert color="primary" %}} 

Aspose.Cells for Java, Perl ile kullanılabilen saf bir Java bileşenidir. Bileşeni kullanmak, Perl'deki diğer yaygın Java API'lerini çağırmakla aynıdır. Perl'de herhangi bir Java kitaplığını çağırmak için önce Perl için Java-Perl uzantısını yüklemeniz gerekir. JVM'ye erişmek için bu gereklidir.

{{% /alert %}} 
## **Gerekli Yazılım ve Kitaplıklar**
 Aşağıdaki yazılım ve kitaplıklar gereklidir.

- Perl.
- Aspose.Cells for Java.
- Java - Perl uzantısı.
- Java Aspose.Cells for Java ve Java-Perl uzantısının gereksinimlerini karşılayan çalışma zamanı.
### **Kılavuz**
 Perl'de bir Java API'i aramak için, önce Perl için Java-Perl uzantısını kurmanız gerekir. (Bu makalenin amaçları doğrultusunda, Perl'in düzgün bir şekilde kurulduğunu ve ayarlandığını varsayıyoruz.) Java-Perl uzantısını adresinden edinebilirsiniz.[Metzzo/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7)

 Bu belgenin sonunda, Aspose.Cells for Java'i çağıran bir Perl betiği örneği bulunmaktadır. Çalıştırmak için aşağıdaki adımları izleyin:

1. Java-4.7.tar.gz dosyasını indirin ve yerel sürücünüze açın.
1. Perl için bu paketi yükleyin.
1.  JavaServer'ı başlatın. Komut şöyle olacaktır:

{{< highlight "java" >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

 burada ..., uygulamanızın gerektirdiği tüm kitaplıkları içermesi gereken sınıf yoludur.

 Aspose.Cells for Java'i kullanmak için en az iki JAR dosyası içermelidir:

1. **Aspose.Cells.jar** Aspose.Cells for Java den
1. **Java Sunucusu.jar** Java-4.7.tar.gz adresinden
1. Aspose.Cells for Java API'i çağıran Perl betiğini çalıştırın.

 Perl'de Java ile nasıl çalışılacağı hakkında daha fazla bilgi için adresindeki Java - Perl uzantısı belgelerine bakın.<https://metacpan.org/release/METZZO/Java-4.7>

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
