---  
title: Получить все скрытые индексы строк после обновления автофильтра 
type: docs  
weight: 320  
url: /ru/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: Узнайте, как получить все индексы скрытых строк после обновления AutoFilter, используя API Aspose.Cells for Node.js via C++.  
keywords: Получить все индексы скрытых строк после обновления AutoFilter Node.js через C++, получить все индексы скрытых строк после обновления AutoFilter Node.js через C++, извлечь все индексы скрытых строк после обновления AutoFilter Node.js через C++  
---  

## **Возможные сценарии использования**  

Когда вы применяете автофильтр к ячейкам листа, некоторые строки автоматически скрываются. Но возможно, что некоторые строки уже скрыты вручную пользователем Excel и не скрыты автофильтром. Поэтому трудно определить, какие строки скрыты автофильтром, а какие скрыты вручную пользователем Excel. API Aspose.Cells for Node.js via C++ решает эту проблему с помощью массива [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-). Этот метод возвращает индексы строк всех скрытых строк, скрытых автофильтром, а не вручную пользователем Excel.  

## **Получить все скрытые индексы строк после обновления автофильтра**  

Посмотрите следующий пример кода, который загружает [пример файла Excel](64716909.xlsx), содержащий некоторые строки, скрытые вручную пользователем Excel. Код применяет автофильтр и обновляет его с помощью метода [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-), который возвращает индексы всех скрытых строк автофильтром. Затем он выводит индексы скрытых строк на консоль вместе с именами ячеек и их значениями.  

## **Образец кода**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.js" >}}


## **Вывод в консоль**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}  
