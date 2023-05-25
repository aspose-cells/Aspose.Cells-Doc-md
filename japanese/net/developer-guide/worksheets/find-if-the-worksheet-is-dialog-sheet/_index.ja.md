---
title: ワークシートがダイアログシートかどうかを確認する
type: docs
weight: 90
url: /ja/net/find-if-the-worksheet-is-dialog-sheet/
description: ダイアログシートは古い形式のシートです。この記事では、C# API または .NET ライブラリを使用して、Excel ワークシートがダイアログ シートであるかどうかをプログラム的に判断する手順とサンプル コードを説明します。
keywords: find excel worksheet dialog type c#, worksheet dialog c#
---
##  **考えられる使用シナリオ**

ダイアログ シートは、ダイアログ ボックスを含むシートの古い形式です。このスクリーンショットに示すように、このようなシートは Microsoft Excel の古いバージョン (例: 2003) で挿入できます。新しいバージョン (Microsoft Excel 2016 など) では VBA を使用して挿入することもできます。

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

シートがダイアログ シートであるか、他のタイプのシートであるかを確認するには、[**ワークシートの種類**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)Aspose.Cells によって提供されるプロパティ。列挙値を返す場合[**シートタイプダイアログ**](https://reference.aspose.com/cells/net/aspose.cells/sheettype)、つまり、ダイアログ シートを扱っていることになります。

##  **ワークシートがダイアログシートかどうかを確認する**

次のサンプルコードは、[サンプル Excel ファイル](64716820.xlsx)ダイアログ シートが含まれています。チェックするのは、[**ワークシートの種類**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)プロパティはそれを比較します[**シートタイプダイアログ**](https://reference.aspose.com/cells/net/aspose.cells/sheettype)そしてメッセージを出力します。詳細については、以下のサンプル コードのコンソール出力を参照してください。

##  **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

##  **コンソール出力**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
