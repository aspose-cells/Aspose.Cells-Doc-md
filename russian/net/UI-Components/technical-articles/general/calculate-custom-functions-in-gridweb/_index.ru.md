---
title: Расчет пользовательских функций в GridWeb
type: docs
weight: 90
url: /ru/net/calculate-custom-functions-in-gridweb/
---
## **Возможные сценарии использования**
Aspose.Cells.GridWeb поддерживает расчет пользовательских функций с помощью свойства GridWeb.CustomCalculationEngine. Это свойство принимает экземпляр интерфейса GridAbstractCalculationEngine. Пожалуйста, реализуйте интерфейс GridAbstractCalculationEngine и вычисляйте свои пользовательские функции с помощью собственной логики.
## **Расчет пользовательских функций в GridWeb**
Следующий пример кода добавляет пользовательскую функцию с именем MYTESTFUNC() в ячейку B3. Затем мы вычисляем значение этой функции, реализуя интерфейс GridAbstractCalculationEngine. Мы вычисляем MYTESTFUNC() таким образом, что он умножает свой параметр на 2 и возвращает результат. Поэтому, если его параметр равен 9, он вернет 2 * 9 = 18.
### **Образец кода**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
