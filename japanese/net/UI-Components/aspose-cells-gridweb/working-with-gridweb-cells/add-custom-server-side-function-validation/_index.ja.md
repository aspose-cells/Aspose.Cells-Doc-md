---
title: カスタムサーバーサイド関数の検証を追加
type: docs
weight: 110
url: /ja/net/aspose-cells-gridweb/add-custom-server-side-function-validation/
keywords: GridWeb、サーバーサイドの検証
description: この記事では、GridWebでサーバーサイドの検証を行う方法について紹介します。
---

## **可能な使用シナリオ**
場合によっては、サーバーサイドでデータの検証を実装する必要があることがあります。Aspose.Cells.GridWebを使用すると、カスタムのサーバーサイドデータ検証を追加できます。セルの範囲またはエリアを指定する必要があります。また、コールバックのためのクライアントサイドの検証関数を設定することもできます。
## **カスタムサーバーサイド関数の検証を追加**
サーバーの検証クラスを設定する必要があります。このクラスは、GridCustomServerValidationインターフェースを実装している必要があります。また、クライアントサイドの検証関数（クライアントサイドでJavaScriptで書かれた関数）を設定する必要があります。この関数は、コールバック時にクライアントエンドでデータを検証するために必要です。必要に応じて、GridValidation.ErrorMessageプロパティおよびGridValidation.ErrorTitleプロパティを使用してエラーメッセージ文字列とタイトルを設定できます。以下のサンプルコードを実行した後、特定のシナリオでステップバイステップで機能がどのように動作するかを示す一連のスクリーンショットを参照してください。 

![todo:image_alt_text](add-custom-server-side-function-validation_1.png)

![todo:image_alt_text](add-custom-server-side-function-validation_2.png)

![todo:image_alt_text](add-custom-server-side-function-validation_3.png)

![todo:image_alt_text](add-custom-server-side-function-validation_4.png)

![todo:image_alt_text](add-custom-server-side-function-validation_5.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
