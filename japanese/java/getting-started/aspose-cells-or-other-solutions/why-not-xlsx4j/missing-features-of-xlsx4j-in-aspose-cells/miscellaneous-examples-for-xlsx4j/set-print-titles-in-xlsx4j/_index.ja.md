---
title: xlsx4j で印刷タイトルを設定する
type: docs
weight: 40
url: /ja/java/set-print-titles-in-xlsx4j/
---
## **Aspose.Cells - 印刷タイトルの設定**
Aspose.Cells を使用すると、印刷されたワークシートのすべてのページで行ヘッダーと列ヘッダーを繰り返すように指定できます。これを行うには、[ページ設定](/java/PageSetup)クラスの setPrintTitleColumns および setPrintTitleRows プロパティ。

繰り返される行または列は、行番号または列番号を渡すことによって定義されます。たとえば、行は $1:$2 として定義され、列は $A:$B として定義されます。

**Java**

{{< highlight "java" >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/setprinttitles/AsposeSetPrintTitles.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[印刷オプションの設定](/cells/ja/java/page-setup-features/#setting-print-options).

{{% /alert %}}
