---
title: كرر الصفوف والأعمدة
type: docs
weight: 50
url: /ar/java/iterate-rows-and-columns/
---
## **Aspose.Cells - تكرار الصفوف والأعمدة**

يمكن تكرار الصفوف والأعمدة باستخدام مجموعة الصفوف والأعمدة.

**Java**

{{< highlight "java" >}}

 // الوصول إلى أقصى نطاق عرض

نطاق المدى = workheet.getCells (). getMaxDisplayRange () ؛

int tcols = range.getColumnCount () ،

int trows = range.getRowCount () ،

System.out.println ("إجمالي الصفوف:" + trows) ؛

System.out.println ("إجمالي الأعمدة:" + tcols) ؛

صفوف RowCollection = cells.getRows () ،

 لـ (int i = 0 ؛ i< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

## **Apache POI SS - HSSF XSSF - تكرار الصفوف والأعمدة**

يمكن تكرار الصفوف و Cells على الورقة. رمز عينة مذكور أدناه:

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

## **تحميل كود الجري**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **تنزيل نموذج التعليمات البرمجية**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/ src / main / java / com / aspose / خلية / أمثلة / featurescomparison / cellrowscolumns / iterate)

