---
title: 大きなスプレッドシートを読み込む際のjava.lang.OutOfMemoryErrorの修正方法
type: docs
weight: 20
url: /ja/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---

{{% alert color="primary" %}} 

Workbookコンストラクターが大きなスプレッドシートを読み込む際にjava.lang.OutOfMemoryErrorをスローする可能性が高いです。この例外は、利用可能なメモリが十分でないため、スプレッドシートを完全にメモリに読み込むことができないことを示しています。したがって、[Memory Preferences](/cells/ja/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)を有効にしてスプレッドシートを読み込む必要があります。

{{% /alert %}} 
## **大きなスプレッドシートを読み込む際のjava.lang.OutOfMemoryErrorの修正方法**
Aspose.Cells APIは、大規模なスプレッドシートを効率的に読み込むためのメモリ設定を提供しています。以下に示すように、これらのオプションは、大量のデータセットを含む大規模なスプレッドシートを効率的にWorkbookオブジェクトに読み込むのに役立ちます。 

**Java**

{{< highlight csharp >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
