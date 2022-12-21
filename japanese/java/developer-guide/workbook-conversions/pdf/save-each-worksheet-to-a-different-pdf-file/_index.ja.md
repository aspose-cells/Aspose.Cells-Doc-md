---
title: 各ワークシートを異なる PDF ファイルに保存する
type: docs
weight: 50
url: /ja/java/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}}

Aspose.Cells は、スプレッドシート ファイル (画像、グラフなどを含む) の PDF ドキュメントへの変換をサポートしています。 Aspose.Cells for Java は、スプレッドシートを PDF ドキュメントに変換するために独立して動作することができ、変換に Aspose.PDF for Java を使用する必要がなくなりました。プロセス全体をメモリ内で実行できるため、変換では一時ファイルを作成/使用する必要はありません。

{{% /alert %}}

各ワークシートをテンプレート Excel ファイルに保存して、異なる PDF ファイルを生成する必要がある場合。これは簡単に実現できます。ファイル内のシートを非表示にして、PDF をレンダリングすることに基づいて一度に 1 つのシートを表示しようとする場合があります。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()）スプレッドシートを PDF にレンダリングする直前のメソッド。これにより、式に依存する値が再計算され、正しい値が PDF に表示されます。

{{% /alert %}}
