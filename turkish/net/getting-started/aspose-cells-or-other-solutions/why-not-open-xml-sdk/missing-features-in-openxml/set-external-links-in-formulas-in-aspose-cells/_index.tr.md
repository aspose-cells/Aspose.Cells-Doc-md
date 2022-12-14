---
title: Aspose.Cells'de Formüllerde Dış Bağlantıları Ayarlayın
type: docs
weight: 90
url: /tr/net/set-external-links-in-formulas-in-aspose-cells/
---
{{% alert color="primary" %}} 

Bazen, örneğin bir hücre veya aralık değerini bunlara göre değerlendirmek için formüllere harici dosyalara bağlantılar eklemek gerekir. Aspose.Cells bu özelliği sağlar ve bu belge nasıl kullanılacağını açıklar.

{{% /alert %}} 

Aşağıdaki örnek kod, harici dosyaların formüllere nasıl dahil edileceğini gösterir.

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Set External Links in Formula.xlsx";

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get first Worksheet

Worksheet sheet = workbook.Worksheets[0];

//Get Cells collection

Aspose.Cells.Cells cells = sheet.Cells;

//Set formula with external links

cells["A1"].Formula = "=SUM('[book1.xls]Sheet1'!A2, '[book1.xls]Sheet1'!A4)";

//Set formula with external links

cells["A2"].Formula = "='[book1.xls]Sheet1'!A8";

//Save the workbook

workbook.Save(FileName);

{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Set%20External%20Links%20in%20Formula)
## **Çalışan Örneği İndirin**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
