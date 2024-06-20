---
title: استخدام Aspose.Cells for Java مع Perl
type: docs
weight: 30
url: /ar/java/using-aspose-cells-for-java-with-perl/
---

{{% alert color="primary" %}} 

Aspose.Cells for Java هو عبارة عن مكون جافا نقي يمكن استخدامه مع Perl. يتم استخدام المكون بنفس الطريقة المستخدمة لاستدعاء واجهات برمجة تطبيقات جافا الشائعة الأخرى في Perl. لاستدعاء أي مكتبة جافا في Perl، تحتاج أولاً إلى تثبيت ملحق Java-Perl لـ Perl. هذا مطلوب للوصول إلى JVM.

{{% /alert %}} 
## **البرمجيات والمكتبات المطلوبة**
البرمجيات والمكتبات التالية مطلوبة. 

- Perl.
- Aspose.Cells for Java.
- جافا - تمديد بيرل.
- جافا تشغيل يلبي متطلبات Aspose.Cells for Java وتمديد جافا-بيرل.
### **دليل**
لاستدعاء واجهة برمجية جافا في بيرل، تحتاج إلى تثبيت تمديد جافا-بيرل أولاً. (لأغراض هذه المقالة، نفترض أن بيرل قد تم تثبيته وضبطه بشكل صحيح.) يمكنك الحصول على تمديد جافا-بيرل من [Metzzo/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7)

في نهاية هذه الوثيقة، هناك مثال على نص بيرل يستدعي Aspose.Cells for Java. لتشغيله، اتبع الخطوات التالية: 

1. قم بتنزيل ملف Java-4.7.tar.gz وفك الضغط عليه على القرص المحلي الخاص بك.
1. قم بتثبيت هذه الحزمة لبيرل.
1. قم بتشغيل خادم جافا. سيكون الأمر: 

{{< highlight java >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

حيث ... هو مسار الصف الذي يجب أن يتضمن جميع المكتبات المطلوبة من قبل تطبيقك. 

لاستخدام Aspose.Cells for Java، يجب أن تحتوي على ملفي JAR على الأقل: 

1. **Aspose.Cells.jar** من Aspose.Cells for Java
1. **JavaServer.jar** من Java-4.7.tar.gz
1. قم بتشغيل نص بيرل الذي يستدعي Aspose.Cells for Java API.

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
