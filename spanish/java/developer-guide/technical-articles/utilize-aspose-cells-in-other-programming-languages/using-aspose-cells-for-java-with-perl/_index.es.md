---
title: Usando Aspose.Cells for Java con Perl
type: docs
weight: 30
url: /es/java/using-aspose-cells-for-java-with-perl/
---
{{% alert color="primary" %}} 

Aspose.Cells for Java es un componente Java puro que se puede usar con Perl. Usar el componente es lo mismo que invocar otras API Java comunes en Perl. Para llamar a cualquier biblioteca Java en Perl, primero debe instalar la extensión Java-Perl para Perl. Esto es necesario para acceder a JVM.

{{% /alert %}} 
## **Software y bibliotecas necesarios**
 Se requiere el siguiente software y bibliotecas.

- perla
- Aspose.Cells for Java.
- Java - Extensión Perl.
- Java tiempo de ejecución que cumple con el requisito de Aspose.Cells for Java y Java-extensión de Perl.
### **Guía**
 Para llamar al Java API en Perl, primero debe instalar la extensión Java-Perl para Perl. (Para los fines de este artículo, asumimos que Perl se instaló y configuró correctamente). Puede obtener la extensión Java-Perl de[Metzzo/Java-4.7/](https://metacpan.org/release/METZZO/Java-4.7)

 Al final de este documento, hay un ejemplo de script Perl que llama Aspose.Cells for Java. Para ejecutarlo, siga los siguientes pasos:

1. Descargue el archivo Java-4.7.tar.gz y descomprímalo en su disco local.
1. Instale este paquete para Perl.
1.  Inicie JavaServer. El comando será:

{{< highlight "java" >}}

 java -classpath ...  com.zzo.javaserver.JavaServer 

{{< /highlight >}}

 donde ... es el classpath que debe incluir todas las bibliotecas requeridas por su aplicación.

 Para usar Aspose.Cells for Java, debe contener al menos dos archivos JAR:

1. **Aspose.Cells.jar** desde Aspose.Cells for Java
1. **JavaServer.jar** desde Java-4.7.tar.gz
1. Ejecute el script Perl que invoca el Aspose.Cells for Java API.

 Para obtener más información sobre cómo trabajar con Java en Perl, consulte la documentación de Java - Extensión de Perl en<https://metacpan.org/release/METZZO/Java-4.7>

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
