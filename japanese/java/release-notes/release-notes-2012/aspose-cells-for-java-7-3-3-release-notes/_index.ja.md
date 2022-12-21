---
title: Aspose.Cells for Java 7.3.3 リリースノート
type: docs
weight: 20
url: /ja/java/aspose-cells-for-java-7-3-3-release-notes/
---
{{% alert color="primary" %}} 

このページには、[Aspose.Cells for Java 7.3.3](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.3.3/)

{{% /alert %}} 

私たちです
Aspose.Cells for Java v7.3.3 を発表させていただきます。

新機能

- Row.getLastDataCell() メソッドを追加して、行にデータがある最後のセルを取得します
- 同じスタイル設定を持つセルの同じ Styleobject を取得するための新しい API が追加されました

機能強化

- でCSVをエクスポートするときに空のセル値に引用符を追加します

オプション

例外

- Unicode 文字を使用した条件付き書式が失敗する
- 条件付き書式の領域を追加する前に数式を設定し、ワークシートの名前を変更すると、ブックの保存時にエラーが発生しました
- XLS テンプレート ファイルを再保存すると、NegativeArraySizeException が発生しました

バグ

- 書式設定された日付の値が、MS Excel に表示されているものと異なっていた
- CellCollection がクリアされると、チャート シリーズ名が失われます
- 空白をギャップ/ゼロとして表示すると、XLSX ファイルでは機能しません
- グラフのデータ ラベルの書式設定が正しくない
- レンダリングされた PDF ファイルでフォントの下線が消えた
- フォント スタイルを設定しても、LightCells モードの XLSX では効果がありませんでした
- PDF に保存するとフッターの一部が失われる
