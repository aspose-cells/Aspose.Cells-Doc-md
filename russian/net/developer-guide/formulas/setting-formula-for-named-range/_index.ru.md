---
title: Формула настройки для именованного диапазона
type: docs
weight: 20
url: /ru/net/setting-formula-for-named-range/
---
## **Формула настройки для именованного диапазона**
 Подобно приложению Excel, API-интерфейсы Aspose.Cells предоставляют возможность указать формулу для именованного диапазона при использовании его[Относится к](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto)имущество. Для этой функции может быть множество сценариев использования, некоторые из которых подробно описаны ниже.
### **Установка простой формулы для именованного диапазона**
Простая формула может быть ссылкой на другую ячейку на том же (или другом) листе. В следующем примере создается именованный диапазон в новой электронной таблице и задается ссылка на другую ячейку.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **Установка сложной формулы для именованного диапазона**
Сложная формула может быть чем угодно, например динамическим диапазоном или формулой, охватывающей несколько ячеек на разных листах. В следующем примере создается динамический диапазон с использованием функции ИНДЕКС для получения значения из списка на основе его местоположения.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



Вот еще один пример, в котором именованный диапазон используется для суммирования значений из двух ячеек на разных листах.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
