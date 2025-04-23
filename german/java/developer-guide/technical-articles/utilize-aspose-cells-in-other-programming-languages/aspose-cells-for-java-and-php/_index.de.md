---
title: Aspose.Cells for Java und PHP
type: docs
weight: 20
url: /de/java/aspose-cells-for-java-and-php/
---

{{% alert color="primary" %}} 

PHP-Entwickler können Aspose.Cells for Java in PHP-Anwendungen verwenden. Um mit Aspose.Cells for Java und PHP zu arbeiten, verwenden Sie die PHP-Version 5 (bekannt als PHP5). PHP4 kann ebenfalls verwendet werden, um auf Aspose.Cells for Java zuzugreifen, ist jedoch komplexer als die Verwendung von PHP5. 

{{% /alert %}} 
## **Arbeiten mit PHP**
### **Verwendung von PHP5**
Aspose.Cells for Java bietet PHP5-Wrapper-Klassen, die es Entwicklern erleichtern, die Aspose.Cells-Bibliothek zu verwenden, ohne direkt mit Java-Klassen zu arbeiten. 

Diese Wrapper-Klassen befinden sich im PHP-Verzeichnis des aspose.cells.zip-Archivs in Form einer PHP-Datei. 
## **Verwendung von PHP4**
PHP4 funktioniert auch mit Aspose.Cells for Java, in diesem Fall müssen Entwickler jedoch direkt mit Java-Klassen arbeiten. 

{{% alert color="primary" %}} 

Vergessen Sie nicht, aspose.cells.jar der java.class.path in der php.ini-Datei hinzuzufügen. 

Die PHP-Wrapper-Klassen bieten einige statische Methoden zur Erstellung von PHP-Klassen für die entsprechende Java-Klasse in der Klasse mit der Signatur ClassFactory.createXXX(). Wenn die Konstruktoren überladen sind, werden alle entsprechenden Methoden in der ClassFactory als create+Seriennummer+Klassenname definiert, zum Beispiel: ((createXXX()}, create1XXX(args...), create2XXX(args...) usw. 

Alle Konstanten sind in PHP als Klassenname+" "+Konstantenname definiert, zum Beispiel ist BorderLineType.NONE in PHP als BorderLineType NONE definiert. 

Wenn die Methoden überladen sind, werden sie als Methodenname + Seriennummer definiert, zum Beispiel cell.setValue, cell.setValue1(), cell.setValue2() usw. 

Die Methode clone() ist als cloneObject() definiert. 

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
