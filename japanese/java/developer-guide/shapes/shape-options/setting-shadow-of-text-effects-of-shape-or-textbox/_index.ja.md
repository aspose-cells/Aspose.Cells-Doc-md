---
title: シェイプまたはテキストボックスのテキスト効果の影の設定
type: docs
weight: 670
url: /ja/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}} 

任意の形状またはテキストボックスの**テキスト効果**の**影**を設定できます。[Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody)プロパティを使用してください。これは、形状のテキストの設定を表示し、[FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection)を返します。 これから[FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting)にアクセスした後、[FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType)プロパティを使用して**Shadow**を設定してください。 このプロパティは[PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType)のタイプで、いくつかの値があります。その中には

- [OFFSET_DIAGONAL_BOTTOM_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET-DIAGONAL-BOTTOM-RIGHT)
- [OFFSET_BOTTOM](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET-BOTTOM)
- [OFFSET_DIAGONAL_TOP_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET-DIAGONAL-TOP-RIGHT)
- [INSIDE_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE-LEFT)
- [INSIDE_CENTER](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE-CENTER)
- [PERSPECTIVE_DIAGONAL_UPPER_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE-DIAGONAL-UPPER-LEFT)
- [PERSPECTIVE_DIAGONAL_UPPER_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE-DIAGONAL-UPPER-RIGHT)

{{% /alert %}} 
## **シェイプまたはテキストボックスのテキスト効果の影の設定**
次のサンプルコードで生成された[出力Excelファイル](5473446.xlsx)を次のスクリーンショットで確認できます。スクリーンショットには、**Shadow**の値が**Offset Bottom**として設定されているのが表示されています。

![todo:image_alt_text](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
{{< app/cells/assistant language="java" >}}
