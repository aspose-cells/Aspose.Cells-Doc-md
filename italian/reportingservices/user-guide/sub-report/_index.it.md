---
title: Rapporto secondario
type: docs
weight: 90
url: /it/reportingservices/sub-report/
---
{{% alert color="primary" %}} 

Un sottoreport può essere incorporato in un elemento della tabella. Il formato è: &=subreport{ReportName=nome del report; parametro1 nome = parametro1 valore; nome parametro2 = valore parametro2; ...}

**Un sottoreport in una definizione di report** 

![cose da fare:immagine_alt_testo](sub-report_1.png)

Nell'esempio, il nome del sottoreport è "Sales Order Detail". Ha un parametro, SalesOrderNumber. Il valore del parametro è EmpSalesDetail.SalesOrderNumber.
### **Restrizioni sui sottoreport**
1. Il sottoreport deve essere progettato con Aspose.Cells.ReportingServices Designer.
1. Il sottoreport può essere incorporato solo nella riga del gruppo di tabelle e la riga del gruppo non può contenere alcun elemento tranne il sottoreport. Non è consentito incorporare un sottoreport nelle righe di dettaglio della tabella o nelle righe del piè di pagina.
1. Attualmente, l'annidamento di più di un livello non è supportato. Il sottoreport non può contenere un report incorporato.

{{% /alert %}} 
###### **Questa sezione include i seguenti argomenti:**
- [Creazione dell'elemento della tabella](/cells/it/reportingservices/creating-table-item/)
- [Aggiungi elemento report secondario](/cells/it/reportingservices/add-sub-report-item/)
