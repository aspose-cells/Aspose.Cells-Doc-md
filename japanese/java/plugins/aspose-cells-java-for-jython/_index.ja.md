---
title: Aspose.Cells Java for Jython
type: docs
weight: 70
url: /ja/java/aspose-cells-java-for-jython/
---

## **紹介**

### **Jythonとは何ですか?**

JythonはPythonのJava実装であり、表現力と明瞭さを兼ね備えています。Jythonは商用および非商用の両方で無料で利用可能であり、ソースコードと一緒に配布されています。JythonはJavaと相補的であり、特に次のタスクに適しています:

- **組み込みスクリプト** - JavaプログラマーはJythonライブラリをシステムに追加して、エンドユーザーがアプリケーションに機能を追加するための単純または複雑なスクリプトを書けるようにすることができます。
- **インタラクティブな実験** - Jythonは、Javaパッケージや実行中のJavaアプリケーションとやりとりするために使用できる対話型インタプリタを提供します。これにより、プログラマーはJythonを使用して任意のJavaシステムを実験およびデバッグできます。
- **迅速なアプリケーション開発** - Pythonプログラムは通常、同等のJavaプログラムよりも2〜10倍短くなります。これは直接、プログラマーの生産性向上につながります。PythonとJavaのシームレスな相互作用により、開発中および製品の出荷時に両言語を自由に混在させることができます。

### **Aspose.Cells for Java**

Aspose.Cells for Javaは、Javaの高度なクラスライブラリであり、Java内で幅広いドキュメント処理タスクを直接実行できるようにします。
アプリケーション。

Aspose.Cells for Javaは、Cells（DOC、DOCX、OOXML、RTF）HTML、OpenDocument、PDF、EPUB、XPS、SWF、およびすべての画像フォーマットの処理をサポートしています。Aspose.Cellsを使用すると、Microsoft Cellsを使用せずにドキュメントを生成、変更、および変換できます。
Aspose.Cells Java for Struts 1.3ウェブアプリケーションのシステム要件は次のとおりです。

### **Aspose.Cells Java for Jython**

Aspose.Cells Java for Jythonは、JythonでのAspose.Cells for Java APIの使用例を示すプロジェクトです/提供します

## **システム要件およびサポートされるプラットフォーム**

### **システム要件**

- インストールされているJava 1.5以上

- Aspose.Cellsコンポーネントをダウンロード済み
- Aspose.Cellsコンポーネントをダウンロードしてください
- Jython 2.7.0

### **サポートされているプラットフォーム**

**サポートされているプラットフォームは次のとおりです:**

- Aspose.Cells 15.4およびそれ以上。
- Java IDE（Eclipse、NetBeans ...）

## **インストールと使用のダウンロード**

### **ダウンロード**

**ソーシャルコーディングWebサイトから例をダウンロード**

実行例の次のリリースを以下で言及されるすべてのソーシャルコーディングサイトからダウンロードできます:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**Aspose.Cells for Javaコンポーネントをダウンロード**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **インストール**

- ダウンロードしたAspose.Cells for Java JARファイルを「lib」ディレクトリに配置します。
- _*init*_.pyファイルで「your-lib」をダウンロードしたJARファイル名に置き換えます。

### **を使用する**

次の例コードを使用してHelloWorldドキュメントを作成できます:

{{< highlight java >}}

 from aspose-cells  import Settings

from com.aspose.Cells import Document

from com.aspose.Cells import DocumentBuilder

class HelloWorld:

    def __init__(self):

        dataDir = Settings.dataDir + 'quickstart/'



        workbook = Workbook()



        sheet = workbook.getWorksheets().get(0)



        cell = sheet.getCells().get("A1")



        cell.setValue("Hello World!")



        file_format_type = FileFormatType



        workbook.save(dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )



        print "Document has been saved, please check the output file.";

if __name__ == '__main__':

    HelloWorld()

{{< /highlight >}}

## **サポート、拡張、貢献**

### **サポート**

Asposeが立ち上がって最初の日から、良い製品だけを提供するだけでは不十分だと分かっていました。良いサービスも提供する必要がありました。私たち自身も開発者であり、技術的な問題やソフトウェアの不具合が必要なことを妨げるときにどれだけイライラするか理解しています。私たちは問題を解決するためにここにいて、それを作り出すためではありません。

そのため、無料サポートを提供しています。製品を購入したか、評価を使用しているかに関わらず、私たちの製品を使用するすべての人にフルの注意と尊敬を提供する価値があります。

Aspose.Cells Java for Jythonに関連する問題や提案をログに記録することができます。ログを記録できるプラットフォームは以下のいずれかです:

- [Github](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **拡張と貢献**

Aspose.Cells Java for Jythonはオープンソースであり、そのソースコードは以下にリストアップされた主要なソーシャルコーディングウェブサイトで利用できます。開発者はソースコードをダウンロードし、新しい機能の提案や追加、または既存の機能の改善を行うことを奨励されており、他の人がその恩恵を受けられるようになっています。

### **ソースコード**

最新のソースコードを以下の場所から取得できます

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
