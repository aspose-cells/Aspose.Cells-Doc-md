---
title: Aspose.Cellsを使用してExcelファイルを暗号化およびパスワード保護する
type: docs
weight: 30
url: /ja/net/encrypting-excel-files-using-aspose-cells/
---

{{% alert color="primary" %}} 

マイクロソフトエクセル（97-2007）は、スプレッドシートを暗号化およびパスワード保護することができます。異なる特性を持つ一連の暗号化アルゴリズムである暗号化サービスプロバイダ（CSP）で提供されるアルゴリズムを使用します。デフォルトのCSPは「Office 97/2000互換」または「弱い暗号化（XOR）」です。適切な暗号化キー長を選択することが重要です。一部のCSPは40ビットまたは56ビットを超えるキー長をサポートしていません。それは弱い暗号化と見なされます。強力な暗号化のためには、最低128ビットの鍵長が必要です。Microsoft Windowsには、たとえば「マイクロソフト強力暗号化プロバイダ」のような強力な暗号化タイプを提供するCSPが含まれています。128ビットの暗号化が銀行がインターネットバンキングシステムとの接続を暗号化するために使用するものです。

Aspose.Cellsを使用すると、任意の暗号化タイプでMicrosoft Excelファイルを暗号化およびパスワード保護することができます。

{{% /alert %}} 
## **Microsoft Excel の使用**
Microsoft Excel（ここではMicrosoft Excel 2003）でファイルの暗号化設定を行うには：

1. **ツール**メニューから**オプション**を選択します。
   ダイアログが表示されます。
1. **セキュリティ**タブを選択します。
1. パスワードを入力し、**詳細**をクリックします。 
   **オプション ダイアログ** 

![todo:image_alt_text](encrypting-excel-files-using-aspose-cells_1.png)




1. 暗号化方式を選択し、パスワードを確認します。 

   **暗号化タイプダイアログ** 

![todo:image_alt_text](encrypting-excel-files-using-aspose-cells_2.png)



## **Aspose.Cells を使用した暗号化**
次の例は、Aspose.Cells APIを使用してExcelファイルを暗号化およびパスワード保護する方法を示しています。

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string srcFileName = FilePath + "Encrypting Excel Files.xlsx";

string destFileName = FilePath + "Result Encrypting Excel Files.xlsx";

//Open an excel file.

Workbook workbook = new Workbook(srcFileName);

//Specify XOR encryption type.

workbook.SetEncryptionOptions(EncryptionType.XOR, 40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.

workbook.Settings.Password = "1234";

//Save the excel file.

workbook.Save(destFileName);

{{< /highlight >}}
## **ランニングコードのダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
## **サンプルコードをダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Encrypting%20Excel%20Files)

{{< app/cells/assistant language="csharp" >}}
