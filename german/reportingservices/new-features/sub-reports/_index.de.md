---
title: Unterberichte
type: docs
weight: 20
url: /de/reportingservices/sub-reports/
---

{{% alert color="primary" %}} 

Wir haben die Unterstützung für das Einbetten eines Unterberichts in einer Tabellengruppenzeile integriert. Das Format lautet:

&=subreport{ReportName=your report name; parameter1 name = parameter1 value; parameter2 name = parameter2 value;......} 

{{% /alert %}} 
### **Beispiel**
**Ein Unterbericht in einer Tabelle** 

![todo:image_alt_text](sub-reports_1.png)

Im Beispiel ist der Name des Unterberichts "Verkaufsdetail". Es hat einen Parameter, *SalesOrderNumber*. Der Wert des Parameters ist *EmpSalesDetail.SalesOrderNumber*.
#### **Einschränkungen bei der Verwendung von Unterberichten**
- Der Unterbericht sollte mit dem Aspose.Cells.Reporting Services Designer-Tool entworfen werden.
- Der Unterbericht kann nur in der Tabellengruppenzeile eingebettet werden, und die Gruppenzeile darf keine anderen Elemente außer dem Unterbericht enthalten. Das Einbetten eines Unterberichts in den Tabellendetailzeilen oder Fußzeilen ist nicht erlaubt.
- Derzeit wird keine Verschachtelung von mehr als einer Ebene unterstützt. Der Unterbericht kann keinen eingebetteten Bericht enthalten.
