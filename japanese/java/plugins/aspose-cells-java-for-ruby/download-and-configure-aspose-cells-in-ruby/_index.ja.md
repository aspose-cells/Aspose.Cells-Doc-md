---
title: RubyでAspose.Cellsをダウンロードして構成する
type: docs
weight: 10
url: /ja/java/download-and-configure-aspose-cells-in-ruby/
---

## **必要なライブラリのダウンロード**
以下に記載されている必要なライブラリをダウンロードしてください。これらはAspose.Cells Java for Rubyの実行に必要です。

- [Aspose.Cells for Javaコンポーネント](https://downloads.aspose.com/cells/java/)
## **ソーシャルコーディングサイトから例をダウンロードする**
実行中の例のリリースは、以下に記載されているソーシャルコーディングサイトでダウンロードできます：

**GitHub**

- [Aspose.Cells Java for Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **インストール**
Aspose.cells Java for Ruby gemをインストールすることは非常に簡単です。次の簡単な手順に従ってください:

1. アプリケーションのGemfileに次の行を追加します。 

{{< highlight java >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

2. そして実行します。 

{{< highlight java >}}

 $ bundle

{{< /highlight >}}

**または**

1. 以下のコマンドを実行します。 

{{< highlight java >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **を使用する**
helloworldの例を扱うために必要なファイルを含めます。

{{< highlight java >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

上記のコードを理解しましょう。

1. 最初の行は、Aspose Cellsがロードされて利用可能であることを確認します。
1. Aspose Cellsにアクセスするために必要なファイルを含める。
1. ライブラリを初期化します。Aspose JAVAクラスは、aspose.ymlファイルで提供されたパスからロードされます。
