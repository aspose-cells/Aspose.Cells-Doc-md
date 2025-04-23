---
title: 数式の設定  非英語ユーザーへの通知
type: docs
weight: 20
url: /ja/java/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.CellsはMicrosoft Excelのほとんどの数式/関数をサポートしています。開発者はこれらの数式をAPIまたは[デザインスプレッドシート](/cells/ja/java/what-is-a-designer-spreadsheet/)で使用できます。Aspose.Cellsは、数学、文字列、ブール値、日付/時刻、統計、データベース、検索および参照の数式を大量にサポートしています。数式は英語（米国）スタイルを使用する必要があります。

非英語ユーザーがAspose.Cellsで数式を作成する際には、2つの注意点に従う必要があります：

1. 数式は英語で入力する必要があります。
   たとえば、ドイツ語の"=SUMME()"ではなく、英語の"=SUM()"を使用してください。
1. 関数パラメータを区切る際には常にカンマ(,)を使用してください。
   一部の言語オプションや設定では、関数パラメータの区切り文字がセミコロンですが、Aspose.Cellsでは英語スタイルのカンマを使用します。たとえば、"=IF(C5=0,0,C3/C4)"を使用してください。"=IF(C5=0;0;C3/C4)"ではありません。 

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
