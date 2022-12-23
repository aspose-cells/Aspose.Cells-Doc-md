---
title: PHP でファイルを保存する
type: docs
weight: 20
url: /ja/java/saving-files-in-php/
---
## **Aspose.Cells - ファイルの保存**
### **ファイルをある場所に保存する**
開発者がファイルを保存する必要がある場合**Aspose.Cells Java for PHP**ある保存場所に移動すると、ファイル名 (完全な保存パスを含む) と目的のファイル形式 (**ファイル形式の種類**列挙) の呼び出し中**セーブ**方法**ワークブック**物体。

**PHP コード**

{{< highlight "php" >}}

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
## **実行中のコードをダウンロード**
ダウンロード**ファイルの保存 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
