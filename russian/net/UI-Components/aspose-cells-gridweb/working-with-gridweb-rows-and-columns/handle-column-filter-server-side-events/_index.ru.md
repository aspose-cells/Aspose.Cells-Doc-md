---
title: Управление событиями серверной стороны фильтра столбцов
type: docs
weight: 90
url: /ru/net/aspose-cells-gridweb/handle-column-filter-server-side-events/
keywords: GridWeb,filter,OnBeforeColumnFilter,OnAfterColumnFilter
description: В этой статье рассматривается обработка события фильтрации столбцов в GridWeb.
---

{{% alert color="primary" %}} 

Фильтрация данных, вероятно, является одной из наиболее широко используемых функций Excel, которая позволяет фильтровать данные на основе определенных критериев. Отфильтрованные данные отображают только те строки, которые соответствуют условию, скрывая строки, которые не соответствуют критериям.
Компонент Aspose.Cells.GridWeb предоставляет возможность выполнять фильтрацию данных с использованием его интерфейса. Для расширения его возможностей компонент Aspose.Cells.GridWeb также предоставляет два события, которые могут служить обратным вызовом для механизма фильтрации, выполненной через пользовательский интерфейс GridWeb.

{{% /alert %}} 
## **Обработка события серверной стороны при применении фильтра столбца**
Есть два основных события, подробно описанных ниже.

1. OnBeforeColumnFilter: Срабатывает перед применением фильтра на столбце.
1. OnAfterColumnFilter: Срабатывает после применения фильтра на столбце.

Ниже приведен ASPX-скрипт компонента Aspose.Cells.GridWeb для добавления и назначения упомянутых событий.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



Эти события могут использоваться для получения полезной информации о процессе фильтрации, такой как индекс столбца и значение, на котором должен быть применен фильтр. Ниже приведен фрагмент, демонстрирующий использование события OnBeforeColumnFilter для получения индекса столбца и значения, которое пользователь выбрал в интерфейсе GridWeb для фильтрации.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


С другой стороны, если требуется получить количество отфильтрованных строк после применения фильтра, то можно использовать событие OnAfterColumnFilter, как показано ниже.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

Проверьте введение в все [работающие с событиями GridWeb](/cells/ru/net/aspose-cells-gridweb/working-with-gridweb-events/), а также некоторые детали, как обработать эти события.

{{% /alert %}}
