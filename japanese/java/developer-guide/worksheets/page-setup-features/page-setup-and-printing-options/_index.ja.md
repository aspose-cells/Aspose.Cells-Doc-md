---
title: ページ設定と印刷オプション
type: docs
weight: 10
url: /ja/java/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

開発者は、印刷プロセスを制御するためにページ設定と印刷設定を構成する必要がある場合があります。ページ設定と印刷設定にはさまざまなオプションがあり、Aspose.Cells で完全にサポートされています。

この記事では、コンソール アプリケーションを作成し、Aspose.Cells API.

{{% /alert %}}

## **ページおよび印刷設定の操作**

この例では、Microsoft Excel でワークブックを作成し、Aspose.Cells を使用してページ設定と印刷オプションを設定しました。

### **ページ設定オプションの設定**

まず、Microsoft Excel で簡単なワークシートを作成します。次に、ページ設定オプションを適用します。コードを実行すると、下のスクリーンショットのようにページ設定オプションが変更されます。

**出力ファイル** 

![todo:画像_代替_文章](page-setup-and-printing-options_1.png)

1. Microsoft Excel でいくつかのデータを含むワークシートを作成します。
 1. Microsoft Excel で新しいワークブックを開きます。
 1. データを追加します。
以下はファイルのスクリーンショットです。

      **入力ファイル**

![todo:画像_代替_文章](page-setup-and-printing-options_2.png)

1. ページ設定オプションを設定します。
ページ設定オプションをファイルに適用します。以下は、新しいオプションが適用される前のデフォルト オプションのスクリーンショットです。

   **デフォルトのページ設定オプション**

![todo:画像_代替_文章](page-setup-and-printing-options_3.png)

1. Aspose.Cells をダウンロードしてインストールします。
   1. [ダウンロード](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
1. 開発用コンピューターで解凍します。
全て[Aspose](http://www.aspose.com/)コンポーネントがインストールされると、評価モードで動作します。評価モードには時間制限がなく、生成されたドキュメントに透かしを挿入するだけです。
1. プロジェクトを作成します。
 Java エディター (Eclipse など) を使用してプロジェクトを作成するか、テキスト エディターを使用して簡単なプログラムを作成します。
1. クラスパスを追加します。
1. Aspose.Cells.zip から Aspose.Cells.jar と dom4j_1.6.1.jar を抽出します。
 1. Eclipse でプロジェクトのクラスパスを設定します。
 1. Eclipse でプロジェクトを選択し、**計画**に続く**プロパティ**.
 1. 選択**Java ビルド パス**ダイアログの左側にあります。
 1. [ライブラリ] タブを選択し、**JAR を追加する**また**外部 JAR を追加する** Aspose.Cells.jar と dom4j_1.6.1.jar を選択してビルド パスに追加します。
または、Windows の DOS プロンプトで実行時に設定することもできます。

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. API を呼び出すアプリケーションを作成します。
以下は、この例のコンポーネントで使用されるコードです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

### **印刷オプションの設定**

ページ設定には、ユーザーがワークシート ページの印刷方法を制御できるいくつかの印刷オプション (シート オプションとも呼ばれます) も用意されています。ユーザーは次のことができます。

- ワークシートの特定の印刷領域を選択します。
- タイトルを印刷します。
- グリッド線を印刷します。
- 行/列の見出しを印刷します。
- ドラフト品質を実現します。
- コメントを印刷します。
- セル エラーを出力します。
- ページの順序を定義します。

次の例では、上記の例で作成したファイル (PageSetup.xls) に印刷オプションを適用します。以下のスクリーンショットは、新しいオプションが適用される前のデフォルトの印刷オプションを示しています。
**入力ドキュメント**

![todo:画像_代替_文章](page-setup-and-printing-options_4.png)

コードを実行すると、印刷オプションが変更されます。
**出力ファイル**

![todo:画像_代替_文章](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **概要**

{{% alert color="primary" %}}

この記事では、Aspose.Cells を使用してページ設定とシート印刷オプションを設定する方法を示します。うまくいけば、いくつかの洞察が得られ、これらのオプションを独自のシナリオで使用できます。

 Aspose.Cells は、長年にわたる研究、設計、慎重なチューニングの恩恵を受けています。ご質問、ご意見、ご提案をお待ちしております。[Aspose.Cells フォーラム](https://forum.aspose.com/c/cells/9).迅速な返信を保証します。

{{% /alert %}}
