---
title: DBNumのカスタムパターン書式を指定する
linktitle: DBNumのカスタムパターン書式を指定する
description: Aspose.Cellsは、C++経由のNode.js向けライブラリで、カスタムフォーマットパターンを使用した日付と数値の書式設定をサポートします。この記事では、「dbnum」カスタム書式パターンを指定して数値の表示制御を向上させる方法を示します。
keywords: Aspose.Cells、Node.js（C++経由）、電子スプレッドシート、カスタムフォーマットパターン、フォーマット設定、「dbnum」、表示制御
type: docs
weight: 110
url: /ja/nodejs-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **可能な使用シナリオ**

Aspose.Cells for Node.js via C++は「*DBNum*」カスタムパターンフォーマットをサポートします。たとえば、セルの値が123の場合、「[DBNum2][$-804]General」などのカスタムフォーマットを指定すると、「壹佰贰拾叁」のように表示されます。セルのカスタムフォーマットは、[**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--)メソッドや[**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-)メソッドを使用して指定できます。

## **サンプルコード**

以下のサンプルコードは、「*DBNum*」カスタムパターンの書式設定を指定する方法を示しています。[出力PDF](43352081.pdf)もご確認ください。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-SpecifyDBNumCustomPattern.js" >}}

