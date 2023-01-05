---
title: 大きなスプレッドシートの読み込み中に java.lang.OutOfMemoryError を修正する方法
type: docs
weight: 20
url: /ja/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---
{{% alert color="primary" %}} 

Workbook コンストラクターが大きなスプレッドシートの読み込み中に java.lang.OutOfMemoryError をスローする可能性はかなりあります。この例外は、スプレッドシートをメモリに完全にロードするには使用可能なメモリが不足していることを示唆しています。[メモリ設定](/cells/ja/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}} 
## **大きなスプレッドシートのロード中に java.lang.OutOfMemoryError を修正する方法**
Aspose.Cells API は、スプレッドシートのロードおよび処理中のメモリ消費を最適化するためのメモリ設定を提供します。これらのオプションは、以下に示すように Workbook オブジェクトに巨大なデータ セットを含む大きなスプレッドシートを効率的に読み込むのにも役立ちます。

**Java**

{{< highlight "csharp" >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
