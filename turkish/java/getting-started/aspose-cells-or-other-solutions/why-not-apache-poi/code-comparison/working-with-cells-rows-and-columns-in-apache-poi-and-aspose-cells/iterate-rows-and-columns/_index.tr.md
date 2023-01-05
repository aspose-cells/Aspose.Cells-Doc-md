---
title: Satırları ve Sütunları Yinele
type: docs
weight: 50
url: /tr/java/iterate-rows-and-columns/
---
## **Aspose.Cells - Satırları ve Sütunları Yinele**

Satırlar ve Sütunlar, satırlar ve sütunlar koleksiyonu kullanılarak yinelenebilir.

**Java**

{{< highlight "java" >}}

 //Maksimum Görüntüleme Aralığına Erişin

Aralık aralığı = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Toplam Satır:" + trow);

System.out.println("Toplam Sütunlar:" + tcols);

RowCollection satırları = cell.getRows();

 için (int ben = 0 ; ben< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

## **Apache POI SS - HSSF XSSF - Satırları ve Sütunları Yinele**

Satırlar ve Cells Sayfada yinelenebilir. Örnek kod aşağıda belirtilmiştir:

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

## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Örnek Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/yineleme)

