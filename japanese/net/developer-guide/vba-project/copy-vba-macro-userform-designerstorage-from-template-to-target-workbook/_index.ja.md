---
title: テンプレートから対象のブックへVBAマクロのUserForm DesignerStorageをコピー
type: docs
weight: 130
url: /ja/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **可能な使用シナリオ**

Aspose.Cellsでは、1つのExcelファイルから別のExcelファイルにVBAプロジェクトをコピーできます。VBAプロジェクトには、Document、Procedural、Designerなどさまざまな種類のモジュールが含まれています。すべてのモジュールは簡単なコードでコピーできますが、DesignerモジュールにはDesigner Storageと呼ばれる追加データが必要です。次の2つのメソッドがDesigner Storageに対応しています。

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **テンプレートからターゲットワークブックへのVBAマクロUserForm DesignerStorageのコピー**

次のサンプルコードをご覧ください。それは、[テンプレートExcelファイル](50528345.xlsm)からVBAプロジェクトを空のワークブックにコピーし、[出力Excelファイル](50528346.xlsm)として保存します。テンプレートExcelファイル内のVBAプロジェクトを開くと、以下に示すようにUser Formが表示されます。User FormにはDesigner Storageが含まれているため、[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)および[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)メソッドを使用してコピーされます。

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

以下のスクリーンショットは、テンプレートExcelファイルからコピーされた出力Excelファイルとその内容を示しています。ボタン1をクリックすると、VBAユーザーフォームが開きます。VBAユーザーフォームには、クリックするとメッセージボックスが表示されるコマンドボタンがあります。

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
{{< app/cells/assistant language="csharp" >}}
