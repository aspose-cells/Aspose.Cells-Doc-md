---
title: 名前付き範囲の削除
type: docs
weight: 90
url: /ja/net/Delete-named-ranges/
description: Aspose.Cells for .Net を使用して、Excel または OpenOffice ファイルから定義名または名前付き範囲を削除する方法を学習できます。
---
##  **導入**
Excel ファイル内に定義された名前または名前付き範囲が多すぎる場合は、それらが再度参照されないようにいくつかをクリアする必要があります。

##  **MS Excel で名前付き範囲を削除する**

Excel から名前付き範囲を削除するには、次の手順に従います。
1. Microsoft Excel を開き、名前付き範囲を含むブックを開きます。
2. Excel リボンの [数式] タブに移動します。
3. 「定義名」グループの「名前マネージャー」ボタンをクリックします。これにより、[名前マネージャー] ダイアログ ボックスが開きます。
4. [名前マネージャー] ダイアログ ボックスで、削除する名前付き範囲を選択します。
5. 「削除」ボタンをクリックします。プロンプトが表示されたら、削除を確認します。
6. [閉じる]ボタンをクリックして、[名前管理]ダイアログ ボックスを閉じます。
7. ワークブックを保存して変更を保存します。


##  ** .Net の Aspose.Cells を使用して名前付き範囲を削除します**
.Net の Aspose.Cells を使用すると、名前付き範囲または定義された名前を削除できます。[文章](https://reference.aspose.com/cells/net/aspose.cells/namecollection/remove/#remove)または[索引](https://reference.aspose.com/cells/net/aspose.cells/namecollection/removeat/#removeat)リストにあります。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}

注: 定義された名前が数式で参照されている場合は、削除できません。削除できるのは定義された名前の式のみです。

##  **一部の名前付き範囲を削除します**
定義された名前を削除するときは、その名前がファイル内のすべての式によって参照されているかどうかを確認する必要があります。
名前付き範囲の削除のパフォーマンスを向上させるために、いくつかをまとめて削除できます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}

##  **重複した定義名の削除**
一部の定義名が重複しているため、一部の Excel フィールドが破損します。したがって、これらの重複した名前を削除してファイルを修復できます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}



