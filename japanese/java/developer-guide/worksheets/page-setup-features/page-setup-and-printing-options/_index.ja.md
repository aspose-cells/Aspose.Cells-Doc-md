---
title: ページ設定および印刷オプション
type: docs
weight: 10
url: /ja/java/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

開発者は、印刷プロセスを制御するためにページ設定と印刷設定を構成する必要があります。Aspose.Cellsではページ設定と印刷設定を制御するためのさまざまなオプションがサポートされています。

この記事では、Aspose.Cells APIを使用して、数行のコードでコンソールアプリケーションを作成し、ワークシートにページの設定と印刷オプションを適用する方法を紹介しています。

{{% /alert %}}

## **ページ設定および印刷設定の操作**

この例では、Microsoft Excelでワークブックを作成し、Aspose.Cellsを使用してページ設定と印刷オプションを設定しました。

### **ページの設定オプションを設定する**

まず、Microsoft Excelで簡単なワークシートを作成します。次に、ページ設定オプションを適用します。コードを実行すると、以下のスクリーンショットのようにページ設定オプションが変更されます。

**出力ファイル** 

![todo:image_alt_text](page-setup-and-printing-options_1.png)

1. Microsoft Excelのワークシートにいくつかのデータを作成します。
   1. Microsoft Excelで新しいブックを開きます。
   1. いくつかのデータを追加します。
      以下はファイルのスクリーンショットです。

      **入力ファイル**

![todo:image_alt_text](page-setup-and-printing-options_2.png)

1. ページ設定オプションを設定します。
   ファイルにページ設定オプションを適用します。以下は、新しいオプションが適用される前のデフォルトオプションのスクリーンショットです。

   デフォルトのページ設定オプション

![todo:image_alt_text](page-setup-and-printing-options_3.png)

1. Aspose.Cellsをダウンロードしてインストールします。
   1. [ダウンロード](https://downloads.aspose.com/cells/java) Aspose.Cells for Java。
   1. 開発コンピュータにそれを解凍します。
      すべての[Aspose](http://www.aspose.com/)コンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限がなく、生成された文書にウォーターマークしか挿入されません。
1. プロジェクトを作成してください。
   Javaエディタ（たとえばEclipse）を使用してプロジェクトを作成するか、テキストエディタを使用して簡単なプログラムを作成してください。
1. クラスパスを追加します。
   1. Aspose.Cells.zipからAspose.Cells.jarとdom4j_1.6.1.jarを抽出します。
   1. Eclipseでプロジェクトのクラスパスを設定します。
   1. Eclipse でプロジェクトを選択し、**プロジェクト** をクリックしてから **プロパティ** をクリックします。
   1. ダイアログの左側で **Javaビルドパス** を選択します。
   1. ライブラリタブを選択し、**JARの追加** または **外部JARの追加** をクリックして、Aspose.Cells.jar と dom4j_1.6.1.jar を選択してビルドパスに追加します。
      または、Windows のコマンドプロンプトで実行時に設定することもできます。

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. API を呼び出すアプリケーションを作成します。
   以下は、この例でコンポーネントで使用されるコードです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

### **印刷オプションの設定**

ページ設定設定には、ワークシートページの印刷方法を制御するいくつかの印刷オプション（シートオプションとも呼ばれる）も提供されます。これにより、ユーザーは次のような操作ができます。

- ワークシートの特定の印刷エリアを選択します。
- タイトルを印刷する。
- グリッド線を印刷する。
- 行/列見出しを印刷します。
- 下書き品質を実現する。
- コメントを印刷する。
- セルエラーを印刷する。
- ページ順序を定義する。

次の例では、上記の例（PageSetup.xls）で作成されたファイルに印刷オプションを適用します。以下のスクリーンショットは、新しいオプションが適用される前のデフォルトの印刷オプションを示しています。
**入力ドキュメント**

![todo:image_alt_text](page-setup-and-printing-options_4.png)

コードを実行すると、印刷オプションが変更されます。
**出力ファイル**

![todo:image_alt_text](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **まとめ**

{{% alert color="primary" %}}

本文では、Aspose.Cellsを使用してページ設定およびシート印刷オプションを設定する方法について説明します。お役に立てれば幸いです。お客様のご質問、コメント、提案を[Apose.Cells Forum](https://forum.aspose.com/c/cells/9)で心よりお待ちしております。きめ細やかな対応を保証いたします。

Aspose.Cellsは長年にわたる研究、設計、慎重な調整の成果を受けています。ご質問、コメント、提案を心より歓迎いたします。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
