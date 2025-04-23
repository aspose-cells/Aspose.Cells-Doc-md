---
title: Web拡張機能  Officeアドイン
type: docs
weight: 130
url: /ja/net/web-extensions-office-add-ins/
---

Web拡張機能は、Officeアプリケーションを拡張し、Office文書のコンテンツとやり取りします。Web拡張機能は、ユーザーエクスペリエンスと生産性を向上させるためにOfficeクライアントに追加機能を提供します。

Aspose.CellsもWeb拡張機能と連携する機能を提供しています。

## **Web拡張機能の追加**

ExcelにWeb拡張機能（Officeアドイン）を追加するには、**挿入**タブをクリックしてから**ストア**/**アドインの取得**リンクをクリックします。アドインボックスで、追加したいアドインを参照して追加してください。

Aspose.Cellsは、[**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension)および[**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane)クラスを使用してWeb拡張機能を追加する機能も提供します。次のコードサンプルでは、[**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension) および[**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane) クラスを使用してExcelファイルにWeb拡張機能を追加する方法を示しています。参照のために生成されたコードによって[output Excelファイル](89849869.xlsx)をご覧ください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddWebExtension-1.cs" >}}

## **Web拡張機能情報へのアクセス**

Aspose.Cellsでは、Excelファイル内のWeb拡張機能の情報にアクセスする機能が提供されます。次のコードサンプルは、[sample Excelファイル](89849870.xlsx)をロードしてWeb拡張機能情報にアクセスする方法を示しています。参照のためにコードによって生成されたコンソール出力をご覧ください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AccessWebExtensionInformation-1.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
