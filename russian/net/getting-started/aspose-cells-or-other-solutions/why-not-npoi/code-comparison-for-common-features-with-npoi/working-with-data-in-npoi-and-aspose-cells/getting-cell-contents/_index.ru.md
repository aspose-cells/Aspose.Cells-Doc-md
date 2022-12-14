---
title: Получение Cell Содержание
type: docs
weight: 10
url: /ru/net/getting-cell-contents/
---
## **Aspose.Cells - Получение Cell Содержание**
Для доступа к ячейкам доступен метод Cells[0]или Cells[имя].

**C#**

{{< highlight "cs" >}}

 Рабочая книга рабочая книга = новая рабочая книга("../../data/test.xlsx");

Рабочий лист1 = рабочая книга.Рабочие листы[0];

Cells ячеек = лист1.Cells;

Диапазон диапазона = лист1.Cells.MaxDisplayRange;

int tcols = диапазон.СчетчикКолонок;

int trows = диапазон.RowCount;

 для (int я = 0 ; я< trows; i++)

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
## **NPOI — HSSF XSSF — Получение Cell Содержание**
NPOI предоставляет класс Cell для доступа к различным свойствам ячеек.

**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook("../../data/test.xlsx");

ISheet лист1 = wb.GetSheetAt(0);

 for (индекс int = 0; индекс<= sheet1.LastRowNum; index++)

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
## **Скачать рабочий код**
 Скачать**Получение Cell Содержание** сформировать любой из перечисленных ниже сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Getting.Cell.Contents.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Особенности обработки данных](/cells/ru/net/data-handling-features-in-aspose-cells/).

{{% /alert %}}
