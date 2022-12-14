---
title: Установка теней для текстовых эффектов фигуры или текстового поля
type: docs
weight: 670
url: /ru/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}} 

 Вы можете установить**Тень** из**Текстовые эффекты** любой фигуры или текстового поля. Пожалуйста, используйте[Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody) имущество. Он представляет настройку текста формы и возвращает[FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection) . После доступа[Настройка шрифта](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) от него, пожалуйста, установите**Тень** с помощью[FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType) имущество. Это свойство имеет тип[PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType)который имеет несколько значений. Некоторые из них

- [КОМПЕНСИРОВАТЬ_ДИАГОНАЛЬ_НИЖНИЙ ПРАВЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [OFFSET_BOTTOM](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [КОМПЕНСИРОВАТЬ_ДИАГОНАЛЬ_В ПРАВОМ ВЕРХНЕМ УГЛУ](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [INSIDE_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [ВНУТРИ_ЦЕНТРА](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [ПЕРСПЕКТИВА_ДИАГОНАЛЬ_ВЕРХНИЙ ЛЕВЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [ПЕРСПЕКТИВА_ДИАГОНАЛЬ_ВЕРХНИЙ ПРАВЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **Установка теней для текстовых эффектов фигуры или текстового поля**
 На следующем снимке экрана показано[выходной файл excel](5473446.xlsx) созданный с помощью следующего примера кода. На скриншоте также показано значение**Тень** который был установлен как**Смещение снизу**.

![дело:изображение_альтернативный_текст](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
