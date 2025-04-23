---
title: ブックでのカスタム番号の小数点とグループの区切り記号を指定する
type: docs
weight: 110
url: /ja/net/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Aspose.Cells for .NETAPIを使用して、MS Excelで数値の小数点とグループの区切り記号を変更する。
keywords: Excelの 高度なExcelオプション からシステムの区切り記号を使用する代わりに、Microsoft Excelでは、C#コードを使用してカスタムの小数点と千桁の区切り記号を指定できます（例：Aspose.Cells for .NET API）。
---

{{% alert color="primary" %}}

Microsoft Excelでは、**その他のExcelオプション** から **詳細設定** を使用せずに、カスタムの小数点および千の区切り記号を指定できます。次のスクリーンショットでは、その手順が示されています。

Aspose.Cellsは、数値のフォーマット/解析のためにカスタムセパレータを設定するための[**WorkbookSettings.NumberDecimalSeparator**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/numberdecimalseparator)と[**WorkbookSettings.NumberGroupSeparator**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/numbergroupseparator)プロパティを提供します。

{{% /alert %}}

## **Microsoft Excelを使用してカスタムセパレータを指定する**

次のスクリーンショットは、**詳細設定** タブを示し、**カスタムセパレータ** を指定するセクションを強調しています。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Aspose.Cellsを使用してカスタムセパレータを指定する**

次のサンプルコードは、Aspose.Cells APIを使用してカスタムセパレータを指定する方法を示しています。これにより、カスタム数値の10進セパレータとグループセパレータを、それぞれドットとスペースに設定します。

### C#コードでカスタム数値の10進セパレータとグループセパレータを指定

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CustomDecimalAndGroupSeparator-CustomDecimalAndGroupSeparator.cs" >}}
{{< app/cells/assistant language="csharp" >}}
