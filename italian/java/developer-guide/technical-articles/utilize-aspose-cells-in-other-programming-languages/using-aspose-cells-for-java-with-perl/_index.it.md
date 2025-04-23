---
title: Usare Aspose.Cells for Java con Perl
type: docs
weight: 30
url: /it/java/using-aspose-cells-for-java-with-perl/
---

{{% alert color="primary" %}} 

Aspose.Cells for Java è un componente Java puro che può essere utilizzato con Perl. Utilizzare il componente è l'equivalente di invocare altre API Java comuni in Perl. Per chiamare qualsiasi libreria Java in Perl, è necessario installare prima l'estensione Java-Perl per Perl. Questo è necessario per accedere alla JVM.

{{% /alert %}} 
## **Software e Librerie Richieste**
I seguenti software e librerie sono richiesti. 

- Perl.
- Aspose.Cells for Java.
- Java - Estensione Perl.
- Runtime di Java che soddisfi il requisito di Aspose.Cells for Java e l'estensione Java-Perl.
### **Guida**
Per chiamare un'API Java in Perl, è necessario installare prima l'estensione Java-Perl per Perl. (Ai fini di questo articolo, supponiamo che Perl sia stato installato e configurato correttamente.) Puoi ottenere l'estensione Java-Perl da [Metzzo/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7)

Alla fine di questo documento, c'è un esempio di script Perl che chiama Aspose.Cells for Java. Per eseguirlo, seguire i seguenti passaggi: 

1. Scarica il file Java-4.7.tar.gz e decomprimilo sul tuo disco locale.
1. Installa questo pacchetto per Perl.
1. Avvia JavaServer. Il comando sarà: 

{{< highlight java >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

dove ... è il classpath che deve includere tutte le librerie richieste dalla tua applicazione. 

Per utilizzare Aspose.Cells for Java, devi avere almeno due file JAR: 

1. **Aspose.Cells.jar** da Aspose.Cells for Java
1. **JavaServer.jar** da Java-4.7.tar.gz
1. Esegui lo script Perl che invoca l'API Aspose.Cells for Java.

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
