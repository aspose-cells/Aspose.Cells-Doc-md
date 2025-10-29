---  
title: Поиск данных с использованием исходных значений
type: docs  
weight: 380  
url: /ru/nodejs-cpp/search-data-using-original-values/  
description: Узнайте, как искать данные по исходным значениям через API Aspose.Cells for Node.js via C++.  
keywords: Поиск данных по исходным значениям Node.js через C++, найти данные по исходным значениям Node.js через C++, искать данные по исходным значениям Node.js через C++, находить данные по исходным значениям Node.js через C++  
---  

{{% alert color="primary" %}}  

Иногда значение данных скрыто, потому что оно отформатировано каким-то образом. Например, предположим, что ячейка D4 имеет формулу =Сумма(A1:A2) и ее значение равно 20, но оно отформатировано как ---, то значение 20 скрыто и не может быть найдено с помощью функции поиска в Microsoft Excel. Однако вы можете найти его с помощью Aspose.Cells, используя [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype)  

{{% /alert %}}  

Приведенный ниже образец кода иллюстрирует вышеупомянутый момент. Он находит ячейку D4, которую нельзя найти с помощью опций поиска Microsoft Excel, но Aspose.Cells может найти ее с помощью [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype). Пожалуйста, прочтите комментарии внутри кода для получения дополнительной информации.  

## Код Node.js для поиска данных по исходным значениям  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchDataUsingOriginalValues.js" >}}


## Консольный вывод, сгенерированный образцовым кодом  

Вот вывод в консоль вышеуказанного образца кода.  

{{< highlight java >}}  

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
