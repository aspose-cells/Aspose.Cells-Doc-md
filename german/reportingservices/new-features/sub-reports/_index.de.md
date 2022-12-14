---
title: Unterberichte
type: docs
weight: 20
url: /de/reportingservices/sub-reports/
---
{{% alert color="primary" %}} 

Wir haben die Unterstützung für das Einbetten eines Unterberichts in eine Tabellengruppenzeile integriert. Das Format ist:

&=subreport{ReportName=Ihr Berichtsname; Parameter1-Name = Parameter1-Wert; Parameter2-Name = Parameter2-Wert;......} 

{{% /alert %}} 
### **Beispiel**
**Ein Unterbericht in einer Tabelle** 

![todo: Bild_alt_Text](sub-reports_1.png)

 Im Beispiel lautet der Name des Unterberichts „Sales Order Detail“. Es hat einen Parameter,*Verkaufsauftragsnummer* . Der Wert des Parameters ist*EmpSalesDetail.SalesOrderNumber.*
#### **Einschränkungen bei der Verwendung von Unterberichten**
- Der Unterbericht sollte mit dem Tool Aspose.Cells.Reporting Services Designer entworfen werden.
- Der Unterbericht kann nur in die Tabellengruppenzeile eingebettet werden und die Gruppenzeile darf keine anderen Elemente außer dem Unterbericht enthalten. Das Einbetten eines Unterberichts in die Tabellendetailzeilen oder Fußzeilen ist nicht zulässig.
- Derzeit wird das Verschachteln von mehr als einer Ebene nicht unterstützt. Der Unterbericht darf keinen eingebetteten Bericht enthalten.
