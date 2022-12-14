---
title: كشف الدمج Cells باستخدام Aspose.Cells
type: docs
weight: 30
url: /ar/java/detect-merged-cells-using-aspose-cells/
---
## **Aspose.Cells - كشف مدمج Cells**
في Microsoft Excel ، يمكن دمج عدة خلايا في خلية واحدة. يُستخدم هذا غالبًا لإنشاء جداول معقدة ، أو لإنشاء خلية تحتوي على عنوان يمتد على عدة أعمدة.
Aspose.Cells يسمح لك بتعريف مساحات الخانات المدمجة في ورقة العمل. يمكنك إلغاء دمجهم أيضًا.

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
## **قم بتنزيل كود التشغيل**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDetectMergeCells.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[كشف Cells مدمج في ورقة عمل](/cells/ar/java/detect-merged-cells-in-a-worksheet).

{{% /alert %}}
