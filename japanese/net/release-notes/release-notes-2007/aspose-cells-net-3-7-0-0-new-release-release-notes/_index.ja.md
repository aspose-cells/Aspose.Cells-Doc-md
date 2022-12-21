---
title: Aspose.Cells .Net 3.7.0.0 新しいリリース リリース ノート
type: docs
weight: 170
url: /ja/net/aspose-cells-net-3-7-0-0-new-release-release-notes/
---
{{% alert color="primary" %}} 

このページには、[Aspose.Cells .Net 3.7.0.0 新しいリリース](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-.net-3.7.0.0-new-release/)

{{% /alert %}} 

お客様各位

Aspose.Cells 3.7 for .NETをリリースしました！

名前の変更

 Aspose.Excel は Aspose.Cells に名前が変更されました。

 Aspose.Excel からアップグレードする場合は、Aspose.Excel.dll への参照を削除し、Aspose.Cells.dll への参照を追加する必要があります。また、コード内のすべての「使用」または「インポート」名前空間 Aspose.Excel を Aspose.Cells に変更する必要があります。



エディション タイプの変更

以前は、Professional と Enterprise の 2 つのエディション タイプがありました。これは、1 つのエディション タイプの Professional に変更されました。

Professional エディションには、Enterprise エディションで利用可能だったすべての機能が含まれるようになりました。 Professional エディションをお持ちのお客様は、アップグレード時に Enterprise エディションで利用可能だったすべての機能にアクセスできます。


## **新機能**
- WinForm のデモは、インストール パッケージに含まれています。
パフォーマンスとメモリ使用量が最適化されます。



修正

- AutoFitColumn メソッドを何度も呼び出すと、StackOverflowException が発生する場合があります。
多くの数式を含むファイルを保存する際のバグ
Excel ファイルから SpreadsheetML ファイルへの変換における名前付き範囲およびその他の問題
行と列のスタイル設定
チャート数値軸数値フォーマット設定
コメントでスカンジナビア文字を読む
数式を計算するときのセルの再帰参照エラー


