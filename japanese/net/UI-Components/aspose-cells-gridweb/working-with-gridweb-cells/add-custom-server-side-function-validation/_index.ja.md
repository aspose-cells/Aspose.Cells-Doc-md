---
title: カスタム サーバー側関数検証の追加
type: docs
weight: 110
url: /ja/net/add-custom-server-side-function-validation/
---
## **考えられる使用シナリオ**
場合によっては、サーバー側でデータ検証を実装する必要がある場合があります。 Aspose.Cells.GridWeb では、カスタムのサーバー側データ検証を追加できます。セル範囲または領域を指定する必要があります。カスタムのサーバー側検証を使用して、コールバックのクライアント側検証関数を設定することもできます。
## **カスタム サーバー側関数検証の追加**
を実装するサーバー検証クラスを設定する必要があります。**GridCustomServerValidation**インターフェース経由**GridValidation.ServerValidation**属性。また、クライアント側の検証関数を設定する必要があります (クライアント側の JavaScript で記述する必要があります)。この関数は、コールバック時にクライアント側でデータを検証するために必須です。エラーメッセージ文字列を設定できます**GridValidation.ErrorMessage**とタイトル**GridValidation.ErrorTitle**あなたのニーズのためのプロパティ。以下のサンプル コードを実行した後、特定のシナリオでどのように動作するか (段階的に) を示す一連のスクリーンショットを参照してください。この例では、B2:C3 セルのデータを更新できません。シート内のこれらのセルを編集しようとすると、いくつかのエラー メッセージが表示され、以前の値が復元されます。コンソール ウィンドウ (ブラウザーで) を開いて、特定のイベントに関するセルの情報/詳細を出力できます。

![todo:画像_代替_文章](add-custom-server-side-function-validation_1.png)

![todo:画像_代替_文章](add-custom-server-side-function-validation_2.png)

![todo:画像_代替_文章](add-custom-server-side-function-validation_3.png)

![todo:画像_代替_文章](add-custom-server-side-function-validation_4.png)

![todo:画像_代替_文章](add-custom-server-side-function-validation_5.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
