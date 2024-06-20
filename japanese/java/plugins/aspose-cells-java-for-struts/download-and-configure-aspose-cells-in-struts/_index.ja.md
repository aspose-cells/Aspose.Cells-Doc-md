---
title: Aspose.CellsをStrutsにダウンロードして構成する
type: docs
weight: 10
url: /ja/java/download-and-configure-aspose-cells-in-struts/
---

- 
## **ソースコードからStruts 1.3のAspose.Cells Javaをビルドする**
上記リポジトリからソースコードをチェックアウトした後、以下のmvnコマンドを適用してください:

{{< highlight java >}}

 $ mvn -U clean package 

{{< /highlight >}}

これにより、「Strutsbookapp.war」がターゲットフォルダにビルドされます。

.warファイルをデプロイするには、それを実行中のApache tomcatサーバのwebappディレクトリにコピーするだけです。
