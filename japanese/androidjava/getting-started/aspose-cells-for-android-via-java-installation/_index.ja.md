---
title: Aspose.Cells for Android via Java インストール
type: docs
weight: 30
url: /ja/java/aspose-cells-for-android-via-java-installation/
---
## **システム要求**
Aspose.Cells for Android via Java はプラットフォームに依存せず、Android ランタイム環境がインストールされている任意のプラットフォームで使用でき、Android OS 2.0 以降を実行する Android システムで実行されます。現在、コンポーネントは以下でテストされています。

- Android 5.1 v 22
## **Maven リポジトリから Aspose.Cells for Android via Java をインストールします。**
1. build.gradle に maven リポジトリを追加します。
1. 「Aspose.Cells for Android via Java」JAR を依存関係として追加します。

{{< highlight "java" >}}

 // 1. Add maven repository into your build.gradle 

repositories {

    mavenCentral()

    maven { url "http://repository.aspose.com/repo/" }

}

// 2. Add 'Aspose.Cells for Android via Java' JAR as a dependency

dependencies {

    ...

    ...

    compile (group: 'com.aspose', name: 'aspose-cells', version: '20.6', classifier: 'android.via.java')

}

{{< /highlight >}}
## **利用方法 Aspose.Cells for Android via Java**
このトピックでは、マシンに最新バージョンの Android Studio が既にインストールされており、最新バージョンの Aspose.Cells for Android via Java パッケージも取得していることを前提として、Android Studio IDE で Aspose.Cells for Android via Java をセットアップするために必要な手順について説明します。

{{% alert color="primary" %}} 

Android Studio をまだインストールしていない場合は、まず Android Studio のセットアップを取得して、マシンにインストールする必要があります。 Android Studio の最新バージョンは、次の場所からダウンロードできます。[ここ](https://developer.android.com/studio/index.html#win-bundle)一方、IDE のインストール方法の詳細は利用可能です。[ここ](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

 Aspose.Cells for Android via Java パッケージは からダウンロードできます[ここ](https://downloads.aspose.com/cells/androidjava)Aspose.Cells for Android via Java の各リリース パッケージは、以下に詳述するように、主に 2 つのファイルで構成されていることに注意してください。

- **aspose-cells-xxxjar** Aspose.Cells for Android via Java API からのすべての名前空間を含むメイン ライブラリ ファイルです。
- **aspose-cells-xxx-libs.apk**は、Aspose.Cells for Android via Java API が提供する暗号化および復号化機能に使用されるサードパーティの bcprov-jdk15-146.jar を含む APK です。

{{% /alert %}} 
### **Android Studio で Aspose.Cells for Android via Java を使ってみる**
Android Studio IDE が読み込まれたら、以下に示すように [File] > [New] > [New Project] をクリックします。

![todo:画像_代替_文章](aspose-cells-for-android-via-java-installation_1.png)

以下に示すように、Android Studio のウェルカム画面から新しいプロジェクトを作成することもできます。

![todo:画像_代替_文章](aspose-cells-for-android-via-java-installation_2.png)

次に、アプリケーション名、ドメイン、およびプロジェクト ファイルを保存する場所を指定するよう求められます。選択に応じてデフォルト値を変更するか、そのままにするかを選択して、[次へ] をクリックします。

![todo:画像_代替_文章](aspose-cells-for-android-via-java-installation_3.png)

次のステップでは、アプリケーションをホスト/実行する Android デバイスを指定する必要があります。選択したら、[次へ] ボタンをクリックします。

![todo:画像_代替_文章](aspose-cells-for-android-via-java-installation_4.png)

ここで、定義済みのテンプレート リストからアクティビティを選択する必要があります。デモンストレーションをシンプルにするために、以下に示すように空のアクティビティ テンプレートを選択しました。

![todo:画像_代替_文章](aspose-cells-for-android-via-java-installation_5.png)

[アクティビティのカスタマイズ] ダイアログの [完了] ボタンをクリックして、すべてのデフォルト設定をそのまま維持します。

![todo:画像_代替_文章](aspose-cells-for-android-via-java-installation_6.png)

前のステップで [完了] ボタンをクリックするとすぐに、IDE は以下に示すようにプロジェクトのビルドを開始します。終了するか、[キャンセル] ボタンをクリックします。

![todo:画像_代替_文章](aspose-cells-for-android-via-java-installation_7.png)

これでプロジェクトが IDE に読み込まれましたが、プロジェクト ファイルの完全な階層を表示できるように、ビューを [プロジェクト] に変更することをお勧めします。ビューを変更するには、次のスナップショットを確認してください。

![todo:画像_代替_文章](aspose-cells-for-android-via-java-installation_8.png)

ビューをプロジェクトに変更した後、検索してロードします**build.gradle**ファイルをエディターで開き、以下に示すように次のスニペットを貼り付けます。

{{< highlight "java" >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![todo:画像_代替_文章](aspose-cells-for-android-via-java-installation_9.png)

次に、Aspose.Cells for Android via Java Jar をプロジェクトに追加します。以下に詳述するように、2 つの重要な手順があります。

-  Aspose.Cells for Android via Java Jar を手動で**\アプリ\ライブラリ**フォルダ。
- 以下に示すように、Aspose.Cells for Android via Java Jar をライブラリとしてモジュールに追加します。

![todo:画像_代替_文章](aspose-cells-for-android-via-java-installation_10.png)

Aspose.Cells for Java.Android Jar をライブラリとして追加するモジュールを選択するよう求められます。適切に選択して、[OK] をクリックしてください。

![todo:画像_代替_文章](aspose-cells-for-android-via-java-installation_11.png)

また、APK ファイルをプロジェクトに追加する必要があります。 APK を**\app\src\main\assets**フォルダ。メイン フォルダーの下に assets フォルダーがない場合は、プロジェクト ビューでメイン ノードを右クリックして作成できます。 [新規] > [フォルダー] > [アセット フォルダー] を選択します。

![todo:画像_代替_文章](aspose-cells-for-android-via-java-installation_12.png)

APK がプロジェクトに追加されたら、プロジェクトでロードする必要があります。 APK をロードするには、次の 2 つの方法があります。

- 以下に示すスニペットを使用して APK をカスタム アプリケーション クラスにロードし、カスタム アプリケーション クラスを AndroidManifest.xml に登録します。

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- MainActivity の OnCreate メソッドで APK を読み込みます。

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

これでコードを書く準備が整いました。デモンストレーションを理解しやすくするために、ボタン ウィジェットをレイアウトに追加し、そのクリック イベントを次のように処理します。

{{< highlight "java" >}}

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

IDE インターフェースの再生ボタンを使用して (または SHIFT + F10 を使用して) アプリケーションを実行すると、エミュレーターは以下に示すようにアプリケーションをロードします。

![todo:画像_代替_文章](aspose-cells-for-android-via-java-installation_13.png)

エミュレーターのボタンをクリックすると、コードが実行され、エミュレーターの外部ストレージ フォルダーに新しいスプレッドシートが作成されます。以下に示すように、Android Device Monitor からファイルにアクセスできます。

![todo:画像_代替_文章](aspose-cells-for-android-via-java-installation_14.png)

![todo:画像_代替_文章](aspose-cells-for-android-via-java-installation_15.png)


