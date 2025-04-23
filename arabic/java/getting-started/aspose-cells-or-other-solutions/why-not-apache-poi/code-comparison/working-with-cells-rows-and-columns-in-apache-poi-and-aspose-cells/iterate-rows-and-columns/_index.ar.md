---
title: تكرار الصفوف والأعمدة
type: docs
weight: 50
url: /ar/java/iterate-rows-and-columns/
description: تعلم كيفية تكرار الصفوف والأعمدة من خلال واجهة برمجة التطبيقات Aspose.Cells for Java.
keywords: كيفية تصفح الصفوف والأعمدة في جافا ، تصفح الصفوف باستخدام جافا ، جافا تصفح الأعمدة. 
---

## **كيفية تصفح الصفوف والأعمدة باستخدام Aspose.Cells for Java**

يمكن تصفح الصفوف والأعمدة باستخدام مجموعة الصفوف والأعمدة.

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

## **أباتشي POI SS - HSSF XSSF - تصفح الصفوف والأعمدة**

يمكن تصفح الصفوف والخلايا على الورقة. يتم ذكر الشيفرة العينية أدناه:

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

## **تحميل رمز التشغيل**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **تحميل رمز عينة**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

{{< app/cells/assistant language="java" >}}
