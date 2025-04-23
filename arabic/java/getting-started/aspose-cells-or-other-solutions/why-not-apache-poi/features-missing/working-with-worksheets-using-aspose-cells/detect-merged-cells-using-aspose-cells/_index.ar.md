---
title: الكشف عن الخلايا المدمجة باستخدام Aspose.Cells
type: docs
weight: 30
url: /ar/java/detect-merged-cells-using-aspose-cells/
---

## **Aspose.Cells - كشف الخلايا المدمجة**
في Microsoft Excel، يمكن دمج العديد من الخلايا في خلية واحدة. ويتم ذلك غالبًا لإنشاء جداول معقدة، أو لإنشاء خلية تحتوي على عنوان يمتد عبر عدة أعمدة.
تسمح Aspose.Cells لك بتحديد مناطق الخلايا المدمجة في ورقة العمل. يمكنك أيضًا فك دمجها.

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
## **تحميل رمز التشغيل**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDetectMergeCells.java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [كشف الخلايا المدمجة في ورقة عمل](/cells/ar/java/detect-merged-cells-in-a-worksheet).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
