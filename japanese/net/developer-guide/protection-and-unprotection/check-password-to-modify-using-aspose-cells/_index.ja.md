---
title: Aspose.Cellsを使用して変更用パスワードを確認する
type: docs
weight: 2400
url: /ja/net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

与えられたパスワードが**変更を許可**のパスワードと一致するかどうかをプログラムでチェックする必要がある場合があります。Aspose.Cells は、与えられた**変更を許可**のパスワードが正しいかどうかをチェックするために使用できる WorkbookSettings.WriteProtection.ValidatePassword() メソッドを提供しています。

{{% /alert %}}

## **Microsoft Excelで変更するためのパスワードをチェックする**

Microsoft Excelで作成するワークブックに**開くためのパスワード**および**変更するためのパスワード**を割り当てることができます。これらのパスワードを指定するためのMicrosoft Excelが提供するインターフェースを示すスクリーンショットをご覧ください。

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Aspose.Cellsを使用して変更パスワードを確認する**

次のサンプルコードは、[元のExcel](5112232.xlsx)ファイルをロードします。**開くためのパスワード**は1234であり、**変更するためのパスワード**は5678です。コードはまず、567が正しい**変更するためのパスワード**かどうかをチェックし、falseを返し、次に5678が**変更するためのパスワード**かどうかをチェックし、trueを返します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **コンソール出力**

上記のサンプルコードで[元のExcel](5112232.xlsx)ファイルをロードした後のコンソール出力はこちらです。

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
