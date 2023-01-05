---
title: Aspose.Cells Jython の場合は Java
type: docs
weight: 70
url: /ja/java/aspose-cells-java-for-jython/
---
## **序章**

### **ジソンとは？**

Jython は Python の Java 実装であり、表現力と明快さを兼ね備えています。 Jython は、商用および非商用の両方で自由に利用でき、ソース コードとともに配布されます。 Jython は Java を補完するものであり、特に次のタスクに適しています。

- **埋め込みスクリプト** Java プログラマは、Jython ライブラリをシステムに追加して、エンド ユーザーがアプリケーションに機能を追加する単純または複雑なスクリプトを作成できるようにします。
- **インタラクティブな実験** Jython は、Java パッケージまたは実行中の Java アプリケーションと対話するために使用できる対話型インタープリターを提供します。これにより、プログラマーは Jython を使用して任意の Java システムを実験およびデバッグできます。
- **迅速なアプリケーション開発** Python プログラムは通常、同等の Java プログラムよりも 2 ～ 10 倍短いです。これは、プログラマーの生産性の向上に直接つながります。 Python と Java の間のシームレスなやり取りにより、開発者は開発中および製品の出荷時に 2 つの言語を自由に混在させることができます。

### **Aspose.Cells for Java**

Aspose.Cells for Java は高度なクラス ライブラリ for Java であり、Java 内でさまざまなドキュメント処理タスクを直接実行できます。
アプリケーション。

Aspose.Cells for Java は、Cells (DOC、DOCX、OOXML、RTF) HTML、OpenDocument、PDF、EPUB、XPS、SWF およびすべての画像形式の処理をサポートします。 Aspose.Cellsでできます
Microsoft Cells を使用せずにドキュメントを生成、変更、および変換します。

### **Aspose.Cells Jython の場合は Java**

Aspose.Cells Java for Jython は、Jython での Aspose.Cells for Java API の使用例をデモンストレーション/提供するプロジェクトです。

## **システム要件とサポートされるプラットフォーム**

### **システム要求**

**Jython で Aspose.Cells Java を使用するためのシステム要件は次のとおりです。**

- Java 1.5以上搭載
- ダウンロードした Aspose.Cells コンポーネント
- Jython 2.7.0

### **サポートされているプラットフォーム**

**サポートされているプラットフォームは次のとおりです。**

- Aspose.Cells 15.4 以上。
- Java IDE (Eclipse、NetBeans ...)

## **ダウンロード インストールと使用方法**

### **ダウンロード中**

**ソーシャル コーディング Web サイトからサンプルをダウンロードする**

実行中のサンプルの次のリリースは、以下で言及されているすべてのソーシャル コーディング サイトでダウンロードできます。

- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**Aspose.Cells for Java コンポーネントをダウンロード**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **インストール**

- ダウンロードした Aspose.Cells for Java jar ファイルを「lib」ディレクトリに配置します。
- _*init*_.py ファイルで、「your-lib」をダウンロードした jar ファイル名に置き換えます。

### **使用する**

次のコード例を使用して、HelloWorld ドキュメントを作成できます。

{{< highlight "java" >}}

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

Aspose の最初の日から、私たちはお客様に良い製品を提供するだけでは十分ではないことを知っていました。また、優れたサービスを提供する必要もありました。私たち自身も開発者であり、技術的な問題やソフトウェアの異常によって必要な作業ができなくなると、どれほどイライラするかを理解しています。問題を作成するのではなく、問題を解決するためにここにいます。

そのため、無料サポートを提供しています。私たちの製品を購入したか、評価を使用しているかにかかわらず、私たちの製品を使用するすべての人は、私たちの十分な注意と尊敬に値します.

次のプラットフォームのいずれかを使用して、Jython の Aspose.Cells Java に関連する問題または提案をログに記録できます。

- [ギットハブ](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **拡張して貢献する**

Aspose.Cells Java Jython はオープン ソースであり、そのソース コードは、以下に示す主要なソーシャル コーディング Web サイトで入手できます。開発者は、ソース コードをダウンロードし、新しい機能を提案または追加するか、既存の機能を改善することによって貢献することをお勧めします。これにより、他の人もその恩恵を受けることができます。

### **ソースコード**

最新のソース コードは、次のいずれかの場所から入手できます。

- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
