---
title: Настройка теней для эффектов текста формы или текстового поля с помощью Golang через C++
linktitle: Настройка тени эффектов текста
type: docs
weight: 250
url: /ru/go-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Узнайте, как установить тень эффектов текста для фигур или текстовых блоков, используя Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Вы можете установить **Тень** **Эффектов текста** любой фигуры или текстового блока. Используйте свойство [**Shape.GetTextBody()**](https://reference.aspose.com/cells/go-cpp/shape/gettextbody/). Оно управляет настройками текста фигуры и возвращает объекты [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/). После доступа к нему установите **Тень** через свойство [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/). Это свойство типа [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/), имеющее несколько значений, например:

- Смещение по диагонали вниз и вправо
- Смещение вниз
- Смещение по диагонали вверх и вправо
- Слева внутри
- По центру внутри
- Диагональная перспектива вверху слева
- ПерспективаДиагональНижнийПравый

{{% /alert %}}

Следующий фрагмент кода демонстрирует использование свойства [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/go-cpp/shadoweffect/getpresettype/) для установки тени эффектов текста фигуры или текстового поля.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingShadowOfTextEffectsOfShapeOrTextbox.go" >}}
