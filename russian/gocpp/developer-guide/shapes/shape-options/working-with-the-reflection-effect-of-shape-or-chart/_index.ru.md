---
title: Работа с эффектом отражения фигуры или диаграммы с помощью Golang через C++
linktitle: Работа с эффектом отражения формы или диаграммы
type: docs
weight: 210
url: /ru/go-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Узнайте, как работать с эффектом отражения фигур или диаграмм с помощью Aspose.Cells и Golang через C++.
---

## **Возможные сценарии использования**
Aspose.Cells предоставляет свойство [Shape.Reflection](https://reference.aspose.com/cells/go-cpp/shape/getreflection/) вместе с классом [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/), чтобы работать с эффектом отражения фигуры или диаграммы. Класс [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) содержит следующие свойства, которые можно установить для достижения различных результатов в соответствии с требованиями приложения.

- [Размытие](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getblur/)
- [Направление](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getdirection/)
- [Расстояние](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getdistance/)
- [Направление затухания](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getfadedirection/)
- [Поворот с формой](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getrotwithshape/)
- [Размер](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getsize/)
- [Прозрачность](https://reference.aspose.com/cells/go-cpp/reflectioneffect/gettransparency/)
- [Тип](https://reference.aspose.com/cells/go-cpp/reflectioneffect/gettype/)

## **Работа с эффектом отражения формы или диаграммы**
Следующий пример загружает [исходный Excel-файл](5115424.xlsx), получает доступ к первой фигуре на листе по умолчанию, устанавливает различные свойства класса [Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/) и затем сохраняет книгу в [выходной Excel-файл](5115423.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithTheReflectionEffectOfShapeOrChart.go" >}}
