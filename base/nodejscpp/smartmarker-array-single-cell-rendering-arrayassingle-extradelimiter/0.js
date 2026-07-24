let product = {
    Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
};

let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue('&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")');

let designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");