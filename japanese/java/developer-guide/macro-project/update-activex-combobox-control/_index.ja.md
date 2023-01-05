---
title: ActiveX ComboBox コントロールの更新
type: docs
weight: 900
url: /ja/java/update-activex-combobox-control/
---
## **考えられる使用シナリオ**
Aspose.Cells を使用して、ActiveX ComboBox コントロールの値を読み書きできます。次の方法で ActiveX コントロールにアクセスしてください。[Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl)プロパティとそのタイプを介して確認します[ActiveXControl.Type](https://reference.aspose.com/cells/java/com.aspose.cells/activexcontrol#Type)プロパティ、それは返す必要があります[ControlType.ComboBox](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)値を入力し、それを型キャストします[ComboBoxActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/ComboBoxActiveXControl)オブジェクトを取得し、そのさまざまなプロパティを読み取りまたは変更します。

をダウンロードしてください[サンプルエクセルファイル](5473374.xlsx)次のサンプル コードと[出力エクセルファイル](5473375.xlsx)それによって生成されます。
## **ActiveX ComboBox コントロールの更新**
次のスクリーンショットは、サンプル コードの効果を示しています。[サンプルエクセルファイル](5473374.xlsx).ご覧のとおり、ActiveX ComboBox の値が「これはコンボ ボックス コントロールです」に更新されました。

![todo:画像_代替_文章](update-activex-combobox-control_1.png)
## **サンプルコード**
次のサンプル コードは、内部にある ActiveX ComboBox コントロールの値を更新します。[サンプルエクセルファイル](5473374.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.java" >}}
