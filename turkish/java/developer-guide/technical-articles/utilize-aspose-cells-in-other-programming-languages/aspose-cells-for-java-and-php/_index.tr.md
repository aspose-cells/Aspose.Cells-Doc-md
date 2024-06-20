---
title: Aspose.Cells for Java ve PHP
type: docs
weight: 20
url: /tr/java/aspose-cells-for-java-and-php/
---

{{% alert color="primary" %}} 

PHP geliştiricileri Aspose.Cells for Java'yi PHP uygulamalarında kullanabilir. Aspose.Cells for Java ve PHP ile çalışmak için PHP sürümü 5 (PHP5 olarak bilinir) kullanın. PHP4 de Aspose.Cells for Java'yi erişmek için kullanılabilir ancak PHP5 kullanmaktan daha karmaşıktır. 

{{% /alert %}} 
## **PHP ile Çalışmak**
### **PHP5 Kullanımı**
Aspose.Cells for Java, geliştiricilerin Java sınıflarıyla doğrudan çalışmadan Aspose.Cells kitaplığını kullanmalarını sağlayan PHP5 sarmalayıcı sınıflarını sağlar. 

Bu sarmalayıcı sınıflar, aspose.cells.zip arşivinin PHP dizininde bir PHP dosyası biçiminde bulunabilir. 
## **PHP4 Kullanımı**
PHP4 de Aspose.Cells for Java ile çalışır ancak bu durumda geliştiricilerin Java sınıflarıyla doğrudan çalışmaları gerekir. 

{{% alert color="primary" %}} 

php.ini dosyasında java.class.path'e aspose.cells.jar'ı eklemeyi unutmayın. 

PHP sarmalayıcı sınıfları, ClassFactory'de createXXX() imzası ile karşılık gelen PHP sınıfları oluşturmak için bazı sabit metotlar sağlar. Yapıcılar aşırı yüklü ise, ClassFactory'de tüm karşılık gelen metotlar create+sıra numarası+class adı olarak tanımlanır, örneğin: ((createXXX()}}, create1XXX(args...), create2XXX(args...), ve benzeri. 

Tüm sabitler PHP'de ClassName+" "+ConstantName olarak tanımlanır, örneğin, BorderLineType.NONE PHP'de BorderLineType NONE olarak tanımlanmıştır. 

Eğer metotlar aşırı yüklü ise, method adı + sıra numarası olarak tanımlanır, örneğin cell.setValue, cell.setValue1(), cell.setValue2(), ve benzeri. 

clone() metodu cloneObject() olarak tanımlanmıştır. 

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
