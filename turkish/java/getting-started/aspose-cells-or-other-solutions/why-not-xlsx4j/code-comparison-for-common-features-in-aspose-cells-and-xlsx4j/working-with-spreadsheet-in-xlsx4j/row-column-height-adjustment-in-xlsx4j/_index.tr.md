---
title: xlsx4j'de Satır Sütun Yükseklik Ayarı
type: docs
weight: 50
url: /tr/java/row-column-height-adjustment-in-xlsx4j/
---
## **Aspose.Cells - Sıra Sütun Yükseklik Ayarı**
Cells koleksiyonunun setRowHeight yöntemini çağırarak tek bir satırın yüksekliğini ayarlamak mümkündür. setRowHeight yöntemi aşağıdaki parametreleri alır:

- **Satır dizini**, yüksekliğini değiştirdiğiniz satırın dizini.
- **Satır yüksekliği**, satıra uygulanacak satır yüksekliği.

Cells koleksiyonunun setColumnWidth yöntemini çağırarak bir sütunun genişliğini ayarlayın. setColumnWidth yöntemi aşağıdaki parametreleri alır:

- **Sütun dizini**, genişliğini değiştirdiğiniz sütunun dizini.
- **Sütun genişliği**, istenen sütun genişliği.

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

//Setting the height of all rows in the worksheet to 8

worksheet.getCells().setStandardHeight(8f);

//Setting the height of the second row to 40

cells.setRowHeight(1, 40);



//Setting the width of the second column to 17.5

cells.setColumnWidth(1, 17.5);

{{< /highlight >}}
## **xlsx4j - Satır Sütun Yükseklik Ayarı**
Row.setHt, xlsx4j kullanan satırlar için özel yükseklik ayarlamak için kullanılır. setCustomHeight, TRUE olarak ayarlanmalıdır.

**Java**

{{< highlight "java" >}}

 SpreadsheetMLPackage pkg = SpreadsheetMLPackage.createPackage();

WorksheetPart sheet = pkg.createWorksheetPart(new PartName("/sheet1.xml"), "Sheet1", 1);

CTSheetFormatPr format = Context.getsmlObjectFactory().createCTSheetFormatPr();

format.setDefaultRowHeight(5);

format.setCustomHeight(Boolean.TRUE);

sheet.getJaxbElement().setSheetFormatPr(format);

SheetData sheetData = sheet.getJaxbElement().getSheetData();

Row row = Context.getsmlObjectFactory().createRow();

row.setHt(66.0);

row.setCustomHeight(Boolean.TRUE);

row.setR(1L);

Cell cell1 = Context.getsmlObjectFactory().createCell();

cell1.setV("1234");

row.getC().add(cell1);

Cell cell2 = Context.getsmlObjectFactory().createCell();

cell2.setV("56");

row.getC().add(cell2);

sheetData.getRow().add(row);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/worksheet/adjustheight)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Satır Yüksekliğini ve Sütun Genişliğini Ayarlama](/java/adjusting-row-height-and-volumn-width).

{{% /alert %}}
