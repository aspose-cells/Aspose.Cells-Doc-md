---
title: الحصول على Cell محتويات
type: docs
weight: 10
url: /ar/java/getting-cell-contents/
---
## **Aspose.Cells - الحصول على Cell المحتويات**
طريقة Cells.get () متاحة للوصول إلى الخلايا.

**Java**

{{< highlight "java" >}}

 // الوصول إلى ورقة العمل الأولى في ملف Excel

ورقة عمل ورقة العمل = workbook.getWorksheets (). get (0)؛

Cells خلايا = workheet.getCells () ،

// الوصول إلى أقصى نطاق عرض

نطاق المدى = workheet.getCells (). getMaxDisplayRange () ؛

int tcols = range.getColumnCount () ،

int trows = range.getRowCount () ،

System.out.println ("إجمالي الصفوف:" + trows) ؛

System.out.println ("إجمالي الأعمدة:" + tcols) ؛

// قيمة الوصول Cell B4

//=====================================================

System.out.println (cell.get ("B4"). getValue ()) ؛

Cell خلية = cell.get (3،1) ؛ // قيمة الوصول Cell B4

System.out.println (cell.getValue ()) ،

//=====================================================

صفوف RowCollection = cells.getRows () ،

 لـ (int i = 0 ؛ i< rows.getCount() ; i++)

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
## **Apache POI SS - HSSF XSSF - الحصول على Cell المحتويات**
توفر Apache POI فئة Cell للوصول إلى الخصائص المختلفة للخلايا.

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
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/ src / main / java / com / aspose / cells / أمثلة / featurescomparison / datahandling / getcellcontent)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[ميزات معالجة البيانات باستخدام Aspose.Cells](/cells/ar/java/data-handling-features-using-aspose-cells/)

{{% /alert %}}
