---
title: Вычисление пользовательских функций в GridWeb
type: docs
weight: 90
url: /ru/net/aspose-cells-gridweb/calculate-custom-functions-in-gridweb/
keywords: GridWeb,custom functions,custom,function
description: Эта статья представляет возможности пользовательских функций в GridWeb.
---


## **Возможные сценарии использования**
Aspose.Cells.GridWeb поддерживает вычисление пользовательских функций с помощью свойства GridWeb.CustomCalculationEngine. Это свойство принимает экземпляр интерфейса GridAbstractCalculationEngine. Пожалуйста, реализуйте интерфейс GridAbstractCalculationEngine и вычислите свои пользовательские функции собственной логикой.
## **Вычисление пользовательских функций в GridWeb**
В следующем образце кода добавляется пользовательская функция с именем MYTESTFUNC() в ячейке B3. Затем мы вычисляем значение этой функции, реализуя интерфейс GridAbstractCalculationEngine. Мы вычисляем MYTESTFUNC() таким образом, что умножаем его параметр на 2 и возвращаем результат. Таким образом, если его параметр равен 9, он вернет 2*9 = 18.
### **Образец кода**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
