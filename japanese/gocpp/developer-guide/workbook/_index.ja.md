---
title: Golang経由のC++でワークブックを管理
linktitle: ワークブック
type: docs
weight: 60
url: /ja/go-cpp/managing-workbooks-and-worksheets/
description: Aspose.Cells for C++ APIを使ったブックの管理方法を学習しましょう。
keywords: C++でブックを管理する方法、ブックとワークシートの管理、C++での操作について。
---

{{% alert color="primary" %}}

Aspose.Cells for C++は、ブックとワークシートの作成、開く、操作のための強力で柔軟なAPIを提供します。ここでは、その方法を説明します。

{{% /alert %}}

## **新しいワークブックの作成**
新しいブックを作成するには：

 1. [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)クラスのインスタンスを作成します。
 2. [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/)クラスを使用してワークシートを追加します。
 3. [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/)メソッドを使用して保存します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook.go" >}}
## **既存のブックを開く**
既存のブックを開くには：

 1. [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)クラスのインスタンスを作成し、ファイルパスをコンストラクタに渡します。
 2. [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/)クラスを使ってワークシートにアクセスします。
3. 必要に応じてブックを編集します。
 4. [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/)メソッドを使用して保存します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-1.go" >}}
## **ワークシートの管理**
Aspose.Cells for C++は、ワークシートの追加、削除、名前変更など、多くの管理方法を提供します。

### **ワークシートの追加**
新しいワークシートを追加するには：

 1. ワークブックから[WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/)クラスにアクセスします。
 2. [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_sheettype/)メソッドを使用して新しいワークシートを追加します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-2.go" >}}
### **ワークシートの削除**
ワークシートを削除するには：

 1. ワークブックから[WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/)クラスにアクセスします。
 2. [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat_string/)メソッドを使用してインデックスでワークシートを削除します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-3.go" >}}
### **ワークシートの名前を変更する**
ワークシートの名前を変更するには：

 1. ワークブックから[Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/)クラスにアクセスします。
 2. [SetName](https://reference.aspose.com/cells/go-cpp/worksheet/setname/)メソッドを使ってワークシートの名前を変更します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-4.go" >}}
## **結論**
Aspose.Cells for C++ は、ワークブックとワークシートの管理に役立つ包括的なツールセットを提供します。新しいワークブックの作成、既存のものを開く、またはワークシートを操作する必要がある場合、Aspose.Cellsを使用してExcelファイルをプログラムで操作するのは簡単です。
