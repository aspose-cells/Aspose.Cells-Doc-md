---
title: Aspose.Cells for Java and PHP
type: docs
weight: 20
url: /java/aspose-cells-for-java-and-php/
---

{{% alert color="primary" %}} 

PHP developers can use Aspose.Cells for Java in PHP applications. To work with Aspose.Cells for Java and PHP, use PHP version 5 (known as PHP5). PHP4 can also be used to access Aspose.Cells for Java but it's more complex than using PHP5. 

{{% /alert %}} 
## **Working with PHP**
### **Using PHP5**
Aspose.Cells for Java provides PHP5 wrapper classes that make it easier for developers to use the Aspose.Cells library without working with Java classes directly. 

These wrapper classes can be found in the PHP directory of aspose.cells.zip archive in the form of a PHP file. 
## **Using PHP4**
PHP4 also works with Aspose.Cells for Java but in this case, developers would need to work with Java classes directly. 

{{% alert color="primary" %}} 

Don't forget to add aspose.cells.jar to java.class.path in the php.ini file. 

The PHP wrapper classes provide some static methods to create PHP classes for the corresponding Java class, in the ClassFactory with signature createXXX(). If the constructors are overloaded, all corresponding methods in the ClassFactory are defined as create+serial number+class name, for example: ((createXXX()}}, create1XXX(args...), create2XXX(args...), and so on. 

All constants are defined in PHP as ClassName+" "+ConstantName, for example, BorderLineType.NONE is defined as BorderLineType NONE in PHP. 

If the methods are overloaded, they are defined as method name + serial number, for example cell.setValue, cell.setValue1(), cell.setValue2(), and so on. 

The clone() method is defined as cloneObject(). 

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
