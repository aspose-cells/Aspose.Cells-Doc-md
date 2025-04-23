---
title: 数式の設定  非英語ユーザーへの通知
type: docs
weight: 10
url: /ja/python-net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NETは、Microsoft Excelのほとんどの式や関数をサポートしています。これらの式はAPIまたは[デザイナー スプレッドシート](/cells/ja/net/what-is-a-designer-spreadsheet/)を使って利用可能です。サポートされる数式には、数学関数、文字列関数、ブール値関数、日時関数、統計関数、データベース関数、検索と参照関数など多数あります。式は英語（米国）スタイルで指定してください。

{{% /alert %}} 

## **非英語のユーザー向けの注意**
Aspose.Cells for Python via .NETを使用して、非英語ユーザーが式を作成する際に必要な2つの注意点をご紹介します。

1. 式は英語で入力する必要があります。たとえば、"=SUM()" を使用し、"=SUMME()" ではなく、ドイツ語の "=SUMME()" を使用しないでください。
1. 常に関数のパラメーターを区切るためにコンマ（,）を使用します。一部の言語設定やオプションでは、関数パラメーターの区切り文字はセミコロンですが、Aspose.Cells for Python via .NETは英語スタイルのコンマを使用します。例えば、"=IF (C5=0,0,C3/C4)"を使用し、"=IF(C5=0;0;C3/C4)"ではありません。

