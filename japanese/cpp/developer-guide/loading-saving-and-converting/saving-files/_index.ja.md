---
title: ファイルの保存
type: docs
weight: 20
url: /ja/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells を使用すると、ファイルの作成と保存、および既存のファイルの操作が可能になります。この記事では、ファイルを保存するさまざまな方法について説明します。

{{% /alert %}} 
## **ファイルを保存するさまざまな方法**
Aspose.Cells は[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)これは Microsoft Excel ファイルを表し、Excel ファイルを操作するために必要なメソッドを提供します。の[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラスが提供する[セーブ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)Excelファイルを保存するために使用される方法。の[セーブ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)メソッドには、さまざまな方法でファイルを保存するために使用される多くのオーバーロードがあります。ファイルが保存されるファイル形式は、[SaveFormat](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)列挙。
## **ファイルをある場所に保存する**
ファイルを保存場所に保存するには、ファイル名 (保存パスを含む) と目的のファイル形式 ([SaveFormat](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)列挙) を呼び出すとき[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)オブジェクトの[セーブ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation.cpp" >}}


## **ストリームへのファイルの保存**
ファイルをストリームに保存するには、MemoryStream または FileStream オブジェクトを作成し、 を呼び出してファイルをそのストリーム オブジェクトに保存します。[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)オブジェクトの[セーブ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)方法。を使用して目的のファイル形式を指定します。[SaveFormat](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)を呼び出すときの列挙[セーブ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream.cpp" >}}
