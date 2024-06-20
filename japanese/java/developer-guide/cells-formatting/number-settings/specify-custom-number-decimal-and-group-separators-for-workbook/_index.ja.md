---
title: ブックでのカスタム番号の小数点とグループの区切り記号を指定する
type: docs
weight: 100
url: /ja/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: この記事では、Aspose.Cells for Java APIを使用してMS Excelで番号の小数点およびグループの区切り記号を変更する方法を示しています。
keywords: エクセルのカスタム小数点セパレータを指定する、エクセルのカスタム小数点セパレータを指定するためのjava、エクセルのカスタムグループセパレータを指定する、エクセルのカスタムグループセパレータを指定するためのjava、エクセルのカスタム小数点およびグループセパレータを指定する、エクセルのカスタム小数点およびグループセパレータを指定するためのjava、エクセルの小数点およびグループセパレータを変更するためのjava、エクセルの小数点およびグループセパレータを変更する、エクセルの小数点セパレータを変更するためのjava、エクセルの小数点セパレータを変更する、エクセルのグループセパレータを変更するためのjava、エクセルのグループセパレータを変更する
---

{{% alert color="primary" %}}

Microsoft Excelでは、**その他のExcelオプション** から **詳細設定** を使用せずに、カスタムの小数点および千の区切り記号を指定できます。次のスクリーンショットでは、その手順が示されています。

Aspose.Cellsは、[**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator)および[WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator)プロパティを提供しており、数値のフォーマット設定/解析のためにカスタムセパレータを設定できます。

{{% /alert %}}

## **Microsoft Excelを使用してカスタムセパレータを指定する**

1. **ファイル** タブで **オプション** を開きます。
1. **詳細設定** タブを開きます。
1. **編集オプション** セクションの設定を変更します。

次のスクリーンショットは、**詳細設定** タブを示し、**カスタムセパレータ** を指定するセクションを強調しています。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Aspose.Cellsを使用してカスタムセパレータを指定する**

次のサンプルコードは、Aspose.Cells APIを使用してカスタムセパレータを指定する方法を示しています。これにより、数字 **123,456.789** が **123 456.789** と表示されるようになります。このスクリーンショットは、そのコードによって生成された出力PDFを示しています。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
