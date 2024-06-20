---
title: ExcelまたはOpenOfficeにハイパーリンクを挿入する
linktitle: ハイパーリンクの管理
type: docs
weight: 45
url: /ja/python-net/insert-hyperlinks-to-excel/
description: MS Excel なしに Aspose.Cells for Python via .NET ライブラリを使用して Excel ファイルにハイパーリンクを挿入する方法
keywords: Python Excel ライブラリ、Python にハイパーリンクを挿入、Python にハイパーリンクを追加、Python に URL へのリンクを挿入、Python にセルへのリンクを挿入、外部ファイルへのリンクを追加
---

{{% alert color="primary" %}} 

ハイパーリンクは、2つのエンティティ間のリンクを作成するために使用されます。特にウェブサイトを含め、誰もがハイパーリンクの使用に慣れています。
Aspose.Cells for Python via .NETを使用すると、開発者はMicrosoft Excelファイルでさまざまな種類のハイパーリンクを作成できます。このトピックでは、Aspose.Cells for Python via .NETでサポートされているハイパーリンクの種類とExcelファイルでの使用方法について説明します。

{{% /alert %}} 
## **ハイパーリンクの追加方法**
Aspose.Cells for Python via .NETを使用すると、開発者はAPIまたはデザイナースプレッドシート（ハイパーリンクが手動で作成され、その後Aspose.Cells for Python via .NETを使用して他のスプレッドシートにインポートされるスプレッドシート）を使用して、Excelファイルにハイパーリンクを追加できます。

Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を提供します。[Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[WorksheetCollection](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)が含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。[Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスには、Excelファイルに異なるハイパーリンクを追加するためのさまざまなメソッドが提供されています。

## **URLへのリンクの追加方法**
[Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスには、[hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)コレクションが含まれています。[hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)コレクションの各アイテムは[Hyperlink](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink)を表します。[hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)コレクションの[add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str)メソッドを呼び出すことで、URLへのハイパーリンクを追加できます。

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、URLアドレス。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToURL-1.py" >}}

{{% alert color="primary" %}} 

上記の例では、空のセル**A1**にURLへのハイパーリンクが追加されます。このような場合、セルが空の場合、URLアドレスもその空のセルの値として追加されます。セルが空でない場合は、ハイパーリンクが追加されても、セルの値はプレーンテキストのように見えます。それをハイパーリンクのように見えるようにするには、そのセルに適切な書式設定を適用します。

{{% /alert %}} 

## **同じファイル内のセルへのリンクの追加方法**
同じExcelファイルのセルにハイパーリンクを追加することができます。[hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)コレクションの[add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str)メソッドは、内部および外部ハイパーリンクの両方に対して機能します。

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、対象セルのアドレス。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToAnotherCell-1.py" >}}

## **外部ファイルへのリンクの追加方法**
外部のExcelファイルにハイパーリンクを追加することができます。[hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)コレクションの[add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str)メソッドは、以下のパラメータを取ります。

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
 - URL、対象のアドレス、外部のExcelファイル。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToExternalFile-1.py" >}}

## **高度なトピック**
- [画像ハイパーリンクを追加する](/cells/ja/python-net/add-image-hyperlinks/)
- [ハイパーリンクのタイプの検出](/cells/ja/python-net/detect-hyperlink-type/)
- [ワークシートのハイパーリンクの編集](/cells/ja/python-net/editing-hyperlinks-of-worksheet/)
- [範囲内のハイパーリンクを取得](/cells/ja/python-net/get-hyperlinks-in-range/)

