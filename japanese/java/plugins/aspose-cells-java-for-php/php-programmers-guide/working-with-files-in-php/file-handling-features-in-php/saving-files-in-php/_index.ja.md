---
title: PHPでファイルを保存する
type: docs
weight: 20
url: /ja/java/saving-files-in-php/
---

## **Aspose.Cells - ファイルの保存**
### **開発者がファイルをストレージに保存する必要がある場合、**Aspose.Cells Java for Ruby**を使用して**Workbook**オブジェクトの**save**メソッドを呼び出す際に、ファイル名(完全なストレージパスを含む)と希望のファイル形式(**FileFormatType**列挙型を使用)を単純に指定することができます。**
開発者が **Aspose.Cells Java for PHP** を使用してファイルをストレージに保存する必要がある場合は、**Workbook** オブジェクトの **save** メソッドを呼び出す際に、ファイル名（完全なストレージパスを含む）と desired file format（**FileFormatType** 列挙型を使用）を簡単に指定できます。

**PHPコード**

{{< highlight php >}}

 $fileFormatType = new FileFormatType();

//Creating an Workbook object with an Excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Save in default (Excel2003) format

$workbook->save($dataDir . "book.default.out.xls");

//Save in Excel2003 format

$workbook->save($dataDir . "book.out.xls",$fileFormatType->EXCEL_97_TO_2003);

//Save in Excel2007 xlsx format

$workbook->save($dataDir . "book.out.xlsx", $fileFormatType->XLSX);

//Save in SpreadsheetML format

$workbook->save($dataDir . "book.out.xml", $fileFormatType->EXCEL_2003_XML);

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから、**ファイルを保存する（Aspose.Cells）**をダウンロードしてください：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
