---
title: ライセンスを適用する
type: docs
weight: 40
url: /ja/java/applying-a-license/
---

{{% alert color="primary" %}}

Aspose.Cellsの評価が完了したら、[Asposeのウェブサイト](https://purchase.aspose.com/buy)でライセンスを購入してください。提供されている異なる[ライセンスタイプ](https://purchase.aspose.com/policies/license-types/)について知っておいてください。ご質問がある場合は、[Asposeの営業チームにお問い合わせ](https://about.aspose.com/contact)してください。

Asposeのライセンスには、新しいバージョンや修正版が登場した場合に1年間の無料アップグレード資格が含まれています。テクニカルサポートは、ライセンスを取得したユーザーと評価ユーザーの両方に対して無料で無制限で提供されます。

ライセンスはプレーンテキストのXMLファイルであり、製品名、ライセンスされた開発者数、サブスクリプションの有効期限などの詳細が含まれています。ファイルはデジタル署名されているため、ファイルを変更しないでください。ファイルに余分な改行を追加すると、ファイルが無効になります。

ドキュメントの操作を行う前にライセンスを設定する必要があります。Documentオブジェクトを作成する前にこれを行う必要があります。1つのアプリケーションまたはプロセスにつき、ライセンスを1度だけ設定する必要があります。

{{% /alert %}}

## **ライセンスファイルを読み込む**

Aspose.Cells for Android via Javaでは、ライセンスは[埋め込みリソースとして](/cells/ja/java/applying-a-license/#applying-a-license-from-an-embedded-resource)使用するか、ストリームから読み込むことができます。

1. ライセンスファイルを**/mnt/sdcard/**に配置します。
1. ファイルを参照するストリームを作成します。
1. ライセンスファイルを含むストリームをSetLicenseメソッドに渡します。

**Java**

{{< highlight java >}}

 String dataDir = Environment.getExternalStorageDirectory().getPath() + "/";

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream(dataDir + "Aspose.Cells.Android.lic");

// Instantiate the License class

License license = new License();

//Set the license through the stream object

license.setLicense(fstream);

{{< /highlight >}}

### **埋め込みリソースからライセンスを適用する**

Androidパッケージファイルから名前でライセンスにアクセスします。

1. アプリケーションの**res/raw**フォルダにライセンスファイルを追加します。
   ライセンスファイルは**res/raw**フォルダに表示されるはずです。
以下のコードサンプルでリソースからライセンスをアクセス/ロードします。

**Java**

{{< highlight java >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
