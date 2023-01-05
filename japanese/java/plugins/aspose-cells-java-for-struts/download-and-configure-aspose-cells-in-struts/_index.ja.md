---
title: Struts で Aspose.Cells をダウンロードして構成する
type: docs
weight: 10
url: /ja/java/download-and-configure-aspose-cells-in-struts/
---
- 
## **ソースコードから Struts 1.3 用に Aspose.Cells Java をビルドする**
上記のリポジトリのいずれかからソース コードをチェックアウトした後、次の mvn コマンドを適用します。

{{< highlight "java" >}}

 $ mvn -U clean package 

{{< /highlight >}}

これにより、ターゲットの Teller に「Strutsbookapp.war」がビルドされます。

.war ファイルを展開するには、実行中の Apache tomcat サーバーの webapp ディレクトリにコピーするだけです。
