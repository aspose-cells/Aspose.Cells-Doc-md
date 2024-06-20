---
title: 複数のドキュメントにフッターを追加する
type: docs
weight: 80
url: /ja/sharepoint/add-footer-to-multiple-documents/
---

複数のExcelファイルにフッターを追加する場合は、リボンバーで「Aspose.Cellsでフッターを追加」オプションを選択してください。

![todo:image_alt_text](add-footer-to-multiple-documents_1.png)



データソースフォルダからすべてのExcelファイルを取得し、ファイルリストテーブルを作成します。

フッターを追加する必要があるファイルを選択し、**フッターを追加**ボタンをクリックして選択したファイルにフッターを追加します。 

![todo:image_alt_text](add-footer-to-multiple-documents_2.png)



フッター追加の設定中には次のオプションが利用可能です:

**セクション**

フッター位置を追加: 左セクション、中央セクション、右セクション。

**フッタースクリプト**

It represents Footer formatting script. Script commands: Command | Description| &P Current page number| &N Page count|&D Current date| &T Current time &A Sheet name &F File name without path &"<FontName>" Font name, for example: &"Arial" &"<FontName>, <FontStyle>" Font name and font style, for example: &"Arial,Bold" &<FontSize> Font size. If this command is followed by a plain number to be printed in the header, it will be separated from the font height with a space character. &G Image script For example: "&Arial,Bold&8Footer Note".
