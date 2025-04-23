---
title: 行の高さと列の幅の調整
type: docs
weight: 10
url: /ja/go-cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}}

スプレッドシートで行や列にデータを追加する際、行の高さや列の幅を変更する必要があることがあります。時々、行や列に書式を適用することで、データを表示するために現在の高さや幅を変更する必要があります。通常、ユーザーはMicrosoft Excelを使用してWYSIWYG環境で行の高さと列の幅を調整します。しかし、Aspose.Cellsを使用すると、開発者はランタイムでこれらの操作を実行できます。

{{% /alert %}}

## **行で操作する**

### **行の高さを調整**

Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)クラスを提供します。[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)クラスには、Excelファイルを操作するために必要なメソッドが含まれる[WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/)があります。ワークシートは[Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/)クラスで表されます。[Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/)クラスは、シート内のすべてのセルを表す[Cells](https://reference.aspose.com/cells/go-cpp/cells/)コレクションを提供します。[Cells](https://reference.aspose.com/cells/go-cpp/cells/)コレクションには、行や列を管理するためのいくつかのメソッドがあります。詳細については以下で説明します。

#### **1行の高さを設定する**

単一の行の高さを設定するには、[Cells](https://reference.aspose.com/cells/go-cpp/cells/)コレクションの[SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/)メソッドを呼び出します。[SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/)メソッドは、以下のパラメータを取ります：

- **行インデックス**：高さを変更する行のインデックス。
- **行の高さ**：行に適用する行の高さ。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-GPP-SettingHeightOfRow.go" >}}

#### **ワークシート内のすべての行の高さを設定する**

すべての行に同じ高さを設定する必要がある場合は、[Cells](https://reference.aspose.com/cells/go-cpp/cells/)コレクションの[SetStandardHeight](https://reference.aspose.com/cells/go-cpp/cells/setstandardheight/)メソッドを使用して設定できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingHeightOfAllRowsInWorksheet.go" >}}

## **列で操作する**

### **列の幅を設定する**

列の幅を設定するには、 [Cells](https://reference.aspose.com/cells/go-cpp/cells/) コレクションの [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) メソッドを呼び出します。 [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) は以下のパラメータを取ります。

- **列インデックス**：幅を変更する列のインデックス。
- **列の幅**：設定したい列の幅。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfColumn.go" >}}

### **ワークシート内のすべての列の幅を設定する**

ワークシート内のすべての列に同じ列幅を設定するには、 [Cells](https://reference.aspose.com/cells/go-cpp/cells/) コレクションの [SetStandardWidth](https://reference.aspose.com/cells/go-cpp/cells/setstandardwidth/) メソッドを使用します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfAllColumnsInWorksheet.go" >}}
