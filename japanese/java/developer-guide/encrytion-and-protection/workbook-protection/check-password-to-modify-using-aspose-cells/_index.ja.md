---
title: Aspose.Cells を使用して変更するパスワードを確認してください
type: docs
weight: 190
url: /ja/java/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

割り当てることができます**開くためのパスワード**そして**変更するパスワード**Microsoft Excel でワークブックを作成している間。これらのパスワードを指定するために Excel が提供するインターフェース Microsoft を示すこのスクリーンショットを参照してください。

![todo:画像_代替_文章](check-password-to-modify-using-aspose-cells_1.png)

場合によっては、指定されたパスワードが一致するかどうかを確認する必要があります**変更するパスワード**プログラム的に。 Aspose.Cells提供[**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword(java.lang.String)）変更するために指定されたパスワードが正しいかどうかを確認するために使用できるメソッド。

{{% /alert %}}

## Java 確認するコード Aspose.Cells を使用して変更するパスワード

次のサンプル コードは、[ソースエクセル](5473057.xlsx)ファイル。として開くためのパスワードがあります*1234*および変更するパスワード*5678*.コードは最初に以下をチェックします*567*変更する正しいパスワードであり、それが返されます**間違い**そして、それは*5678*変更するパスワードであり、それが返されます**真実**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Java コードによって生成されたコンソール出力

上記のサンプル コードをロードした後のコンソール出力は次のとおりです。[ソースエクセル](5473057.xlsx)ファイル。

{{< highlight "java" >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
