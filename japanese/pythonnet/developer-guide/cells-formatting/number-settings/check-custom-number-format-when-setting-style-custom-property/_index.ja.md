---
title: スタイル.Customプロパティを設定する際にカスタム番号書式をチェックする
description: Aspose.Cellsは、スプレッドシートファイルを操作するためのPythonライブラリで、スタイル設定時のカスタム数字書式の確認をサポートします。この記事では、Aspose.Cellsライブラリを使ってカスタム数字書式を確認し、スタイルが正しいかどうかを確かめる方法を紹介します。
keywords: Aspose.Cells、Pythonライブラリ、スプレッドシート、スタイリング、カスタム数値書式設定、チェック、検証
type: docs
weight: 170
url: /ja/python-net/check-custom-number-format-when-setting-style-custom-property/
---

## **可能な使用シナリオ**

[**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom)プロパティに無効なカスタム番号形式を割り当てた場合、Aspose.Cellsは例外をスローしません。ただし、Aspose.Cellsに割り当てたカスタム番号形式が有効かどうかをチェックする場合は、[**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/)プロパティを**true**に設定してください。

## **スタイルのカスタムプロパティを設定する際のカスタム番号形式をチェック**

次のサンプルコードは、[**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom)プロパティに無効なカスタム番号形式を割り当てます。すでに[**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/)プロパティを**true**に設定しているため、例外（無効な番号形式など）がスローされます。詳細についてはコード内のコメントをお読みください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CheckCustomFormatPattern.py" >}}

