---
title: Aspose.Cells for Java ve PHP
type: docs
weight: 20
url: /tr/java/aspose-cells-for-java-and-php/
---
{{% alert color="primary" %}} 

 PHP geliştiricileri PHP uygulamalarında Aspose.Cells for Java kullanabilirler. Aspose.Cells for Java ve PHP ile çalışmak için PHP sürüm 5'i (PHP5 olarak bilinir) kullanın. PHP4, Aspose.Cells for Java'e erişmek için de kullanılabilir, ancak PHP5 kullanmaktan daha karmaşıktır.

{{% /alert %}} 
## **PHP ile çalışmak**
### **PHP5'i Kullanma**
 Aspose.Cells for Java, geliştiricilerin doğrudan Java sınıflarıyla çalışmadan Aspose.Cells kitaplığını kullanmasını kolaylaştıran PHP5 sarmalayıcı sınıfları sağlar.

 Bu sarmalayıcı sınıfları, bir PHP dosyası biçiminde aspose.cells.zip arşivinin PHP dizininde bulunabilir.
## **PHP4'ü kullanma**
 PHP4, Aspose.Cells for Java ile de çalışır, ancak bu durumda, geliştiricilerin doğrudan Java sınıflarıyla çalışması gerekir.

{{% alert color="primary" %}} 

 php.ini dosyasındaki java.class.path'e aspose.cells.jar'ı eklemeyi unutmayın.

 PHP sarmalayıcı sınıfları, ClassFactory'de createXXX() imzasıyla karşılık gelen Java sınıfı için PHP sınıfları oluşturmak için bazı statik yöntemler sağlar. Yapıcılar aşırı yüklenirse, ClassFactory'deki karşılık gelen tüm yöntemler create+seri numarası+sınıf adı olarak tanımlanır, örneğin: ((createXXX()}}, create1XXX(args...), create2XXX(args...), ve bunun gibi.

Tüm sabitler PHP'de ClassName+" "+SabitAd olarak tanımlanır, örneğin BorderLineType.NONE, PHP'de BorderLineType NONE olarak tanımlanır.

 Yöntemler aşırı yüklenirse, yöntem adı + seri numarası olarak tanımlanırlar, örneğin cell.setValue, cell.setValue1(), cell.setValue2(), vb.

 clone() yöntemi cloneObject() olarak tanımlanır.

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
