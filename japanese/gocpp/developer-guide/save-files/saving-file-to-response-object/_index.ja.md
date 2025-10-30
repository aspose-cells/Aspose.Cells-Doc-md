---
title: GolangとC++を用いてResponseオブジェクトにファイルを保存
linktitle: レスポンスオブジェクトへのファイルの保存
type: docs
weight: 50
url: /ja/go-cpp/saving-file-to-response-object/
description: Aspose.Cells for C++を使用してファイルを動的に保存し、直接クライアントのブラウザに送信する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、ファイルを操作することができます。この記事では、ファイルをレスポンスオブジェクトに保存するさまざまな方法を説明します。

{{% /alert %}}

## **レスポンスオブジェクトへのファイルの保存**

ファイルを動的に生成し、それをクライアントブラウザに直接送信することも可能です。そのためには、次のパラメータを受け入れる[**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/)メソッドの特別なオーバーロードバージョンを使用します。

- **HttpResponse**オブジェクト。
- ファイル名。
- [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/)、出力ファイルのcontent-dispositionタイプ。
- [**SaveOptions**](https://reference.aspose.com/cells/go-cpp/saveoptions/)、ファイル形式タイプ。

[**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/) 列挙型は、ブラウザに送信されるファイルが、ブラウザ内で直接開くか、.xls/.xlsx または他の拡張子に関連付けられたアプリケーションで開くオプションを提供するかを決定します。

列挙型には、以下の事前定義された保存タイプが含まれています:

|**タイプ**|**説明**|
| :- | :- |
|アタッチメント|スプレッドシートをブラウザに送り、.xls/.xlsx や他の拡張子に関連付けられたアプリケーションで添付ファイルとして開きます|
|インライン|ドキュメントをブラウザに送り、スプレッドシートをディスクに保存するかブラウザ内で開くオプションを表示します|

### **XLS ファイル**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject.go" >}}
### **XLSX ファイル**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-1.go" >}}
### **PDF ファイル**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-2.go" >}}
### **注**

NET5 および .Netstandard に含まれていないオブジェクト "System.Web.HttpResponse" により、
この機能は Aspose.Cells .NET5 および .Netstandard バージョンに存在しないため、ファイルをストリームに保存し、ストリームに対して操作を行うために、以下のコードを参照してください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-3.go" >}}
