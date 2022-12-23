---
title: Aspose.Cells for Java y PHP
type: docs
weight: 20
url: /es/java/aspose-cells-for-java-and-php/
---
{{% alert color="primary" %}} 

 Los desarrolladores de PHP pueden usar Aspose.Cells for Java en aplicaciones PHP. Para trabajar con Aspose.Cells for Java y PHP, utilice la versión 5 de PHP (conocida como PHP5). PHP4 también se puede usar para acceder a Aspose.Cells for Java pero es más complejo que usar PHP5.

{{% /alert %}} 
## **Trabajando con PHP**
### **Usando PHP5**
 Aspose.Cells for Java proporciona clases contenedoras de PHP5 que facilitan a los desarrolladores el uso de la biblioteca Aspose.Cells sin trabajar directamente con las clases Java.

 Estas clases contenedoras se pueden encontrar en el directorio PHP del archivo aspose.cells.zip en forma de archivo PHP.
## **Usando PHP4**
 PHP4 también funciona con Aspose.Cells for Java pero, en este caso, los desarrolladores tendrían que trabajar directamente con las clases Java.

{{% alert color="primary" %}} 

 No olvide agregar aspose.cells.jar a java.class.path en el archivo php.ini.

 Las clases contenedoras de PHP proporcionan algunos métodos estáticos para crear clases de PHP para la clase Java correspondiente, en ClassFactory con la firma createXXX(). Si los constructores están sobrecargados, todos los métodos correspondientes en ClassFactory se definen como crear+número de serie+nombre de clase, por ejemplo: ((createXXX()}}, create1XXX(args...), create2XXX(args...), etcétera.

Todas las constantes se definen en PHP como ClassName+" "+ConstantName, por ejemplo, BorderLineType.NONE se define como BorderLineType NONE en PHP.

 Si los métodos están sobrecargados, se definen como nombre de método + número de serie, por ejemplo, cell.setValue, cell.setValue1(), cell.setValue2(), etc.

 El método clone() se define como cloneObject().

{{% /alert %}} 

**PHP**

{{< highlight "csharp" >}}

 <?php

require_once("java/Java.inc");

require("AsposeCells.php");

$workbook = ClassFactory::createWorkbook();

$workbook->open5("t1.xls");

$cell = $workbook->getWorksheets()->get(0)->getCells()->getCell(0, 0);

$cell->setValue6("Hello World!"); 

$workbook->save5("t.xls");

?>



{{< /highlight >}}
