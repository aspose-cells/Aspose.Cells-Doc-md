---
title: Как получить информацию о подключении OData
type: docs
weight: 60
url: /ru/java/how-to-get-odata-connection-information/
---

## **Получение информации о подключении OData**

Могут возникнуть случаи, когда разработчикам необходимо извлечь информацию OData из файла Excel. Aspose.Cells предоставляет свойство [**Workbook.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup), которое возвращает информацию DataMashup, присутствующую в файле Excel. Эта информация представлена классом DataMashup. Класс DataMashup предоставляет свойство PowerQueryFormulas, которое возвращает коллекцию PowerQueryFormulaCollction. Из PowerQueryFormulaCollction вы можете получить доступ к PowerQueryFormula и PowerQueryFormulaItem.

В следующем фрагменте кода демонстрируется использование этих классов для извлечения информации OData.

Исходный файл, использованный в следующем фрагменте кода, прикреплен для вашего ознакомления.

[Исходный файл](ODataSample.xlsx)

### **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **Вывод в консоль**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
