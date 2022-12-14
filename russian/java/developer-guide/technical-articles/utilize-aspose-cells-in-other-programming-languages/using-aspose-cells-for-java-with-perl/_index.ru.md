---
title: Использование Aspose.Cells for Java с Perl
type: docs
weight: 30
url: /ru/java/using-aspose-cells-for-java-with-perl/
---
{{% alert color="primary" %}} 

Aspose.Cells for Java — это чистый компонент Java, который можно использовать с Perl. Использование компонента аналогично вызову других распространенных API-интерфейсов Java в Perl. Чтобы вызвать любую библиотеку Java в Perl, вам нужно сначала установить расширение Java-Perl для Perl. Это необходимо для доступа к JVM.

{{% /alert %}} 
## **Необходимое программное обеспечение и библиотеки**
 Требуется следующее программное обеспечение и библиотеки.

- Перл.
- Aspose.Cells for Java.
- Java - Perl-расширение.
- Java, которая соответствует требованиям расширения Aspose.Cells for Java и Java-Perl.
### **Руководство**
 Чтобы вызвать Java API в Perl, вам нужно сначала установить расширение Java-Perl для Perl. (Для целей этой статьи мы предполагаем, что Perl установлен и настроен правильно.) Вы можете получить расширение Java-Perl от[Меццо/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7)

 В конце этого документа есть пример сценария Perl, который вызывает Aspose.Cells for Java. Чтобы запустить его, выполните следующие действия:

1. Загрузите файл Java-4.7.tar.gz и разархивируйте его на локальный диск.
1. Установите этот пакет для Perl.
1.  Запустите JavaServer. Команда будет:

{{< highlight "java" >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

 где ... — это путь к классам, который должен включать все библиотеки, необходимые вашему приложению.

 Чтобы использовать Aspose.Cells for Java, он должен содержать как минимум два JAR-файла:

1. **Aspose.Cells.jar** от Aspose.Cells for Java
1. **JavaServer.jar** с Java-4.7.tar.gz
1. Запустите сценарий Perl, который вызывает Aspose.Cells for Java API.

 Для получения дополнительной информации о том, как работать с Java в Perl, см. документацию Java — расширение Perl на<https://metacpan.org/release/METZZO/Java-4.7>

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
