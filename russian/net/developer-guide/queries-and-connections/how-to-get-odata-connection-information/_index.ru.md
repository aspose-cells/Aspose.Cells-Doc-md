---
title: Как получить информацию о подключении OData
type: docs
weight: 60
url: /ru/net/how-to-get-odata-connection-information/
---

## **Получение информации о подключении OData**

Возможно, существуют случаи, когда разработчики нуждаются в извлечении информации OData из файла Excel. Aspose.Cells предоставляет свойство [**Workbook.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup), которое возвращает информацию DataMashup, представленную классом [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup). Класс [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) предоставляет свойство [**PowerQueryFormulas**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas), возвращающее коллекцию [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction). Из [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction) можно получить доступ к [**PowerQueryFormula**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) и [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

В следующем фрагменте кода демонстрируется использование этих классов для извлечения информации OData.

Исходный файл, использованный в следующем фрагменте кода, прикреплен для вашего ознакомления.

[Исходный файл](96928098.xlsx)

### **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **Вывод в консоль**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
