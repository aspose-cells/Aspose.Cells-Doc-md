---
title: ワークシート内の図形を前面または背面に送る（Golang + C++）
linktitle: ワークシート内でShape FrontまたはBackを送信する
type: docs
weight: 3400
url: /ja/go-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Aspose.Cells for C++を利用して、ワークシート内の図形のz順位置を変更する方法を学びます。
---

## **可能な使用シナリオ**

同一位置に複数の図形が存在する場合、その表示順はz順位置によって決まります。Aspose.Cellsは[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/)メソッドを提供し、これを使って図形のz順位置を変更します。図形を背面に送るには-1、-2、-3のような負の数を、前面に持ち上げるには1、2、3のような正の数を使います。

## **ワークシート内でShape FrontまたはBackを送信する**

以下のサンプルコードは[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/)メソッドの使用例です。コードで使用されている[サンプルExcelファイル](50528330.xlsx)と、それによって生成された[出力Excelファイル](50528331.xlsx)を参照してください。スクリーンショットは、コード実行後のサンプルExcelファイルの効果を示しています。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SendShapeFrontOrBackInsideTheWorksheet.go" >}}
