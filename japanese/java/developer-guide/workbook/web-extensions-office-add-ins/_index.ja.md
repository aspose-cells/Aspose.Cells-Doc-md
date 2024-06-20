---
title: Web拡張機能  Officeアドイン
type: docs
weight: 120
url: /ja/java/web-extensions-office-add-ins/
---

Web拡張機能は、Officeアプリケーションを拡張し、Office文書のコンテンツとやり取りします。Web拡張機能は、ユーザーエクスペリエンスと生産性を向上させるためにOfficeクライアントに追加機能を提供します。

Aspose.CellsもWeb拡張機能と連携する機能を提供しています。

## **Web拡張機能の追加**

ExcelにWeb拡張機能（Officeアドイン）を追加するには、**挿入**タブをクリックし、**ストア**/**アドインの取得**リンクをクリックしてください。アドインボックスで、追加したいアドインを参照して追加します。

Aspose.Cellsは、**WebExtension**および**WebExtensionTaskPane**クラスを使用してWeb拡張機能を追加する機能も提供しています。以下のコードサンプルは、**WebExtension**および**WebExtensionTaskPane**クラスを使用してExcelファイルにWeb拡張機能を追加する方法を示しています。参照のためにコードによって生成されたExcelファイルは、[出力Excelファイル](AddWebExtension_Out.xlsx)で確認できます。

### **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddWebExtension-1.java" >}}

## **Web拡張機能情報へのアクセス**

Aspose.Cellsは、Excelファイル内のWeb拡張機能の情報にアクセスする機能を提供しています。以下のコードサンプルは、[サンプルExcelファイル](WebExtensionsSample.xlsx)をロードしてWeb拡張機能情報にアクセスする方法を示しています。参照のためにコードによって生成されたコンソール出力も確認できます。

### **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AccessWebExtensionInformation-1.java" >}}

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
