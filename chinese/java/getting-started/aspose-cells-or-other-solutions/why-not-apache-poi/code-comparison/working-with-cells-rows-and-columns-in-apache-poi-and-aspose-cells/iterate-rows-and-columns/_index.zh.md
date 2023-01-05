---
title: 迭代行和列
type: docs
weight: 50
url: /zh/java/iterate-rows-and-columns/
---
## **Aspose.Cells - 迭代行和列**

可以使用行和列集合迭代行和列。

**Java**

{{< highlight "java" >}}

 //访问最大显示范围

范围 range = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("总行数：" + trows);

System.out.println("总列数：" + tcols);

RowCollection 行 = cells.getRows();

对于 (int i = 0 ; i< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

## **Apache POI SS - HSSF XSSF - 迭代行和列**

Rows 和 Cells 可以在 Sheet 上迭代。示例代码如下：

**Java**

{{< highlight "java" >}}

 Workbook wb = WorkbookFactory.create(inStream);

Sheet sheet = wb.getSheetAt(0);

for (Row row : sheet)

{

  for (Cell cell : row)

  {

    System.out.println("Iteration.");

  }

}

{{< /highlight >}}

## **下载运行代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **下载示例代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

