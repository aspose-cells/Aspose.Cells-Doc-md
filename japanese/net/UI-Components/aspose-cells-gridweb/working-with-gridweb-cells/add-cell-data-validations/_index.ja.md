---
title: Cell データ検証を追加
type: docs
weight: 90
url: /ja/net/add-cell-data-validations/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb を使用すると、追加できます**データ検証**GridWorksheet.Validations.Add() メソッドを使用します。このメソッドを使用して、指定する必要があります**Cell 範囲**.ただし、単一の GridCell でデータ検証を作成する場合は、GridCell.CreateValidation() メソッドを使用して直接行うことができます。同様に、あなたは削除することができます**データ検証**GridCell.RemoveValidation() メソッドを使用して GridCell から。

{{% /alert %}} 
## **GridWeb の GridCell でデータ検証を作成する**
次のサンプル コードは、**データ検証**セル B3 に20 ～ 40 以外の値を入力すると、セル B3 が表示されます。**検証エラー**の形で**赤XXXX**このスクリーンショットに示すように。

![todo:画像_代替_文章](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
