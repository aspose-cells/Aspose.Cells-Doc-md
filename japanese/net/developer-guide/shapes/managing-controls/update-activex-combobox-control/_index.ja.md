---
title: ActiveX ComboBox コントロールの更新
type: docs
weight: 170
url: /ja/net/update-activex-combobox-control/
---
## **考えられる使用シナリオ**
Aspose.Cells を使用して、ActiveX ComboBox コントロールの値を読み書きできます。次の方法で ActiveX コントロールにアクセスしてください。[Shape.ActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol)プロパティとそのタイプを介して確認します[ActiveXControl.Type](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/activexcontrolbase/properties/type)プロパティ、それは返す必要があります[ControlType.ComboBox](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype)値を入力し、それを型キャストします[ComboBoxActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol)オブジェクトを取得し、そのさまざまなプロパティを読み取りまたは変更します。

をダウンロードしてください[サンプルエクセルファイル](5115124.xlsx)次のサンプル コードで使用されます。
## **ActiveX ComboBox コントロールの更新**
次のスクリーンショットは、サンプル コードの効果を示しています。[サンプルエクセルファイル](5115124.xlsx).ご覧のとおり、ActiveX ComboBox の値が「これはコンボ ボックス コントロールです」に更新されました。

|![todo:画像_代替_文章](update-activex-combobox-control_1.png)|
|:- |
## **サンプルコード**
次のサンプル コードは、内部にある ActiveX ComboBox コントロールの値を更新します。[サンプルエクセルファイル](5115124.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.cs" >}}
