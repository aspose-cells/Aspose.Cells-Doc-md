---
title: ワークシートがダイアログシートであるかを検索する
type: docs
weight: 90
url: /ja/python-net/find-if-the-worksheet-is-dialog-sheet/
description: Dialogシートは古い形式のシートです。この記事では、エクセルのワークシートがDialogシートかどうかをプログラムで確認するための手順とサンプルコードをAspose.Cells for Python via .NETライブラリを使用して提供します。
keywords: Python Excelライブラリ、PythonでExcelワークシートのダイアログタイプを見つける方法、Pythonでのワークシートダイアログ表示。
---

## **可能な使用シナリオ**

可能な使用シナリオ

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Aspose.Cells for Python via .NETが提供する[**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/)プロパティを使用して、シートがダイアログシートか他のタイプのシートかどうかを確認できます。列挙値[**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/)を返す場合は、ダイアログシートを扱っていることを示します。

## **ワークシートがダイアログシートであるかを検索する**

[サンプルExcelファイル](64716820.xlsx)を読み込み、ダイアログシートを含むかどうかをチェックし、[**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/)プロパティをチェックして[**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/)と比較し、メッセージを表示します。サンプルコードのコンソール出力も参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}

## **コンソール出力**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
