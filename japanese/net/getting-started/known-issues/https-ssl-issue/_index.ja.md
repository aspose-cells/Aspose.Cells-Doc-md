---
title: HTTPS SSL の問題
type: docs
weight: 20
url: /ja/net/https-ssl-issue/
---
## **HTTPS/SSL の問題**
一部のユーザーは、Aspose.Cells で生成された Excel ファイルのダウンロードに問題があると報告しています。保存ダイアログが開くと、ファイル名には Excel ファイルではなく aspx ページの名前が含まれ、ファイルの種類は空白です。
### **説明**
HTTP 圧縮の問題を解決するために、HTTP 応答ヘッダーを変更しました。これにより、HTTPS/SSL を介してクライアント ブラウザにファイルを送信する際に問題が発生する可能性があります。
### **解決**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
