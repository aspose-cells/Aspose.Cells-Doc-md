---
title: ワークシートの管理
type: docs
weight: 20
url: /ja/go-cpp/manage-worksheets/
---

{{% alert color="primary" %}}

開発者は、Aspose.Cellsの柔軟なAPIを使用してMicrosoft Excelファイルでワークシートを簡単に作成および管理できます。このトピックでは、Microsoft Excelファイルでワークシートを追加および削除する方法について説明します。

{{% /alert %}}

Aspose.Cells は [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスを提供しており、Excel ファイルを表します。[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスは、Excel ファイル内の各ワークシートにアクセスできる [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) コレクションを含みます。

ワークシートは [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスで表されます。 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスは、ワークシートの管理に役立つ多くのメソッドを提供します。

## **新しいExcelファイルにワークシートを追加する**

プログラムで新しいExcelファイルを作成するには：

1. [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスのオブジェクトを作成します。
1. [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) コレクションの [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_string/) メソッドを呼び出します。空のワークシートが自動的にExcelファイルに追加されます。新しいワークシートのシートインデックスを渡すことで参照できます。
1. ワークシートの参照を取得します。
1. ワークシートで作業を実行します。
1. [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスの [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) メソッドを呼び出して、新しいワークシートを含むExcelファイルを保存します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingWorksheetsToNewExcelFile.go" >}}

## **Sheet Indexを使用してワークシートにアクセスする**

次のサンプルコードは、インデックスを指定して任意のワークシートにアクセスまたは取得する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessingWorksheetsUsingSheetIndex.go" >}}

## **Sheet Indexを使用してワークシートを削除する**

名前でワークシートを削除することは、名前がわかっている場合に便利です。名前がわからない場合は、[RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat) のオーバーロード版を使用し、ワークシートのシートインデックスを引数として渡します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingWorksheetsUsingSheetIndex.go" >}}
