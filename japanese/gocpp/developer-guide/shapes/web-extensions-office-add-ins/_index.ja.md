---
title: Web拡張機能  Officeアドイン（Golang + C++）
linktitle: Web拡張機能  Officeアドイン
type: docs
weight: 130
url: /ja/go-cpp/web-extensions-office-add-ins/
description: Aspose.CellsとGolangを使ってExcelファイルにWeb拡張機能（Officeアドイン）を追加およびアクセスする方法。
---

Web拡張機能はOfficeアプリケーションを拡張し、Officeドキュメント内のコンテンツと連携します。これにより、Officeクライアントの機能性と生産性が向上します。

Aspose.CellsもWeb拡張機能と連携する機能を提供しています。

## **Web拡張機能の追加**

ExcelにWeb拡張機能（Officeアドイン）を追加できます。**挿入**タブをクリックし、その後**ストア**/**アドインを取得**リンクをクリックしてください。アドインボックスで目的のアドインを参照して追加します。

Aspose.Cellsは、[**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/)と[**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/)クラスを使用してWeb拡張を追加する機能も提供します。次のコード例は、[**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/)と[**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/)クラスを使用してExcelファイルにWeb拡張を追加する方法を示しています。詳細は[出力Excelファイル](89849869.xlsx)を参照してください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns.go" >}}
## **Web拡張機能情報へのアクセス**

Aspose.Cellsは、Excelファイル内のWeb拡張情報にアクセスする機能を提供します。次のコード例は、[サンプルExcelファイル](89849870.xlsx)をロードし、Web拡張情報にアクセスする方法を示しています。結果はコンソール出力から確認できます。

### **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns-1.go" >}}
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
