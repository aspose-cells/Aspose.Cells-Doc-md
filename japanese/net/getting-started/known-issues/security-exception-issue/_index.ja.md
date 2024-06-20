---
title: セキュリティ例外の問題
type: docs
weight: 30
url: /ja/net/security-exception-issue/
---

## **Security Exception Problem**
Aspose.Cellsを使用しようとした際に、一部のユーザーが"Security Exception"エラーを受け取ることがあります。この問題は一般的にWebアプリケーションで発生します。
### **説明**
Aspose.Cellsはいくつかの重要な機能を提供するために**Win32 GDI APIs**を呼び出さなければなりません。Webサーバーが厳格な信頼レベルを持っている場合、このセキュリティ例外が発生する可能性があります。
### **解決策**
新しいアセンブリの呼び出しを許可するセキュリティ権限を与えるために新しい許可セットを作成してください。
