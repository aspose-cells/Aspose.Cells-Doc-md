---
title: Apache POI ve Aspose.Cells kullanarak Pivot Tablolar oluşturun
type: docs
weight: 40
url: /tr/java/create-pivot-tables-using-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Pivot Tablo Oluştur**
Aspose.Cells'i kullanarak bir pivot tablo oluşturmak için:

1. Cell nesnesinin setValue yöntemini kullanarak çalışma sayfası hücrelerine bazı veriler ekleyin. Ayrıca önceden verilerle doldurulmuş bir şablon dosyası da kullanırsınız. Veriler, pivot tablonun veri kaynağı olarak kullanılacaktır.
1. PivotTableCollection ekleme yöntemini ({{Worksheet }}nesnesi içine alınmış) çağırarak çalışma sayfasına bir pivot tablo ekleyin.
1. Dizinini geçirerek PivotTableCollection koleksiyonundan yeni PivotTable nesnesine erişin.

**Java**

{{< highlight "java" >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Obtaining the reference of the newly added worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

sheet.setName("PivotTable");

Cells cells = sheet.getCells();

// Setting the value to the cells

Cell cell = cells.get("A1");

cell.setValue("Sport");

cell = cells.get("B1");

cell.setValue("Quarter");

cell = cells.get("C1");

cell.setValue("Sales");

cell = cells.get("A2");

cell.setValue("Golf");

cell = cells.get("A3");

cell.setValue("Golf");

cell = cells.get("A4");

cell.setValue("Tennis");

cell = cells.get("A5");

cell.setValue("Tennis");

cell = cells.get("A6");

cell.setValue("Tennis");

cell = cells.get("A7");

cell.setValue("Tennis");

cell = cells.get("A8");

cell.setValue("Golf");

cell = cells.get("B2");

cell.setValue("Qtr3");

cell = cells.get("B3");

cell.setValue("Qtr4");

cell = cells.get("B4");

cell.setValue("Qtr3");

cell = cells.get("B5");

cell.setValue("Qtr4");

cell = cells.get("B6");

cell.setValue("Qtr3");

cell = cells.get("B7");

cell.setValue("Qtr4");

cell = cells.get("B8");

cell.setValue("Qtr3");

cell = cells.get("C2");

cell.setValue(1500);

cell = cells.get("C3");

cell.setValue(2000);

cell = cells.get("C4");

cell.setValue(600);

cell = cells.get("C5");

cell.setValue(1500);

cell = cells.get("C6");

cell.setValue(4070);

cell = cells.get("C7");

cell.setValue(5000);

cell = cells.get("C8");

cell.setValue(6430);

PivotTableCollection pivotTables = sheet.getPivotTables();

// Adding a PivotTable to the worksheet

int index = pivotTables.add("=A1:C8", "E3", "PivotTable1");

// Accessing the instance of the newly added PivotTable

PivotTable pivotTable = pivotTables.get(index);

// Unshowing grand totals for rows.

pivotTable.setRowGrand(false);

// Dragging the first field to the row area.

pivotTable.addFieldToArea(PivotFieldType.ROW, 0);

// Dragging the second field to the column area.

pivotTable.addFieldToArea(PivotFieldType.COLUMN, 1);

// Dragging the third field to the data area.

pivotTable.addFieldToArea(PivotFieldType.DATA, 2);

{{< /highlight >}}
## **Apache POI SS (HSSF + XSSF) - Pivot Tablolar Oluşturun**
**Java**

{{< highlight "java" >}}

 XSSFWorkbook wb = new XSSFWorkbook();

XSSFSheet sheet = wb.createSheet();

//Create some data to build the pivot table on

setCellData(sheet);

XSSFPivotTable pivotTable = sheet.createPivotTable(new AreaReference("A1:D4"), new CellReference("H5"));

//Configure the pivot table

//Use first column as row label

pivotTable.addRowLabel(0);

//Sum up the second column

pivotTable.addColumnLabel(DataConsolidateFunction.SUM, 1);

//Set the third column as filter

pivotTable.addColumnLabel(DataConsolidateFunction.AVERAGE, 2);

//Add filter on forth column

pivotTable.addReportFilter(3);

{{< /highlight >}}
## **Çalışan Kodu İndir**
 Şunun için çalışan örnekleri indirin:**Apache POI ve Aspose.Cells kullanarak Pivot Tablolar oluşturun** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells-Java-vs-POI-SS-v1.5)
## **Kaynak Kodunu İndir**
 için kaynak kodunu indirin**Apache POI ve Aspose.Cells kullanarak Pivot Tablolar oluşturun** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Pivot Tablolar ve Pivot Grafikler Oluşturun](/cells/tr/java/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}
