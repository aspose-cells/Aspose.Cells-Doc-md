---
title: ファイルを応答オブジェクトに保存する
type: docs
weight: 50
url: /ja/net/saving-file-to-response-object/
---
{{% alert color="primary" %}}

Aspose.Cells により、ファイルの操作が可能になります。この記事では、ファイルを応答オブジェクトに保存するさまざまな方法について説明します。

{{% /alert %}}

## **ファイルを応答オブジェクトに保存する**

ファイルを動的に生成し、クライアント ブラウザに直接送信することもできます。そのためには、特別なオーバーロードされたバージョンの**[保存](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5)**次のパラメータを受け入れるメソッド:

-  ASP.NET**[HttpResponse](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8)**物体。
- ファイル名。
- **[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**、出力ファイルの content-disposition タイプ。
- **[保存オプション](https://reference.aspose.com/cells/net/aspose.cells/saveoptions)**、ファイル形式の種類

の**[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**列挙は、ブラウザに送信されるファイルが、ブラウザで直接開くか、.xls/.xlsx または別の拡張子に関連付けられたアプリケーションで開くオプションを提供するかどうかを決定します。

列挙には、次の定義済み保存タイプが含まれます。

|**タイプ**|**説明**|
|:- |:- |
|付属品|スプレッドシートをブラウザーに送信し、.xls/.xlsx またはその他の拡張子に関連付けられた添付ファイルとしてアプリケーションで開きます|
|列をなして|ドキュメントをブラウザに送信し、スプレッドシートをディスクに保存するかブラウザ内で開くかを選択するオプションを提示します|

### **XLS ファイル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **XLSX ファイル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **PDF ファイル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **ノート**

オブジェクト「System.Web.HttpResponse」が.NET5および.Netstandardに含まれていないため、
したがって、この関数は Aspose.Cells .NET5 および .Netstandard バージョンには存在しません。次のコードを参照して、ファイルをストリームに保存し、ストリームに対して操作を行うことができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

