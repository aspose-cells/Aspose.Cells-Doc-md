---
title: ブックでのカスタム番号の小数点とグループの区切り記号を指定する
linktitle: ブックでのカスタム番号の小数点とグループの区切り記号を指定する
type: docs
weight: 110
url: /ja/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Aspose.Cells for Node.js via C++を使用してExcelの数値の小数点と桁区切り記号を変更します。 
keywords: Excelのノード.jsにおいて、カスタム小数点記号や桁区切り記号をC++経由で指定し変更します。
---

{{% alert color="primary" %}}

Microsoft Excelでは、**その他のExcelオプション** から **詳細設定** を使用せずに、カスタムの小数点および千の区切り記号を指定できます。次のスクリーンショットでは、その手順が示されています。

Aspose.Cellsは、[**WorkbookSettings.setNumberDecimalSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberDecimalSeparator-string-)と[**WorkbookSettings.setNumberGroupSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberGroupSeparator-string-)メソッドを提供し、数値のフォーマッティングやパースのためにカスタムセパレータを設定します。

{{% /alert %}}

## **Microsoft Excelを使用してカスタムセパレータを指定する**

次のスクリーンショットは、**詳細設定** タブを示し、**カスタムセパレータ** を指定するセクションを強調しています。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Aspose.Cells for Node.js via C++を使用したカスタムセパレータの指定方法**

次のサンプルコードは、Aspose.Cells APIを使用してカスタムセパレータを指定する方法を示しています。これにより、カスタム数値の10進セパレータとグループセパレータを、それぞれドットとスペースに設定します。

### Node.jsコードによるカスタム数値小数点および桁区切り記号の指定

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-SpecifyCustomNumberDecimalAndGroupSeparators.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
