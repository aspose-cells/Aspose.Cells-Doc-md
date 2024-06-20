---
title: Aspose.Cells for Java y PHP
type: docs
weight: 20
url: /es/java/aspose-cells-for-java-and-php/
---

{{% alert color="primary" %}} 

Los desarrolladores de PHP pueden usar Aspose.Cells for Java en aplicaciones PHP. Para trabajar con Aspose.Cells for Java y PHP, use la versión de PHP 5 (conocida como PHP5). También se puede utilizar PHP4 para acceder a Aspose.Cells for Java, pero es más complicado que usar PHP5. 

{{% /alert %}} 
## **Trabajando con PHP**
### **Usando PHP5**
Aspose.Cells for Java proporciona clases de envoltorio de PHP5 que facilitan a los desarrolladores el uso de la biblioteca Aspose.Cells sin necesidad de trabajar directamente con las clases de Java. 

Estas clases de envoltorio se pueden encontrar en el directorio de PHP del archivo aspose.cells.zip en forma de un archivo PHP. 
## **Usando PHP4**
PHP4 también funciona con Aspose.Cells for Java, pero en este caso, los desarrolladores necesitarían trabajar directamente con las clases de Java. 

{{% alert color="primary" %}} 

No olvide agregar aspose.cells.jar a java.class.path en el archivo php.ini. 

Las clases de envoltorio de PHP proporcionan algunos métodos estáticos para crear clases de PHP para la clase de Java correspondiente, en la Clase de Fábrica con la firma createXXX(). Si los constructores están sobrecargados, todos los métodos correspondientes en la Clase de Fábrica se definen como create+número de serie+nombre de la clase, por ejemplo: ((createXXX()}, create1XXX(args...), create2XXX(args...), y así sucesivamente. 

Todas las constantes se definen en PHP como NombreDeLaClase+" "+NombreDeLaConstante, por ejemplo, BorderLineType.NONE se define como BorderLineType NONE en PHP. 

Si los métodos están sobrecargados, se definen como nombre del método + número de serie, por ejemplo cell.setValue, cell.setValue1(), cell.setValue2(), y así sucesivamente. 

El método clone() se define como cloneObject(). 

{{% /alert %}} 

**PHP**

{{< highlight csharp >}}

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
