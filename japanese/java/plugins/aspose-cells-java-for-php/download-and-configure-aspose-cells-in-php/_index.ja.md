---
title: PHPでAspose.Cellsをダウンロードして構成する
type: docs
weight: 10
url: /ja/java/download-and-configure-aspose-cells-in-php/
---

## **必要なライブラリのダウンロード**
以下に記載されている必須ライブラリをダウンロードしてください。これらはAspose.Cells Java for PHPの例の実行に必要です。

- **Aspose:** [Aspose.Cells for Java コンポーネント](https://downloads.aspose.com/cells/java/)
- [PHP/Java Bridge](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **ソーシャルコーディングサイトから例をダウンロードする**
実行中の例のリリースは、以下に記載されているソーシャルコーディングサイトでダウンロードできます：

-----
### **GitHub**
- **Aspose.Cells Java for PHP Examples** 
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **Linuxプラットフォーム上のソースコードの構成方法**
次のシンプルな手順に従ってソースコードを開いて拡張する方法を見ていきます
## **1. Tomcatサーバーのインストール**
Tomcatサーバーをインストールするには、Linuxコンソールで以下のコマンドを入力してください。これにより、Tomcatサーバーが正常にインストールされます。 

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. PHP/JavaBridgeのダウンロードと構成**
PHP/JavaBridgeのバイナリをダウンロードするには、Linuxコンソールで以下のコマンドを入力してください。 

{{< highlight actionscript3 >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


次のコマンドをLinuxコンソールで入力して、PHP/JavaBridgeのバイナリを解凍してください。 

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


これにより、**JavaBridge.war** ファイルが展開されます。次に、次のコマンドをLinuxコンソールで入力して、このファイルをtomcat88の **webapps** フォルダにコピーしてください。 

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


By copying, tomcat8 will automatically create a new folder "**JavaBridge**" in **webapps**. Once the folder is created, make sure your tomcat8 is running and then check <http://localhost:8080/JavaBridge> in browser, it should open a default page of JavaBridge. 

エラーメッセージが表示された場合は、次のコマンドをLinuxコンソールで入力して **FastCGI** をインストールしてください。

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

After installing php5.5 cgi, restart tomcat8 server and check <http://localhost:8080/JavaBridge> again in the browser.

If **JAVA_HOME** error is displayed, then open /etc/default/tomcat8 file and uncomment the line that sets the JAVA_HOME. Check <http://localhost:8080/JavaBridge> in browser again, it should come with PHP/JavaBridge Examples page. 
## **3. Aspose.Cells Java for PHPの構成**
webapps/JavaBridgeフォルダ内で以下のコマンドを入力して、PHPの例をクローンしてください。  

{{< highlight actionscript3 >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP] 

{{< /highlight >}}

## **Windowsプラットフォームでのソースコードの構成方法**
Windowsプラットフォーム上でPHP/Java Bridgeを構成するためには、以下の簡単な手順に従ってください。

\1. PHP5をインストールし、通常どおりに構成してください。
\2. JRE 6（Javaランタイム環境）をインストールしていない場合は、C:\Program Filesなどで確認できます。 ダウンロードはこちら できます。私はJRE 6を使用しています。それはPHP Java Bridge（PJB）と互換性があるためです。

\3. Apache Tomcat 8.0をインストールしてください。ダウンロードはこちら できます。

4. [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download) をダウンロードしてください。 このファイルをtomcatのwebappsディレクトリにコピーしてください。
（例： C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps）

\5. tomcat apacheサービスを再起動してください。

6.Go to <http://localhost:8080/JavaBridge/test.php> to check if php works. You can find other examples in there

7. Aspose.Cells JavaのjarファイルをC：\ Program Files\ Apache Software Foundation\ Tomcat 8.0\ webapps\ JavaBridge\ WEB-INF\ libにコピーします

\8. [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) の例をC:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\フォルダ内にクローンしてください。

\8. フォルダ C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java を、Aspose.Cells Java for PHPの例フォルダにコピーしてください。

\10. apache tomcatサービスを再起動し、例を使用し始めてください。 
