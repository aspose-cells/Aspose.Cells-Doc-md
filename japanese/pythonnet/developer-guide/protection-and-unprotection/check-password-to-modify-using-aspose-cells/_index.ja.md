---
title: Aspose.Cells for Python via .NETを使った編集用パスワードの確認
type: docs
weight: 2400
url: /ja/python-net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

時には、プログラム側で与えられたパスワードが**変更用パスワード**と一致するかどうかを確認する必要があります。Aspose.Cells for Python via .NETは、WorkbookSettings.write_protection.validate_password()メソッドを提供し、変更用パスワードの正誤を確認できます。

{{% /alert %}}

## **Microsoft Excelで変更するためのパスワードをチェックする**

Microsoft Excelで作成するワークブックに**開くためのパスワード**および**変更するためのパスワード**を割り当てることができます。これらのパスワードを指定するためのMicrosoft Excelが提供するインターフェースを示すスクリーンショットをご覧ください。

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Aspose.Cells for Python via .NETを使った変更用パスワードの確認**

次のサンプルコードは、[元のExcel](5112232.xlsx)ファイルをロードします。**開くためのパスワード**は1234であり、**変更するためのパスワード**は5678です。コードはまず、567が正しい**変更するためのパスワード**かどうかをチェックし、falseを返し、次に5678が**変更するためのパスワード**かどうかをチェックし、trueを返します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckPasswordToModifyUsingAsposeCells.py" >}}

### **コンソール出力**

上記のサンプルコードで[元のExcel](5112232.xlsx)ファイルをロードした後のコンソール出力はこちらです。

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
