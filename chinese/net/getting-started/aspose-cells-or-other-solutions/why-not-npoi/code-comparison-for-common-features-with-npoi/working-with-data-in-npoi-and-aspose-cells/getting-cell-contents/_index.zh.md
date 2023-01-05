---
title: 获取 Cell 内容
type: docs
weight: 10
url: /zh/net/getting-cell-contents/
---
## **Aspose.Cells - 获取 Cell 内容**
Cells[0] 或 Cells[name] 方法可用于访问单元格。

**C#**

{{< highlight "cs" >}}

工作簿 workbook = new Workbook("../../data/test.xlsx");

工作表 sheet1 = workbook.Worksheets[0];

Cells 单元格 = sheet1.Cells；

范围range = sheet1.Cells.MaxDisplayRange;

int tcols = range.ColumnCount;

int trows = range.RowCount;

对于 (int i = 0 ; i< trows; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		if (cells[i, j].Type != CellValueType.IsNull)

		{

			Console.WriteLine(cells[i, j].Name + " - " + cells[i, j].Value);

		}

	}

}

{{< /highlight >}}
## **NPOI - HSSF XSSF - 获取 Cell 内容**
NPOI 提供 Cell 类来访问单元格的各种属性。

**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook("../../data/test.xlsx");

ISheet sheet1 = wb.GetSheetAt(0);

 for (int 索引 = 0; 索引<= sheet1.LastRowNum; index++)

{

    IRow row = sheet1.GetRow(index);

    foreach (ICell cell in row.Cells)

    {

        CellReference cellRef = new CellReference(row.RowNum, cell.ColumnIndex);

        Console.Write(cellRef.FormatAsString());

        Console.Write(" - ");

        switch (cell.CellType)

        {

            case CellType.String:

                Console.Write(cell.StringCellValue);

                break;

            case CellType.Numeric:

                if (DateUtil.IsCellDateFormatted(cell))

                    Console.Write(cell.DateCellValue);

                else

                    Console.Write(cell.NumericCellValue);

                break;

            case CellType.Boolean:

                Console.Write(cell.BooleanCellValue);

                break;

            case CellType.Formula:

                Console.Write(cell.CellFormula);

                break;

        }

        Console.WriteLine();

    }

}

{{< /highlight >}}
## **下载运行代码**
下载**获取 Cell 内容**形成以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Getting.Cell.Contents.Aspose.Cells.zip)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[数据处理功能](/cells/zh/net/data-handling-features-in-aspose-cells/).

{{% /alert %}}
