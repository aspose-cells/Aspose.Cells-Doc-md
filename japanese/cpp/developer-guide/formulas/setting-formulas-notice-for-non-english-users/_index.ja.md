---
title: 数式の設定  非英語ユーザー向けの注意点（C++）
linktitle: 数式の設定  非英語ユーザーへの通知
type: docs
weight: 10
url: /ja/cpp/setting-formulas-notice-for-non-english-users/
description: Aspose.Cellsを使った英語（米国）スタイルで非英語ユーザー向けにAspose.Cells for C++の数式を設定する方法を学びます。
---

{{% alert color="primary" %}} 

Aspose.Cellsは、Microsoft Excelのほとんどの数式や関数をサポートしています。開発者はこれらの数式をAPIまたは[デザイナースプレッドシート](/cells/ja/cpp/what-is-a-designer-spreadsheet/)で使用できます。Aspose.Cellsは、多くの数学、文字列、ブール値、日付/時間、統計、データベース、ルックアップ、リファレンスの数式をサポートします。数式は英語（米国）スタイルで指定する必要があります。

{{% /alert %}} 

## **非英語のユーザー向けの注意**
非英語ユーザーがAspose.Cellsで数式を作成する際には、2つの注意点に従う必要があります：

1. 式は英語で入力する必要があります。たとえば、"=SUM()" を使用し、"=SUMME()" ではなく、ドイツ語の "=SUMME()" を使用しないでください。
1. 関数パラメータは常にコンマ（,）で区切ります。一部の言語設定やオプションでは、関数パラメータの区切り文字がセミコロン（;）の場合がありますが、Aspose.Cellsは英語スタイルのコンマを使用します。例えば、「=IF (C5=0,0,C3/C4)」を使用し、「=IF(C5=0;0;C3/C4)」は避けてください。
{{< app/cells/assistant language="cpp" >}}
