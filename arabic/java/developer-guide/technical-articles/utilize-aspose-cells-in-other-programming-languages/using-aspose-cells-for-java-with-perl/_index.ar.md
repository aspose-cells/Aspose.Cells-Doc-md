---
title: استخدام Aspose.Cells for Java مع Perl
type: docs
weight: 30
url: /ar/java/using-aspose-cells-for-java-with-perl/
---
{{% alert color="primary" %}} 

Aspose.Cells for Java هو مكون Java خالص يمكن استخدامه مع Perl. استخدام المكون مماثل لاستدعاء واجهات برمجة تطبيقات أخرى مشتركة Java في Perl. للاتصال بأي مكتبة Java في Perl ، تحتاج إلى تثبيت ملحق Perl Java لـ Perl أولاً. هذا مطلوب للوصول إلى JVM.

{{% /alert %}} 
## **البرامج والمكتبات المطلوبة**
 البرامج والمكتبات التالية مطلوبة.

- بيرل.
- Aspose.Cells for Java.
- Java - ملحق بيرل.
- وقت تشغيل Java الذي يفي بمتطلبات امتداد Aspose.Cells for Java و Java-Perl.
### **مرشد**
 للاتصال بالرقم Java API في Perl ، تحتاج إلى تثبيت ملحق Perl Java لـ Perl أولاً. (لأغراض هذه المقالة ، نفترض أنه تم تثبيت Perl وضبطه بشكل صحيح.) يمكنك الحصول على امتداد Java-Perl من[ميتزو / Java-4.7 /](https://metacpan.org/release/METZZO/Java-4.7)

 في نهاية هذا المستند ، يوجد مثال على نص برل يستدعي Aspose.Cells for Java. لتشغيله ، اتبع الخطوات التالية:

1. قم بتنزيل الملف Java-4.7.tar.gz وفك ضغطه على محرك الأقراص المحلي.
1. قم بتثبيت هذه الحزمة لـ Perl.
1.  ابدأ تشغيل JavaServer. سيكون الأمر:

{{< highlight "java" >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

 حيث ... هو مسار الفصل الذي يجب أن يتضمن جميع المكتبات التي يتطلبها تطبيقك.

 لاستخدام Aspose.Cells for Java ، يجب أن يحتوي على ملفي JAR على الأقل:

1. **Aspose.Cells.jar** من Aspose.Cells for Java
1. **JavaServer.jar** من Java-4.7.tar.gz
1. قم بتشغيل سكربت Perl الذي يستدعي Aspose.Cells for Java API.

 لمزيد من المعلومات حول كيفية العمل مع Java في Perl ، راجع توثيق Java - ملحق Perl على<https://metacpan.org/release/METZZO/Java-4.7>

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
