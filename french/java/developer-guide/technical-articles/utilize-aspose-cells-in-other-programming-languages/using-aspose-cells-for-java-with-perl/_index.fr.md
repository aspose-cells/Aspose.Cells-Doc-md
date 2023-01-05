---
title: Utilisation de Aspose.Cells for Java avec Perl
type: docs
weight: 30
url: /fr/java/using-aspose-cells-for-java-with-perl/
---
{{% alert color="primary" %}} 

Aspose.Cells for Java est un composant Java pur qui peut être utilisé avec Perl. L'utilisation du composant revient à invoquer d'autres API Java courantes en Perl. Pour appeler une bibliothèque Java en Perl, vous devez d'abord installer l'extension Java-Perl pour Perl. Ceci est nécessaire pour accéder à la JVM.

{{% /alert %}} 
## **Logiciels et bibliothèques requis**
 Les logiciels et bibliothèques suivants sont requis.

- Perle.
- Aspose.Cells for Java.
- Java - Extension Perl.
- Java runtime qui répond aux exigences des extensions Aspose.Cells for Java et Java-Perl.
### **Guide**
 Pour appeler un Java API en Perl, vous devez d'abord installer l'extension Java-Perl pour Perl. (Pour les besoins de cet article, nous supposons que Perl a été installé et configuré correctement.) Vous pouvez obtenir l'extension Java-Perl à partir de[Metzo/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7)

 A la fin de ce document, il y a un exemple de script Perl qui appelle Aspose.Cells for Java. Pour l'exécuter, suivez les étapes suivantes :

1. Téléchargez le fichier Java-4.7.tar.gz et décompressez-le sur votre disque local.
1. Installez ce paquet pour Perl.
1.  Démarrez JavaServer. La commande sera :

{{< highlight "java" >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

 où ... est le chemin de classe qui doit inclure toutes les bibliothèques requises par votre application.

 Pour utiliser Aspose.Cells for Java, doit contenir au moins deux fichiers JAR :

1. **Aspose.Cells.jar** du Aspose.Cells au for Java
1. **JavaServer.jar** de Java-4.7.tar.gz
1. Exécutez le script Perl qui invoque le Aspose.Cells for Java API.

 Pour plus d'informations sur l'utilisation de Java en Perl, consultez la documentation de Java - Extension Perl sur<https://metacpan.org/release/METZZO/Java-4.7>

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
