---
title: Как получить информацию о соединении OData
type: docs
weight: 60
url: /ru/java/how-to-get-odata-connection-information/
---
## **Получить информацию о соединении OData**

Могут быть случаи, когда разработчикам необходимо извлечь информацию OData из файла Excel. Aspose.Cells обеспечивает[**Workbook. DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup)свойство, которое возвращает информацию DataMashup, присутствующую в файле Excel. Эта информация представлена классом DataMashup. Класс DataMashup предоставляет свойство PowerQueryFormulas, которое возвращает коллекцию PowerQueryFormulaCollction. Из PowerQueryFormulaCollction вы можете получить доступ к PowerQueryFormula и PowerQueryFormulaItem.

В следующем фрагменте кода показано использование этих классов для получения информации OData.

Исходный файл, используемый в следующем фрагменте кода, прилагается для справки.

[Исходный файл](ODataSample.xlsx)

### **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **Консольный вывод**

Имя соединения: Заказы

Название: Источник

Значение: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Название: Orders_table

Значение: Источник{[Name="Заказы",Signature="table"]}[Данные]