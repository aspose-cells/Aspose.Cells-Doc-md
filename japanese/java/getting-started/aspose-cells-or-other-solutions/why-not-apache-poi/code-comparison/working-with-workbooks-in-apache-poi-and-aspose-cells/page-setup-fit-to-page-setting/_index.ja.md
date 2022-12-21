---
title: ページ設定 - ページ設定に合わせる
type: docs
weight: 30
url: /ja/java/page-setup-fit-to-page-setting/
---
## **Aspose.Cells - ページ設定 - ページ設定に合わせる**
ワークシートの内容を特定のページ数に合わせるには、[ページ設定](/cells/ja/java/page-setup-fit-to-page-setting/)クラスの setFitToPagesTall および setFitToPagesWide メソッド。これらのメソッドは、ワークシートのスケーリングにも使用されます。

**Java**

{{< highlight "java" >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Accessing the first worksheet in the Excel file

WorksheetCollection worksheets = workbook.getWorksheets();

int sheetIndex = worksheets.add();

Worksheet sheet = worksheets.get(sheetIndex);

PageSetup pageSetup = sheet.getPageSetup();

// Setting the number of pages to which the length of the worksheet will

// be spanned

pageSetup.setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned

pageSetup.setFitToPagesWide(1);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - ページ設定 - ページ設定に合わせる**
Apache POI SS は、setFitHeight および setFitWidth メソッドを使用して、ページに合わせる設定を行います。

**Java**

{{< highlight "java" >}}

 Workbook wb = new XSSFWorkbook();  //or new HSSFWorkbook();

Sheet sheet = wb.createSheet("format sheet");

PrintSetup ps = sheet.getPrintSetup();

sheet.setAutobreaks(true);

ps.setFitHeight((short) 1);

ps.setFitWidth((short) 1);

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/fittoonepage)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[ページ オプションの設定](http://www.aspose.com/docs/display/cellsjava/Setting+Page+Options).

{{% /alert %}}
