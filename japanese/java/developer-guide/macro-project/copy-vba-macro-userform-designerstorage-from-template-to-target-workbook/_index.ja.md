---
title: テンプレートから対象のブックへVBAマクロのUserForm DesignerStorageをコピー
type: docs
weight: 60
url: /ja/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **可能な使用シナリオ**

Aspose.Cellsを使用して、1つのExcelファイルから別のExcelファイルにVBAプロジェクトをコピーできます。VBAプロジェクトにはドキュメント、手続き、デザイナーなどのさまざまなタイプのモジュールが含まれています。すべてのモジュールは簡単なコードでコピーできますが、デザイナーモジュールの場合はアクセスまたはコピーする必要のある追加データがあります。

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-)

## **テンプレートからターゲットワークブックへのVBAマクロUserForm DesignerStorageのコピー**

以下のサンプルコードを参照してください。 これは、[テンプレートExcelファイル](50528367.xlsm) からVBAプロジェクトを空のブックにコピーし、それを [出力Excelファイル](50528366.xlsm) として保存します。 テンプレートExcelファイル内のVBAプロジェクトを開くと、以下のようにユーザーフォームが表示されます。 ユーザーフォームにはデザイナーが含まれていますので、 [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-) メソッドおよび [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-) メソッドを使用してコピーされます。

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

以下のスクリーンショットは、テンプレートExcelファイルからコピーされた出力Excelファイルとその内容を示しています。 **Button 1**をクリックすると、VBAユーザーフォームが開き、そこにはさらにメッセージボックスが表示されます。

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
