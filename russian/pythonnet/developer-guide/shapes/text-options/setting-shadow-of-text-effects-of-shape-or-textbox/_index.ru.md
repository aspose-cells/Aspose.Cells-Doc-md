---
title: Установка тени текстовых эффектов формы или текстового поля
type: docs
weight: 250
url: /ru/python-net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

Вы можете установить **Тень** из **Текстовых эффектов** любой формы или текстового поля. Пожалуйста, используйте свойство [**Shape.text_body**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_body). Оно представляет установку текста формы и возвращает объекты [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting). После получения доступа к нему, пожалуйста, установите **Тень** через свойство [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type). Это свойство имеет тип [**PresetShadowType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/presetshadowtype/), который имеет несколько значений. Некоторые из них -

- OFFSET_DIAGONAL_BOTTOM_RIGHT
- OFFSET_BOTTOM
- OFFSET_DIAGONAL_TOP_RIGHT
- ВНУТРЕННИЙ_СЛЕВЫЙ_УГОЛ
- ВНУТРЕННИЙ_ЦЕНТР
- ПЕРСПЕКТИВНЫЙ_ВЕРХНЯЯ_ЛЕВАЯ_ДИАГОНАЛЬ
- ПЕРСПЕКТИВНЫЙ_ВЕРХНЯЯ_ПРАВАЯ_ДИАГОНАЛЬ

{{% /alert %}}

Приведенный ниже код демонстрирует использование свойства [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type) для установки тени эффектов текста формы или текстового поля.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SettingTextEffectsShadowOfShapeOrTextbox-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
