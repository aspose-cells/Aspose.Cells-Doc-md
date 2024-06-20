---
title: Çalışma Kitabı İçinde Sayfaları Kopyalama
type: docs
weight: 20
url: /tr/net/copy-worksheets-within-a-workbook/
---

**Aspose.Cells**, **Aspose.Cells.WorksheetCollection.AddCopy()** adlı aşırı yüklenmiş bir yöntem sağlar, bu yöntem, bir çalışma sayfasını koleksiyona eklemek ve var olan bir çalışma sayfasından veri kopyalamak için kullanılır. Yöntemin bir versiyonu, kaynak çalışma sayfasının dizinini bir parametre olarak alır. Diğer versiyon, kaynak çalışma sayfasının adını parametre olarak alır.

Aşağıdaki örnek, bir çalışma kitabı içinde mevcut bir çalışma sayfasının nasıl kopyalanacağını gösterir.

{{< highlight csharp >}}

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
## **Örnek Kod İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)
