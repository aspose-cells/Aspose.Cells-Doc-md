---
title: ライセンスの適用
type: docs
weight: 40
url: /ja/java/applying-a-license/
---
{{% alert color="primary" %}}

Aspose.Cellsの評価に満足したら、[ライセンスを購入する](https://purchase.aspose.com/buy)Aspose ウェブサイトで。さまざまなことに慣れ親しむ[ライセンスの種類](https://purchase.aspose.com/policies/license-types/)提供されます。ご不明な点がございましたら、お気軽にお問い合わせください。[Aspose 営業チームにお問い合わせください](https://about.aspose.com/contact).

すべての Aspose ライセンスには、この期間中に出てくる新しいバージョンまたは修正への無料アップグレードのための 1 年間のサブスクリプションが含まれています。テクニカル サポートは無料で無制限で、ライセンス ユーザーと評価ユーザーの両方に提供されます。

ライセンスは、製品名、ライセンスを受けた開発者の数、サブスクリプションの有効期限などの詳細を含むプレーン テキストの XML ファイルです。ファイルはデジタル署名されているため、ファイルを変更しないでください。ファイルに余分な改行を追加しても、ファイルは無効になります。

ドキュメントの操作を行う前に、ライセンスを設定する必要があります。 Document オブジェクトを作成する前に、必ずこれを行ってください。アプリケーションまたはプロセスごとに 1 回だけライセンスを設定する必要があります。

{{% /alert %}}

## **ライセンス ファイルのロード**

Aspose.Cells for Android via Java では、ライセンスは[リソースとして組み込まれている](/cells/ja/java/applying-a-license/#applying-a-license-from-an-embedded-resource)、またはストリームからロード:

1. ライセンス ファイルを任意の場所に置きます。**/mnt/sdcard/**.
1. ファイルを参照するストリームを作成します。
1. ストリーム (ライセンス ファイルを含む) を SetLicense メソッドに渡します。

**Java**

{{< highlight "java" >}}

 String dataDir = Environment.getExternalStorageDirectory().getPath() + "/";

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream(dataDir + "Aspose.Cells.Android.lic");

// Instantiate the License class

License license = new License();

//Set the license through the stream object

license.setLicense(fstream);

{{< /highlight >}}

### **組み込みリソースからのライセンスの適用**

Android パッケージ ファイルからリソースとしてライセンスに名前でアクセスするには:

1. ライセンス ファイルをリソースとしてアプリケーションの**解像度/生**フォルダ。
ライセンス ファイルは、**解像度/生**フォルダ。
1. 次のコード サンプルを使用して、リソースからライセンスにアクセスして読み込みます。

**Java**

{{< highlight "java" >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
