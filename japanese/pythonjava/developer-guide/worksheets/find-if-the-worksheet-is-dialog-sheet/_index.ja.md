---
title: ワークシートがダイアログシートであるかを検索する
type: docs
weight: 70
url: /ja/python-java/find-if-the-worksheet-is-dialog-sheet/
---

## **可能な使用シナリオ**
ダイアログシートは、ダイアログボックスを含むシートの古い形式です。このようなシートは、Microsoft Excel 2003などの古いバージョンによって挿入される場合があります（以下のスクリーンショットで示されています）。また、Microsoft Excel 2016などの最新バージョンではVBAによって挿入することもできます。

![todo:image_alt_text](DialogSheet.png)
## **ワークシートがダイアログシートであるかを検索する**
Aspose.Cells for Python via Java では、ワークシートがダイアログ シートかどうかを確認する機能を提供します。これには、[Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type) プロパティがあります。[Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type) が列挙値 [SheetType.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG) を返す場合、ダイアログ シートが操作対象であることを意味します。

次のコードスニペットには、ダイアログ シートの確認方法が示されています。コードによって生成されるコンソール出力例が以下に示されています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **コンソール出力**
{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
