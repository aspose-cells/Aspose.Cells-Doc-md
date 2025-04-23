---
title: HTMLをエクセルブックオブジェクトにロードする際にDIVタグのレイアウトをサポート
type: docs
weight: 50
url: /ja/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}} 

通常、divタグのレイアウトはExcelブックオブジェクトにHTMLをロードする際に無視されます。ただし、divタグのレイアウトが無視されないようにしたい場合は、[HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag)プロパティを**true**に設定してください。このプロパティの既定値は**false**です。

{{% /alert %}} 

次のサンプルコードは、[HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) プロパティの使用法を示しています。入力HTML内で使用されたAsposeロゴ(5115218.png)およびコードによって生成された出力エクセルファイル(5115220.xlsx)をダウンロードしてください。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DivTagsLayout-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
