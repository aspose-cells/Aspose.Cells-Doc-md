---
title: PHP で Aspose.Cells をダウンロードして構成する
type: docs
weight: 10
url: /ja/java/download-and-configure-aspose-cells-in-php/
---
## **必要なライブラリをダウンロード**
下記の必要なライブラリをダウンロードします。これらは、Aspose.Cells Java for PHP の例を実行するために必要です。

- **Aspose:** [Aspose.Cells for Java コンポーネント](https://downloads.aspose.com/cells/java/)
- [PHP/Java ブリッジ](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **ソーシャル コーディング サイトからサンプルをダウンロードする**
実行中のサンプルの次のリリースは、以下のソーシャル コーディング サイトからダウンロードできます。

-----
### **GitHub**
- **Aspose.Cells Java for PHP 例** 
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **Linux プラットフォームでソース コードを構成する方法**
使用中にソース コードを開いて拡張するには、次の簡単な手順に従ってください。
## **1. Tomcat サーバーをインストールする**
Tomcat サーバーをインストールするには、Linux コンソールで次のコマンドを発行します。これにより、Tomcat サーバーが正常にインストールされます。

{{< highlight "actionscript3" >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. PHP/JavaBridge をダウンロードして構成する**
PHP/JavaBridge バイナリをダウンロードするには、Linux コンソールで次のコマンドを発行します。

{{< highlight "actionscript3" >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Linux コンソールで次のコマンドを発行して、PHP/JavaBridge バイナリを解凍します。

{{< highlight "actionscript3" >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


これは抽出します**JavaBridge.war**ファイル。それを tomcat88 にコピーします。**ウェブアプリ**Linux コンソールで次のコマンドを発行して、フォルダを削除します。

{{< highlight "actionscript3" >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


コピーすることで、tomcat8は自動的に新しいフォルダを作成します」**JavaBridge**" の**ウェブアプリ**.フォルダが作成されたら、tomcat8 が実行されていることを確認してから確認してください<http://localhost:8080/JavaBridge>ブラウザで、JavaBridge のデフォルト ページを開く必要があります。

エラーメッセージが表示されたらインストール**高速CGI**Linux コンソールで次のコマンドを発行します。

{{< highlight "actionscript3" >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

php5.5 cgiをインストール後、tomcat8サーバーを再起動して確認<http://localhost:8080/JavaBridge>再びブラウザで。

もしも**JAVA_HOME**エラーが表示されたら、/etc/default/tomcat8 ファイルを開き、JAVA_HOME を設定する行のコメントを外します。ブラウザで <http://localhost:8080/JavaBridge> を再度確認すると、PHP/JavaBridge Examples ページが表示されます。
## **3. Aspose.Cells Java for PHP の例を設定します。**
 webapps/JavaBridge フォルダー内で次のコマンドを発行して、PHP の例を複製します。

{{< highlight "actionscript3" >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP]{{< /highlight >}}

## **Windows プラットフォームでのソース コードの設定方法**
以下の簡単な手順に従って、Windows プラットフォームで PHP/Java Bridge を構成してください。

\1. PHP5 をインストールし、通常どおりに構成します
\2.まだインストールしていない場合は、JRE 6 (Java ランタイム環境) をインストールします。これは C:\Program Files などで確認できます。ここからダウンロードできます。 PHP Java Bridge (PJB) と互換性があるため、JRE 6 を使用しています。

\3. Apache Tomcat 8.0 をインストールします。ここからダウンロードできます

4.ダウンロード[JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download).このファイルを tomcat webapps ディレクトリにコピーします。
(例: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

\5. Tomcat Apache サービスを再起動します。

 6.に行く<http://localhost:8080/JavaBridge/test.php>PHPが動作するかどうかを確認します。そこに他の例を見つけることができます

7. Aspose.Cells Java jar ファイルを C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib にコピーします。

 \8.クローン[Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ フォルダー内の例。

\8.フォルダー C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java を Aspose.Cells Java for PHP のサンプル フォルダーにコピーします。

 10円。 Apache tomcat サービスを再起動し、例を使用して開始します。
