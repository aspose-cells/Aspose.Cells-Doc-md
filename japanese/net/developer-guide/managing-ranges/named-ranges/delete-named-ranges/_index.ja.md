---
title: 名前付き範囲の削除
type: docs
weight: 90
url: /ja/net/Delete-named-ranges/
description: Aspose.Cells for .Netを使用して、ExcelファイルまたはOpenOfficeファイルから定義された名前や名前付き範囲を削除する方法を学ぶことができます。
---

## **紹介**
Excelファイルに多くの定義名や名前付き範囲がある場合、参照されないためにいくつかをクリアする必要があります。

## **MS Excelで名前付き範囲を削除する**

Excelから名前付き範囲を削除するには、次の手順に従うことができます：
1. Microsoft Excelを開き、名前付き範囲が含まれているワークブックを開きます。
2. Excelリボンの「数式」タブに移動します。
3. 「定義された名前」グループの「名前マネージャー」ボタンをクリックします。これにより名前マネージャーのダイアログボックスが開きます。
4. 名前マネージャーのダイアログボックスで、削除したい名前付き範囲を選択します。
5. 「削除」ボタンをクリックします。プロンプトが表示されたら削除を確認します。
6. 「閉じる」ボタンをクリックして名前マネージャーのダイアログボックスを閉じます。
7. 変更を保存するためにワークブックを保存します。


## **Aspose.Cells for .Netを使用して名前付き範囲を削除する**
Aspose.Cells for .Netを使用すると、[テキスト](https://reference.aspose.com/cells/net/aspose.cells/namecollection/remove/#remove) または[インデックス](https://reference.aspose.com/cells/net/aspose.cells/namecollection/removeat/#removeat)を使用して、名前付き範囲や定義名を削除できます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}

注意：定義された名前が数式によって参照されている場合、削除することはできません。定義名の数式の削除のみ可能です。

## **一部の名前付き範囲を削除する**
定義名を削除する際には、ファイル内のすべての数式によって参照されているかどうかを確認する必要があります。
名前付き範囲を削除のパフォーマンスを改善するために、一緒に何個かを削除することができます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}

## **重複した定義名を削除する**
一部のExcelファイルは、いくつかの定義名が重複しているため壊れています。したがって、これらの重複した名前を削除してファイルを修復できます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}



{{< app/cells/assistant language="csharp" >}}
