---
title: Обнаружение слияния Cells в xlsx4j
type: docs
weight: 20
url: /ru/java/detect-merged-cells-in-xlsx4j/
---
## **Aspose.Cells - Обнаружение слияния Cells**
В Microsoft Excel несколько ячеек можно объединить в одну. Это часто используется для создания сложных таблиц или для создания ячейки с заголовком, охватывающим несколько столбцов.
Aspose.Cells позволяет идентифицировать объединенные области ячеек на листе. Вы также можете разъединить их.

**Java**

{{< highlight "java" >}}

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
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/detectmergecells/AsposeDetectMergeCells.java)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Обнаружение слияния Cells на рабочем листе](/cells/ru/java/detect-merged-cells-in-a-worksheet).

{{% /alert %}}
