---
title: Как получить информацию о соединении OData
type: docs
weight: 60
url: /ru/net/how-to-get-odata-connection-information/
---
## **Получить информацию о соединении OData**

 Могут быть случаи, когда разработчикам необходимо извлечь информацию OData из файла Excel. Aspose.Cells обеспечивает[**Workbook. DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup) свойство, которое возвращает информацию DataMashup, присутствующую в файле Excel. Эта информация представлена[**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) учебный класс.[**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)класс обеспечивает[**Формулы PowerQuery**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas) свойство, возвращающее[**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction) коллекция. От[**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction), вы можете получить доступ к[**Формула PowerQuery**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) а также[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

В следующем фрагменте кода показано использование этих классов для получения информации OData.

Исходный файл, используемый в следующем фрагменте кода, прилагается для справки.

[Исходный файл](96928098.xlsx)

### **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **Консольный вывод**

Имя соединения: Заказы

Название: Источник

Значение: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Название: Orders_table

Значение: Источник{[Name="Заказы",Signature="table"]}[Данные]