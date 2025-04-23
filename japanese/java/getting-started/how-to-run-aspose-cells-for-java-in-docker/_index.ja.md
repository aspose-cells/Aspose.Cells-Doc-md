---
title: Docker で Aspose.Cells for Java を実行する方法
type: docs
description: "Linux向けにDockerコンテナでAspose.Cells for Javaを実行する。"
weight: 139
url: /ja/java/how-to-run-aspose-cells-in-docker/
---

マイクロサービスとコンテナ化を組み合わせることで、開発スタックにどのような技術があっても、Dockerを使用してAspose.Cellsの機能を簡単に統合することができます。 Dockerを使用すると、.NET、C++、またはJavaなどの技術に関係なく、アプリケーションにAspose.Cellsの機能を簡単に統合できます。

マイクロサービスを対象としている場合、またはスタックの主要な技術が .NET、C++、Java ではなくても、Aspose.Cells の機能が必要な場合、または既にスタックで Docker を使用している場合は、Dockerコンテナで Aspose.Cells for Java を利用することに興味を持つかもしれません。

## 前提条件

- システムに Docker をインストールする必要があります。 

## Javaアプリケーションの作成

この例では、簡単な xlsx ファイルを作成し、保存し、読み込む Java アプリケーションを作成します。そのアプリケーションは Docker でビルドして実行できます。

### Javaアプリケーションの作成

Eclipse を使用して次のコードで Java アプリケーションを作成します。この例では、Aspose.Cells for Java を使用して新しい xlsx ワークシートを作成し、そのシート名とセル値を設定し、その後それらを読み取り出力します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "TestDocker.java" >}}

### Javaアプリケーションをjarパッケージにする

次の図は、Eclipse の「エクスポート」メニューを使用して jar パッケージを作成する方法を示しています。

**![Eclipseを使用してJarを作成](MakeJar.png)**

Aspose.Cells for Java を使用して Java プログラムを書いたので、jar パッケージを取得しました。次に、dockerfile を作成します。

### Dockerfileの設定

次に、Dockerfileを作成および構成します。

1. Dockerfile を作成し、jar パッケージと隣接する位置に配置します。このファイル名は拡張子なしで維持します（デフォルトのまま）。
2. Dockerfile で次を指定します：

{{< highlight plain >}}
   FROM williamyeh/java8:latest

   VOLUME /tmp

   ADD TestDocker.jar app.jar

   ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
{{< /highlight >}}

### Dockerでアプリケーションのビルドと実行

今、アプリケーションは Docker でビルドおよび実行できます。お気に入りのコマンドプロンプトを開き、Dockerfile があるフォルダに移動し、次のコマンドを実行します：

{{< highlight plain >}}
docker build -t java-app .
{{< /highlight >}}

上記のコマンドを実行すると、XLSX ワークシートの出力とコマンドラインの結果が得られます。この時点で、Java プログラムは Linux Docker で正常に実行されました。
{{< app/cells/assistant language="java" >}}
