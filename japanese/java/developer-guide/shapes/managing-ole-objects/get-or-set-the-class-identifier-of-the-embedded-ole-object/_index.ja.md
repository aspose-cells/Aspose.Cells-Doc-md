---
title: 埋め込みOLEオブジェクトのクラス識別子を取得または設定する
type: docs
weight: 920
url: /ja/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **可能な使用シナリオ**
Aspose.Cellsは、埋め込みOLEオブジェクトのクラス識別子を取得または設定するために使用できる[OleObject.ClassIdentifier](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ClassIdentifier)プロパティを提供します。OLEオブジェクトのクラス識別子は実際にはGUID（グローバルユニーク識別子）です。 GUIDは常に16バイトの長さであり、そのためクラス識別子も16バイトの長さです。 これらはWindowsレジストリ内によく見られ、クライアントアプリケーション内のさまざまな埋め込まれたリソースを含む埋め込みOLEオブジェクトの開き方についてホストアプリケーションに情報を提供します。
## **埋め込まれたOLEオブジェクトのクラス識別子を取得または設定する**
次のスクリーンショットは、埋め込まれたPowerPointのOLEオブジェクトを含む[sample excel file](5473378.xls)から読み取られた、つまりGUIDであるOLEオブジェクトのクラス識別子を示しています。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **サンプルコード**
次のサンプルコードは、[サンプルエクセルファイル](5473378.xls)を使用して実行され、OLEオブジェクトの*クラス識別子*を出力するコンソール出力を示しています。表示されるGUIDは、スクリーンショット内に表示されるものとまったく同じです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **コンソール出力**
これは[サンプルエクセルファイル](5473378.xls)を使用して実行した上記サンプルコードのコンソール出力です。

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
