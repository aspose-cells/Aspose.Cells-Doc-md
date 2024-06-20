---
title: Установка тени текстовых эффектов формы или текстового поля
type: docs
weight: 670
url: /ru/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}} 

Вы можете установить **тень** **текстовых эффектов** любой формы или текстового поля. Пожалуйста, используйте свойство [Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody). Оно представляет настройку текста формы и возвращает [FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection). После получения доступа к [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) из него, установите **тень** через свойство [FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType). Это свойство имеет тип [PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType), у которого есть несколько значений. Некоторые из них:

- [СМЕЩЕНИЕ_ДИАГОНАЛЬНОЕ_СНИЗУ_СПРАВА](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [СМЕЩЕНИЕ_СНИЗУ](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [СМЕЩЕНИЕ_ДИАГОНАЛЬНОЕ_СВЕРХУ_СПРАВА](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [ВНУТРИ_СЛЕВА](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [ВНУТРИ_ПО_ЦЕНТРУ](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [ПЕРСПЕКТИВА_ДИАГОНАЛЬНАЯ_ВЕРХНЯЯ_СЛЕВА](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [ПЕРСПЕКТИВА_ДИАГОНАЛЬНАЯ_ВЕРХНЯЯ_СПРАВА](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **Настройка тени текстовых эффектов формы или текстового поля**
На следующем снимке экрана показан [исходный файл Excel вывода](5473446.xlsx), сгенерированный с помощью следующего образцового кода. На снимке экрана также показано значение **тени**, которое было установлено как **Нижняя граница**.

![todo:image_alt_text](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
