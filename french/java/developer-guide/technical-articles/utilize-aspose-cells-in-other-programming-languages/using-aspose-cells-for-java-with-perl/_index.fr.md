---
title: Utiliser Aspose.Cells for Java avec Perl
type: docs
weight: 30
url: /fr/java/using-aspose-cells-for-java-with-perl/
---

{{% alert color="primary" %}} 

Aspose.Cells for Java est un composant Java pur qui peut être utilisé avec Perl. Utiliser ce composant est similaire à invoquer d'autres API Java courantes en Perl. Pour appeler une bibliothèque Java en Perl, vous devez d'abord installer l'extension Java-Perl pour Perl. Cela est nécessaire pour accéder à la JVM.

{{% /alert %}} 
## **Logiciels et bibliothèques requis**
Les logiciels et bibliothèques suivants sont requis. 

- Perl.
- Aspose.Cells for Java.
- Java - extension Perl.
- environnement d'exécution Java qui satisfait les requis de Aspose.Cells for Java et de l'extension Java-Perl.
### **Guide**
Pour appeler une API Java en Perl, vous devez d'abord installer l'extension Java-Perl pour Perl. (Aux fins de cet article, nous supposons que Perl a été installé et configuré correctement.) Vous pouvez obtenir l'extension Java-Perl depuis [Metzzo/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7)

À la fin de ce document, un exemple de script Perl appelant Aspose.Cells for Java est présenté. Pour l'exécuter, suivez les étapes suivantes : 

1. Téléchargez le fichier Java-4.7.tar.gz et décompressez-le sur votre lecteur local.
1. Installez ce package pour Perl.
1. Démarrez JavaServer. La commande sera : 

{{< highlight java >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

où ... est le classpath qui doit inclure toutes les bibliothèques requises par votre application. 

Pour utiliser Aspose.Cells for Java, vous devez contenir au moins deux fichiers JAR : 

1. **Aspose.Cells.jar** de Aspose.Cells for Java
1. **JavaServer.jar** de Java-4.7.tar.gz
1. Exécutez le script Perl qui invoque l'API Aspose.Cells for Java.

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
