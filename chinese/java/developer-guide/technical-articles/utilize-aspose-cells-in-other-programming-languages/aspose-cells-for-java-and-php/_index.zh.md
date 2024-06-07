---
title: Aspose.Cells for Java and PHP
type: docs
weight: 20
url: /zh/java/aspose-cells-for-java-and-php/
---

{{% alert color="primary" %}} 

PHP开发人员可以在PHP应用程序中使用Aspose.Cells for Java。要使用Aspose.Cells for Java和PHP，请使用PHP版本5（称为PHP5）。也可以使用PHP4来访问Aspose.Cells for Java，但相对于使用PHP5更加复杂。 

{{% /alert %}} 
## **使用PHP**
### **使用PHP5**
Aspose.Cells for Java提供了PHP5包装类，使开发人员无需直接处理Java类即可使用Aspose.Cells库。 

这些包装类可以在aspose.cells.zip存档的PHP目录中以PHP文件的形式找到。 
## **使用PHP4**
PHP4也可以与Aspose.Cells for Java一起使用，但在这种情况下，开发人员需要直接处理Java类。 

{{% alert color="primary" %}} 

不要忘记在php.ini文件中将aspose.cells.jar添加到java.class.path中。 

PHP包装类提供了一些静态方法来为相应的Java类创建PHP类，在ClassFactory中具有createXXX()签名。如果构造函数被重载，ClassFactory中的所有相应方法都定义为create+序号+类名，例如：((createXXX()}}, create1XXX(args...), create2XXX(args...),等等。 

所有常量在PHP中都被定义为ClassName+" "+ConstantName，例如，BorderLineType.NONE在PHP中被定义为BorderLineType NONE。 

如果方法被重载，它们被定义为方法名+序号，例如cell.setValue, cell.setValue1(), cell.setValue2()等。 

clone()方法被定义为cloneObject()。 

{{% /alert %}} 

PHP

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
