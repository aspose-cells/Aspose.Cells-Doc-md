---
title: 数式の設定 - 英語以外のユーザーへの通知
type: docs
weight: 10
url: /ja/net/setting-formulas-notice-for-non-english-users/
---
{{% alert color="primary" %}} 

Aspose.Cells は、Microsoft Excel の一部である数式/関数のほとんどをサポートしています。開発者は、API または[デザイナー スプレッドシート](/cells/ja/net/what-is-a-designer-spreadsheet/)Aspose.Cells は、数学、文字列、ブール、日付/時刻、統計、データベース、ルックアップ、および参照式の膨大なセットをサポートしています。数式は、英語 (米国) スタイルを使用して指定する必要があります。

{{% /alert %}} 
## **英語以外のユーザーへの通知**
英語以外のユーザーが Aspose.Cells を使用して数式を作成する場合に従う必要がある 2 つのヒントがあります。

1. 数式は英語で入力する必要があります。たとえば、ドイツ語の「=SUMME()」ではなく、英語の「=SUM()」を使用します。
1. 関数のパラメーターを区切るには、常にコンマ (,) を使用します。一部の言語オプションまたは設定では、関数パラメーターの区切り文字はセミコロンですが、Aspose.Cells では英語スタイルのコンマが使用されます。たとえば、「=IF(C5=0;0;C3/C4)」ではなく「=IF (C5=0,0,C3/C4)」を使用します。
