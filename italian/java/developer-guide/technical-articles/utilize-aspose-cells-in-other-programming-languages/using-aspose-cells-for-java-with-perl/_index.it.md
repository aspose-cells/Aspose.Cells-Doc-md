---
title: Usando Aspose.Cells for Java con Perl
type: docs
weight: 30
url: /it/java/using-aspose-cells-for-java-with-perl/
---
{{% alert color="primary" %}} 

Aspose.Cells for Java è un componente Java puro che può essere utilizzato con Perl. L'utilizzo del componente equivale a richiamare altre comuni API Java in Perl. Per chiamare qualsiasi libreria Java in Perl, devi prima installare l'estensione Java-Perl per Perl. Questo è necessario per accedere a JVM.

{{% /alert %}} 
## **Software e librerie richiesti**
 Sono richiesti il software e le librerie seguenti.

- Perle.
- Aspose.Cells for Java.
- Java - Estensione Perl.
- Runtime Java che soddisfa il requisito di Aspose.Cells for Java e l'estensione Java-Perl.
### **Guida**
 Per chiamare un'API Java in Perl, devi prima installare l'estensione Java-Perl per Perl. (Ai fini di questo articolo, supponiamo che Perl sia stato installato e impostato correttamente.) È possibile ottenere l'estensione Java-Perl da[Metzzo/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7)

 Alla fine di questo documento, c'è un esempio di script Perl che chiama Aspose.Cells for Java. Per eseguirlo, attenersi alla seguente procedura:

1. Scarica il file Java-4.7.tar.gz e decomprimilo sull'unità locale.
1. Installa questo pacchetto per Perl.
1.  Avvia JavaServer. Il comando sarà:

{{< highlight "java" >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

 dove ... è il classpath che deve includere tutte le librerie richieste dalla tua applicazione.

 Per utilizzare Aspose.Cells for Java, deve contenere almeno due file JAR:

1. **Aspose.Cells.jar** dal Aspose.Cells for Java
1. **javaserver.jar**da Java-4.7.tar.gz
1. Eseguire lo script Perl che richiama l'API Aspose.Cells for Java.

 Per ulteriori informazioni su come lavorare con Java in Perl, vedere la documentazione dell'estensione Java - Perl su<https://metacpan.org/release/METZZO/Java-4.7>

**Giava**

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
