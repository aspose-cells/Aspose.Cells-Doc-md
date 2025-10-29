---
title: Работа с эффектом тени фигуры или диаграммы с помощью Golang через C++
linktitle: Работа с эффектом тени формы или диаграммы
type: docs
weight: 220
url: /ru/go-cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Узнайте, как управлять эффектом тени фигур или диаграмм используя Aspose.Cells for C++.
---

## **Возможные сценарии использования**
Aspose.Cells предоставляет метод [GetShadowEffect()](https://reference.aspose.com/cells/go-cpp/shape/getshadoweffect/) вместе с классом [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/), чтобы работать с эффектом тени фигур или диаграмм. Класс [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/) содержит следующие свойства, которые можно установить для достижения различных результатов в соответствии с требованиями приложения.

- [GetAngle()](https://reference.aspose.com/cells/go-cpp/shadoweffect/getangle/)
- [GetBlur()](https://reference.aspose.com/cells/go-cpp/shadoweffect/getblur/)
- [GetColor()](https://reference.aspose.com/cells/go-cpp/shadoweffect/getcolor/)
- [GetDistance()](https://reference.aspose.com/cells/go-cpp/shadoweffect/getdistance/)
- [GetPresetType()](https://reference.aspose.com/cells/go-cpp/shadoweffect/getpresettype/)
- [GetSize()](https://reference.aspose.com/cells/go-cpp/shadoweffect/getsize/)
- [GetTransparency()](https://reference.aspose.com/cells/go-cpp/shadoweffect/gettransparency/)

## **Работа с теневым эффектом формы или диаграммы**
Следующий пример загружает [исходный Excel-файл](5115425.xlsx), получает доступ к первой фигуре на первом листе, устанавливает подполя свойства [GetShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getshadoweffect/) и затем сохраняет книгу в [выходной Excel-файл](5115411.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithTheShadowEffectOfShapeOrChart.go" >}}
