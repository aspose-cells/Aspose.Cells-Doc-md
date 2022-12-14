---
title: Заполнить данные сначала по строке, а затем по столбцу
type: docs
weight: 1000
url: /ru/net/populate-data-first-by-row-then-by-column/
---
{{% alert color="primary" %}} 

Заполнение электронной таблицы данными сначала по строкам, а затем по столбцам повышает общую производительность.

{{% /alert %}} 

Размещение данных в последовательности A1, B1, A2, B2 выполняется быстрее, чем в A1, A2, B1, B2. Если на листе много ячеек и вы следуете второй последовательности, то есть заполняете данные построчно, этот совет может значительно ускорить работу программы.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-PopulateDataEfficiently-PopulateDataFirstByRowThenColumns.cs" >}}
