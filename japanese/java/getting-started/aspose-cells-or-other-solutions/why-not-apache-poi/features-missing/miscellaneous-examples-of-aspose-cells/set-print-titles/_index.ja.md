---
title: 印刷タイトルの設定
type: docs
weight: 10
url: /ja/java/set-print-titles/
---

## **Aspose.Cells - 印刷タイトルの設定**
Aspose.Cellsを使用すると、印刷されたワークシートの全ページで行と列の見出しを指定できます。これには、[PageSetup](/java/pagesetup)クラスのsetPrintTitleColumnsおよびsetPrintTitleRowsプロパティを使用します。

繰り返す行または列は、その行番号または列番号を渡すことで定義されます。たとえば、行は$1:$2と定義され、列は$A:$Bと定義されます。

**Java**

{{< highlight java >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **ランニングコードのダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintTitles.java)

{{% alert color="primary" %}} 

詳細については、[印刷オプションの設定](/cells/ja/java/page-setup-features/#setting-print-options) をご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
