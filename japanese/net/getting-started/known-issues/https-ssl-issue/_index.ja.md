---
title: HTTPS SSLの問題
type: docs
weight: 20
url: /ja/net/https-ssl-issue/
---

## **HTTPS/SSLの問題**
Aspose.Cellsで生成されたExcelファイルをダウンロードする際に問題が発生したという報告があります。保存ダイアログが開くと、ファイル名にはExcelファイルの代わりにaspxページの名前が含まれ、ファイルタイプは空白です。
### **説明**
HTTP応答ヘッダーを変更して、HTTP圧縮に関連する問題を解決しました。これにより、HTTPS/SSLを介してクライアントブラウザにファイルを送信する際に問題が発生する可能性があります。
### **解決策**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
{{< app/cells/assistant language="csharp" >}}
