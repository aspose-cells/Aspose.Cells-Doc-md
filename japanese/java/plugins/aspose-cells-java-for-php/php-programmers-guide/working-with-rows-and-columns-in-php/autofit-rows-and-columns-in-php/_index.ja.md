---
title: PHPで行と列を自動調整
type: docs
weight: 20
url: /ja/java/autofit-rows-and-columns-in-php/
---

## **Aspose.Cells - 行と列の自動調整**
### **行の自動調整**
行の幅と高さを自動調整する最も直感的な方法は、Worksheet クラスのautoFitRowメソッドを呼び出すことです。autoFitRowメソッドは、サイズ変更する行のインデックス（row index）をパラメーターとして取ります。

**PHPコード**

{{< highlight php >}}

 public static function autofit_row($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Auto-fitting the 3rd row of the worksheet

    $worksheet->autoFitRow(2);

    # Auto-fitting the 3rd row of the worksheet based on the contents in a range of

    # cells (from 1st to 9th column) within the row

    #$worksheet->autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Autofit Row.xls");

    print "Autofit Row Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **列の自動調整**
列の幅と高さを自動調整する最も簡単な方法は、Worksheet クラスのautoFitColumnメソッドを呼び出すことです。autoFitColumnメソッドは、サイズ変更する列のインデックス（column index）をパラメーターとして取ります。

**PHPコード**

{{< highlight php >}}

 public static function autofit_column($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Auto-fitting the 4th column of the worksheet

    $worksheet->autoFitColumn(3);

    # Auto-fitting the 4th column of the worksheet based on the contents in a range of

    # cells (from 1st to 9th row) within the column

    #$worksheet->autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Autofit Column.xls");

    print "Autofit Column Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下に挙げるどのソーシャルコーディングサイトから、**行と列の自動調整（Aspose.Cells）**をダウンロードしてください：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
