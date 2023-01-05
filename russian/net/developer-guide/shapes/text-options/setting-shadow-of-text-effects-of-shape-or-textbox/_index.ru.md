---
title: Установка теней для текстовых эффектов фигуры или текстового поля
type: docs
weight: 250
url: /ru/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}}

 Вы можете установить**Тень** из**Текстовые эффекты** любой фигуры или текстового поля. Пожалуйста, используйте[**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody) имущество. Он представляет настройку текста формы и возвращает[**Настройка шрифта**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) объекты. После доступа к нему установите**Тень** с помощью[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) имущество. Это свойство типа[**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype)который имеет несколько значений. Некоторые из них

- OffsetDiagonalBottomRight
- смещение снизу
- OffsetDiagonalTopRight
- ВнутриСлева
- InsideCenter
- перспективадиагональверхнийлевый
- ПерспективаДиагональНижнейПравой

{{% /alert %}}

Следующий фрагмент кода демонстрирует использование[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype)свойство, чтобы установить тень текстовых эффектов Shape или TextBox.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
