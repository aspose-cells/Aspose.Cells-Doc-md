---
title: 式の設定  非英語ユーザーへの通知（JavaScript経由でC++を使用）
linktitle: 数式の設定  非英語ユーザーへの通知
type: docs
weight: 10
url: /ja/javascript-cpp/setting-formulas-notice-for-non-english-users/
---  

{{% alert color="primary" %}} 

Aspose.CellsはMicrosoft Excelに含まれるほとんどの式や関数をサポートしています。これらの式はAPIまたは[designer spreadsheets](/cells/ja/javascript-cpp/what-is-a-designer-spreadsheet/)を使用して利用できます。Aspose.Cellsは、数学、文字列、ブール、日付/時間、統計、データベース、ルックアップ、リファレンスの多種多様な式をサポートします。式は英語（USスタイル）で指定すべきです。

{{% /alert %}} 

## **非英語のユーザー向けの注意**
非英語ユーザーがAspose.Cellsで数式を作成する際には、2つの注意点に従う必要があります：

1. 式は英語で入力する必要があります。たとえば、"=SUM()" を使用し、"=SUMME()" ではなく、ドイツ語の "=SUMME()" を使用しないでください。
1. 関数パラメータは常にコンマ（,）で区切ります。一部の言語設定やオプションでは、関数パラメータの区切り文字がセミコロン（;）の場合がありますが、Aspose.Cellsは英語スタイルのコンマを使用します。例えば、「=IF (C5=0,0,C3/C4)」を使用し、「=IF(C5=0;0;C3/C4)」は避けてください。
