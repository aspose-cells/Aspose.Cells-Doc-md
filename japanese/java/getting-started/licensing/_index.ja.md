---
title: ライセンス
type: docs
weight: 50
url: /ja/java/licensing/
description: Aspose.Cells for JAVAでは、Javaのライセンスとサブスクリプションポリシーを使用して、購入のための異なる計画や無料トライアル、30日間の評価用の一時ライセンスを提供しています。
keywords: Javaでディスクまたはストリームからライセンスを適用する。Javaでディスクまたはストリームからライセンスを設定する。Aspose.Cells for Javaにライセンスを適用する。.
---

## **Aspose.Cells コンポーネントでライセンスを適用する方法**

ライセンスの設定

ライセンスは、製品名、ライセンスされた開発者の数、サブスクリプションの有効期限などの詳細が含まれるプレーンテキストのXMLファイルです。ファイルはデジタル署名されているため、ファイルを変更しないでください。ファイルに行を追加した場合でも、それは無効になります。Aspose.Cellsを利用する前にライセンスを設定する必要があります。アプリケーションまたはプロセスごとにライセンスを1回だけ設定する必要があります。

ライセンスは、次の場所からストリームまたはファイルからロードできます：1. 明示的なパス。

1. 明示的なパス。
1. Aspose.Cells.jar を含むフォルダ。

[License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) メソッドを使用して、コンポーネントにライセンスを付与します。ライセンスを設定する最も簡単な方法は、Aspose.Cells.jar と同じフォルダにライセンスファイルを配置し、次の例に示すようにパスを指定せずにファイル名だけを指定することです。

### **ディスクからライセンスを適用する方法**

この例では、**Aspose.Cells** はアプリケーションの JAR のフォルダにライセンスファイルを検索しようとします。

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **ストリームからライセンスを適用する方法**

ストリームからライセンスを初期化します。

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Aspose.Cells.GridWeb でライセンスを適用する方法**

ウェブアプリケーションでライセンスコードを処理するための推奨される場所。

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **メータード ライセンスの適用方法**

Aspose.Cellsでは、開発者がメータードキーを適用することができます。これは新しいライセンスメカニズムです。新しいライセンスメカニズムは、既存のライセンス方法と併用されます。API機能の使用に基づいて請求を受けたい顧客は、メータードライセンスを使用できます。詳細については、[メータードライセンスFAQ](https://purchase.aspose.com/faqs/licensing/metered)セクションを参照してください。

メーターキーを設定する方法を示すサンプルコードは、新しいクラス [Metered](https://reference.aspose.com/cells/java/com.aspose.cells/Metered) が導入されました。

{{< highlight java >}}

//Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.setMeteredKey("************", "************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

System.out.println(workbook.isLicensed());

//Get the Consumption quantity

double amountBefore = Metered.getConsumptionQuantity();

System.out.println(amountBefore);

Workbook workbook2 = new Workbook("Book1.xlsx");

workbook2.save("out1.xlsx");

//Get the Consumption quantity again which should be greater a bit

double amountAfter = Metered.getConsumptionQuantity();

System.out.println(amountAfter);

{{< /highlight >}}
