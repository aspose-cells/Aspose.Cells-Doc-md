---
title: Aspose.Cells for Java 和 PHP
type: docs
weight: 20
url: /zh/java/aspose-cells-for-java-and-php/
---
{{% alert color="primary" %}} 

 PHP 开发人员可以在 PHP 应用程序中使用 Aspose.Cells for Java。要使用 Aspose.Cells for Java 和 PHP，请使用 PHP 版本 5（称为 PHP5）。 PHP4也可以用来访问Aspose.Cells for Java但是比用PHP5复杂多了。

{{% /alert %}} 
## **使用 PHP**
### **使用 PHP5**
 Aspose.Cells for Java 提供 PHP5 包装器类，使开发人员可以更轻松地使用 Aspose.Cells 库，而无需直接使用 Java 类。

这些包装类可以 PHP 文件的形式在 aspose.cells.zip 存档的 PHP 目录中找到。
## **使用 PHP4**
 PHP4 也适用于 Aspose.Cells for Java，但在这种情况下，开发人员需要直接使用 Java 类。

{{% alert color="primary" %}} 

不要忘记将 aspose.cells.jar 添加到 php.ini 文件中的 java.class.path 中。

 PHP 包装类提供了一些静态方法来为相应的 Java 类创建 PHP 类，在 ClassFactory 中带有签名 createXXX()。如果重载构造函数，ClassFactory中所有对应的方法定义为create+序号+类名，例如：((createXXX()}}, create1XXX(args...), create2XXX(args...),等等。

所有常量在PHP中定义为ClassName+" "+ConstantName，例如BorderLineType.NONE在PHP中定义为BorderLineType NONE。

如果方法被重载，则定义为方法名+序号，例如cell.setValue、cell.setValue1()、cell.setValue2()等。

 clone() 方法定义为 cloneObject()。

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
