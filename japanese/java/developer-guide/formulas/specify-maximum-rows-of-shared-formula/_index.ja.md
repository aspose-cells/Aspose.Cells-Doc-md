---
title: 共有式の最大行数を指定
type: docs
weight: 40
url: /ja/java/specify-maximum-rows-of-shared-formula/
---

## **可能な使用シナリオ**

共有数式のデフォルトの最大行数は64です。これは1000などの任意の数値にできます。共有数式のパフォーマンスは、行数の異なる数で変化します。そのため、Aspose.Cellsは共有数式の最大行数を指定するのに使用できる [0] プロパティを提供しています。共有数式は、共有数式の総行数がそれよりも大きい場合、次のスクリーンショットに示されているように、複数の共有数式に分割されます。

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **共有式の最大行数を指定**

以下のサンプルコードは、[出力Excelファイル](61767869.xlsx)に100行の共有数式をセルD1に追加し、共有数式の最大行数を5に設定して保存する方法を説明しています。出力Excelファイルの内容を抽出して、*sheet1.xml*をチェックすると、上記のスクリーンショットでハイライトされた部分の後に共有数式が分割されているのが見えます。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
{{< app/cells/assistant language="java" >}}
