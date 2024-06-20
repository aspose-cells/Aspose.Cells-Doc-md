---
title: セルデータの検証を追加する
type: docs
weight: 90
url: /ja/net/aspose-cells-gridweb/add-cell-data-validations/
keywords: GridWeb,検証,データ検証,グリッド検証
description: この記事では、GridWebでデータ検証（GridValidation）を追加する方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWebを使用して、GridWorksheet.Validations.Add()メソッドを使用して**データ検証**を追加することができます。このメソッドを使用すると、**セル範囲**を指定する必要があります。ただし、単一のGridCellにデータ検証を作成したい場合は、GridCell.CreateValidation()メソッドを直接使用できます。同様に、GridCell.RemoveValidation()メソッドを使用して、GridCellから**データ検証**を削除することもできます。

{{% /alert %}} 
## **GridWebのGridCellにデータの妥当性を作成する**
次のサンプルコードは、セルB3に**データの妥当性**を作成します。20から40の範囲外の値を入力すると、このスクリーンショットに示されているように、セルB3に**バリデーションエラー**が**赤のXXXX**の形で表示されます。

![todo:image_alt_text](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
