---
title: Çalışma Kitabı İçinde Sayfaları Taşıma
type: docs
weight: 30
url: /tr/net/move-worksheets-within-workbook/
---

Aspose.Cells, Aspose.Cells.Worksheet.MoveTo() adlı bir yöntem sağlar, bu yöntem, bir çalışma sayfasını elektronik tabloda başka bir konuma taşımak için kullanılır. Yöntem, hedef çalışma sayfası dizinini bir parametre olarak alır.

Aşağıdaki örnek, bir çalışma kitabı içinde bir çalışma sayfasının başka bir konuma nasıl taşınacağını gösterir.

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Move Worksheet.xlsx";

//Open an existing excel file.

Workbook wb = new Workbook(FileName);

//Create a Worksheets object with reference to

//the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Get the first worksheet.

Worksheet worksheet = sheets[0];

string test = worksheet.Name;

//Move the first sheet to the third position in the workbook.

worksheet.MoveTo(2);

//Save the excel file.

wb.Save(FileName);

{{< /highlight >}}
## **Örnek Kod İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Move%20Worksheet%20%28Aspose.Cells%29.zip)
