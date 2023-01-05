---
title: 行ヘッダーと列ヘッダーのカスタマイズ
type: docs
weight: 40
url: /ja/net/customize-row-and-column-headers/
---
{{% alert color="primary" %}} 

Microsoft Excel と同様に、Aspose.Cells.GridWeb も行 (1、2、3 などの数字) と列 (A、B、C などのアルファベット) に標準のヘッダーまたはキャプションを使用します。 Aspose.Cells.GridWeb ではキャプションのカスタマイズも可能です。このトピックでは、Aspose.Cells.GridWeb API を使用して実行時に行ヘッダーと列ヘッダーをカスタマイズする方法について説明します。

{{% /alert %}} 
## **行ヘッダーのカスタマイズ**
行のヘッダーまたはキャプションをカスタマイズするには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. GridWorksheetCollection でワークシートにアクセスします。
1. 指定した行のキャプションを設定します。

**行 1 と 2 のヘッダーはカスタマイズされています** 

![todo:画像_代替_文章](customize-row-and-column-headers_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CustomizeHeaders.aspx-CustomizeRowHeader.cs" >}}
## **列ヘッダーのカスタマイズ**
列のヘッダーまたはキャプションをカスタマイズするには:

1. Aspose.Cells.GridWeb コントロールを Web フォームに追加します。
1. GridWorksheetCollection でワークシートにアクセスします。
1. 指定された列のキャプションを設定します。

**列 1、2、および 3 のヘッダーはカスタマイズされています** 

![todo:画像_代替_文章](customize-row-and-column-headers_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CustomizeHeaders.aspx-CustomizeColumnHeader.cs" >}}
