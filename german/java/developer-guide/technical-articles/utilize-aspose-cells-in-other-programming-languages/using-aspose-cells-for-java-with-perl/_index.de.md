---
title: Verwenden von Aspose.Cells for Java mit Perl
type: docs
weight: 30
url: /de/java/using-aspose-cells-for-java-with-perl/
---
{{% alert color="primary" %}} 

Aspose.Cells for Java ist eine reine Java-Komponente, die mit Perl verwendet werden kann. Die Verwendung der Komponente entspricht dem Aufruf anderer gängiger Java-APIs in Perl. Um eine Java-Bibliothek in Perl aufzurufen, müssen Sie zuerst die Java-Perl-Erweiterung für Perl installieren. Dies ist für den Zugriff auf JVM erforderlich.

{{% /alert %}} 
## **Erforderliche Software und Bibliotheken**
 Die folgende Software und Bibliotheken sind erforderlich.

- Perl.
- Aspose.Cells for Java.
- Java – Perl-Erweiterung.
- Java-Laufzeit, die die Anforderungen von Aspose.Cells for Java und Java-Perl-Erweiterung erfüllt.
### **Handbuch**
 Um eine Java API in Perl anzurufen, müssen Sie zuerst die Java-Perl-Erweiterung für Perl installieren. (Für die Zwecke dieses Artikels gehen wir davon aus, dass Perl ordnungsgemäß installiert und eingestellt wurde.) Sie können die Erweiterung Java-Perl von herunterladen[Mezzo/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7)

 Am Ende dieses Dokuments finden Sie ein Beispiel für ein Perl-Skript, das Aspose.Cells for Java aufruft. Führen Sie die folgenden Schritte aus, um es auszuführen:

1. Laden Sie die Datei Java-4.7.tar.gz herunter und entpacken Sie sie auf Ihr lokales Laufwerk.
1. Installieren Sie dieses Paket für Perl.
1.  Starten Sie JavaServer. Der Befehl lautet:

{{< highlight "java" >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

 wobei ... der Klassenpfad ist, der alle von Ihrer Anwendung benötigten Bibliotheken enthalten muss.

 Um Aspose.Cells for Java zu verwenden, sollten mindestens zwei JAR-Dateien enthalten sein:

1. **Aspose.Cells.jar** von Aspose.Cells for Java
1. **JavaServer.jar** von Java-4.7.tar.gz
1. Führen Sie das Perl-Skript aus, das Aspose.Cells for Java API aufruft.

 Weitere Informationen zum Arbeiten mit Java in Perl finden Sie in der Dokumentation zu Java - Perl-Erweiterung unter<https://metacpan.org/release/METZZO/Java-4.7>

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
