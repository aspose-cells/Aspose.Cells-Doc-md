---
title: ページブレークの管理
type: docs
weight: 30
url: /ja/go-cpp/managing-page-breaks/
---

{{% alert color="primary" %}}

定義によると、ページブレークはテキストフローの中で１つのページが終わり、次のページが始まる場所です。Microsoft Excelでは、ユーザーは任意の選択したワークシートのセルにページブレークを追加できます。

ページブレークの追加により、そのセルの位置にページが終了し、ページブレーク以降のデータは次のページに印刷されます。単純に言えば、ページブレークによりワークシートが指定に従って複数のページに分割されます。Aspose.Cellsを使用して実行時にワークシートにページブレークを追加することもできます。Aspose.Cellsでは、以下のタイプのページブレークを追加できます。

- 水平ページブレーク
- 垂直ページブレーク

後続の議論では、Aspose.Cellsを使用して、どのようにしてワークシートに水平または垂直のページブレークを追加できるかについて説明します。

{{% /alert %}}

## **ページブレーク**

Aspose.Cells は [Workbook](https://reference.aspose.com/cells/go-cpp/workbook) クラスを提供しており、Excel ファイルを表します。 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook) クラスは [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection) コレクションを含み、それを使ってExcelファイル内の各ワークシートにアクセスできます。

ワークシートは [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスで表されます。 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスはワークシートの管理に使用される多くのメソッドを提供します。ページ区切りを追加するには、[AddPageBreaks](https://reference.aspose.com/cells/go-cpp/worksheet/addpagebreaks) メソッドを使用します。

### **ページブレークの追加**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingPageBreaks.go" >}}
