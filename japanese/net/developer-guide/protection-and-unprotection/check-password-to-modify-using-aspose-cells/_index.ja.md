---
title: Aspose.Cells を使用して変更するパスワードを確認してください
type: docs
weight: 2400
url: /ja/net/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

場合によっては、指定されたパスワードが一致するかどうかを確認する必要があります**変更するパスワード**プログラム的に。 Aspose.Cells は WorkbookSettings.WriteProtection.ValidatePassword() メソッドを提供します。これを使用して、変更する指定されたパスワードが正しいかどうかを確認できます。

{{% /alert %}}

## **Microsoft Excel で変更するパスワードを確認してください**

割り当てることができます**開くためのパスワード**と**変更するパスワード**Microsoft Excel でワークブックを作成している間。これらのパスワードを指定するために Excel が提供するインターフェース Microsoft を示すこのスクリーンショットを参照してください。

|![todo:画像_代替_文章](check-password-to-modify-using-aspose-cells_1.png)|
|:- |

## **Aspose.Cells を使用して変更するパスワードを確認してください**

次のサンプル コードは、[ソースエクセル](5112232.xlsx)ファイル。 1234 として開くパスワードと 5678 として変更するパスワードがあります。コードは最初に 567 が変更する正しいパスワードであるかどうかを確認し、false を返し、次に 5678 が変更するパスワードであるかどうかを確認し、true を返します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **コンソール出力**

上記のサンプル コードをロードした後のコンソール出力は次のとおりです。[ソースエクセル](5112232.xlsx)ファイル。

{{< highlight "java" >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
