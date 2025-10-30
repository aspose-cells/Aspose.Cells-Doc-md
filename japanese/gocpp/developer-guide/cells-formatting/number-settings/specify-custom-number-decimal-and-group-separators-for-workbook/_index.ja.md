---
title: GolangとC++を使用してブックのカスタム数字小数点と桁区切り記号を指定
linktitle: カスタムの小数点と桁区切りセパレーターを指定する
type: docs
weight: 110
url: /ja/go-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Aspose.Cells for C++ APIを使用したMS ExcelとGolangでの数字の小数点と桁区切り記号の変更
keywords: Excelでカスタム小数点セパレーターを指定、C++でのExcelカスタム小数点セパレーター指定、Excelのカスタム桁区切りセパレーター指定、C++でのExcelカスタム桁区切りセパレーター指定、Excelの小数点と桁区切りセパレーターをカスタマイズ、C++でのExcelの小数点と桁区切りセパレーターの変更、Excelの小数点と桁区切りセパレーターの変更、Excelの小数点セパレーターの変更、C++でのExcelの小数点セパレーターの変更、Excelの桁区切りセパレーターの変更、C++でのExcelの桁区切りセパレーターの変更
---

{{% alert color="primary" %}}

Microsoft Excelでは、**その他のExcelオプション** から **詳細設定** を使用せずに、カスタムの小数点および千の区切り記号を指定できます。次のスクリーンショットでは、その手順が示されています。

Aspose.Cellsは、数値のフォーマット/解析のためにカスタムセパレータを設定するための[**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getnumberdecimalseparator/)と[**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/)プロパティを提供します。

{{% /alert %}}

## **Microsoft Excelを使用してカスタムセパレータを指定する**

次のスクリーンショットは、**詳細設定** タブを示し、**カスタムセパレータ** を指定するセクションを強調しています。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Aspose.Cellsを使用してカスタムセパレータを指定する**

次のサンプルコードは、Aspose.Cells APIを使用してカスタムセパレータを指定する方法を示しています。これにより、カスタム数値の10進セパレータとグループセパレータを、それぞれドットとスペースに設定します。

### C++コードでカスタムの小数点と桁区切りセパレーターを指定する

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyCustomNumberDecimalAndGroupSeparatorsForWorkbook.go" >}}
