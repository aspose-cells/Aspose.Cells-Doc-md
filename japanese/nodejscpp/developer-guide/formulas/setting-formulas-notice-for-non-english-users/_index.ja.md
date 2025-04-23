---
title: 数式の設定  非英語ユーザーへの通知（Node.js経由C++）
linktitle: 数式の設定  非英語ユーザーへの通知
type: docs
weight: 10
url: /ja/nodejs-cpp/setting-formulas-notice-for-non-english-users/
---  

{{% alert color="primary" %}} 

 Aspose.Cellsは、Microsoft Excelのほとんどの数式/関数をサポートしています。開発者はこれらの数式をAPIまたは[designer spreadsheets](/cells/ja/nodejs-cpp/what-is-a-designer-spreadsheet/)のいずれかで使用できます。Aspose.Cellsは、膨大な数学、文字列、ブール値、日付/時刻、統計、データベース、検索、参照の数式をサポートしています。これらの数式は英語（米国）スタイルで指定してください。

{{% /alert %}} 

## **非英語のユーザー向けの注意**
非英語ユーザーがAspose.Cellsで数式を作成する際には、2つの注意点に従う必要があります：

1. 式は英語で入力する必要があります。たとえば、"=SUM()" を使用し、"=SUMME()" ではなく、ドイツ語の "=SUMME()" を使用しないでください。
1. 関数パラメータは常にコンマ（,）で区切ります。一部の言語設定やオプションでは、関数パラメータの区切り文字がセミコロン（;）の場合がありますが、Aspose.Cellsは英語スタイルのコンマを使用します。例えば、「=IF (C5=0,0,C3/C4)」を使用し、「=IF(C5=0;0;C3/C4)」は避けてください。  
