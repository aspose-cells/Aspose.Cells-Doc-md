---
title: xlsx4j で印刷タイトルを設定する
type: docs
weight: 40
url: /ja/java/set-print-titles-in-xlsx4j/
---

## **Aspose.Cells - 印刷タイトルの設定**
Aspose.Cells は、印刷されたワークシートのすべてのページで行と列のヘッダーを繰り返すことができます。そのためには、[PageSetup](/java/PageSetup) クラスの setPrintTitleColumns および setPrintTitleRows プロパティを使用してください。

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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/setprinttitles/AsposeSetPrintTitles.java)

{{% alert color="primary" %}} 

詳細については、[印刷オプションの設定](/cells/ja/java/page-setup-features/#setting-print-options) をご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
