---
title: ファイルの保存
type: docs
weight: 20
url: /ja/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells を使用すると、ファイルの作成と保存、および既存のファイルの操作が可能になります。この記事では、ファイルを保存するさまざまな方法について説明します。

{{% /alert %}} 
##  **ファイルを保存するさまざまな方法**
 Aspose.Cells は、[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)これは Microsoft Excel ファイルを表し、Excel ファイルを操作するために必要なメソッドを提供します。の[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスが提供するのは、[保存](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Excel ファイルを保存するために使用されるメソッド。の[保存](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドには、さまざまな方法でファイルを保存するために使用される多くのオーバーロードがあります。ファイルが保存されるファイル形式は、[保存形式](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)列挙。
##  **ファイルを任意の場所に保存する**
ファイルを保管場所に保存するには、ファイル名 (保管パスを含む) と希望のファイル形式 (ファイル形式から指定) を指定します。[保存形式](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)列挙型) を呼び出すとき[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)オブジェクトの[保存](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


##  **ファイルをストリームに保存する**
ファイルをストリームに保存するには、MemoryStream または FileStream オブジェクトを作成し、メソッドを呼び出してファイルをそのストリーム オブジェクトに保存します。[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)オブジェクトの[保存](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法。を使用して希望のファイル形式を指定します。[保存形式](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)を呼び出すときの列挙[保存](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}
