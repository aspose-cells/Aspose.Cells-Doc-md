---
title: Работа со свечением фигуры или диаграммы с помощью Golang через C++
linktitle: Работа с эффектом свечения формы или диаграммы
type: docs
weight: 240
url: /ru/go-cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Узнайте, как работать с эффектом свечения форм или графиков с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**
Aspose.Cells предоставляет свойство [Shape.Glow](https://reference.aspose.com/cells/go-cpp/shape/getgloweffect/) вместе с классом [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/), чтобы работать со свечением фигуры или диаграммы. Класс [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) содержит следующие свойства, которые можно установить для достижения различных результатов в соответствии с требованиями приложения.

- [GlowEffect.Size](https://reference.aspose.com/cells/go-cpp/gloweffect/getsize/)
- [GlowEffect.Transparency](https://reference.aspose.com/cells/go-cpp/gloweffect/gettransparency/)
- [GlowEffect.Color](https://reference.aspose.com/cells/go-cpp/gloweffect/getcolor/)

## **Работа с эффектом свечения формы или диаграммы**
Следующий пример кода загружает [исходный excel файл](5115407.xlsx) и получает доступ к первой фигуре в первом листе, устанавливает под-свойства свойства [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) и сохраняет рабочую книгу в [выходной excel файл](5115414.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithTheGlowEffectOfShapeOrChart.go" >}}
