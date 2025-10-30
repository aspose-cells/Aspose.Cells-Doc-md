---
title: スタイル.Customプロパティを設定する際にカスタム番号書式をチェックする
linktitle: スタイル.Customプロパティを設定する際にカスタム番号書式をチェックする
description: Aspose.Cellsは、スプレッドシートファイルを操作するためのNode.jsライブラリであり、スタイリング時のカスタム数字書式の確認をサポートします。この記事では、スタイリングの正確性を保証するために、カスタム数字書式を確認する方法を紹介します。
keywords: Aspose.Cells、Node.jsライブラリ、スプレッドシート、スタイリング、カスタム数字書式、確認、検証
type: docs
weight: 170
url: /ja/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **可能な使用シナリオ**

無効なカスタム数字フォーマットを[**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-)メソッドに割り当てても、Aspose.Cells for Node.js via C++は例外をスローしません。ただし、Aspose.Cellsに割り当てたカスタム数字フォーマットが有効かどうかを確認したい場合は、[**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-)メソッドを**true**に設定してください。

## **Style.setCustom(string)メソッドにおけるカスタム数字フォーマットの検証**

以下のサンプルコードは、不正なカスタム数値フォーマットを[**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-)メソッドに割り当てる例です。既に[**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-)メソッドを**true**に設定しているため、例外（例：無効な数値フォーマット）がスローされます。コード内のコメントを参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-CheckCustomNumberFormat.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
