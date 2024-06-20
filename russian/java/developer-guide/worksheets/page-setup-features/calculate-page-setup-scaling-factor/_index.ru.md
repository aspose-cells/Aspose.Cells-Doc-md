---
title: Вычислить масштабирование настройки страницы
type: docs
weight: 260
url: /ru/java/calculate-page-setup-scaling-factor/
---

{{% alert color="primary" %}} 

Когда вы устанавливаете масштаб страницы с помощью опции **Fit to n page(s) wide by m tall**, Microsoft Excel вычисляет масштабирование настройки страницы. Вы можете вычислить то же самое, используя свойство [SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale). Это свойство возвращает значение типа double, которое можно преобразовать в процентное значение. Например, если оно возвращает 0,5079621076, то это означает, что масштабирование составляет 51%.

{{% /alert %}} 
## **Вычислить масштабирование настройки страницы**
Следующий образец кода иллюстрирует, как вычислить масштабирование настроек страницы, используя свойство [SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **Вывод в консоль**
Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

 0.5079621076583862

{{< /highlight >}}
