---
title: Как получить информацию о подключении OData
type: docs
weight: 60
url: /ru/python-net/how-to-get-odata-connection-information/
---

## **Получение информации о подключении OData**

Могут возникнуть ситуации, когда разработчикам потребуется извлечь информацию OData из файла Excel. Aspose.Cells for Python via .NET предоставляет свойство [**Workbook.data_mashup**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/data_mashup), которое возвращает информацию DataMashup, содержащуюся в файле Excel. Эта информация представлена классом [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup). Класс [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup) предоставляет свойство [**power_query_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup/power_query_formulas), возвращающее коллекцию [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/). Из [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/) можно получить доступ к [**PowerQueryFormula**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformula) и [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulaitem).

В следующем фрагменте кода демонстрируется использование этих классов для извлечения информации OData.

Исходный файл, использованный в следующем фрагменте кода, прикреплен для вашего ознакомления.

[Исходный файл](96928098.xlsx)

### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-GetOdataDetails-1.py" >}}

### **Вывод в консоль**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}

