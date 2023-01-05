---
title: Aspose.Cells for Java および PHP
type: docs
weight: 20
url: /ja/java/aspose-cells-for-java-and-php/
---
{{% alert color="primary" %}} 

 PHP 開発者は、PHP アプリケーションで Aspose.Cells for Java を使用できます。 Aspose.Cells for Java と PHP を使用するには、PHP バージョン 5 (PHP5 として知られています) を使用します。 PHP4 を使用して Aspose.Cells for Java にアクセスすることもできますが、PHP5 を使用するよりも複雑です。

{{% /alert %}} 
## **PHP の操作**
### **PHP5 の使用**
Aspose.Cells for Java は、開発者が Java クラスを直接操作しなくても Aspose.Cells ライブラリを簡単に使用できるようにする PHP5 ラッパー クラスを提供します。

これらのラッパー クラスは、PHP ファイルの形式で aspose.cells.zip アーカイブの PHP ディレクトリにあります。
## **PHP4 の使用**
PHP4 は Aspose.Cells for Java でも機能しますが、この場合、開発者は Java クラスを直接操作する必要があります。

{{% alert color="primary" %}} 

 aspose.cells.jar を php.ini ファイルの java.class.path に追加することを忘れないでください。

 PHP ラッパー クラスは、対応する Java クラスの PHP クラスを作成するためのいくつかの静的メソッドを提供します。コンストラクターがオーバーロードされている場合、ClassFactory 内の対応するすべてのメソッドは、作成 + シリアル番号 + クラス名として定義されます。たとえば、((createXXX()}}、create1XXX(args...)、create2XXX(args...)、等々。

すべての定数は PHP で ClassName+" "+ConstantName として定義されます。たとえば、BorderLineType.NONE は PHP で BorderLineType NONE として定義されます。

メソッドがオーバーロードされている場合は、メソッド名 + シリアル番号として定義されます (たとえば、cell.setValue、cell.setValue1()、cell.setValue2() など)。

 clone() メソッドは cloneObject() として定義されています。

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
