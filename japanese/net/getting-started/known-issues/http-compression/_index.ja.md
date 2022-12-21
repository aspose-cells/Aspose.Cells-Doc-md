---
title: HTTP 圧縮
type: docs
weight: 10
url: /ja/net/http-compression/
---
## **HTTP 圧縮の問題**
一部のユーザーは、IIS で HTTP 圧縮を構成すると、生成されたファイルをクライアント ブラウザーに送信するときにエラーが発生すると報告しています。
### **説明**
を使用しております**「コンテンツ処理」、「インライン; ファイル名=test.xls」**ブラウザに強制的にファイルを開くヘッダーと**「コンテンツの性質」、「添付; ファイル名=test.xls」**ブラウザに強制的に開くようにするヘッダー**名前を付けて保存**ダイアログを開き、Microsoft Excel を使用してファイルを開きます。ただし、いくつかの例外が存在します。
### **例外**
次のコードを使用して、Aspose のバグではないことを確認できます。

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **ソリューション**
この問題を解決するには、次の回避策のいずれかを使用できます。

- 指定された ASP.NET ファイル (Aspose.Cells を呼び出すコードを含む) を、圧縮されていない別のフォルダーに移動します。
- 動的コンテンツの HTTP 圧縮を無効にします。
- 生成されたファイルをサーバーに保存し、ユーザーにリンクを提供します。

 HTTP 圧縮を使用したい場合は、常に使用してください。*OpenInExcel*代わりのオプション*ブラウザで開く*IIS 圧縮を有効にしたことがわかっている場合のオプション。
