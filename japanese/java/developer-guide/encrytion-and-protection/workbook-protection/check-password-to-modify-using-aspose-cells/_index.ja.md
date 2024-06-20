---
title: Aspose.Cellsを使用して変更用パスワードを確認する
type: docs
weight: 190
url: /ja/java/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Microsoft Excelでブックを作成する際に**開くためのパスワード**と**変更用のパスワード**を割り当てることができます。これらのパスワードを指定するインターフェースを提供しているMicrosoft Excelのスクリーンショットをご覧ください。

![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)

時々、プログラムで指定されたパスワードが**変更用のパスワード**と一致するかどうかをチェックする必要があります。Aspose.Cellsは、指定された変更用パスワードが正しいかどうかを確認するための[**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword(java.lang.String))メソッドを提供しています。

{{% /alert %}}

## Aspose.Cellsを使用して変更用パスワードを確認するためのJavaコード

以下のサンプルコードは、[ソースExcel](5473057.xlsx)ファイルをロードします。開くためのパスワードは*1234*、変更用のパスワードは*5678*です。コードはまず*567*が変更用のパスワードの正しさを確認し、**false**を返し、次に*5678*が変更用のパスワードであるかどうかを確認し、**true**を返します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Javaコードによって生成されるコンソール出力

以上が、上記サンプルコードによって生成された[ソースExcel](5473057.xlsx)ファイルをロードした後のコンソール出力です。

{{< highlight java >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
