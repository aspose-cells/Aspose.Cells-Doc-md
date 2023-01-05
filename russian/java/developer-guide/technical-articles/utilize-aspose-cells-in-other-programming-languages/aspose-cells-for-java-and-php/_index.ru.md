---
title: Aspose.Cells for Java и PHP
type: docs
weight: 20
url: /ru/java/aspose-cells-for-java-and-php/
---
{{% alert color="primary" %}} 

 Разработчики PHP могут использовать Aspose.Cells for Java в приложениях PHP. Для работы с Aspose.Cells for Java и PHP используйте PHP версии 5 (известной как PHP5). PHP4 также можно использовать для доступа к Aspose.Cells for Java, но это сложнее, чем использование PHP5.

{{% /alert %}} 
## **Работа с PHP**
### **Использование PHP5**
 Aspose.Cells for Java предоставляет классы-оболочки PHP5, которые упрощают разработчикам использование библиотеки Aspose.Cells без прямой работы с классами Java.

 Эти классы-оболочки можно найти в каталоге PHP архива aspose.cells.zip в виде файла PHP.
## **Использование PHP4**
 PHP4 также работает с классами Aspose.Cells for Java, но в этом случае разработчикам придется работать с классами Java напрямую.

{{% alert color="primary" %}} 

 Не забудьте добавить aspose.cells.jar в java.class.path в файле php.ini.

 Классы-оболочки PHP предоставляют некоторые статические методы для создания классов PHP для соответствующего класса Java в ClassFactory с сигнатурой createXXX(). Если конструкторы перегружены, все соответствующие методы в ClassFactory определяются как create+серийный номер+имя класса, например: ((createXXX()}}, create1XXX(args...), create2XXX(args...), и так далее.

Все константы определены в PHP как ClassName+" "+ConstantName, например, BorderLineType.NONE определяется как BorderLineType NONE в PHP.

 Если методы перегружены, они определяются как имя метода + серийный номер, например, cell.setValue, cell.setValue1(), cell.setValue2() и т. д.

 Метод clone() определен как cloneObject().

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
