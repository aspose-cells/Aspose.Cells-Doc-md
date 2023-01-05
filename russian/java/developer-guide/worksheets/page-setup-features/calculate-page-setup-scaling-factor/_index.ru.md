---
title: Вычислить коэффициент масштабирования параметров страницы
type: docs
weight: 260
url: /ru/java/calculate-page-setup-scaling-factor/
---
{{% alert color="primary" %}} 

Когда вы устанавливаете Масштабирование параметров страницы с помощью**Вместить до n страниц в ширину и m в высоту** опция, Microsoft Excel вычисляет коэффициент масштабирования параметров страницы. Вы можете рассчитать то же самое, используя[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale) имущество. Это свойство возвращает двойное значение, которое можно преобразовать в процентное значение. Например, если он возвращает 0,5079621076, это означает, что коэффициент масштабирования равен 51%.

{{% /alert %}} 
## **Вычислить коэффициент масштабирования параметров страницы**
 В следующем примере кода показано, как рассчитать коэффициент масштабирования параметров страницы с помощью[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale)имущество.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **Консольный вывод**
Вот вывод консоли приведенного выше примера кода.

{{< highlight "java" >}}

 0.5079621076583862

{{< /highlight >}}
