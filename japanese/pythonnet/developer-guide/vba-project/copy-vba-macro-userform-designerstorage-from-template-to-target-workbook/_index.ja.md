---
title: テンプレートから対象のブックへVBAマクロのUserForm DesignerStorageをコピー
type: docs
weight: 130
url: /ja/python-net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **可能な使用シナリオ**

Aspose.Cells for Python via .NETは、一つのExcelファイルから別のExcelファイルへVBAプロジェクトをコピーすることを可能にします。VBAプロジェクトは、ドキュメント、手続き、デザイナーなど様々なタイプのモジュールで構成されています。すべてのモジュールは簡単なコードでコピー可能ですが、デザイナーモジュールにはDesigner Storageと呼ばれる追加データがあり、これにアクセスまたはコピーが必要です。以下の二つのメソッドは、Designer Storageを扱います。

- [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str)
- [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage/)

## **テンプレートからターゲットワークブックへのVBAマクロUserForm DesignerStorageのコピー**

次のサンプルコードをご覧ください。それは、[テンプレートExcelファイル](50528345.xlsm)からVBAプロジェクトを空のワークブックにコピーし、[出力Excelファイル](50528346.xlsm)として保存します。テンプレートExcelファイル内のVBAプロジェクトを開くと、以下に示すようにUser Formが表示されます。User FormにはDesigner Storageが含まれているため、[**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str)および[**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage)メソッドを使用してコピーされます。

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

以下のスクリーンショットは、テンプレートExcelファイルからコピーされた出力Excelファイルとその内容を示しています。ボタン1をクリックすると、VBAユーザーフォームが開きます。VBAユーザーフォームには、クリックするとメッセージボックスが表示されるコマンドボタンがあります。

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.py" >}}

