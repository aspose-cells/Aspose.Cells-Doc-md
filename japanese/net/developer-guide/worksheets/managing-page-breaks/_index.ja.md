---
title: ページブレークの管理
type: docs
weight: 30
url: /ja/net/managing-page-breaks/
description: この記事では、C# APIまたは.NETライブラリを使用してExcelワークシートにページブレークを追加、ページブレークをクリア、または特定のページブレークを削除する方法についてのサンプルコードと説明が提供されています。
keywords: C#でページブレーク、Excelページブレーク、ページブレークのクリア、特定のページブレークを削除
---

{{% alert color="primary" %}}

定義によると、ページブレークはテキストフローの中で１つのページが終わり、次のページが始まる場所です。Microsoft Excelでは、ユーザーは任意の選択したワークシートのセルにページブレークを追加できます。

ページブレークが追加されるセルの位置によっては、ページが終了し、ページブレークの後のデータの残りが次のページで印刷されます。単純に言えば、ページブレークは、指定に応じてワークシートを複数のページに分割します。Aspose.Cellsを使用して、実行時にワークシートにページブレークを追加することもできます。Aspose.Cellsでは、以下の2種類のページブレークを追加できます。

- 水平ページブレーク
- 垂直ページブレーク

後続の議論では、Aspose.Cellsを使用して、どのようにしてワークシートに水平または垂直のページブレークを追加できるかについて説明します。

{{% /alert %}}

## **ページブレーク**

Aspose.CellsはExcelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスするための[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは、ワークシートを管理するために使用される幅広い範囲のプロパティとメソッドを提供しています。

ページブレークを追加するには、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks)および[**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)プロパティを使用します。

[**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks)および[**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)プロパティは、いくつかのページブレークを含む可能性があるコレクションであり、各コレクションには水平および垂直ページブレークを管理するためのいくつかのメソッドが含まれています。

### **ページブレークの追加**

ワークシートにページブレークを追加するには、各**Add**メソッドに追加するページブレークが配置されるセルの名前を指定して呼び出します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

ページビューモードまたは印刷プレビューモードで、これらの改ページがどのように動作するかを確認できます。

{{% /alert %}}

### **すべてのページの改ページをクリアする**

ワークシートのすべてのページブレークをクリアするには、各[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection)および[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection)コレクションの[**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear)メソッドを呼び出します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **特定の改ページを削除する**

特定のページブレークを削除するには、各**RemoveAt**メソッドに削除されるページブレークのインデックスを指定して呼び出します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **重要なこと**

ページ設定の設定で**FitToPages**プロパティ（すなわち[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)および[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)）を設定すると、ページブレークの設定が影響を受けます。そのため、ワークシートを印刷する場合、ページブレークの設定は考慮されませんが、それらはまだ設定されています。
