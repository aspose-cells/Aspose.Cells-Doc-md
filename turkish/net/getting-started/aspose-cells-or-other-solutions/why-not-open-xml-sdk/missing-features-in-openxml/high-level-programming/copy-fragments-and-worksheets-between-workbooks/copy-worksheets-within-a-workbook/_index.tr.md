---
title: Çalışma Kitabındaki Çalışma Sayfalarını Kopyalama
type: docs
weight: 20
url: /tr/net/copy-worksheets-within-a-workbook/
---
**Aspose.Cells** aşırı yüklenmiş bir yöntem sağlar,**Aspose.Cells.WorksheetCollection.AddCopy()**, koleksiyona bir çalışma sayfası eklemek için kullanılır ve mevcut bir çalışma sayfasından verileri kopyalar. Yöntemin bir sürümü, kaynak çalışma sayfasının dizinini parametre olarak alır. Diğer sürüm, parametre olarak kaynak çalışma sayfasının adını alır.

Aşağıdaki örnek, bir çalışma kitabı içinde varolan bir çalışma sayfasının nasıl kopyalanacağını gösterir.

{{< highlight "csharp" >}}

 //Create a new Workbook.

//Open an existing Excel file.

Workbook wb = new Workbook("ResultedBook.xls");

//Create a Worksheets object with reference to

//the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Copy data to a new sheet from an existing

//sheet within the Workbook.

sheets.AddCopy("MySheet");

//Save the Excel file.

wb.Save("Copy Worksheet.xls");

{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)
