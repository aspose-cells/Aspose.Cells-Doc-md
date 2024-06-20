---
title: Aspose.Cells for JavaとPHP
type: docs
weight: 20
url: /ja/java/aspose-cells-for-java-and-php/
---

{{% alert color="primary" %}} 

PHP開発者はAspose.Cells for JavaをPHPアプリケーションで使用できます。Aspose.Cells for JavaとPHPを使用するには、PHPバージョン5（PHP5としても知られています）を使用してください。PHP4でもAspose.Cells for Javaにアクセスすることができますが、PHP5を使用するよりも複雑です。 

{{% /alert %}} 
## **PHPでの操作**
### **PHP5の使用**
Aspose.Cells for Javaは、開発者がJavaクラスを直接扱うことなくAspose.Cellsライブラリを使用できるようにするPHP5ラッパークラスを提供します。 

これらのラッパークラスは、aspose.cells.zipアーカイブのPHPディレクトリにPHPファイルの形で見つけることができます。 
## **PHP4の使用**
PHP4はAspose.Cells for Javaとも連携しますが、この場合、開発者はJavaクラスを直接使用する必要があります。 

{{% alert color="primary" %}} 

php.iniファイルのjava.class.pathにaspose.cells.jarを追加することを忘れないでください。 

PHPラッパークラスは、ClassFactoryでcreateXXX()というシグネチャで対応するJavaクラスのPHPクラスを作成するいくつかの静的メソッドを提供します。コンストラクタがオーバーロードされている場合、ClassFactory内のすべての対応するメソッドは、create+連番+クラス名、例えば: ((createXXX()}}, create1XXX(args...), create2XXX(args...)などとして定義されます。 

すべての定数は、ClassName+" "+ConstantNameとしてPHPで定義されます。たとえば、BorderLineType.NONEはPHPでBorderLineType NONEとして定義されます。 

メソッドがオーバーロードされている場合、メソッド名+連番として定義されます。たとえば、cell.setValue、cell.setValue1()、cell.setValue2()などです。 

clone()メソッドはcloneObject()として定義されます。 

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
