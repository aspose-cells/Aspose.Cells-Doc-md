---
title: Unterbericht
type: docs
weight: 90
url: /de/reportingservices/sub-report/
---
{{% alert color="primary" %}} 

Ein Unterbericht kann in ein Tabellenelement eingebettet werden. Das Format ist: &=subreport{ReportName=Name Ihres Berichts; Parameter1-Name = Parameter1-Wert; Parameter2-Name = Parameter2-Wert; ...}

**Ein Unterbericht in einer Berichtsdefinition** 

![todo: Bild_alt_Text](sub-report_1.png)

Im Beispiel lautet der Name des Unterberichts „Sales Order Detail“. Es hat einen Parameter, SalesOrderNumber. Der Wert des Parameters ist EmpSalesDetail.SalesOrderNumber.
### **Einschränkungen für Unterberichte**
1. Der Unterbericht sollte mit Aspose.Cells.ReportingServices Designer gestaltet werden.
1. Der Unterbericht kann nur in die Tabellengruppenzeile eingebettet werden, und die Gruppenzeile darf keine Elemente außer dem Unterbericht enthalten. Das Einbetten eines Unterberichts in die Tabellendetailzeilen oder Fußzeilen ist nicht zulässig.
1. Derzeit wird das Verschachteln von mehr als einer Ebene nicht unterstützt. Der Unterbericht darf keinen eingebetteten Bericht enthalten.

{{% /alert %}} 
###### **Dieser Abschnitt umfasst die folgenden Themen:**
- [Tabellenelement erstellen](/cells/de/reportingservices/creating-table-item/)
- [Unterberichtselement hinzufügen](/cells/de/reportingservices/add-sub-report-item/)
