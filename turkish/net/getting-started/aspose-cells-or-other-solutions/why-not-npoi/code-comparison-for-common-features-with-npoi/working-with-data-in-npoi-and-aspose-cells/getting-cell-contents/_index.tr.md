---
title: Cell İçindekileri Alma
type: docs
weight: 10
url: /tr/net/getting-cell-contents/
---
## **Aspose.Cells - Cell İçeriğini Alma**
Hücrelere erişmek için Cells[0]veya Cells[name]yöntemi kullanılabilir.

**C#**

{{< highlight "cs" >}}

 Çalışma kitabı çalışma kitabı = new Workbook("../../data/test.xlsx");

Çalışma sayfası sayfası1 = çalışma kitabı.Çalışma sayfaları[0];

Cells hücre = sayfa1.Cells;

Aralık aralığı = sayfa1.Cells.MaxDisplayRange;

int tcols = aralık.ColumnCount;

int trows = aralık.RowCount;

 için (int ben = 0 ; ben< trows; i++)

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
## **NPOI - HSSF XSSF - Cell İçeriğini Alma**
NPOI, hücrelerin çeşitli özelliklerine erişmek için Cell sınıfını sağlar.

**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook("../../data/test.xlsx");

ISheet sayfası1 = wb.GetSheetAt(0);

 için (int dizin = 0; dizin<= sheet1.LastRowNum; index++)

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
## **Çalışan Kodu İndir**
 İndirmek**Cell İçindekileri Alma** aşağıda belirtilen sosyal kodlama sitelerinden herhangi birini oluşturun:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Getting.Cell.Contents.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Veri İşleme Özellikleri](/cells/tr/net/data-handling-features-in-aspose-cells/).

{{% /alert %}}
