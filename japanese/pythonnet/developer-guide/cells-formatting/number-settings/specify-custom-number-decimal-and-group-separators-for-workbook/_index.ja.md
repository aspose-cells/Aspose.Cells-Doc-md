---
title: ブックでのカスタム番号の小数点とグループの区切り記号を指定する
type: docs
weight: 110
url: /ja/python-net/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Aspose.Cells for Python via .NET APIを使用して、MS ExcelとC#コードで数値の小数点およびグループ区切り記号を変更します。
keywords: Excelの 高度なExcelオプション からシステムの区切り記号を使用する代わりに、Microsoft Excelでは、C#コードを使用してカスタムの小数点と千桁の区切り記号を指定できます（例：Aspose.Cells for .NET API）。
---

{{% alert color="primary" %}}

Microsoft Excelでは、**その他のExcelオプション** から **詳細設定** を使用せずに、カスタムの小数点および千の区切り記号を指定できます。次のスクリーンショットでは、その手順が示されています。

Aspose.Cells for Python via .NETは、数値のフォーマット/解析にカスタムセパレーターを設定するための [**WorkbookSettings.number_decimal_separator**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/number_decimal_separator/) と [**WorkbookSettings.number_group_separator**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/number_group_separator/) プロパティを提供します。

{{% /alert %}}

## **Microsoft Excelを使用してカスタムセパレータを指定する**

次のスクリーンショットは、**詳細設定** タブを示し、**カスタムセパレータ** を指定するセクションを強調しています。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Aspose.Cells for Python via .NETを使用したカスタムセパレーターの指定**

以下のサンプルコードは、Aspose.Cells for Python via .NET APIを使ったカスタムセパレーターの指定方法を示しています。これは、カスタムの数値小数点とグループセパレーターをそれぞれドットとスペースに設定しています。

### C#コードでカスタム数値の10進セパレータとグループセパレータを指定

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CustomDecimalAndGroupSeparator.py" >}}

{{< app/cells/assistant language="python-net" >}}
