---
title: ワークシートがダイアログシートであるかを検索する
type: docs
weight: 90
url: /ja/net/find-if-the-worksheet-is-dialog-sheet/
description: ダイアログシートは、シートの古い形式です。この記事では、C# APIまたは.NETライブラリを使用して、Excelワークシートがダイアログシートであるかどうかをプログラムで判断するための手順とサンプルコードを提供します。
keywords: Excelワークシートのダイアログタイプを検索する
---

## **可能な使用シナリオ**

可能な使用シナリオ

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Aspose.Cellsが提供する[**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)プロパティを使用して、シートがダイアログシートであるかどうかを見分けることができます。列挙値[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype)が返された場合、ダイアログシートであることがわかります。

## **ワークシートがダイアログシートであるかを検索する**

[サンプルExcelファイル](64716820.xlsx)を読み込み、ダイアログシートを含むかどうかをチェックし、[**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)プロパティをチェックして[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype)と比較し、メッセージを表示します。サンプルコードのコンソール出力も参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **コンソール出力**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
