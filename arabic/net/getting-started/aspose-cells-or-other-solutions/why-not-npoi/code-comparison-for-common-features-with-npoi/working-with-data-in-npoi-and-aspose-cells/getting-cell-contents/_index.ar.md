---
title: الحصول على Cell محتويات
type: docs
weight: 10
url: /ar/net/getting-cell-contents/
---
## **Aspose.Cells - الحصول على Cell المحتويات**
Cells [0] أو Cells [الاسم] طريقة متاحة للوصول إلى الخلايا.

**C#**

{{< highlight "cs" >}}

 مصنف المصنف = مصنف جديد ("../../ data / test.xlsx")؛

ورقة العمل 1 = workbook.Worksheets [0] ،

Cells خلايا = ورقة 1.Cells ؛

نطاق النطاق = sheet1.Cells.MaxDisplayRange ؛

int tcols = range.ColumnCount ؛

trows int = range.RowCount ؛

 لـ (int i = 0 ؛ i< trows; i++)

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
## **NPOI - HSSF XSSF - الحصول على Cell محتويات**
يوفر NPOI فئة Cell للوصول إلى الخصائص المختلفة للخلايا.

**C#**

{{< highlight "cs" >}}

 IWorkbook wb = XSSFWorkbook جديد ("../../ data / test.xlsx") ؛

ISheet sheet1 = wb.GetSheetAt (0) ،

 لـ (int index = 0 ؛ index<= sheet1.LastRowNum; index++)

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
## **قم بتنزيل كود التشغيل**
 تحميل**الحصول على Cell محتويات** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Getting.Cell.Contents.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[ميزات معالجة البيانات](/cells/ar/net/data-handling-features-in-aspose-cells/).

{{% /alert %}}
