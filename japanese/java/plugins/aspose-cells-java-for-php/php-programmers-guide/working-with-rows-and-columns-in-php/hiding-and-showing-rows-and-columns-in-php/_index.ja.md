---
title: PHP での行と列の表示と非表示
type: docs
weight: 50
url: /ja/java/hiding-and-showing-rows-and-columns-in-php/
description: Aspose.Cells for PHP via Java API を使用して行と列を非表示または表示する方法を学習します。
keywords: How to Hide and Show Rows and Columns in PHP, Hide Rows or Columns using PHP, PHP Show Rows or Columns. 
---
##  **Aspose.Cells for PHP - 行と列の可視性の制御**
###  **PHP で行と列を非表示にする方法**
開発者は、Cells コレクションの HideRow メソッドと HideColumn メソッドをそれぞれ呼び出すことで、行または列を非表示にすることができます。どちらのメソッドも、行/列インデックスをパラメータとして受け取り、特定の行または列を非表示にします。

**PHPコード**

{{< highlight "php" >}}

 public static function hide_rows_columns($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();;

    # Hiding the 3rd row of the worksheet

    $cells->hideRow(2);

    # Hiding the 2nd column of the worksheet

    $cells->hideColumn(1);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Hide Rows And Columns.xls");

    print "Hide Rows And Columns Successfully." . PHP_EOL;

}

{{< /highlight >}}
###  **PHP を使用して行と列を表示する方法**
開発者は、Cells コレクションの UnhideRow メソッドと UnhideColumn メソッドをそれぞれ呼び出すことで、非表示の行または列を再表示できます。どちらのメソッドも次の 2 つのパラメータを取ります。

- **行または列のインデックス**特定の行または列を表示するために使用される行または列のインデックス。
- **行の高さまたは列の幅**表示後に行または列に割り当てられる行の高さまたは列の幅。

**PHPコード**

{{< highlight "php" >}}

 public static function unhide_rows_columns($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    $cells = $worksheet->getCells();;

    # Unhiding the 3rd row and setting its height to 13.5

    $cells->unhideRow(2,13.5);

    # Unhiding the 2nd column and setting its width to 8.5

    $cells->unhideColumn(1,8.5);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Unhide Rows And Columns.xls");

    print "Unhide Rows And Columns Successfully." . PHP_EOL;

}

{{< /highlight >}}
##  **実行コードをダウンロード**
ダウンロード**行と列の可視性の制御 (Aspose.Cells)**以下のソーシャル コーディング サイトのいずれかから:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
