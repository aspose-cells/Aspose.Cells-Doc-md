---
title: Установка формулы для именованного диапазона
type: docs
weight: 20
url: /ru/net/setting-formula-for-named-range/
---

## **Установка формулы для именованного диапазона**
Как и приложение Excel, API Aspose.Cells позволяет указать формулу для именованного диапазона при использовании его свойства [RefersTo](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto). Эта функция может быть использована в различных сценариях использования, о некоторых из которых подробно рассказано ниже.
### **Установка простой формулы для именованного диапазона**
Простая формула может представлять собой ссылку на другую ячейку в том же (или другом) листе. В следующем примере создается именованный диапазон в новом электронном таблице и устанавливается его ссылка на другую ячейку.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **Установка сложной формулы для именованного диапазона**
Сложная формула может быть чем-то таким, как динамический диапазон или формула, охватывающая несколько ячеек на различных листах. В следующем примере создается динамический диапазон с использованием функции INDEX для получения значения из списка на основе его расположения.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



Вот еще один пример использования именованного диапазона для суммирования значений из 2 ячеек на разных листах.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
