---
title: HTTP圧縮
type: docs
weight: 10
url: /ja/net/http-compression/
---

## **HTTP圧縮の問題**
一部のユーザーは、IISでHTTP圧縮を構成すると、生成されたファイルをクライアントブラウザに送信する際にエラーが発生すると報告しています。
### **説明**
ブラウザーをファイルを開くように強制するために、**"Content-disposition", "inline; filename=test.xls"**ヘッダーを使用し、**"Content-disposition", "attachment; filename=test.xls"**ヘッダーを使用して**保存**ダイアログを開き、Microsoft Excelを使用してファイルを開くために使用しています。 ただし、いくつかの例外が存在することに注意してください。
### **例外**
Asposeのバグでないことを確認するために、次のコードを使用できます。

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **解決策**
この問題を解決するために、次のワークアラウンドのいずれかを使用できます：

- 指定されたASP.NETファイル（Aspose.Cellsを呼び出すコードを含む）を圧縮されていない別のフォルダに移動します。
- 動的コンテンツのHTTP圧縮を無効にします。
- サーバーに生成されたファイルを保存し、ユーザーにリンクを提供します。

HTTP圧縮を使用する場合は、IIS圧縮を有効にしたことがわかっている場合は、常に*OpenInBrowser*オプションの代わりに*OpenInExcel*オプションを使用してください。
{{< app/cells/assistant language="csharp" >}}
