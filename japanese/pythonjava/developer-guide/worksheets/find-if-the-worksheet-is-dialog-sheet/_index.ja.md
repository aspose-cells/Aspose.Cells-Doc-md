---
title: ワークシートがダイアログ シートかどうかを調べる
type: docs
weight: 70
url: /ja/python-java/find-if-the-worksheet-is-dialog-sheet/
---
## **考えられる使用シナリオ**
ダイアログ シートは、ダイアログ ボックスを含む古い形式のシートです。このようなシートは、このスクリーンショットに示すように、2003 などの古いバージョンの Microsoft Excel で挿入できます。 Microsoft Excel 2016 など、新しいバージョンの VBA で挿入することもできます。

![todo:画像_代替_文章](DialogSheet.png)
## **ワークシートがダイアログ シートかどうかを調べる**
Aspose.Cells for Python via Java は、ワークシートがダイアログ シートであるかどうかを確認する機能を提供します。このために、それは[Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)財産。もしも[Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)列挙値を返します[SheetType.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG)の場合は、ダイアログ シートを扱っていることを意味します。

次のコード スニペットは、ダイアログ シートを確認する方法を示しています。コードによって生成されたコンソール出力を参照用に以下に示します。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **コンソール出力**
ワークシートはダイアログシートです。
