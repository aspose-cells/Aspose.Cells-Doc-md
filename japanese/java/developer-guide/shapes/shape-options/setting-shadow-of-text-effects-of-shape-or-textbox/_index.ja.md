---
title: Shape または TextBox のテキスト効果の影の設定
type: docs
weight: 670
url: /ja/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}} 

を設定できます。**影**の**テキスト効果**任意の Shape または TextBox の。をご利用ください[Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody)財産。シェイプのテキストの設定を表示して返します[フォント設定コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection).アクセス後[フォント設定](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting)そこから、**影**経由[FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType)財産。このプロパティのタイプは[PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType)これにはいくつかの値があります。これらのいくつかは

- [オフセット_対角線_右下](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [OFFSET_BOTTOM](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [オフセット_対角線_右上](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [INSIDE_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [INSIDE_CENTER](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [視点_対角線_左上](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [視点_対角線_右上](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **Shape または TextBox のテキスト効果の影の設定**
次のスクリーンショットは、[出力エクセルファイル](5473446.xlsx)次のサンプル コードで生成されます。スクリーンショットは、**影**として設定されています**オフセット下**.

![todo:画像_代替_文章](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
