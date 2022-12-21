---
title: Aspose.Cells for Java 7.3.2 リリースノート
type: docs
weight: 30
url: /ja/java/aspose-cells-for-java-7-3-2-release-notes/
---
{{% alert color="primary" %}} 

このページには、[Aspose.Cells for Java 7.3.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.3.2/)

{{% /alert %}} 

私たちです
Aspose.Cells for Java v7.3.2 を発表させていただきます。

新機能

- Shape.getRight()/getBottom() は、セルの右下隅から形状のオフセットを取得します
- ワークシートのタブの色をデフォルトの色に設定

機能強化

- PDF 変換でメモリ リソースを解放するための内部ストリームを閉じる
- ワークシートのコピー時にスパークラインをコピー

例外

- XLSファイルを開くとStackOverflowErrorが発生しました
- PDF の保存中に例外が発生しました
- Worksheet.getFreezedPanes()はNullPointerExceptionを引き起こしました
- 空の XML ファイルを開くと例外が発生しました
- PDF への保存で例外が発生しました -I
- PDF への保存で例外が発生しました -II
- PDF への保存で例外が発生しました -III
- PDF への保存で例外が発生しました -IV
- HTM テンプレート ファイルを開くときの例外
- XLS ファイルを開くときの IllegalArgumentException
- XLSファイルを開くときのNullPointerException
- XLS ファイルを開くときの ArrayIndexOutOfBounds 例外
- 自動並べ替えを設定した後にピボットテーブルを保存すると、ClassCastException が発生しました
- Aspose Cells を使用して PDF を保存するときの形状から画像へのエラー
- グリッド線をPDFに印刷するときのCellsException

バグ

- XLS テンプレートに保存された一部のリージョンは、読み取り時に認識されませんでした
- Chart-to-Image が棒グラフのスケールのレンダリングに失敗する
- XLSX から PDF への変換後のデータ損失
- Cellcollection がクリアされている場合、円グラフと散布図が機能しない
