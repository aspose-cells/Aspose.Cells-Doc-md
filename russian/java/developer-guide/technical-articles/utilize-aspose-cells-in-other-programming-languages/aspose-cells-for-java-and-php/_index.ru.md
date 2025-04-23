---
title: Aspose.Cells for Java и PHP
type: docs
weight: 20
url: /ru/java/aspose-cells-for-java-and-php/
---

{{% alert color="primary" %}} 

Разработчики PHP могут использовать Aspose.Cells for Java в приложениях PHP. Для работы с Aspose.Cells for Java и PHP используйте версию PHP 5 (известную как PHP5). PHP4 также может быть использован для доступа к Aspose.Cells for Java, но это сложнее, чем использование PHP5. 

{{% /alert %}} 
## **Работа с PHP**
### **Используя PHP5**
Aspose.Cells for Java предоставляет обертки классов PHP5, которые упрощают работу разработчиков с библиотекой Aspose.Cells без прямой работы с классами Java. 

Эти оберточные классы можно найти в каталоге PHP архива aspose.cells.zip в виде файла PHP. 
## **Использование PHP4**
PHP4 также работает с Aspose.Cells for Java, но в этом случае разработчикам придется напрямую работать с классами Java. 

{{% alert color="primary" %}} 

Не забудьте добавить aspose.cells.jar в java.class.path в файл php.ini. 

Обертки PHP предоставляют некоторые статические методы для создания классов PHP для соответствующего класса Java, в ClassFactory с сигнатурой createXXX(). Если конструкторы перегружены, все соответствующие методы в ClassFactory определены как create+номер+имя класса, например: ((createXXX()}}, create1XXX(args...), create2XXX(args...), и так далее. 

Все константы определены в PHP как ClassName+" "+ConstantName, например, BorderLineType.NONE определено как BorderLineType NONE в PHP. 

Если методы перегружены, они определяются как имя метода + номер, например cell.setValue, cell.setValue1(), cell.setValue2(), и так далее. 

Метод clone() определен как cloneObject(). 

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
{{< app/cells/assistant language="java" >}}
