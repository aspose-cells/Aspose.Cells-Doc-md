---
title: Установка тени текстовых эффектов формы или текстового поля
type: docs
weight: 250
url: /ru/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

Вы можете установить **Тень** из **Текстовых эффектов** любой формы или текстового поля. Пожалуйста, используйте свойство [**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody). Оно представляет установку текста формы и возвращает объекты [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting). После получения доступа к нему, пожалуйста, установите **Тень** через свойство [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype). Это свойство имеет тип [**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype), который имеет несколько значений. Некоторые из них -

- Смещение по диагонали вниз и вправо
- Смещение вниз
- Смещение по диагонали вверх и вправо
- Слева внутри
- По центру внутри
- Диагональная перспектива вверху слева
- ПерспективаДиагональНижнийПравый

{{% /alert %}}

Приведенный ниже код демонстрирует использование свойства [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) для установки тени эффектов текста формы или текстового поля.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
