class Product {
    constructor() {
        this.Tags = null;
    }
}

const product = new Product();
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

const designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");