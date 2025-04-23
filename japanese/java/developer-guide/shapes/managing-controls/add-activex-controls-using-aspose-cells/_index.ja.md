---
title: Aspose.Cells を使用して ActiveX コントロールを追加する
type: docs
weight: 720
url: /ja/java/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cellsを用いてActiveXコントロールを追加するには、[ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl-int-int-int-int-int-int-int-)メソッドを使用します。このメソッドは[ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType)を引数にとり、どのタイプのActiveXコントロールをワークシートに追加するかを指定します。値は以下の通りです。

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK-BOX)
- [COMBO_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO-BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND-BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST-BOX)
- [RADIO_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO-BUTTON)
- [SCROLL_BAR](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL-BAR)
- [スピンボタン](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN-BUTTON)
- [テキストボックス](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT-BOX)
- [トグルボタン](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE-BUTTON)
- [不明](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

ActiveXコントロールを形のコレクションに追加した後、[Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl)プロパティを介してActiveXコントロールオブジェクトにアクセスし、さまざまなプロパティを設定できます。

{{% /alert %}} 
## **Aspose.Cellsを使用してトグルボタンActiveXコントロールを追加**
次のサンプルコードでは、Aspose.Cellsを使用してトグルボタンActiveXコントロールを追加します。このコードで生成された[出力エクセルファイル](5473427.xlsx)を参照してください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
{{< app/cells/assistant language="java" >}}
