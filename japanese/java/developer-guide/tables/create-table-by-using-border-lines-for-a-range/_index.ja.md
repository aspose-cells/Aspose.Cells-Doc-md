---
title: 範囲に境界線を使用してテーブルを作成する
type: docs
weight: 50
url: /ja/java/create-table-by-using-border-lines-for-a-range/
description: 境界線を使用して範囲でテーブルを作成する方法 Aspose.Cells for Javaは、範囲に境界線を追加するために使用できる使いやすいAPIを提供しています。
keywords: テーブルを作成し、範囲をテーブルに変換する、範囲をテーブルにエクセル、エクセル範囲をテーブル、境界線を伴う範囲をテーブルに変換する、範囲からテーブルを作成する方法、範囲をテーブルに変換する、エクセル範囲をテーブルに変換する、エクセルでテーブルを作成する、範囲をテーブルに変換するjava 
---

{{% alert color="primary" %}}

時には、持っているセルのアドレスに基づいて**範囲**/**セル領域**に境界線を追加してテーブルを作成したい時があります。[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-)メソッドを使用してセルの範囲を作成することができます。[**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-)メソッドは[**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)オブジェクトを返します。[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)オブジェクトを作成し、ボーダー（上、左、下、右）のオプションを指定します。後で、[**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)のセルを取得し、セルに所望の書式を適用することができます。

{{% /alert %}}

以下の例では、[**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)を作成し、範囲セルに境界線を指定する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

上記のコードを実行すると、書式付きのテーブルを含む生成されたExcelファイルを取得できます。ファイルのスクリーンショットは以下の通りです。

![todo:image_alt_text](create-table-by-using-border-lines-for-a-range_1.png)
{{< app/cells/assistant language="java" >}}
