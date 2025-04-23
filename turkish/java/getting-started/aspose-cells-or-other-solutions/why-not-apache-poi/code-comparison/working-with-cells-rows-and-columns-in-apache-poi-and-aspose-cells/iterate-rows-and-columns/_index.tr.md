---
title: Satır ve Sütunları İterele
type: docs
weight: 50
url: /tr/java/iterate-rows-and-columns/
description: Aspose.Cells for Java API leri aracılığıyla Satır ve Sütunları Nasıl İtereleme Öğrenin.
keywords: Java da Satır ve Sütunları İtereleme, Java Kullanarak Satırları İtereleme, Java Sütunlarını İtereleme. 
---

## **Aspose.Cells for Java Kullanarak Satır ve Sütunları Nasıl İtereleme**

Satır ve Sütunlar, satır ve sütun koleksiyonları kullanılarak iterelenebilir.

**Java**

{{< highlight java >}}

 //Access the Maximum Display Range

Range range = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Total Rows:" + trows);

System.out.println("Total Cols:" + tcols);

RowCollection rows = cells.getRows();

for (int i = 0 ; i < rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

## **Apache POI SS - HSSF XSSF - Satır ve Sütunları İtereleme**

Satırlar ve Hücreler Sayfada İterelenebilir. Örnek kod aşağıda belirtilmiştir:

**Java**

{{< highlight java >}}

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

## **Örnek Kod İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

{{< app/cells/assistant language="java" >}}
