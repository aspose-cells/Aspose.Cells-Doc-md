---
title: Linuxにフォントをインストールする方法
type: docs
description: "Linuxにフォントをインストールする方法"
weight: 139
url: /ja/net/how-to-install-font-in-linux/
---

## 概要

Aspose.CellsをLinuxで使用する場合、Linuxはデフォルトのフォントが少ないため、Excelファイルで参照されているフォントがLinuxシステムに存在しない場合があります。
この場合、Aspose.Cellsは類似のフォントを使って文字を表示します。ただし、次のような影響があります：

1. 異なるフォントにより、Excelとは異なるレイアウトで画像がレンダリングされる可能性があります。
2. フォントが変わったために、出力される文字が満足のいくものにならない可能性があります。

より正確な結果を得るために、Linuxに必要なフォントをインストールしてください。Excelファイルで使用するフォントはあなたの環境に存在していることを確認することが重要です。

## Linuxにフォントをインストールする方法

Linuxにフォントをインストールする方法は以下の二つです：

### フォントファイルをLinuxシステムのパスにコピーする

1. プログラムディレクトリに「fonts」というフォルダを作成し、その中に必要なフォントファイルをコピーします。
2. Linux Dockerfileに以下のコマンドを追加します：
```
COPY fonts/ /usr/share/fonts
```
3. これらの操作後、フォントファイルはLinuxシステムのパスにコピーされ、Aspose.Cellsがそのパスを参照して利用します。このシナリオを推奨します。

### Aspose.Cells APIを使用してフォントフォルダを設定
場合によっては、Linuxシステムディレクトリを制御または変更できないことがあります。例としてクラウドサーバーがあります。この場合、第二のシナリオを使用できます。
1. プログラムディレクトリに「fonts」というフォルダを作成し、その中に必要なフォントファイルをコピーします。
2. プログラムコード内で、Aspose.Cells APIを呼び出します：
```
Aspose.Cells.FontConfigs.SetFontFolder("fonts", true);
```
3. この操作により、プログラムはプロジェクトパスからフォントを見つけることができるようになります。

## 関連項目

- [Aspose.Cells for .Net6の実行方法](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
