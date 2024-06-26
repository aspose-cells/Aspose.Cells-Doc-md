---
title: Параметризованный отчет
type: docs
weight: 60
url: /ru/reportingservices/parameterized-report/
---

{{% alert color="primary" %}} 

Параметризованный отчет - это отчет, который принимает входные значения, используемые при обработке отчета. 

С параметризованным отчетом вы можете изменить вывод отчета на основе установленных значений во время выполнения. Службы отчетов поддерживают два вида параметров: параметры запроса и параметры отчета. 

- Параметры запроса используются для выбора или фильтрации данных во время обработки данных. Если указан параметр запроса, значение должно быть предоставлено либо пользователем, либо по умолчанию, чтобы завершить оператор SELECT или хранимую процедуру, извлекающую данные для отчета.
- Параметры отчета используются во время обработки отчета, чтобы показать различные аспекты данных. Обычно параметр отчета используется для фильтрации большого набора записей, но он может иметь другие использования в зависимости от запросов и выражений в отчете.

Параметры отчета отличаются от параметров запроса тем, что они определяются в отчете и обрабатываются сервером отчетов, в то время как параметры запроса определяются как часть запроса набора данных и обрабатываются на сервере базы данных. В Aspose.Cells.Report.Designer параметры запроса указываются при создании запроса в Microsoft Query. 

В Aspose.Cells.Report.Designer можно создавать параметры отчета и сопоставлять параметры запроса с соответствующим параметром отчета. Таким образом, можно выбирать значения для параметров отчета и передавать их в запрос для ограничения данных, полученных из источника данных.

{{% /alert %}} 
###### **Этот раздел включает следующие темы:** 
- [Создание параметров отчета](/cells/ru/reportingservices/creating-report-parameters/)
- [Изменение параметров отчета](/cells/ru/reportingservices/modifying-report-parameters/)
- [Сопоставление параметров запроса с параметрами отчета](/cells/ru/reportingservices/mapping-query-parameters-to-report-parameters/)
