---
title: 获取 Cell 内容
type: docs
weight: 10
url: /zh/java/getting-cell-contents/
---
## **Aspose.Cells - 获取 Cell 内容**
Cells.get() 方法可用于访问单元格。

**Java**

{{< highlight "java" >}}

 //访问Excel文件中的第一个工作表

工作表worksheet = workbook.getWorksheets().get(0);

Cells 细胞 = worksheet.getCells();

//访问最大显示范围

范围 range = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("总行数：" + trows);

System.out.println("总列数：" + tcols);

// 访问Cell B4的值

//=====================================================

System.out.println(cells.get("B4").getValue());

Cell cell = cells.get(3,1); //获取Cell B4的值

System.out.println(cell.getValue());

//=====================================================

RowCollection 行 = cells.getRows();

对于 (int i = 0 ; i< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		if (cells.get(i,j).getType() != CellValueType.IS_NULL)

		{

			System.out.println(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue());

		}

	}

}

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 获取 Cell 内容**
Apache POI 提供 Cell 类来访问单元格的各种属性。

**Java**

{{< highlight "java" >}}

 Sheet sheet1 = wb.getSheetAt(0);

for (Row row : sheet1) {

    for (Cell cell : row) {

        CellReference cellRef = new CellReference(row.getRowNum(), cell.getColumnIndex());

        System.out.print(cellRef.formatAsString());

        System.out.print(" - ");

        switch (cell.getCellType()) {

            case Cell.CELL_TYPE_STRING:

                System.out.println(cell.getRichStringCellValue().getString());

                break;

            case Cell.CELL_TYPE_NUMERIC:

                if (DateUtil.isCellDateFormatted(cell)) {

                    System.out.println(cell.getDateCellValue());

                } else {

                    System.out.println(cell.getNumericCellValue());

                }

                break;

            case Cell.CELL_TYPE_BOOLEAN:

                System.out.println(cell.getBooleanCellValue());

                break;

            case Cell.CELL_TYPE_FORMULA:

                System.out.println(cell.getCellFormula());

                break;

            default:

                System.out.println();

        }

    }

}

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/gettingcellcontent)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[使用 Aspose.Cells 的数据处理功能](/cells/zh/java/data-handling-features-using-aspose-cells/)

{{% /alert %}}
