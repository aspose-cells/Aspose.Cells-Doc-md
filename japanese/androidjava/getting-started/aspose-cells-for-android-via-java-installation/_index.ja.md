---
title: Aspose.Cells for Android via Javaのインストール
type: docs
weight: 30
url: /ja/java/aspose-cells-for-android-via-java-installation/
---

## **システム要件**
Aspose.Cells for Android via Javaはプラットフォームに依存せず、Androidランタイム環境がインストールされている任意のプラットフォームで使用できます。Android OS 2.0以上のAndroidシステムで実行されます。現在、このコンポーネントは次のものとテストされています：

- Android 5.1 v 22
## **MavenリポジトリからAspose.Cells for Android via Javaをインストールする**
1. build.gradleにMavenリポジトリを追加します。 
1. 'Aspose.Cells for Android via Java' JARを依存関係として追加します。

{{< highlight java >}}

 // 1. Add maven repository into your build.gradle 

repositories {

    mavenCentral()

    maven { url "http://repository.aspose.com/repo/" }

}

// 2. Add 'Aspose.Cells for Android via Java' JAR as a dependency

dependencies {

    ...

    ...

    compile (group: 'com.aspose', name: 'aspose-cells', version: '25.9', classifier: 'android.via.java')

}

{{< /highlight >}}
## **Aspose.Cells for Android via Javaの使用方法**
このトピックでは、Android Studio IDEにAspose.Cells for Android via Javaをセットアップするための必要な手順を説明します。この手順には、マシンに最新バージョンのAndroid Studioがインストールされており、Aspose.Cells for Android via Javaの最新バージョンを取得済みであることを前提としています。

{{% alert color="primary" %}} 

まだAndroid Studioをインストールしていない場合は、まずAndroid Studioのセットアップを取得し、マシンにインストールする必要があります。最新バージョンのAndroid Studioは[ここ](https://developer.android.com/studio/index.html#win-bundle)からダウンロードできます。IDEのインストール方法の詳細については、[こちら](https://developer.android.com/studio/install.html)を参照してください。

{{% /alert %}} {{% alert color="primary" %}} 

Aspose.Cells for Android via Javaパッケージは[ここ](https://downloads.aspose.com/cells/androidjava)からダウンロードできます。Aspose.Cells for Android via Javaの各リリースパッケージには、次の2つのファイルが含まれています：

- **aspose-cells-x.x.x.jar**は、Aspose.Cells for Android via Java APIからすべての名前空間を含むメインライブラリファイルです。
- **aspose-cells-x.x.x-libs.apk**は、Aspose.Cells for Android via Java APIで提供される暗号化および復号施設用の3rdパーティbcprov-jdk15-146.jarを含むAPKです。

{{% /alert %}} 
### **Android StudioでAspose.Cells for Android via Javaを始める**
Android Studio IDEがロードされたら、ファイル > 新規 > 新しいプロジェクトをクリックします。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_1.png)

Android Studioのウェルカム画面からも新しいプロジェクトを作成できます。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_2.png)

次に、アプリケーション名、ドメイン、プロジェクトファイルの保存場所を指定するよう要求されます。デフォルト値を変更するか、そのままにして次に進んでください。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_3.png)

次に、ホスト/実行するAndroidデバイスを指定する必要があります。選択したら、次のボタンをクリックします。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_4.png)

次に、事前定義されたテンプレートの中からActivityを選択する必要があります。デモをシンプルにするために、Empty Activityテンプレートを選択しました。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_5.png)

デフォルトの設定を保持するため、アクティビティのカスタマイズダイアログの[完了]ボタンをクリックしてください。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_6.png)

前のステップの[完了]ボタンをクリックすると、下のようにIDEがプロジェクトのビルドを開始します。完了するか[キャンセル]ボタンをクリックしてください。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_7.png)

プロジェクトがIDEにロードされましたが、プロジェクトファイルの完全な階層を表示するためにビューを[Project]に変更することができます。ビューを変更するには、以下のスナップショットを確認してください。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_8.png)

プロジェクトを[Project]に変更した後、エディタで**build.gradle**ファイルを見つけてロードし、以下のスニペットを以下のように貼り付けてください。

{{< highlight java >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_9.png)

次に、Aspose.Cells for Android via Java Jarをプロジェクトに追加します。以下に詳細な2つの重要な手順があります。

- Aspose.Cells for Android via Java Jarを**\app\libs**フォルダに手動でコピーします。
- 以下に示すように、Aspose.Cells for Android via Java Jarをライブラリとしてモジュールに追加します。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_10.png)

Aspose.Cells for Java.Android Jarをライブラリとして追加するモジュールを選択するように促されます。適切な選択をして[OK]をクリックしてください。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_11.png)

また、プロジェクトにAPKファイルを追加する必要があります。APKを**\app\src\main\assets**フォルダにコピーする必要があります。メインフォルダの下にassetsフォルダがない場合は、Projectビューでメインノードを右クリックし、[New] > [Folder] > [Asset Folder]を選択して作成できます。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_12.png)

プロジェクトにAPKを追加した後、APKをプロジェクトにロードする必要があります。次に示すように、APKをロードする方法が2つあります。

- カスタムアプリケーションクラスで提供されているスニペットを使用してAPKをロードし、カスタムアプリケーションクラスをAndroidManifest.xmlに登録します。

{{< highlight java >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- MainActivityのOnCreateメソッドでAPKをロードします。

{{< highlight java >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

これでコードの記述準備が整いました。わかりやすいデモを維持するために、レイアウトにButtonウィジェットを追加し、そのクリックイベントを処理します。

{{< highlight java >}}

 private class TestTask extends AsyncTask<Void, String, Boolean> {

    @Override

    protected Boolean doInBackground(Void... params) {

        Boolean result = false;

        Workbook book = new Workbook();

        Worksheet sheet = book.getWorksheets().get(0);

        Cells cells = sheet.getCells();

        Cell cell = cells.get("A1");

        cell.putValue("Hello World!");

        try {

            book.save(SD_PATH + "output.xlsx");

        } catch (Exception e) {

            e.printStackTrace();

        }

        return result;

    }

}

{{< /highlight >}}

IDEインターフェイスの再生ボタン（またはSHIFT + F10を使用）をクリックしてアプリケーションを実行すると、エミュレータがアプリケーションをロードします。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_13.png)

エミュレータのボタンをクリックすると、コードが実行されてエミュレータの外部ストレージフォルダに新しいスプレッドシートが作成されます。Android Device Monitorからファイルにアクセスできます。

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_14.png)

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_15.png)


