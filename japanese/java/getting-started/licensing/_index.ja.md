---
title: Licensing
type: docs
weight: 50
url: /ja/java/licensing/
description: JAVA の Aspose.Cells では、さまざまな購入プランが提供されるか、Licensing と Java のサブスクリプション ポリシーを使用した評価用の無料トライアルと 30 日間の一時ライセンスが提供されます。
keywords: Java Apply License from Disk or Stream. Java Set License from Disk or Stream. Apply License in Aspose.Cells for Java.
---
##  **Aspose.Cells コンポーネントにライセンスを適用する方法**

ライセンスは、製品名、ライセンスが付与されている開発者の数、サブスクリプションの有効期限などの詳細が含まれるプレーン テキストの XML ファイルです。ファイルはデジタル署名されているため、ファイルを変更しないでください。ファイルに不注意で余分な改行を追加した場合でも、ファイルは無効になります。

Aspose.Cells の評価制限を回避するには、Aspose.Cells を利用する前にライセンスを設定する必要があります。ライセンスを設定する必要があるのは、アプリケーションまたはプロセスごとに 1 回だけです。

ライセンスは、次の場所にあるストリームまたはファイルからロードできます。

1. 明示的なパス。
1. Aspose.Cells.jar が含まれるフォルダー。

使用[License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) メソッドでコンポーネントのライセンスを取得します。多くの場合、ライセンスを設定する最も簡単な方法は、次の例に示すように、ライセンス ファイルを Aspose.Cells.jar と同じフォルダーに置き、パスを指定せずにファイル名だけを指定することです。

###  **ディスクからライセンスを適用する方法**

この例では**Aspose.Cells**は、アプリケーションの JAR が含まれるフォルダー内のライセンス ファイルの検索を試みます。

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

###  **ストリームからライセンスを適用する方法**

ストリームからライセンスを初期化します。

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

###  **Aspose.Cells.GridWeb でライセンスを適用する方法**

ライセンス コードは、Web アプリケーション内の最初に処理される場所に配置することをお勧めします。

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **従量制課金ライセンスを適用する方法**

Aspose.Cells を使用すると、開発者は従量制キーを適用できます。これは新しいライセンスメカニズムです。新しいライセンス メカニズムは、既存のライセンス方式と併用されます。 API 機能の使用量に基づいて請求されることを希望する顧客は、従量制ライセンスを使用できます。詳細については、を参照してください。[従量制 Licensing よくある質問](https://purchase.aspose.com/faqs/licensing/metered)セクション。

新しいクラス[従量制](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)従量制キーを適用するために導入されました。以下は、従量制の公開キーと秘密キーを設定する方法を示すサンプル コードです。

{{< highlight "java" >}}

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
