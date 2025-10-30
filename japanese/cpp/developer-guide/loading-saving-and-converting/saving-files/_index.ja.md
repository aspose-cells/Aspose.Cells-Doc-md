---
title: ファイルの保存
type: docs
weight: 20
url: /ja/cpp/saving-files/
---

{{% alert color="primary" %}} 

Aspose.Cellsを使用すると、ファイルの作成や保存、既存のファイルの操作が可能になります。この記事では、ファイルを保存するさまざまな方法について説明します。

{{% /alert %}} 
## **ファイルを保存する異なる方法**
Aspose.CellsはMicrosoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)を提供し、Excelファイルと操作するために必要なメソッドを提供します。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスはExcelファイルを保存するために使用される[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドを提供します。[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドには、ファイルをさまざまな方法で保存するための多くのオーバーロードがあります。ファイルの保存形式は[SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)列挙型によって決定されます。
## **ファイルを任意の場所に保存する**
ファイルを保存するには、[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)オブジェクトの[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドを呼び出す際に、ファイル名（ストレージパスを含む）と[SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)列挙型から望ましいファイル形式を指定します。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


## **ストリームにファイルを保存する**
ファイルをストリームに保存するには、MemoryStreamまたはFileStreamオブジェクトを作成し、[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)オブジェクトの[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドを呼び出してそのストリームオブジェクトにファイルを保存します。[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドを呼び出す際に、[SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)列挙型を使用して望ましいファイル形式を指定します。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}

## **PDFにファイルを保存する**
希望するコンテンツを PDF ファイルとして保存するために Aspose.Cells for C++ ライブラリを使用する方法について説明されています。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) オブジェクトを作成するか、既存の Excel ファイルを読み込んで [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) オブジェクトを構築し、[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) メソッドを呼び出してファイルを PDF に保存します。Save メソッドを呼び出す際には、[SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 列挙型を使用して希望するファイル形式を指定します。


{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToPdf-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
