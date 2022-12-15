---
title: Aspose.Cells for Java och PHP
type: docs
weight: 20
url: /sv/java/aspose-cells-for-java-and-php/
---
{{% alert color="primary" %}} 

 PHP-utvecklare kan använda Aspose.Cells for Java i PHP-applikationer. För att arbeta med Aspose.Cells for Java och PHP, använd PHP version 5 (känd som PHP5). PHP4 kan också användas för att komma åt Aspose.Cells for Java men det är mer komplext än att använda PHP5.

{{% /alert %}} 
## **Arbetar med PHP**
### **Använder PHP5**
 Aspose.Cells for Java tillhandahåller PHP5-omslagsklasser som gör det lättare för utvecklare att använda Aspose.Cells-biblioteket utan att arbeta med Java-klasser direkt.

 Dessa omslagsklasser kan hittas i PHP-katalogen i aspose.cells.zip-arkivet i form av en PHP-fil.
## **Använder PHP4**
 PHP4 fungerar också med Aspose.Cells for Java men i det här fallet skulle utvecklare behöva arbeta med Java klasser direkt.

{{% alert color="primary" %}} 

 Glöm inte att lägga till aspose.cells.jar till java.class.path i php.ini-filen.

 PHP-omslagsklasserna tillhandahåller några statiska metoder för att skapa PHP-klasser för motsvarande Java-klass, i ClassFactory med signatur createXXX(). Om konstruktörerna är överbelastade, definieras alla motsvarande metoder i ClassFactory som create+serienummer+klassnamn, till exempel: ((createXXX()}}, create1XXX(args...), create2XXX(args...), och så vidare.

Alla konstanter definieras i PHP som ClassName+" "+ConstantName, till exempel, BorderLineType.NONE definieras som BorderLineType NONE i PHP.

 Om metoderna är överbelastade definieras de som metodnamn + serienummer, till exempel cell.setValue, cell.setValue1(), cell.setValue2() och så vidare.

 Metoden clone() definieras som cloneObject().

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
