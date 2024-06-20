---
title: ページブレークの管理
type: docs
weight: 30
url: /ja/cpp/managing-page-breaks/
---

{{% alert color="primary" %}} 

定義によると、ページブレークはテキストフローの中で１つのページが終わり、次のページが始まる場所です。Microsoft Excelでは、ユーザーは任意の選択したワークシートのセルにページブレークを追加できます。

ページブレークの追加により、そのセルの位置にページが終了し、ページブレーク以降のデータは次のページに印刷されます。単純に言えば、ページブレークによりワークシートが指定に従って複数のページに分割されます。Aspose.Cellsを使用して実行時にワークシートにページブレークを追加することもできます。Aspose.Cellsでは、以下のタイプのページブレークを追加できます。

- 水平ページブレーク
- 垂直ページブレーク

後続の議論では、Aspose.Cellsを使用して、どのようにしてワークシートに水平または垂直のページブレークを追加できるかについて説明します。

{{% /alert %}} 
## **ページブレーク**
Aspose.CellsはExcelファイルを表す[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) クラスを提供します。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) クラスにはExcelファイル内の各ワークシートにアクセスを許可する[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection) コレクションが含まれています。

ワークシートは[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスで表されます。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスは、ワークシートを管理するために使用されるさまざまなメソッドを提供します。ページブレークを追加するには、[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスの [AddPageBreaks](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) メソッドを使用します。
### **ページブレークの追加**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
