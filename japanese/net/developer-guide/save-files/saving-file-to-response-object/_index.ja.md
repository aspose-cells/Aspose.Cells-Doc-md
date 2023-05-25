---
title: ファイルを応答オブジェクトに保存する
type: docs
weight: 50
url: /ja/net/saving-file-to-response-object/
---
{{% alert color="primary" %}}

Aspose.Cellsによりファイル操作が可能になります。この記事では、ファイルを応答オブジェクトに保存するさまざまな方法について説明します。

{{% /alert %}}

##  **ファイルを応答オブジェクトに保存する**

ファイルを動的に生成し、クライアントのブラウザに直接送信することもできます。これを行うには、特別なオーバーロードされたバージョンの**[保存](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5)**次のパラメータを受け入れるメソッド:

- ASP.NET **[HttpResponse](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8)**物体。
- ファイル名。
- *[コンテンツの配置](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**、出力ファイルのコンテンツ配置タイプ。
- *[保存オプション](https://reference.aspose.com/cells/net/aspose.cells/saveoptions)**、ファイル形式のタイプ

の**[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**列挙は、ブラウザに送信されるファイルが、ブラウザ内で直接開くオプション、または .xls/.xlsx または別の拡張子に関連付けられたアプリケーションで開くオプションを提供するかどうかを決定します。

列挙には、次の事前定義された保存タイプが含まれています。

|**タイプ**|**説明**|
| :- | :- |
|Attachment|スプレッドシートをブラウザに送信し、.xls/.xlsx またはその他の拡張子に関連付けられた添付ファイルとしてアプリケーションで開きます。|
|Inline|ドキュメントをブラウザに送信し、スプレッドシートをディスクに保存するか、ブラウザ内で開くかを選択するオプションを表示します。|

###  **XLS ファイル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

###  **XLSX ファイル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

###  **PDF ファイル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

###  **ノート**

.NET5や.Netstandardには含まれていないオブジェクト「System.Web.HttpResponse」のため、
したがって、この関数は Aspose.Cells .NET5 および .Netstandard バージョンには存在しないため、次のコードを参照してファイルをストリームに保存し、ストリームに対して操作を行うことができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

