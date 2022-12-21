---
title: Ruby で Aspose.Cells をダウンロードして構成する
type: docs
weight: 10
url: /ja/java/download-and-configure-aspose-cells-in-ruby/
---
## **必要なライブラリをダウンロード**
下記の必要なライブラリをダウンロードします。これらは、Ruby の例で Aspose.Cells Java を実行するために必要です。

- [Aspose.Cell for Java コンポーネント](https://downloads.aspose.com/cells/java/)
## **ソーシャル コーディング サイトからサンプルをダウンロードする**
実行中のサンプルの次のリリースは、以下のソーシャル コーディング サイトからダウンロードできます。

**GitHub**

- [Aspose.Cells Ruby の場合は Java](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **インストール**
Ruby gem に Aspose.cells Java をインストールするのは非常にシンプルで簡単です。次の簡単な手順に従ってください。

1. この行をアプリケーションの Gemfile に追加します。

{{< highlight "java" >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. そして、実行します

{{< highlight "java" >}}

 $ bundle

{{< /highlight >}}

**また**

1. 次のコマンドを実行します。

{{< highlight "java" >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **使用する**
helloworld の例で作業するために必要なファイルを含めます。

{{< highlight "java" >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

上記のコードを理解しましょう。

1. 最初の行は、aspose セルがロードされ、利用可能であることを確認します。
1. aspose セルにアクセスするために必要なファイルを含めます。
1. ライブラリを初期化します。 aspose JAVA クラスは、aspose.yml ファイルで提供されるパスからロードされます。
