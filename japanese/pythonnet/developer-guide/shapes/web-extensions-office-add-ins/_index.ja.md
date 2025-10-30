---
title: Web拡張機能  Officeアドイン
type: docs
weight: 130
url: /ja/python-net/web-extensions-office-add-ins/
---

Web拡張機能は、Officeアプリケーションを拡張し、Office文書のコンテンツとやり取りします。Web拡張機能は、ユーザーエクスペリエンスと生産性を向上させるためにOfficeクライアントに追加機能を提供します。

Aspose.Cells for Python via .NETは、Web拡張機能の操作もサポートしています。

## **Web拡張機能の追加**

ExcelにWeb拡張機能（Officeアドイン）を追加するには、**挿入**タブをクリックしてから**ストア**/**アドインの取得**リンクをクリックします。アドインボックスで、追加したいアドインを参照して追加してください。

Aspose.Cells for Python via .NETは、[**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension)と[**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane)クラスを使ってWeb拡張機能を追加できる機能も提供しています。以下のコードサンプルは、[**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension)と[**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane)クラスを使ってExcelファイルにWeb拡張を追加する例です。コードによって生成された[出力Excelファイル](89849869.xlsx)も参照してください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AddWebExtension-1.py" >}}

## **Web拡張機能情報へのアクセス**

Aspose.Cells for Python via .NETは、Excelファイル内のWeb拡張の情報にアクセスする機能も提供しています。以下のサンプルコードでは、[サンプルExcelファイル](89849870.xlsx)をロードしてWeb拡張の情報にアクセスする方法を示します。結果として得られるコンソール出力も参考にしてください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AccessWebExtensionInformation-1.py" >}}

### **コンソール出力**

{{< highlight java >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
