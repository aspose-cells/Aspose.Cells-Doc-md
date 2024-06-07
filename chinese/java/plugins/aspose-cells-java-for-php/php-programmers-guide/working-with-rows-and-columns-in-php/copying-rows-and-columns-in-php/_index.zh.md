---
title: 在PHP中复制行和列
type: docs
weight: 30
url: /zh/java/copying-rows-and-columns-in-php/
---

## **Aspose.Cells - 复制行和列**
### **复制行**
Aspose.Cells提供了Cells类的copyRow方法。该方法从源行复制包括公式、数值、注释、单元格格式、隐藏单元格、图像和其他绘图对象在内的所有类型的数据到目标行。

copyRow方法接受以下参数：

- 源Cells对象，
- 源行索引，以及
- 目标行索引。

**PHP代码**

{{< highlight php >}}

 public static function copy_rows($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook($dataDir . 'Book1.xls');

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Copy the second row with data, formattings, images and drawing objects

    # to the 12th row in the $worksheet->

    $worksheet->getCells()->copyRow($worksheet->getCells(),1,11);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Copy Rows.xls");

    print "Copy Rows Successfully." . PHP_EOL;

}

{{< /highlight >}}
### **复制列**
Aspose.Cells提供了Cells类的copyColumn方法，该方法可以从源列复制所有类型的数据，包括带有更新引用的公式和数值、注释、单元格格式、隐藏单元格、图片和其他绘图对象到目标列。

copyColumn方法接受以下参数:

- 源Cells对象，
- 源列索引，以及
- 目标列索引。

**PHP代码**

{{< highlight php >}}

 public static function copy_columns($dataDir)

{

    # Instantiating a Workbook object by excel file path

    $workbook = new Workbook();

    # Accessing the first worksheet in the Excel file

    $worksheet = $workbook->getWorksheets()->get(0);

    # Put some data into header rows (A1:A4)

    $i = 0;

    while($i < 5)

    {

        $worksheet->getCells()->get($i, 0)->setValue("Header Row #$i");

        $i++;

    }


    # Put some detail data (A5:A999)

    $i = 5;

    while ($i < 1000) {

        $worksheet->getCells()->get($i, 0)->setValue("Detail Row #$i");

        $i++;

    }

    # Create another Workbook.

    $workbook1 = new Workbook();

    # Get the first worksheet in the book.

    $worksheet1 = $workbook1->getWorksheets()->get(0);

    # Copy the first column from the first worksheet of the first workbook into

    # the first worksheet of the second workbook.

    $worksheet1->getCells()->copyColumn($worksheet->getCells(),0,2);

    # Autofit the column.

    $worksheet1->autoFitColumn(2);

    # Saving the modified Excel file in default (that is Excel 2003) format

    $workbook->save($dataDir . "Copy Columns.xls");

    print "Copy Columns Successfully." . PHP_EOL;

}

{{< /highlight >}}
## **下载运行代码**
从下面提到的任何社交编码网站下载**复制行和列（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithRowsAndColumns/RowsAndColumns.php)
