---
title: Golangを使用したC++で名前付き範囲を削除
linktitle: 名前付き範囲の削除
type: docs
weight: 90
url: /ja/go-cpp/delete-named-ranges/
description: Aspose.Cells for C++を使用してExcelまたはOpenOfficeファイルから定義された名前や名前付き範囲を削除する方法を学びます。
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

## **Aspose.Cells for C++を使用した名前付き範囲の削除**
Aspose.Cells for C++を使えば、リスト内の[テキスト](https://reference.aspose.com/cells/go-cpp/namecollection/remove_stringarray/)または[インデックス](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/)で名前付き範囲や定義済み名前を削除できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges.go" >}}
注意：定義された名前が数式で参照されている場合は削除できません。定義された名前の数式のみ削除可能です。

## **一部の名前付き範囲を削除する**
定義名を削除する際には、ファイル内のすべての数式によって参照されているかどうかを確認する必要があります。
名前付き範囲を削除するパフォーマンスを向上させるために、一部をまとめて削除できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges-1.go" >}}
## **重複した定義名を削除する**
定義された名前が重複しているためにExcelファイルが壊れることがあります。これらの重複した名前を削除してファイルを修復できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges-2.go" >}}
