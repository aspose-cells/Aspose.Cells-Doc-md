---
title: ページ設定  ページに合わせて設定
type: docs
weight: 30
url: /ja/java/page-setup-fit-to-page-setting/
---

## **Aspose.Cells - ページ設定 - ページに合わせて設定**
ワークシートのコンテンツを特定のページ数に合わせるには、PageSetupクラスのsetFitToPagesTallおよびsetFitToPagesWideメソッドを使用します。 これらのメソッドはワークシートを拡大縮小するためにも使用されます。

**Java**

{{< highlight java >}}

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
## **Apache POI SS - HSSF＆XSSF - ページ設定 - ページに合わせて設定**
Apache POI SSは、fit to pageの設定にsetFitHeightとsetFitWidthメソッドを使用します。

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();  //or new HSSFWorkbook();

Sheet sheet = wb.createSheet("format sheet");

PrintSetup ps = sheet.getPrintSetup();

sheet.setAutobreaks(true);

ps.setFitHeight((short) 1);

ps.setFitWidth((short) 1);

{{< /highlight >}}
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/fittoonepage)

{{% alert color="primary" %}} 

詳細については、[ページのオプション設定](http://www.aspose.com/docs/display/cellsjava/Setting+Page+Options)を参照してください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
