---
title: Användning av Aspose.Cells for Java med Perl
type: docs
weight: 30
url: /sv/java/using-aspose-cells-for-java-with-perl/
---

{{% alert color="primary" %}} 

Aspose.Cells for Java är en ren Java-komponent som kan användas med Perl. Att använda komponenten är samma som att åberopa andra vanliga Java API: er i Perl. För att anropa något Java-bibliotek i Perl måste du först installera Java-Perl-tillägget för Perl. Detta behövs för att komma åt JVM.

{{% /alert %}} 
## **Nödvändig mjukvara och bibliotek**
Följande mjukvara och bibliotek krävs. 

- Perl.
- Aspose.Cells for Java.
- Java - Perl-tillägg.
- Java-runtime som uppfyller kravet på Aspose.Cells for Java och Java-Perl-tillägg.
### **Handbok**
För att anropa ett Java API i Perl måste du först installera Java-Perl-tillägget för Perl. (För denna artikels syften antar vi att Perl har installerats och ställts in korrekt.) Du kan få Java-Perl-tillägget från [Metzzo/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7)

I slutet av detta dokument finns ett exempel på Perl-skript som anropar Aspose.Cells for Java. För att köra det följer du följande steg: 

1. Ladda ner filen Java-4.7.tar.gz och packa upp den till din lokala enhet.
1. Installera detta paket för Perl.
1. Starta JavaServer. Kommandot kommer att vara: 

{{< highlight java >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

där ... är classpath som måste inkludera alla bibliotek som krävs av din applikation. 

För att använda Aspose.Cells for Java bör innehålla minst två JAR-fil: 

1. **Aspose.Cells.jar** från Aspose.Cells for Java
1. **JavaServer.jar** från Java-4.7.tar.gz
1. Kör Perl-skriptet som åberopar Aspose.Cells for Java API.

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
