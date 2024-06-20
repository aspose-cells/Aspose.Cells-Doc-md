---
title: レスポンスオブジェクトへのファイルの保存
type: docs
weight: 50
url: /ja/net/saving-file-to-response-object/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、ファイルを操作することができます。この記事では、ファイルをレスポンスオブジェクトに保存するさまざまな方法を説明します。

{{% /alert %}}

## **レスポンスオブジェクトへのファイルの保存**

ファイルを動的に生成し、それをクライアントブラウザに直接送信することも可能です。そのためには、次のパラメータを受け入れる[**Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5)メソッドの特別なオーバーロードバージョンを使用します。

- ASP.NET [**HttpResponse**](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8)オブジェクト。
- ファイル名。
- [**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)、出力ファイルのcontent-dispositionタイプ。
- [**SaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/saveoptions)、ファイル形式の種類

[**ContentDisposition**](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition) 列挙型は、ブラウザに送信されるファイルが、ブラウザ内で直接開くか、.xls/.xlsx または他の拡張子に関連付けられたアプリケーションで開くオプションを提供するかを決定します。

列挙型には、以下の事前定義された保存タイプが含まれています:

|**タイプ**|**説明**|
| :- | :- |
|アタッチメント|スプレッドシートをブラウザに送り、.xls/.xlsx や他の拡張子に関連付けられたアプリケーションで添付ファイルとして開きます|
|インライン|ドキュメントをブラウザに送り、スプレッドシートをディスクに保存するかブラウザ内で開くオプションを表示します|

### **XLS ファイル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **XLSX ファイル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **PDF ファイル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **注**

NET5 および .Netstandard に含まれていないオブジェクト "System.Web.HttpResponse" により、
この機能は Aspose.Cells .NET5 および .Netstandard バージョンに存在しないため、ファイルをストリームに保存し、ストリームに対して操作を行うために、以下のコードを参照してください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

