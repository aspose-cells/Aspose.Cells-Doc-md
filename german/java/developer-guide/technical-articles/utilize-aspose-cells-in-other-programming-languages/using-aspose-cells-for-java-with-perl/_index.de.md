---
title: Verwendung von Aspose.Cells for Java mit Perl
type: docs
weight: 30
url: /de/java/using-aspose-cells-for-java-with-perl/
---

{{% alert color="primary" %}} 

Aspose.Cells for Java ist eine reine Java-Komponente, die mit Perl verwendet werden kann. Die Verwendung der Komponente ist identisch mit dem Aufruf anderer allgemeiner Java-APIs in Perl. Um eine beliebige Java-Bibliothek in Perl aufzurufen, muss zunächst die Java-Perl-Erweiterung für Perl installiert werden. Dies ist erforderlich, um auf die JVM zuzugreifen.

{{% /alert %}} 
## **Erforderliche Software und Bibliotheken**
Die folgende Software und die folgenden Bibliotheken werden benötigt. 

- Perl.
- Aspose.Cells for Java.
- Java - Perl-Erweiterung.
- Java-Laufzeitumgebung, die die Anforderungen von Aspose.Cells for Java und der Java-Perl-Erweiterung erfüllt.
### **Leitfaden**
Um eine Java-API in Perl aufzurufen, müssen Sie zunächst die Java-Perl-Erweiterung für Perl installieren. (Für die Zwecke dieses Artikels nehmen wir an, dass Perl ordnungsgemäß installiert und eingerichtet wurde.) Sie können die Java-Perl-Erweiterung von [Metzzo/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7) erhalten.

Am Ende dieses Dokuments finden Sie ein Beispiel für ein Perl-Skript, das Aspose.Cells for Java aufruft. Um es auszuführen, befolgen Sie die folgenden Schritte: 

1. Laden Sie die Datei Java-4.7.tar.gz herunter und entpacken Sie sie auf Ihrem lokalen Laufwerk.
1. Installieren Sie dieses Paket für Perl.
1. Starten Sie JavaServer. Der Befehl lautet: 

{{< highlight java >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

wo ... der Klassenpfad ist, der alle für Ihre Anwendung erforderlichen Bibliotheken enthalten muss. 

Um Aspose.Cells for Java zu verwenden, müssen mindestens zwei JAR-Dateien enthalten sein: 

1. **Aspose.Cells.jar** aus Aspose.Cells for Java
1. **JavaServer.jar** aus Java-4.7.tar.gz
1. Führen Sie das Perl-Skript aus, das die Aspose.Cells for Java API aufruft.

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
