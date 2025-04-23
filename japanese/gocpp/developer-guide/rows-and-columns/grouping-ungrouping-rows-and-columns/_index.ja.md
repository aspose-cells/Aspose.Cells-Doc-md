---
title: 行と列のグルーピングおよびグループ解除
type: docs
weight: 30
url: /ja/go-cpp/grouping-ungrouping-rows-and-columns/
---

## **紹介**

Microsoft Excelファイルでは、データの概要を作成して、1回のマウスクリックで詳細のレベルを表示したり非表示にしたりできます。

「アウトライン記号」の**1、2、3、+、-**をクリックして、ワークシート内のセクションの要約または見出しを提供する行または列のみをすばやく表示するか、個々の要約または見出しの下に詳細を表示するためにこの記号を使用できます。

## **行と列のグループ管理**

Aspose.Cellsは、Microsoft Excelファイルを表す [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスを提供します。 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスは、Excelファイル内の各ワークシートにアクセスできる [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) コレクションを持ち、ワークシートは [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスで表されます。 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスは、すべてのセルを表す [Cells](https://reference.aspose.com/cells/go-cpp/cells/) コレクションを提供します。

[Cells](https://reference.aspose.com/cells/go-cpp/cells/) コレクションは、ワークシート内の行や列を管理するための複数のメソッドを提供し、これらの一部を詳しく解説します。

### **行と列のグループ化**

[Cells](https://reference.aspose.com/cells/go-cpp/cells/) コレクションの [GroupRows](https://reference.aspose.com/cells/go-cpp/cells/grouprows/) および [GroupColumns](https://reference.aspose.com/cells/go-cpp/cells/groupcolumns/) メソッドを呼び出すことで、行または列をグループ化することが可能です。両方のメソッドは以下のパラメータを取ります。

- 最初の行/列インデックス、グループ内の最初の行または列。
- 最後の行/列インデックス、グループ内の最後の行または列。
- 非表示かどうか、グループ化後に行または列を非表示にするかどうかを指定するブールパラメータ。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupingRowsColumns.go" >}}

#### **グループ設定**

Microsoft Excelでは、以下を表示するためのグループ設定を構成できます:

- 詳細の下の要約行。
- 詳細の右側の要約列。

## **行と列のグループ解除**

グループ化された行または列のグループ解除には、 [Cells](https://reference.aspose.com/cells/go-cpp/cells/) コレクションの [UngroupRows](https://reference.aspose.com/cells/go-cpp/cells/ungrouprows/) および [UngroupColumns](https://reference.aspose.com/cells/go-cpp/cells/ungroupcolumns/) メソッドを呼び出します。これらの両方のメソッドは2つのパラメータを取ります。

- 最初の行または列インデックス、解除される最初の行または列。
- 最後の行または列インデックス、解除される最後の行または列。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UnGroupingRowsColumns.go" >}}
