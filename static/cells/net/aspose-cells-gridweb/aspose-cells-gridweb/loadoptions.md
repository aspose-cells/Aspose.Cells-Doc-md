##LoadOptions for GridWeb
This article introduces how to work with load options in GridWeb.
There are some loadoptions we can set before import the file.
we can use [GridLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridloadoptions/) (for general file) and [GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridtxtloadoptions/) (for csv file)
## **load with other encode **
For the csv file, it is actually a text-based file, without the specific encoding described in the xlsx format file.
Therefore, users can set specific character encoding before loading the file.
here is a sample code to load with chinese:
```csharp
GridTxtLoadOptions topt = new GridTxtLoadOptions();
topt.Encoding = (Encoding.GetEncoding("GB2312"));
GridWeb1.LoadOptions = topt;
String filePath = Server.MapPath("~/workbook/chinesefile.csv");
GridWeb1.ImportExcelFile(filePath);
```
