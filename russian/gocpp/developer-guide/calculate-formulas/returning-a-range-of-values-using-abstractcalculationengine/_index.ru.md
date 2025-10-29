---
title: Возврат диапазона значений с помощью AbstractCalculationEngine и Golang через C++
linktitle: Возвращение Диапазона Значений с Использованием AbstractCalculationEngine
description: Эта статья представляет абстрактный движок вычислений, который возвращает диапазон значений в Microsoft Excel с использованием Aspose.Cells и Golang через C++. Загружая или создавая файл Excel, можно использовать методы Aspose.Cells для получения диапазона значений и возврата результата. В конце сохраняем изменённый файл Excel на диск.
keywords: Aspose.Cells, Excel, абстрактный расчетный движок, возвращающий серию значений
type: docs
weight: 55
url: /ru/go-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет класс [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/), который используется для реализации определяемых пользователем или пользовательских функций, которые не поддерживаются Microsoft Excel в качестве встроенных функций.

В данной статье будет объяснено, как вернуть диапазон значений из [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/).

{{% /alert %}}

Следующий код демонстрирует использование класса [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) и возвращает диапазон значений через его метод.

Создайте класс с функцией `CalculateCustomFunction`. Этот класс реализует [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine.go" >}}
Теперь используйте вышеуказанную функцию в вашей программе.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine-1.go" >}}
