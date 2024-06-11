---
title: Aspose.Cells for Java和PHP
type: docs
weight: 20
url: /zh/java/aspose-cells-for-java-and-php/
---

{{% alert color="primary" %}} 

PHP开发人员可以在PHP应用程序中使用Aspose.Cells for Java。要使用Aspose.Cells for Java和PHP，使用PHP版本5（称为PHP5）。也可以使用PHP4来访问Aspose.Cells for Java，但比使用PHP5更复杂。 

{{% /alert %}} 
## **使用 PHP**
### **使用 PHP5**
Aspose.Cells for Java提供了PHP5包装类，让开发人员可以更容易地使用Aspose.Cells库，而不需要直接使用Java类。 

这些包装类可以在 aspose.cells.zip 存档的 PHP 目录中找到，以 PHP 文件的形式存在。 
## **使用 PHP4**
在这种情况下，PHP4也可以与Aspose.Cells for Java一起工作，但是开发人员需要直接使用Java类。 

{{% alert color="primary" %}} 

不要忘记在 php.ini 文件中的 java.class.path 添加 aspose.cells.jar。 

PHP 包装类提供了一些静态方法来为对应的 Java 类创建 PHP 类，使用类工厂（ClassFactory）的 createXXX() 签名。如果构造函数被重载，那么在类工厂中定义了所有对应的方法，格式为 create+序号+类名，例如：((createXXX()}}, create1XXX(args...), create2XXX(args...), 依此类推。 

在 PHP 中，所有常量都以 ClassName+" "+ConstantName 的形式定义，例如，BorderLineType.NONE 在 PHP 中被定义为 BorderLineType NONE。 

如果方法被重载，它们将被定义为方法名 + 序号，例如 cell.setValue, cell.setValue1(), cell.setValue2()，依此类推。 

clone() 方法被定义为 cloneObject()。 

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
