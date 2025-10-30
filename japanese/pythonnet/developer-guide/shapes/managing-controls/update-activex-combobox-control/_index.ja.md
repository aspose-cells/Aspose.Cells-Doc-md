---
title: ActiveX ComboBoxコントロールを更新
type: docs
weight: 170
url: /ja/python-net/update-activex-combobox-control/
---

## **可能な使用シナリオ**
Aspose.Cells for Python via .NETを使用してActiveXコンボボックスコントロールの値を読み書きできます。[Shape.active_x_control](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control)プロパティを介してActiveXコントロールにアクセスし、その[type](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/activexcontrolbase/type/)を確認してください。値は[ControlType.COMBO_BOX](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype)を返し、それを[ComboBoxActiveXControl](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol)オブジェクトにタイプキャストし、その様々なプロパティを読み取ったり変更したりできます。

以下のサンプルコードで使用される[サンプルExcelファイル](5115124.xlsx)をダウンロードしてください。
## **ActiveX ComboBoxコントロールを更新**
以下のスクリーンショットは、[サンプルExcelファイル](5115124.xlsx)に対するサンプルコードの効果を示しています。見るとおり、ActiveX ComboBoxの値が"これはコンボボックスコントロールです"に更新されています。

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **サンプルコード**
次のサンプルコードでは、[サンプルExcelファイル](5115124.xlsx)内のActiveX ComboBoxコントロールの値を更新します。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-UpdateActiveXComboBoxControl.py" >}}
{{< app/cells/assistant language="python-net" >}}
