---
title: VBA マクロ UserForm DesignerStorage をテンプレートからターゲット ワークブックにコピーする
type: docs
weight: 60
url: /ja/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **考えられる使用シナリオ**

Aspose.Cells を使用すると、VBA プロジェクトを 1 つの Excel ファイルから別の Excel ファイルにコピーできます。 VBA プロジェクトは、Document、Procedural、Designer などのさまざまなタイプのモジュールで構成されています。すべてのモジュールは単純なコードでコピーできますが、Designer モジュールの場合、アクセスまたはコピーする必要がある Designer Storage と呼ばれる追加データがいくつかあります。次の 2 つの方法は、デザイナー ストレージを処理します。

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String))
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[]))

## **VBA マクロ UserForm DesignerStorage をテンプレートからターゲット ワークブックにコピーする**

以下のサンプルコードをご覧ください。から VBA プロジェクトをコピーします。[テンプレートエクセルファイル](50528367.xlsm)空のワークブックに保存し、[出力エクセルファイル](50528366.xlsm).テンプレートの Excel ファイル内で VBA プロジェクトを開くと、次のようなユーザー フォームが表示されます。ユーザー フォームは Designer Storage で構成されているため、次を使用してコピーされます。[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String)） と[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[])メソッド。

![todo:画像_代替_文章](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

次のスクリーンショットは、テンプレート Excel ファイルからコピーされた出力 Excel ファイルとその内容を示しています。ボタン 1 をクリックすると、クリックするとメッセージ ボックスを表示するコマンド ボタンを持つ VBA ユーザー フォームが開きます。

![todo:画像_代替_文章](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
