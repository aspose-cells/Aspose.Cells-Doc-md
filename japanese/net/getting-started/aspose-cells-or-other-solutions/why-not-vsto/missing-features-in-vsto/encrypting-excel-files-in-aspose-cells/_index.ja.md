---
title: Aspose.Cells で Excel ファイルを暗号化する
type: docs
weight: 90
url: /ja/net/encrypting-excel-files-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007) では、スプレッドシートを暗号化し、パスワードで保護できます。暗号化サービス プロバイダー (CSP) によって提供されるアルゴリズムを使用します。これは、さまざまなプロパティを持つ一連の暗号化アルゴリズムです。デフォルトの CSP は「Office 97/2000 互換」または「弱い暗号化 (XOR)」です。適切な暗号化キーの長さを選択することが重要です。一部の CSP は、40 ビットまたは 56 ビットを超えるビットをサポートしていません。これは弱い暗号化と見なされます。強力な暗号化を行うには、128 ビット以上のキー長が必要です。 Microsoft Windows には、「Microsoft 強力な暗号化プロバイダー」などの強力な暗号化タイプも提供する CSP が含まれています。 128 ビット暗号化は、銀行がインターネット バンキング システムとの接続を暗号化するために使用するものです。

Aspose.Cells を使用すると、目的の暗号化タイプで Microsoft Excel ファイルを暗号化し、パスワードで保護できます。

{{% /alert %}} 
## **Microsoft エクセルを使う**
Microsoft Excel (ここでは Microsoft Excel 2003) でファイル暗号化設定を設定するには:

1. から**ツール**メニュー、選択**オプション**.
ダイアログが表示されます。
1. を選択**安全**タブ。
1. パスワードを入力してクリック**高度** 
   **オプションダイアログ** 

![todo:画像_代替_文章](encrypting-excel-files-in-aspose-cells_1.png)




1. 暗号化タイプを選択し、パスワードを確認します。

   **暗号化タイプダイアログ** 

![todo:画像_代替_文章](encrypting-excel-files-in-aspose-cells_2.png)



## **Aspose.Cellsで暗号化**
次の例は、Aspose.Cells API を使用して Excel ファイルを暗号化し、パスワードで保護する方法を示しています。

**C#**

{{< highlight "csharp" >}}

 //Instantiate a Workbook object.

//Open an excel file.

Workbook workbook = new Workbook("Book1.xls");

//Specify XOR encryption type.

workbook.SetEncryptionOptions(EncryptionType.XOR,40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.

workbook.Settings.Password = "1234";

//Save the excel file.

workbook.Save("encryptedBook1.xls");



{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Encrypting%20Excel%20Files)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1))
