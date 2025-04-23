---
title: 数式の設定  非英語ユーザーへの通知
type: docs
weight: 10
url: /ja/net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cellsは、Microsoft Excelの一部であるほとんどの式/関数をサポートしています。開発者は、APIまたは[デザイナースプレッドシート](/cells/ja/net/what-is-a-designer-spreadsheet/)を使用してこれらの式を使用することができます。Aspose.Cellsは、数学、文字列、ブール値、日付/時刻、統計、データベース、検索および参照の式の大規模なセットをサポートしています。これらの式は、英語（米国）スタイルのカンマを使用して指定する必要があります。

{{% /alert %}} 
## **非英語のユーザー向けの注意**
非英語ユーザーがAspose.Cellsで数式を作成する際には、2つの注意点に従う必要があります：

1. 式は英語で入力する必要があります。たとえば、"=SUM()" を使用し、"=SUMME()" ではなく、ドイツ語の "=SUMME()" を使用しないでください。
1. 常に関数パラメータを区切る際には、カンマ(,)を使用してください。言語オプションや設定によっては、関数パラメータの区切り文字がセミコロンになることがありますが、Aspose.Cellsは英語スタイルのカンマを使用します。たとえば、"=IF (C5=0,0,C3/C4)" を使用し、"=IF(C5=0;0;C3/C4)" を使用しないでください。
{{< app/cells/assistant language="csharp" >}}
