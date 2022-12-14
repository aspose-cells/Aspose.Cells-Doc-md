---
title: Cell İçindekileri Alma
type: docs
weight: 10
url: /tr/java/getting-cell-contents/
---
## **Aspose.Cells - Cell İçeriğini Alma**
Hücrelere erişmek için Cells.get() yöntemi mevcuttur.

**Java**

{{< highlight "java" >}}

 //Excel dosyasındaki ilk çalışma sayfasına erişim

Çalışma sayfası çalışma sayfası = workbook.getWorksheets().get(0);

Cells hücreler = worksheet.getCells();

//Maksimum Görüntüleme Aralığına Erişin

Aralık aralığı = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Toplam Satır:" + trow);

System.out.println("Toplam Sütunlar:" + tcols);

// Cell B4 erişim değeri

//=====================================================

System.out.println(cells.get("B4").getValue());

Cell hücre = hücreler.get(3,1); //Cell B4 erişim değeri

System.out.println(cell.getValue());

//=====================================================

RowCollection satırları = cell.getRows();

 için (int ben = 0 ; ben< rows.getCount() ; i++)

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
## **Apache POI SS - HSSF XSSF - Cell İçeriğini Alma**
Apache POI, hücrelerin çeşitli özelliklerine erişmek için Cell sınıfını sağlar.

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
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/gettingcellcontent)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Aspose.Cells kullanan Veri İşleme Özellikleri](/cells/tr/java/data-handling-features-using-aspose-cells/)

{{% /alert %}}
