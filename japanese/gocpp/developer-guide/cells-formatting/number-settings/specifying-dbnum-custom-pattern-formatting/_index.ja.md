---
title: C++経由でGolangによるDBNumカスタムパターン書式設定
linktitle: DBNumのカスタムパターン書式を指定する
description: Aspose.Cellsは、カスタム書式パターンを使用して日付と数値の書式設定をサポートするC++用のスプレッドシート操作ライブラリです。この記事では、Aspose.Cellsライブラリを使用して「dbnum」のカスタム書式パターンを指定し、ユーザーが数値の表示方法をより細かく制御できるようにします。
keywords: Aspose.Cells、C++ライブラリ、電子スプレッドシート、カスタム書式パターン、書式設定、「dbnum」、表示制御
type: docs
weight: 110
url: /ja/go-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **可能な使用シナリオ**

Aspose.Cellsは*DBNum*カスタムパターン書式設定をサポートしています。例：セルの値が123の場合、カスタム書式を[DBNum2][$-804]Generalと指定すると、「壹佰贰拾叁」と表示されます。セルのカスタム書式は[**Cell.GetStyle()**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/)メソッドと[**Style.Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/)プロパティを使用して指定できます。

## **サンプルコード**

以下のサンプルコードは、「*DBNum*」カスタムパターンの書式設定を指定する方法を示しています。[出力PDF](43352081.pdf)もご確認ください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingDbnumCustomPatternFormatting.go" >}}
