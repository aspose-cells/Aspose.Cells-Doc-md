---
title: ライセンス
type: docs
weight: 50
url: /ja/java/licensing/
---
{{% alert color="primary" %}} 

の評価版をダウンロードできます**Aspose.Cells**for Java から[そのダウンロードページ](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) Maven リポジトリ。評価版は、製品のライセンス版とまったく同じ機能を提供します。さらに、評価版は、ライセンスを購入し、数行のコードを追加してライセンスを適用するだけで、ライセンスが付与されます。

評価に満足したら**Aspose.Cells**、 あなたはできる[ライセンスを購入する](https://purchase.aspose.com)Aspose ウェブサイトで。提供されるさまざまなサブスクリプションの種類に慣れてください。ご不明な点がございましたら、お気軽に Aspose 営業チームまでお問い合わせください。

すべての Aspose ライセンスには、この期間中に出てくる新しいバージョンまたは修正への無料アップグレードのための 1 年間のサブスクリプションが含まれています。テクニカル サポートは無料で無制限で、ライセンス ユーザーと評価ユーザーの両方に提供されます。

{{% /alert %}} {{% alert color="primary" %}} 

テストしたい場合**Aspose.Cells**評価版の制限がない場合は、30 日間の一時ライセンスをリクエストしてください。を参照してください。[仮免許を取得するには？](https://purchase.aspose.com/temporary-license)詳細については。

{{% /alert %}}

## **評価版の制限事項**

の評価版**Aspose.Cells**製品 (ライセンスが指定されていない) は製品の全機能を提供しますが、1 つのプログラムで 100 個のファイルを開くことができ、評価用のウォーターマーク付きの追加のワークシートに制限されています。

制限事項を以下に示します。

### **第 1 の制限: 開いているファイルの数**

プログラムを実行すると、100 個の Excel ファイルしか開くことができません。アプリケーションがこの数を超えると、例外がスローされます。

### **2 番目の制限: 評価用透かし付きワークシート**

![todo:画像_代替_文章](licensing_1.png)

このワークシートは常にアクティブなワークシートとして表示されます。ライセンス版のみ、アクティブなワークシートを他のワークシートに設定できます。

## **ライセンスの設定**

ライセンスは、製品名、ライセンスが付与されている開発者の数、サブスクリプションの有効期限などの詳細を含むプレーン テキストの XML ファイルです。ファイルはデジタル署名されているため、ファイルを変更しないでください。ファイルに余分な改行を誤って追加しても、それは無効になります。

評価制限を回避したい場合は、Aspose.Cells を利用する前にライセンスを設定する必要があります。アプリケーションまたはプロセスごとに 1 回だけライセンスを設定する必要があります。

ライセンスは、次の場所にあるストリームまたはファイルからロードできます。

1. 明示的なパス。
1. Aspose.Cells.jar を含むフォルダー。

使用[License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) コンポーネントのライセンスを取得する方法。多くの場合、ライセンスを設定する最も簡単な方法は、次の例に示すように、ライセンス ファイルを Aspose.Cells.jar と同じフォルダーに置き、パスを指定せずにファイル名のみを指定することです。

### **例 1**

この例では**Aspose.Cells**は、アプリケーションの JAR を含むフォルダーでライセンス ファイルを見つけようとします。

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **例 2**

ストリームからライセンスを初期化します。

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Aspose.Cells.GridWebでのライセンス申請に関する注意事項**

ライセンス コードは、最初に処理する Web アプリケーション内の場所に配置することをお勧めします。

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **従量制ライセンスの適用**

Aspose.Cells を使用すると、開発者は従量制のキーを適用できます。これは、新しいライセンス メカニズムです。新しいライセンス メカニズムは、既存のライセンス方法と共に使用されます。 API 機能の使用量に基づいて課金されることを希望するお客様は、従量制ライセンスを使用できます。詳細については、を参照してください。[従量制ライセンスに関する FAQ](https://purchase.aspose.com/faqs/licensing/metered)セクション。

新しいクラス[従量制](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)従量制キーを適用するために導入されました。以下は、従量制の公開鍵と秘密鍵を設定する方法を示すサンプル コードです。

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
