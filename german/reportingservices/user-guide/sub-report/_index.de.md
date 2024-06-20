---
title: Unterbericht
type: docs
weight: 90
url: /de/reportingservices/sub-report/
---

{{% alert color="primary" %}} 

Ein Unterbericht kann in einem Tabellenelement eingebettet werden. Das Format lautet: &=subreport{BerichtName=Ihr Berichtsname; Parameter1-Name = Parameter1-Wert; Parameter2-Name = Parameter2-Wert; ...}

**Ein Unterbericht in einer Berichtsdefinition** 

![todo:image_alt_text](sub-report_1.png)

Im Beispiel ist der Name des Unterberichts „Sales Order Detail“. Er hat einen Parameter, SalesOrderNumber. Der Wert des Parameters ist EmpSalesDetail.SalesOrderNumber.
### **Einschränkungen für Unterberichte**
1. Der Unterbericht sollte mit Aspose.Cells.ReportingServices Designer erstellt werden.
1. Der Unterbericht kann nur in der Gruppenzeilen der Tabelle eingebettet werden, und die Gruppenzeile darf keine Elemente außer dem Unterbericht enthalten. Das Einbetten eines Unterberichts in den Detailzeilen oder Fußzeilen der Tabelle ist nicht erlaubt.
1. Derzeit wird keine Verschachtelung von mehr als einer Ebene unterstützt. Der Unterbericht kann keinen eingebetteten Bericht enthalten.

{{% /alert %}} 
###### **Dieser Abschnitt umfasst die folgenden Themen:** 
- [Erstellen von Tabellenelementen](/cells/de/reportingservices/creating-table-item/)
- [Untergeordnetes Berichtselement hinzufügen](/cells/de/reportingservices/add-sub-report-item/)
