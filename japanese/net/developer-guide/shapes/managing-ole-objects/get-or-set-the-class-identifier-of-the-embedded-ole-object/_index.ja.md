---
title: 埋め込み OLE オブジェクトのクラス識別子を取得または設定します
type: docs
weight: 200
url: /ja/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---
## **考えられる使用シナリオ**
Aspose.Cells は[OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier)埋め込まれた ole オブジェクトのクラス識別子を取得または設定するために使用できるプロパティ。 Ole Object Class Identifiers は、実際には GUID、つまり Globally Unique Identifiers です。 GUID は常に 16 バイト長であるため、クラス識別子も 16 バイト長です。それらは多くの場合、Windows レジストリ内にあり、クライアント アプリケーション内のさまざまな埋め込みリソースを含む埋め込み ole オブジェクトを開く方法に関する情報をホスト アプリケーションに提供します。
## **埋め込み OLE オブジェクトのクラス識別子を取得または設定します**
次のスクリーンショットは、Ole オブジェクト クラス識別子、つまり、[サンプルエクセルファイル](5115190.xls)埋め込まれた PowerPoint ole オブジェクトを含みます。

![todo:画像_代替_文章](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **サンプルコード**
で実行した次のサンプル コードを参照してください。[サンプルエクセルファイル](5115190.xls)Oleオブジェクトのクラス識別子、つまりGUIDを出力するコンソール出力。印刷された GUID は、スクリーンショット内に示されているものとまったく同じです。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **コンソール出力**
これは、上記のサンプル コードを次のコマンドで実行したときのコンソール出力です。[サンプルエクセルファイル](5115190.xls).

{{< highlight "java" >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
