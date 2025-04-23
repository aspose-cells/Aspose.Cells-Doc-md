---
title: Usar Aspose.Cells for Java con Perl
type: docs
weight: 30
url: /es/java/using-aspose-cells-for-java-with-perl/
---

{{% alert color="primary" %}} 

Aspose.Cells for Java es un componente puro de Java que se puede usar con Perl. El uso del componente es igual que invocar otras API comunes de Java en Perl. Para llamar a cualquier biblioteca de Java en Perl, primero debes instalar la extensión Java-Perl para Perl. Esto es necesario para acceder JVM.

{{% /alert %}} 
## **Software y bibliotecas requeridos**
Se requieren el siguiente software y bibliotecas. 

- Perl.
- Aspose.Cells for Java.
- Java - extensión Perl.
- Tiempo de ejecución Java que cumple con el requisito de Aspose.Cells for Java y la extensión Java-Perl.
### **Guía**
Para llamar a una API de Java en Perl, primero debes instalar la extensión Java-Perl para Perl. (Para los propósitos de este artículo, asumimos que Perl ha sido instalado y configurado correctamente). Puedes obtener la extensión Java-Perl en [Metzzo/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7)

Al final de este documento, hay un ejemplo de script de Perl que llama al Aspose.Cells for Java. Para ejecutarlo, siga los siguientes pasos: 

1. Descargue el archivo Java-4.7.tar.gz y descomprímalo en su disco local.
1. Instale este paquete para Perl.
1. Inicie JavaServer. El comando será: 

{{< highlight java >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

donde ... es la ruta de clase que debe incluir todas las bibliotecas requeridas por su aplicación. 

Para utilizar Aspose.Cells for Java, debe contener al menos dos archivos JAR: 

1. **Aspose.Cells.jar** de Aspose.Cells for Java
1. **JavaServer.jar** de Java-4.7.tar.gz
1. Ejecute el script de Perl que invoca la API Aspose.Cells for Java.

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
