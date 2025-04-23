---
title: Обнаружение объединенных ячеек с использованием Aspose.Cells
type: docs
weight: 30
url: /ru/java/detect-merged-cells-using-aspose-cells/
---

## **Aspose.Cells - Обнаружение объединенных ячеек**
В Microsoft Excel несколько ячеек могут быть объединены в одну. Это часто используется для создания сложных таблиц или для создания ячейки, содержащей заголовок, который охватывает несколько столбцов.
Aspose.Cells позволяет определить области объединенных ячеек в листе электронной таблицы. Вы также можете отменить объединение ячеек.

**Java**

{{< highlight java >}}

 //Get the merged cells list to put it into the arraylist object

ArrayList<CellArea> al = worksheet.getCells().getMergedCells();

//Define cellarea

CellArea ca;

//Define some variables

int frow, fcol, erow, ecol;

// Print Message

System.out.println("Merged Areas: \n"+ al.toString());

//Loop through the arraylist and get each cellarea to unmerge it

for(int i = al.size()-1 ; i > -1; i--)

{

	ca = new CellArea();

	ca = (CellArea)al.get(i);

	frow = ca.StartRow;

	fcol = ca.StartColumn;

	erow = ca.EndRow;

	ecol = ca.EndColumn;

	System.out.println((i+1) + ". [" + fcol +"," + frow +"] " + "[" + ecol +"," + erow +"]");

	worksheet.getCells().unMerge(frow, fcol, erow, ecol);

}

{{< /highlight >}}
## **Скачать работающий код**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDetectMergeCells.java)

{{% alert color="primary" %}} 

Для получения дополнительной информации посетите [Обнаружение объединенных ячеек на листе Excel](/cells/ru/java/detect-merged-cells-in-a-worksheet).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
